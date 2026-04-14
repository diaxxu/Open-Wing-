# Avionics and Electrical Systems

**Document:** ELEC-001  
**Revision:** A  

---

## 1. Design Philosophy

The avionics suite is intentionally minimalist. FAR Part 103 does not require any instruments or avionics. However, safe flight requires at minimum:

1. Airspeed indication
2. Altitude awareness
3. Engine health monitoring (EGT/CHT)
4. Compass for navigation

Everything beyond this list is optional. The electrical system is 12V DC, negative-ground, using an automotive-style battery purely for ignition backup and instrumentation. The Rotax 447 has a built-in magneto ignition that runs independent of battery voltage — the battery is **not** required for engine operation once started.

**Total electrical load at cruise: ≤ 8W (instruments + lighting if any)**  
**Battery capacity: 5 Ah @ 12V = 60 Wh → 7.5 hours at 8W**  
The battery is a failsafe, not a primary power source.

---

## 2. Required Instruments (Minimum Safe Configuration)

| Instrument | Type | Source | Cost (approx) |
|---|---|---|---|
| Airspeed indicator (ASI) | Mechanical, pitot-static | Aircraft Spruce, Wicks | $60–$120 |
| Altimeter | Mechanical, static port | Aircraft Spruce, Wicks | $80–$150 |
| Compass | Magnetic, wet | Any aviation supplier | $25–$60 |
| EGT gauge | Thermocouple, 2-cyl | UMA, Grand Rapids | $45–$90 |
| CHT gauge | Thermocouple, 2-cyl | UMA, Grand Rapids | $45–$90 |
| Oil pressure gauge | Mechanical, 0–100 PSI | Westach, Aircraft Spruce | $35–$75 |
| Tachometer | Electronic, magneto pickup | Tiny Tach, Westach | $30–$70 |

**Total minimum instrument cost: $320–$655**

---

## 3. Pitot-Static System

### 3.1 Pitot Tube

A simple aluminum pitot tube fabricated from 6.35mm (¼") OD aluminum tube:

```
Pitot tube geometry:
  Location: Left wing leading edge, 500mm outboard of root
  Height above wing surface: 150mm
  Orientation: Aligned with chord line (parallel to FRL at 0° AoA)
  
  Construction:
  - 6.35mm OD × 0.89mm wall 6061-T6 tube, 200mm long
  - Bend at 90° for pitot inlet facing forward
  - Drill 3× 1.5mm drain holes at lowest point
  - Connect to ASI with 4mm OD flexible PVC tubing
  
  Install away from propwash and wake interference.
  Mount with 2× AN526-10R sheet metal screws through aluminum tab.
```

### 3.2 Static Port

```
Static port: 2× holes, 3mm diameter, one each side of fuselage
Location: x = 2.5m aft of datum (mid-fuselage, away from high-velocity regions)
Height: Mid-fuselage on the neutral pressure line

Static port fabrication:
  - Clean 3mm hole in aluminum skin, perpendicular to surface
  - Debur completely (rough edge causes pressure error)
  - Install AN fitting or push-fit plastic barb
  - Cross-connect port and starboard lines with T-fitting to average pressure
  - Route to ASI and altimeter static ports

Static error test (before first flight):
  Block pitot, open static. Airspeed should read zero.
  Block both, gently blow into pitot: ASI should increase.
  If VSI drifts on ground with wind: static port is in bad location — move it.
```

---

## 4. Engine Monitoring

### 4.1 EGT/CHT Wiring

The Rotax 447 has two cylinders. Each requires one EGT (exhaust gas temperature) and one CHT (cylinder head temperature) thermocouple.

```
Thermocouple types:
  EGT: Type K (NiCr/NiAl), rated to 1250°C, stainless-sheathed
  CHT: Type K, bayonet-style, fits standard Rotax CHT boss
  
EGT probe installation:
  Location: 50–75mm downstream of exhaust port on each cylinder
  Clamp with exhaust clamp or drill/tap for bung fitting
  
Normal EGT ranges (Rotax 447):
  Cruise: 600–750°C
  Maximum continuous: 850°C
  Danger: >900°C (lean mixture, risk of piston damage)
  
CHT ranges:
  Cruise: 160–210°C
  Maximum: 230°C
  Danger: >250°C
```

### 4.2 Oil Pressure Monitoring

```
Rotax 447 oil injection system — monitor with 0–100 PSI sender
Sender: Bourdon tube type, 1/8" NPT, standard automotive

Normal oil pressure: 50–70 PSI at cruise RPM
Minimum: 35 PSI (below this: reduce power, check immediately)
Maximum: 90 PSI (cold start, normal — will drop as oil warms)
```

---

## 5. Electrical System Wiring

### 5.1 System Architecture

```
POWER DISTRIBUTION:

[Rotax 447 Alternator/Generator 12V, ~90W]
          │
          ▼
[Battery Isolator Diode]
          │
    ┌─────┴──────┐
    │            │
[12V, 5Ah     [Main Bus Bar]
 Battery]       │
    │           ├── [5A] → ASI/Altimeter (none, mechanical)
    │           ├── [5A] → EGT/CHT Display
    │           ├── [5A] → Tachometer
    │           ├── [5A] → Oil Pressure Gauge
    │           ├── [5A] → Position Lights (optional)
    │           ├── [10A] → Ignition system (dual CDI)
    │           └── [Main switch / Kill switch]
    │
    └── [Battery Master Switch (SPST)]
```

### 5.2 Wire Gauge Table

| Circuit | Current Draw | Wire Gauge | Wire Type |
|---|---|---|---|
| Main power feed from alternator | 10A max | 14 AWG | MIL-W-22759 |
| Battery feed to main bus | 10A max | 14 AWG | MIL-W-22759 |
| Ignition (dual CDI) | 5A | 16 AWG | MIL-W-22759 |
| EGT/CHT display | 0.5A | 22 AWG | MIL-W-22759 |
| Tachometer | 0.1A | 22 AWG | MIL-W-22759 |
| Thermocouple extension | <0.05A | Thermocouple extension wire (Type K) | Match thermocouple type |
| Ground bus | 10A total | 14 AWG | MIL-W-22759 |

> **Critical:** Use aviation-grade wire (MIL-W-22759, silver-plated copper with PTFE insulation) throughout. Automotive wire is acceptable as a cost substitute but degrades faster in aviation environments. Never use solid-conductor wire.

### 5.3 Circuit Protection

| Circuit | Fuse/Breaker | Type |
|---|---|---|
| Main bus feed | 15A | ATC blade fuse |
| Ignition | 5A | ATC blade fuse |
| Instruments | 5A | ATC blade fuse |
| Lights (if fitted) | 5A | ATC blade fuse |

Mount fuse block at instrument panel, accessible from cockpit without tools.

### 5.4 Grounding

```
Star ground topology: all components ground to a single copper buss bar
mounted on the firewall (negative terminal of battery).

Ground straps:
  - Engine block to firewall: 14 AWG, length ≤ 300mm, copper braided
  - Instrument panel to firewall: 16 AWG
  - Tail cone (static ports) to main bus: 18 AWG
  
Do NOT ground through aluminum tube members or the fuselage structure.
Current through structure causes corrosion at joints.
```

---

## 6. Kill Switch / Ignition Safety

The Rotax 447 uses a dual CDI (capacitive discharge ignition). Both circuits must be grounded to stop the engine:

```
Kill switch circuit:
  - SPST toggle switch, panel-mounted and labeled IGNITION / KILL
  - Switch in UP position = ignition ACTIVE (grounding wire open)
  - Switch in DOWN/KILL position = grounds both CDI kill wires → engine stops
  
  Wire:   2× 18 AWG from kill wire terminals on each CDI module → switch → ground

IMPORTANT: Test kill switch function on the ground before first flight.
           Pull switch to KILL at idle RPM — engine should stop within 3 seconds.
           Failure to stop: check wiring continuity, CDI ground path.
```

---

## 7. Optional: Arduino Telemetry Module

For builders wanting basic in-flight data logging, an Arduino Nano-based module can be added to log:
- GPS position and groundspeed (via NEO-6M or BN-220 GPS module)
- Barometric altitude (BMP280)
- EGT/CHT values (MAX31855 thermocouple amplifiers, one per K-type probe)
- Airspeed (differential pressure sensor: MPXV7002DP)
- G-force (MPU-6050 IMU)

**This is purely optional and does not affect airworthiness.** See `/electronics/firmware/` for the Arduino sketch.

### 7.1 Bill of Materials (Arduino Logger)

| Component | Part | Cost (USD) |
|---|---|---|
| Microcontroller | Arduino Nano Every | $11 |
| GPS module | BN-220 or NEO-6M | $12 |
| Baro sensor | BMP280 breakout | $3 |
| Thermocouple amp (×4) | MAX31855 breakout | $4 × 4 = $16 |
| Differential pressure | MPXV7002DP + ADC | $8 |
| IMU | MPU-6050 breakout | $3 |
| SD card logger | SPI SD module | $3 |
| SD card | 8GB microSD | $5 |
| Enclosure | 3D printed (PLA) | $2 |
| Connectors (JST, XT30) | Assorted | $8 |
| Wire | 26 AWG silicone | $5 |
| **Total** | | **~$76** |

Total added weight: ≈ 120g (negligible)
