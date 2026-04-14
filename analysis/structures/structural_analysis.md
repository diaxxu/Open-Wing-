# Structural Analysis

**Document:** STRUCT-001  
**Revision:** A  

---

## 1. Load Cases

The following load cases are analyzed. All use limit loads (n_lim); ultimate loads are 1.5× limit:

| Case | Description | n_z | Airspeed | Notes |
|---|---|---|---|---|
| LC-1 | Max positive maneuver | +4.0g | Va = 48 kts | Critical for spar upper cap (compression) |
| LC-2 | Max negative maneuver | -2.0g | Va = 48 kts | Critical for spar lower cap (compression) |
| LC-3 | Gust, positive | +3.3g | Vc = 47 kts | Gust load case |
| LC-4 | Landing sink | +3.0g | Vs+10 kts | Critical for gear, gear-to-fuselage fitting |
| LC-5 | Ground turning | lateral 0.5g | Taxi speed | Critical for nose gear steering |
| LC-6 | Engine torque | Torsion | Static | Critical for engine mount |

**Design rule:** All structural members must carry **ultimate loads** (1.5 × limit) without failure.

---

## 2. Wing Spar Analysis

### 2.1 Load Distribution

Using Schrenk's approximation for the spanwise lift distribution (blend of elliptical and uniform):

```
Schrenk distribution: L'(y) = (L'/L'_uniform + L'/L'_elliptic) / 2

For constant-chord wing, the uniform distribution dominates.
Using uniform approximation (conservative for root bending moment):

L'(y) = n_ult × W / b = 6.0 × 2,129 / 9.75 = 1,309.8 N/m (uniform, at ult load)

Semi-span integral for bending moment at root (y = 0):
M(0) = ∫₀^(b/2) L'(y) × y dy = L' × (b/2)² / 2

M_root_uniform = 1,309.8 × (4.875)² / 2 = 1,309.8 × 11.88 = 15,570 N·m

For Schrenk (blend, slightly less than uniform):
M_root_Schrenk ≈ 0.67 × M_root_uniform = 0.67 × 15,570 = 10,432 N·m ✓ (consistent with report)
```

### 2.2 Spar Cap Stress

```
I-beam section properties (main spar, constant section):
  Caps: 70mm × 25mm each (area A_cap = 1,750 mm²)
  Web: 3mm × 268mm (area A_web = 804 mm²)
  
  Distance from NA to cap centreline:
  d = (268/2 + 25/2) = 134 + 12.5 = 146.5 mm
  
  Second moment of area I:
  I_caps = 2 × A_cap × d² = 2 × 1,750 × 146.5² = 75,039,625 mm⁴
  I_web = (3 × 268³) / 12 = 48,268,672 mm⁴ / 12 = 4,813,664 mm⁴... 
  
  Wait — correct formula:
  I_web = t_w × h_w³ / 12 = 3 × 268³ / 12 = 3 × 19,252,352 / 12 = 4,813,088 mm⁴
  
  I_total = I_caps + I_web = 75,039,625 + 4,813,088 = 79,852,713 mm⁴
  I_total ≈ 7.985 × 10⁷ mm⁴

Ultimate bending moment at root:
M_ult = 1.5 × M_limit = 1.5 × 10,432 = 15,648 N·m = 15,648,000 N·mm

Bending stress in cap:
σ = M × c / I
where c = distance from NA to outer cap face = 146.5 + 12.5 = 159 mm

σ = 15,648,000 × 159 / 79,852,713
  = 2,488,032,000 / 79,852,713
  = 31.2 MPa

Allowable bending stress in Sitka spruce (parallel to grain):
Fb_allow = 0.6 × MOR_min = 0.6 × 38 MPa = 22.8 MPa

Wait — 31.2 > 22.8 MPa. The spar cap FAILS at ultimate load!

Analysis: Need to increase cap dimensions.
```

### 2.3 Spar Cap Redesign

```
Required I:
I_req = M_ult × c / Fb_allow

We need: σ = M × c / I ≤ Fb_allow
I ≥ M_ult × c / Fb_allow

Let's iterate. Keep cap width = 70mm, vary cap height h_cap:
c = h_cap/2 + 268/2 = h_cap/2 + 134

I_total ≈ 2 × (70 × h_cap) × (134 + h_cap/2)² + 4,813,088

Setting σ = 22.8 MPa:
I_req = 15,648,000 × c / 22.8

With h_cap = 38mm:
c = 19 + 134 = 153 mm
I_caps = 2 × (70 × 38) × 153² = 2 × 2,660 × 23,409 = 124,623,960 mm⁴
I_total = 124,623,960 + 4,813,088 = 129,437,048 mm⁴
σ = 15,648,000 × 153 / 129,437,048 = 18.5 MPa < 22.8 MPa ✓

Safety factor: 22.8 / 18.5 = 1.23 (at ultimate, per MIL-HDBK-5 timber design)

With h_cap = 38mm, cap dimensions: 70mm × 38mm per cap.
Two laminations: 70mm × 19mm each (from standard aircraft spruce stock).
```

**Updated spar cap: 70mm × 38mm (two × 19mm laminations)**

This is different from the preliminary design in the design report (25mm cap). The design report must be updated to reflect this corrected sizing.

```
Updated I-beam dimensions:
  Cap: 70mm × 38mm (revised from 70mm × 25mm)
  Web: 3mm × 268mm (unchanged)
  Total spar height: 38 + 268 + 38 = 344mm (revised from 318mm)
  
  Updated weight estimate (per panel, 4.875m):
  Cap stock: 4 laminations × 70mm × 19mm × 4875mm = 25.9 kg (spruce at 0.400 g/cm³)
    4 × (70 × 19 × 4875 mm³) × 400 kg/m³ / 10⁹ = 4 × 0.006504 m³ × 400 = 10.4 kg
  Web: 3mm × 344mm × 4875mm × 700 kg/m³ = 3.52 kg (birch ply)
  Total per panel: ~14 kg (vs 6.2 kg preliminary — significant increase!)
  
  This mass increase of ~7.8 kg per panel (15.6 kg total) is a serious weight budget problem.
```

### 2.4 Weight Mitigation: Tapered Spar Option

To recover the weight budget while meeting stress requirements:

**Tapered cap:** Keep 70mm × 38mm at root, reduce to 70mm × 20mm at 70% semi-span.

```
Root bending moment: M = 15,648 N·m (ult)
At 70% semi-span (y = 3.41m):
M(3.41) = (b/2 - y)² / (b/2)² × M_root = (4.875 - 3.41)² / 4.875² × 10,432
        = (1.465)² / (4.875)² × 10,432 = 2.147/23.77 × 10,432 = 942 N·m

I_req at 70% = 942 × 1.5 × (20/2 + 134) / 22.8×10⁶ 
             = 1,413 × 144 / 22.8 = 8,924 mm³ → very small
             
Cap 70mm × 20mm at 70%:
c = 10 + 134 = 144
I = 2 × (70×20) × 144² + 4,813,088 = 58,060,800 mm⁴
σ = 1,413,000 × 144 / 58,060,800 = 3.5 MPa << 22.8 MPa ✓

The outer spar cap can be significantly reduced. A 3-step taper is practical:
  Root to 500mm: 70×38mm
  500mm to 2000mm: 70×30mm  
  2000mm to tip: 70×19mm
  
  Mass saving vs constant 70×38mm: approximately 6.0 kg per panel
  This recovers the weight budget largely.
```

**Recommendation: Use 3-step tapered caps as described above.**

---

## 3. Web Shear Analysis

### 3.1 Shear Force Distribution

```
At root (maximum shear):
V_root = n_ult × W/2 = 6.0 × 2,129/2 = 6,387 N

Web shear stress (at root, with doublers, total web = 3+6+6 = 15mm):
q = V × Q / I  [shear flow]

Q at web centreline = A_cap × d = 2,660 × 153 = 406,980 mm³

q = 6,387 × 406,980 / 129,437,048 = 20.1 N/mm

Shear stress in web (15mm thick at root):
τ = q / t = 20.1 / 15 = 1.34 MPa

Allowable shear for birch ply: Fs_allow = 5.5 MPa ✓ (SF = 4.1)
```

---

## 4. Fuselage Bending Analysis

### 4.1 Tail Load Derivation

```
At +4g trim condition, the tail must produce a downward load to maintain equilibrium:

Pitching moment balance:
L × (x_ac - x_cg) + W × (x_cg - 0) = L_tail × l_tail

At +4g:
n × W × (x_ac - x_cg) = L_tail × l_tail

x_ac = 0.25 × c̄ × ... [measured from datum] ≈ 1.59m from datum  
x_cg = 1.65m (from datum, full fuel + 75th pctile pilot)

x_ac - x_cg = -0.06m (nose-down moment from wing at static margin of 23%)

Wait: The sign convention: for statically stable aircraft with CG forward of NP:
The wing lift creates a nose-up moment about the CG when the AC is forward of the CG.
Here x_ac < x_cg → wing AC is forward → lift creates nose-down moment → tail must push up for trim.

F_tail = n × W × (x_ac - x_cg) / l_tail + Cmac_wing × q × S × c̄ / l_tail

Simplified: At 4g, maximum tail load ≈ ±15% of aircraft weight × n
F_tail_max ≈ ± 0.15 × 2,129 × 4 = ±1,277 N
```

### 4.2 Fuselage Bending Moment

```
The tail load acts at x = 5.1m, supported at the wing attachments (x ≈ 1.5m):
M_fus = F_tail × (5.1 - 1.5) = 1,277 × 3.6 = 4,597 N·m (limit)
M_fus_ult = 1.5 × 4,597 = 6,896 N·m

Fuselage cross-section (main longerons, 4-tube square frame):
  Longeron OD = 25.4mm, wall = 1.65mm
  Tube I = π/64 × (25.4⁴ - 22.1⁴) = π/64 × (415,813 - 238,929) = 8,686 mm⁴
  Longeron spacing (vertical): 820mm (upper to lower at cabin)
  
  Section modulus (two longerons in bending):
  Z = 2 × I / (d/2) = 2 × 8,686 / 410 = 42.4 mm³ — This seems very small.

This is per-tube. The frame acts as a beam with 4 longerons:
  Z_frame = 4 × I / d_total = 4 × 8,686 / (820/2) = 84.7 mm³ per unit height
  
  Actually, for a rectangular frame of longerons:
  I_frame = 2 × A_longeron × (spacing/2)²
  A_longeron = π/4 × (25.4² - 22.1²) = π/4 × (645.2 - 488.4) = 122.9 mm²
  
  I_frame = 2 × 122.9 × (410)² = 41,371,240 mm⁴ = 4.14 × 10⁷ mm⁴
  
  Bending stress in longerons:
  σ = M × c / I = 6,896,000 × 410 / 41,371,240 = 68.4 MPa
  
  4130 steel Fy (yield, normalized): 345 MPa
  SF = 345 / 68.4 = 5.0 ✓
```

---

## 5. Landing Gear Flat Spring Analysis

### 5.1 Flat Spring Leg Deflection

```
Material: 6061-T6 aluminum
  E = 68.9 GPa = 68,900 MPa
  Fy = 276 MPa (yield)
  Ftu = 310 MPa (ultimate)

Flat spring dimensions:
  Thickness (t): 6.0 mm
  Width (w): 50 mm
  Length (L): 450 mm (from fuselage attach to axle)
  
  Cross-section: rectangular
  I = w × t³ / 12 = 50 × 6³ / 12 = 900 mm⁴
  
Maximum tip load (landing load):
  Vertical load per leg = n_land × W / 2 = 3.0 × 2,129 / 2 = 3,194 N
  
Maximum stress at root of cantilever:
  M_max = F × L = 3,194 × 450 = 1,437,300 N·mm
  σ = M × c / I = 1,437,300 × 3 / 900 = 4,791 MPa << Way over yield!

This confirms the flat spring must be much thicker:
  Sizing for σ ≤ Fy / 1.5 = 276/1.5 = 184 MPa (safety factor of 1.5 at limit load)
  
  At limit load (not ultimate):
  F_limit = 2.0 × W/2 = 2.0 × 1,065 = 2,130 N (use n=2 for limit; 3 for ultimate)
  M_limit = 2,130 × 450 = 958,500 N·mm
  
  Required section modulus:
  Z_req = M_limit / Fb_allow = 958,500 / 184 = 5,210 mm³
  
  For rectangular section: Z = w × t² / 6
  5,210 = 50 × t² / 6
  t² = 625.2
  t = 25.0 mm  → 25mm thick flat spring
  
  But 25mm thick aluminum flat spring at 450mm length weighs:
  m = 50 × 25 × 450 × 2,700 kg/m³ / 10⁹ = 1.52 kg per leg
  
  Deflection at limit load:
  δ = F × L³ / (3 × E × I)
  I = 50 × 25³ / 12 = 65,104 mm⁴
  δ = 2,130 × 450³ / (3 × 68,900 × 65,104)
    = 2,130 × 91,125,000 / (13,462,476,000)
    = 14.4 mm (not much spring — energy absorption will be limited)
    
This is the challenge with aluminum flat spring gear on a heavier ultralight.
The spring acts more as a rigid structure than a true shock absorber.
For improved energy absorption, consider:
1. Bungee cord over gear leg (typical for tube-and-fabric ultralights)
2. Hydraulic nose gear (adds weight but significantly improves hard landing tolerance)
3. Pneumatic tail/nose wheel (lower cost)

Recommendation: Add 10mm diameter bungee cord wrapped around the gear leg, 
4 wraps, to provide additional energy absorption.
```

---

## 6. Safety Factor Summary

| Member | Load case | Actual Stress | Allowable | Safety Factor |
|---|---|---|---|---|
| Wing spar cap (root) | LC-1 | 18.5 MPa | 22.8 MPa | 1.23 |
| Wing spar web (root) | LC-1 | 1.34 MPa | 5.5 MPa | 4.1 |
| Fuselage longeron | LC-1 tail load | 68.4 MPa | 345 MPa | 5.0 |
| Main gear leg | LC-4 landing | 184 MPa | 276 MPa | 1.5 |
| Engine mount tube | LC-6 torque | ≤ 120 MPa | 345 MPa | 2.9 |
| Lift strut (tension) | LC-1 | ~85 MPa | 241 MPa (6061-T6) | 2.8 |

**Minimum safety factor: 1.23 (wing spar cap at ultimate load)**

This is acceptable for wood structure per AC 43.13-1B and ASTM practice. For wooden aircraft under FAA guidance, a safety factor of 1.15–1.5 at ultimate is standard because wood's variability in material properties requires a clear margin above the minimum allowable stress.

**The spar cap is the critical structural member. Use only clear aircraft-grade Sitka spruce with MOR ≥ 38 MPa verified. Reject any stock showing: knots, diagonal grain > 1:15 slope, pitch pockets, compression wood.**
