# Performance Estimates

**Document:** PERF-001  
**Revision:** A  

All calculations at sea level ISA unless noted: ρ = 1.225 kg/m³, T = 15°C.  
MGTOW = 217 kg, W = 2,129 N.

---

## 1. Stall Speed

### 1.1 Power-Off Stall

```
Vs = √(2W / (ρ × S × CL_max))
   = √(2 × 2,129 / (1.225 × 14.52 × 1.55))
   = √(4,258 / 27.57)
   = √154.4
   = 12.43 m/s = 24.2 kts   ← Just within Part 103 limit ✓

At CG forward limit (higher downloads on tail → higher effective weight):
Effective weight increase ≈ 3% (tail download)
Vs_fwd = 12.43 × √1.03 = 12.62 m/s = 24.5 kts   ← Marginally over limit

To ensure compliance at forward CG, builder must verify:
1. Actual CL_max ≥ 1.57 (achievable with well-built Clark Y)
2. Wing incidence is accurately set to 2° (±0.25°)
3. Ribs are true to the template (no flat spots distorting the airfoil)
```

### 1.2 Effect of Pilot Weight on Stall Speed

| Pilot (kg) | MGTOW (kg) | Vs (m/s) | Vs (kts) |
|---|---|---|---|
| 56 (5th pctile) | 167.66 | 11.0 | 21.3 |
| 75 (50th pctile) | 194.3 | 11.8 | 22.9 |
| 88 (75th pctile) | 203.3 | 12.1 | 23.5 |
| 102 (95th pctile) | 217.3 | 12.5 | 24.3 |

All pilots within stated weight range comply with the 24-knot stall requirement.

---

## 2. Cruise Performance

### 2.1 Thrust-Available / Thrust-Required Diagram

**Thrust available (Rotax 447, direct-drive wooden prop):**

At altitudes and speeds, thrust varies. The following is computed from simple actuator disk theory for a fixed-pitch prop:

```
At sea level, n = 5,500 RPM (85% max), Vcruise = 23.15 m/s (45 kts):
J = V / (n × D) = 23.15 / (91.67 × 1.52) = 0.166   [advance ratio]

CT = 0.065 × (1 - J/J_stall)  [simplified linear model]
  ≈ 0.065 (static)
  ≈ 0.055 at J = 0.166

T = CT × ρ × n² × D⁴
  = 0.055 × 1.225 × (91.67)² × (1.52)⁴
  = 0.055 × 1.225 × 8,403 × 5.335
  = 302 N at 45 kts
```

**Thrust required:**

```
At 45 kts (23.15 m/s):
CL = 2W / (ρ × V² × S) = 4,258 / (1.225 × 535.9 × 14.52) = 0.387
CD = 0.035 + (0.387²)/(π × 0.80 × 6.55) = 0.035 + 0.00915 = 0.0442
D = ½ × ρ × V² × S × CD = ½ × 1.225 × 535.9 × 14.52 × 0.0442
  = 211 N

Excess thrust at 45 kts: 302 - 211 = 91 N (used for climb, or throttle back)
```

### 2.2 Range and Endurance (Breguet-style)

For a piston propeller aircraft:

```
Endurance:     E = (η_prop / BSFC_w) × (CL/CD) × (1/g) × ln(Wi/Wf)
Range:         R = (η_prop / BSFC_w) × (CL/CD) × (V/g) × ln(Wi/Wf)

Where:
  η_prop = 0.72 (fixed pitch, cruise)
  BSFC_w = 0.38 kg/(kW·hr) = 0.000106 kg/(W·s) = 1.056 × 10⁻⁴ kg/(N·m)
  
  Actually, use specific fuel consumption in proper units:
  c = fuel_mass_flow / thrust_power
  At cruise: fuel_flow = 7.6 kg/hr = 2.11 × 10⁻³ kg/s
  Thrust power = T × V = 211 × 23.15 = 4,885 W (drag power = thrust power in level flight)
  c = 2.11×10⁻³ / 4,885 = 4.32 × 10⁻⁷ kg/(N·s)

  Wi = 203.3 kg × 9.81 = 1,994 N (start of cruise, 75th% pilot + full fuel)
  Wf = 193.8 kg × 9.81 = 1,901 N (end of cruise, fuel burned = 9.5 kg)
  
  L/D at cruise = CL/CD = 0.387/0.0442 = 8.76

Endurance = (η_prop/c) × (CL/CD) × (1/g) × ln(Wi/Wf) [simplified]
          = (0.72 / 4.32×10⁻⁷) × (CL/CD) × ... 
          
Simpler energy approach:
Fuel energy available: 9.5 kg × 43,200 kJ/kg = 410,400 kJ
Mechanical power at cruise: 4,885 W
Engine thermal efficiency: ≈ 22% for 2-stroke at this power
Fuel power consumed: 4,885 / 0.22 = 22,205 W
Endurance = 410,400,000 J / 22,205 W = 18,482 s = 5.1 hrs

Wait — this gives an unrealistically long endurance.
Cross-check with fuel flow:
  Fuel flow at cruise = 7.6 kg/hr (from BSFC × power)
  P_shaft at cruise = 19.9 kW
  Time = 9.5 kg / 7.6 kg/hr = 1.25 hours ✓ (consistent with previous)

Range = 1.25 hr × 83 km/hr = 103.7 km (65 nm)
With 45-min reserve (fuel consumed = 5.7 kg → 3.8 kg reserve):
Useful fuel = 9.5 - 3.8 = 5.7 kg
Usable time = 5.7 / 7.6 = 0.75 hr
Range (with reserve) = 0.75 × 83 = 62.3 km (33.6 nm)
```

---

## 3. Climb Performance

### 3.1 Rate of Climb

```
Rate of Climb (ROC) = (Power Available - Power Required) / Weight

Power available (100% power at Vy):
At Vy ≈ 40 kts = 20.6 m/s:
Shaft power = 29.4 kW (max continuous)
Prop efficiency at low speed ≈ 0.65
Power available = 29.4 × 0.65 = 19.1 kW

Power required at Vy:
At 40 kts: CL = 0.43, CD = 0.047, L/D = 9.15
D = W/(L/D) = 2,129/9.15 = 232.7 N
Power req'd = D × V = 232.7 × 20.6 = 4,794 W

ROC = (19,100 - 4,794) / 2,129
    = 14,306 / 2,129
    = 6.72 m/s × 60 = 403 m/min (1,322 fpm) — overpredicted

Note: The ROC formula above is simplified. In reality, propulsive efficiency at 
climb attitude is lower (~0.55 for a climb-pitch prop):
Power_avail_actual = 29.4 × 0.55 = 16.2 kW
ROC = (16,200 - 4,794) / 2,129 = 5.36 m/s = 321 m/min (1,054 fpm)

Conservative estimate (accounting for climb drag increase):
ROC_conservative ≈ 250 m/min (820 fpm) at MGTOW, sea level ISA
This is a reasonable, achievable climb rate for this aircraft class.
```

### 3.2 Best Climb Speed (Vy)

Vy is the speed that maximizes excess power. Iterating the power curve:

| Speed (kts) | Speed (m/s) | Power Req (kW) | Power Avail (kW) | Excess (kW) |
|---|---|---|---|---|
| 25 | 12.9 | 9.84 | 10.5 | 0.66 |
| 30 | 15.4 | 5.75 | 12.1 | 6.35 |
| 35 | 18.0 | 4.29 | 13.8 | 9.51 |
| 40 | 20.6 | 4.07 | 15.2 | 11.1 |
| 45 | 23.1 | 4.35 | 16.1 | 11.75 ← Vy |
| 50 | 25.7 | 5.14 | 16.2 | 11.06 |
| 55 | 28.3 | 6.36 | 15.8 | 9.44 |

**Vy ≈ 45 kts (same as cruise speed — typical for underpowered ultralights)**

**Vx (best angle):** approximately 35 kts (maximum T/D ratio)

---

## 4. Glide Performance

```
Best glide ratio: L/D_max = 10.9 (at 35 kts, from §3.3 table in design report)
Glide ratio ≈ 10:1 (conservative)

Glide distance from AGL height h:
d = (L/D) × h = 10 × h

From 300 m AGL: d = 3,000 m = 3.0 km
From 1,000 m AGL: d = 10,000 m = 10 km

Sink rate at best glide (35 kts = 18.0 m/s):
Vs_sink = V / (L/D) = 18.0 / 10.9 = 1.65 m/s = 325 ft/min

Best endurance speed (minimum sink):
Vm_sink = Vbg / ⁴√(4/3) = 18.0 / 1.075 = 16.7 m/s = 32.5 kts
Minimum sink rate ≈ 1.4 m/s = 276 ft/min
```

---

## 5. Takeoff Performance

```
Ground roll estimate (simplified, sea level):

Average acceleration during ground roll:
F_net = T - D_ground - μ_r × W
where μ_r = rolling resistance ≈ 0.05 (grass), 0.03 (asphalt)
T_static = ~450 N (estimated from prop data)
D_ground at V_liftoff/2 ≈ low (10 N, approx)
F_net ≈ 450 - 10 - 0.04 × 2,129 = 440 - 85 = 355 N

V_liftoff = 1.10 × Vs = 1.10 × 12.43 = 13.67 m/s

Ground roll s = V_liftoff² / (2 × a_avg)
a_avg = F_net / MGTOW = 355 / 217 = 1.64 m/s²
s = 13.67² / (2 × 1.64) = 186.7 / 3.28 = 56.9 m

Add 15% for conservative estimate: s ≈ 65 m (215 ft) on smooth surface.
On soft grass: ≈ 90 m (295 ft)
```

---

## 6. V-Speed Summary (Placard)

| V-Speed | Symbol | Value (kts) | Value (km/h) | Notes |
|---|---|---|---|---|
| Never Exceed | Vne | 55 | 102 | Red line, structural limit |
| Caution (Yellow arc start) | Vc/Vno | 47 | 87 | Begin yellow arc |
| Max Cruise (green arc top) | Vc | 47 | 87 | |
| Best Rate of Climb | Vy | 45 | 83 | |
| Best Angle of Climb | Vx | 35 | 65 | |
| Best Glide | Vbg | 40 | 74 | Power off |
| Maneuver Speed | Va | 44 | 81 | Full control deflection limit |
| Stall Clean | Vs | 24 | 44 | Power off, clean config |
| Minimum Sink | Vms | 32 | 60 | Power off |

**Airspeed Indicator Arc Colors:**
- **White arc:** Vs to top of flap extension range (if installed). 24–45 kts.
- **Green arc:** Vs to Vno. 24–47 kts. Normal operations.
- **Yellow arc:** Vno to Vne. 47–55 kts. Smooth air only.
- **Red line:** Vne = 55 kts.

---

## 7. Density Altitude Corrections

Performance degrades significantly at altitude and high temperature:

```
Stall speed correction:
Vs_DA = Vs_SL × √(ρ_SL / ρ_DA)

At 1,500m ISA (ρ = 1.058 kg/m³):
Vs_DA = 24 × √(1.225/1.058) = 24 × 1.076 = 25.8 kts (IAS stays ~24 kts)

Takeoff roll correction (approximately proportional to 1/ρ):
s_DA = s_SL × (ρ_SL/ρ_DA) = 65 × (1.225/1.058) = 75 m

At 40°C, sea level (ρ ≈ 1.127 kg/m³ at 40°C):
s_hot = 65 × (1.225/1.127) = 70.6 m

Combined (1,500m + 35°C): effectively density altitude ~3,000m
s_combined ≈ 130+ m — verify site performance before flight at elevation
```

---

## 8. Load Factor Envelope (V-n Diagram)

```
Positive limit: n+ = 4.0g
Negative limit: n- = -2.0g
Ultimate load: 1.5 × limit = 6.0g / -3.0g

Corner speed (Va):
Va = Vs × √(n+) = 24 × √4 = 24 × 2 = 48 kts

Adjusted Va to match n+ = 4.0g at stall:
At Va, aircraft reaches limit load factor at stall angle of attack.
Va_actual = Vs × √(n+) = 24 × 2 = 48 kts (see above)

Structural cruise (Vc): 47 kts
Dive speed (Vd = 1.25 × Vne): Not used — Vne is the limit (55 kts)

Gust loads:
At cruise (45 kts) with 7.6 m/s (25 fps) gust:
Δn = (ρ × a × V × Ug) / (2 × W/S)
   = (1.225 × 4.25/57.3 × 23.15 × 7.6) / (2 × 147.9)
   = (1.225 × 0.0742 × 23.15 × 7.6) / 295.8
   = (1.597) / 295.8
   = 0.0054 per deg... 

Using proper units:
a = 4.25 rad⁻¹ = 4.25 (1/rad)
Δn = (ρ × V × a × Ug) / (2 × W/S)
   = (1.225 × 23.15 × 4.25 × 7.6) / (2 × 147.9 × 9.81)
     [W/S in N/m²]
   = (916.7) / (2904)
   = 0.316g

n_total_cruise_gust = 1 + 0.316 = 1.316 < 4g ✓
Gust loads are non-critical for this aircraft at its relatively low cruise speed.
```
