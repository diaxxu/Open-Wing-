/*
 * OpenWing ULA-1 — Flight Data Logger
 * =====================================
 * Arduino Nano Every (or Uno/Mega compatible)
 * 
 * Logs to SD card at 5 Hz:
 *   - GPS lat/lon, altitude, groundspeed
 *   - Barometric altitude + pressure
 *   - EGT (cyl 1 and 2) via MAX31855
 *   - CHT (cyl 1 and 2) via MAX31855
 *   - Airspeed (MPXV7002DP differential pressure sensor)
 *   - 3-axis acceleration (MPU-6050)
 *   - Timestamp
 *
 * WIRING:
 *   GPS BN-220:     TX→D2(SoftSerial RX), 3.3V, GND
 *   BMP280:         SDA→A4, SCL→A5 (I2C)
 *   MAX31855 EGT1:  CS→D4, CLK→D13, DO→D12 (SPI shared)
 *   MAX31855 EGT2:  CS→D5
 *   MAX31855 CHT1:  CS→D6
 *   MAX31855 CHT2:  CS→D7
 *   MPXV7002DP:     VOUT→A0, 5V, GND
 *   MPU-6050:       SDA→A4, SCL→A5 (I2C, addr 0x68)
 *   SD card:        MOSI→D11, MISO→D12, CLK→D13, CS→D10
 *
 * SAFETY NOTE:
 *   This device is for DATA LOGGING ONLY.
 *   It does NOT provide flight-critical information.
 *   Do NOT rely on this system for navigation or airspeed reference.
 *   The mechanical ASI and altimeter are the primary instruments.
 *
 * Libraries required (install via Arduino Library Manager):
 *   - TinyGPS++ (Mikal Hart)
 *   - Adafruit_BMP280
 *   - Adafruit_MAX31855
 *   - MPU6050 (Electronic Cats or I2Cdevlib)
 *   - SD (built-in)
 *   - SoftwareSerial (built-in)
 */

#include <Arduino.h>
#include <SPI.h>
#include <SD.h>
#include <Wire.h>
#include <SoftwareSerial.h>
#include <TinyGPS++.h>
#include <Adafruit_BMP280.h>
#include <Adafruit_MAX31855.h>
#include <MPU6050.h>

// ─── Pin Definitions ───────────────────────────────────────────
#define GPS_RX_PIN      2       // Software serial RX from GPS TX
#define GPS_TX_PIN      3       // Not used (GPS is receive-only)
#define SD_CS_PIN       10

#define MAX31855_CLK    13
#define MAX31855_DO     12
#define EGT1_CS_PIN     4
#define EGT2_CS_PIN     5
#define CHT1_CS_PIN     6
#define CHT2_CS_PIN     7

#define AIRSPEED_PIN    A0      // MPXV7002DP output

// ─── Constants ─────────────────────────────────────────────────
#define LOG_RATE_HZ     5       // Logging frequency
#define LOG_INTERVAL_MS (1000 / LOG_RATE_HZ)

// Airspeed calibration (MPXV7002DP: Vout = 5V × (0.2 × P_kPa + 0.5))
// P_kPa = (Vout/Vcc - 0.5) / 0.2
// q_Pa = P_kPa × 1000
// V_ms = sqrt(2 × q / rho)
#define AIRSPEED_VCC    5.0f    // Supply voltage
#define AIRSPEED_OFFSET 512     // ADC offset (zero differential pressure)
#define RHO_SL          1.225f  // Air density kg/m³ (sea level, corrected in flight)
#define ADC_VREF        5.0f
#define ADC_MAX         1023

// Altitude reference (set to field elevation before engine start)
float baro_alt_offset_m = 0.0f;

// ─── Object Instances ──────────────────────────────────────────
SoftwareSerial   gpsSerial(GPS_RX_PIN, GPS_TX_PIN);
TinyGPSPlus      gps;
Adafruit_BMP280  bmp;
Adafruit_MAX31855 egt1(EGT1_CS_PIN, MAX31855_CLK, MAX31855_DO);
Adafruit_MAX31855 egt2(EGT2_CS_PIN, MAX31855_CLK, MAX31855_DO);
Adafruit_MAX31855 cht1(CHT1_CS_PIN, MAX31855_CLK, MAX31855_DO);
Adafruit_MAX31855 cht2(CHT2_CS_PIN, MAX31855_CLK, MAX31855_DO);
MPU6050          imu;
File             logFile;

// ─── State ─────────────────────────────────────────────────────
unsigned long lastLogTime   = 0;
unsigned long logFileNumber = 0;
char          logFileName[16];
bool          sdOk  = false;
bool          bmpOk = false;
bool          imuOk = false;

// EGT warning thresholds
const float EGT_WARN_C = 800.0f;
const float EGT_MAX_C  = 900.0f;
const float CHT_WARN_C = 220.0f;
const float CHT_MAX_C  = 250.0f;

// ─── Setup ────────────────────────────────────────────────────
void setup() {
    Serial.begin(115200);
    delay(1000);
    Serial.println(F("OpenWing ULA-1 Data Logger v1.0"));
    Serial.println(F("================================="));
    
    // GPS
    gpsSerial.begin(9600);
    Serial.println(F("[GPS] Initializing..."));
    
    // BMP280 barometric sensor
    bmpOk = bmp.begin(0x76);  // Try address 0x76 (some modules use 0x77)
    if (!bmpOk) bmpOk = bmp.begin(0x77);
    if (bmpOk) {
        bmp.setSampling(Adafruit_BMP280::MODE_NORMAL,
                        Adafruit_BMP280::SAMPLING_X2,
                        Adafruit_BMP280::SAMPLING_X16,
                        Adafruit_BMP280::FILTER_X4,
                        Adafruit_BMP280::STANDBY_MS_125);
        // Set altitude offset to zero at current pressure
        float p0 = bmp.readPressure();
        Serial.print(F("[BMP280] OK. Ground pressure: "));
        Serial.print(p0 / 100.0f, 1);
        Serial.println(F(" hPa"));
    } else {
        Serial.println(F("[BMP280] ERROR — no sensor found. Check wiring."));
    }
    
    // MPU-6050 IMU
    Wire.begin();
    imu.initialize();
    imuOk = imu.testConnection();
    if (imuOk) {
        imu.setFullScaleAccelRange(MPU6050_ACCEL_FS_4);  // ±4g range
        imu.setFullScaleGyroRange(MPU6050_GYRO_FS_250);  // ±250 deg/s
        Serial.println(F("[MPU6050] OK."));
    } else {
        Serial.println(F("[MPU6050] ERROR — check wiring."));
    }
    
    // SD Card
    if (SD.begin(SD_CS_PIN)) {
        sdOk = true;
        // Find next available log file number
        for (uint16_t n = 1; n < 9999; n++) {
            snprintf(logFileName, sizeof(logFileName), "FLIGHT%04d.CSV", n);
            if (!SD.exists(logFileName)) {
                logFileNumber = n;
                break;
            }
        }
        logFile = SD.open(logFileName, FILE_WRITE);
        if (logFile) {
            // Write CSV header
            logFile.println(F(
                "millis,gps_time,gps_lat,gps_lon,gps_alt_m,gps_spd_kts,"
                "baro_alt_m,baro_pres_hpa,"
                "egt1_c,egt2_c,cht1_c,cht2_c,"
                "airspeed_ms,airspeed_kts,"
                "accel_x_g,accel_y_g,accel_z_g,"
                "gyro_p_dps,gyro_q_dps,gyro_r_dps"
            ));
            logFile.flush();
            Serial.print(F("[SD] Logging to: "));
            Serial.println(logFileName);
        } else {
            sdOk = false;
            Serial.println(F("[SD] ERROR — cannot open log file."));
        }
    } else {
        Serial.println(F("[SD] ERROR — card not found. Insert SD card."));
    }
    
    Serial.println(F("\n[SYSTEM] Logger running. Logging every 200ms."));
    Serial.println(F("[SAFETY] Mechanical ASI/ALT are primary flight instruments."));
    Serial.println(F(""));
}

// ─── Main Loop ────────────────────────────────────────────────
void loop() {
    // ── Feed GPS ──
    while (gpsSerial.available()) {
        gps.encode(gpsSerial.read());
    }
    
    // ── Log at set interval ──
    unsigned long now = millis();
    if (now - lastLogTime >= LOG_INTERVAL_MS) {
        lastLogTime = now;
        
        // Read all sensors
        SensorData data = readSensors();
        
        // Check engine limits and warn via serial
        checkEngineWarnings(data);
        
        // Log to SD
        if (sdOk && logFile) {
            writeLog(data, now);
        }
        
        // Debug output to serial (at 1 Hz to avoid flooding)
        static uint8_t serialDiv = 0;
        if (++serialDiv >= LOG_RATE_HZ) {
            serialDiv = 0;
            printStatus(data);
        }
    }
}

// ─── Data Structures ──────────────────────────────────────────
struct SensorData {
    // GPS
    bool     gpsValid;
    float    lat, lon;
    float    gpsAlt_m;
    float    gpsSpd_kts;
    uint32_t gpsTime;    // HHMMSS
    
    // Baro
    float    baroAlt_m;
    float    baroPres_hPa;
    
    // Engine
    float    egt1_C, egt2_C;
    float    cht1_C, cht2_C;
    
    // Airspeed
    float    airspeed_ms;
    float    airspeed_kts;
    
    // IMU
    float    ax_g, ay_g, az_g;
    float    gp_dps, gq_dps, gr_dps;
};

// ─── Sensor Reading ───────────────────────────────────────────
SensorData readSensors() {
    SensorData d = {};
    
    // ── GPS ──
    d.gpsValid    = gps.location.isValid() && gps.location.age() < 2000;
    d.lat         = d.gpsValid ? gps.location.lat() : 0.0f;
    d.lon         = d.gpsValid ? gps.location.lng() : 0.0f;
    d.gpsAlt_m    = gps.altitude.isValid() ? gps.altitude.meters() : 0.0f;
    d.gpsSpd_kts  = gps.speed.isValid()    ? gps.speed.knots()     : 0.0f;
    if (gps.time.isValid()) {
        d.gpsTime = gps.time.hour() * 10000UL + 
                    gps.time.minute() * 100UL + 
                    gps.time.second();
    }
    
    // ── BMP280 ──
    if (bmpOk) {
        d.baroPres_hPa = bmp.readPressure() / 100.0f;
        d.baroAlt_m    = bmp.readAltitude(1013.25f) - baro_alt_offset_m;
        // baro_alt_offset_m set to field elevation on ground, so altitude reads AGL
    }
    
    // ── MAX31855 Thermocouples ──
    // Note: MAX31855 returns NaN if thermocouple is open-circuit
    d.egt1_C = egt1.readCelsius();
    d.egt2_C = egt2.readCelsius();
    d.cht1_C = cht1.readCelsius();
    d.cht2_C = cht2.readCelsius();
    
    // Substitute 0 for NaN (sensor fault)
    if (isnan(d.egt1_C)) d.egt1_C = -1.0f;
    if (isnan(d.egt2_C)) d.egt2_C = -1.0f;
    if (isnan(d.cht1_C)) d.cht1_C = -1.0f;
    if (isnan(d.cht2_C)) d.cht2_C = -1.0f;
    
    // ── Airspeed (MPXV7002DP) ──
    int   adcRaw   = analogRead(AIRSPEED_PIN);
    float vout     = (adcRaw / (float)ADC_MAX) * ADC_VREF;
    float dp_kPa   = (vout / AIRSPEED_VCC - 0.5f) / 0.2f;
    float dp_Pa    = dp_kPa * 1000.0f;
    
    if (dp_Pa > 0.5f) {   // Only valid for positive pressure differential
        d.airspeed_ms  = sqrtf(2.0f * dp_Pa / RHO_SL);
        d.airspeed_kts = d.airspeed_ms / 0.514444f;
    } else {
        d.airspeed_ms  = 0.0f;
        d.airspeed_kts = 0.0f;
    }
    
    // ── IMU (MPU-6050) ──
    if (imuOk) {
        int16_t ax, ay, az, gx, gy, gz;
        imu.getMotion6(&ax, &ay, &az, &gx, &gy, &gz);
        
        // ±4g range: sensitivity = 8192 LSB/g
        d.ax_g = ax / 8192.0f;
        d.ay_g = ay / 8192.0f;
        d.az_g = az / 8192.0f;
        
        // ±250 deg/s range: sensitivity = 131 LSB/(deg/s)
        d.gp_dps = gx / 131.0f;
        d.gq_dps = gy / 131.0f;
        d.gr_dps = gz / 131.0f;
    }
    
    return d;
}

// ─── Engine Warning Check ─────────────────────────────────────
void checkEngineWarnings(const SensorData& d) {
    bool warn = false;
    
    if (d.egt1_C > EGT_MAX_C || d.egt2_C > EGT_MAX_C) {
        Serial.println(F("!!! EGT CRITICAL — REDUCE POWER IMMEDIATELY !!!"));
        warn = true;
    } else if (d.egt1_C > EGT_WARN_C || d.egt2_C > EGT_WARN_C) {
        Serial.println(F("! EGT WARNING — approaching limit, check mixture"));
        warn = true;
    }
    
    if (d.cht1_C > CHT_MAX_C || d.cht2_C > CHT_MAX_C) {
        Serial.println(F("!!! CHT CRITICAL — REDUCE POWER / CHECK COOLING !!!"));
        warn = true;
    } else if (d.cht1_C > CHT_WARN_C || d.cht2_C > CHT_WARN_C) {
        Serial.println(F("! CHT WARNING — high cylinder head temp"));
        warn = true;
    }
    
    // Load factor warning (>3.5g in flight)
    float total_g = sqrtf(d.ax_g*d.ax_g + d.ay_g*d.ay_g + d.az_g*d.az_g);
    if (total_g > 3.5f) {
        Serial.print(F("! HIGH G WARNING: "));
        Serial.print(total_g, 1);
        Serial.println(F("g"));
    }
}

// ─── SD Logging ───────────────────────────────────────────────
void writeLog(const SensorData& d, unsigned long t_ms) {
    char buf[200];
    snprintf(buf, sizeof(buf),
        "%lu,%06lu,%.6f,%.6f,%.1f,%.1f,"   // millis, gps_time, lat, lon, alt, spd
        "%.1f,%.2f,"                         // baro_alt, baro_pres
        "%.0f,%.0f,%.0f,%.0f,"              // egt1, egt2, cht1, cht2
        "%.2f,%.1f,"                         // airspeed m/s, kts
        "%.3f,%.3f,%.3f,"                    // accel xyz
        "%.2f,%.2f,%.2f",                    // gyro pqr
        t_ms,
        (unsigned long)d.gpsTime,
        (double)d.lat, (double)d.lon,
        (double)d.gpsAlt_m, (double)d.gpsSpd_kts,
        (double)d.baroAlt_m, (double)d.baroPres_hPa,
        (double)d.egt1_C, (double)d.egt2_C,
        (double)d.cht1_C, (double)d.cht2_C,
        (double)d.airspeed_ms, (double)d.airspeed_kts,
        (double)d.ax_g, (double)d.ay_g, (double)d.az_g,
        (double)d.gp_dps, (double)d.gq_dps, (double)d.gr_dps
    );
    
    logFile.println(buf);
    
    // Flush every 5 seconds to avoid SD card write failures in turbulence
    static uint8_t flushCount = 0;
    if (++flushCount >= LOG_RATE_HZ * 5) {
        flushCount = 0;
        logFile.flush();
    }
}

// ─── Serial Status Display ────────────────────────────────────
void printStatus(const SensorData& d) {
    Serial.print(F("GPS:"));
    if (d.gpsValid) {
        Serial.print(d.gpsSpd_kts, 1);
        Serial.print(F("kts "));
        Serial.print(d.gpsAlt_m, 0);
        Serial.print(F("m"));
    } else {
        Serial.print(F("NO FIX"));
    }
    
    Serial.print(F("  IAS:"));
    Serial.print(d.airspeed_kts, 1);
    Serial.print(F("kts"));
    
    Serial.print(F("  ALT:"));
    Serial.print(d.baroAlt_m, 0);
    Serial.print(F("m"));
    
    Serial.print(F("  EGT:"));
    Serial.print(d.egt1_C, 0);
    Serial.print(F("/"));
    Serial.print(d.egt2_C, 0);
    Serial.print(F("C  CHT:"));
    Serial.print(d.cht1_C, 0);
    Serial.print(F("/"));
    Serial.print(d.cht2_C, 0);
    Serial.print(F("C"));
    
    Serial.print(F("  G:"));
    float g_total = sqrtf(d.ax_g*d.ax_g + d.ay_g*d.ay_g + d.az_g*d.az_g);
    Serial.print(g_total, 2);
    Serial.print(F("g"));
    
    if (sdOk) {
        Serial.print(F(" [LOG]"));
    } else {
        Serial.print(F(" [NO SD]"));
    }
    
    Serial.println();
}
