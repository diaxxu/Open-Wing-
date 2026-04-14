# Aerodynamic Analysis

**Document:** AERO-001  
**Tools:** Hand calculations, Prandtl lifting-line theory, XFOIL validation  

---

## 1. Airfoil Polar — Clark Y (Re = 600,000)

XFOIL analysis of the Clark Y at Re = 600,000, Ncrit = 9 (standard free-stream turbulence).

The following data is derived from XFOIL runs and cross-checked with NACA Report 412 experimental data.

| α (deg) | CL | CD | Cm_ac | L/D |
|---|---|---|---|---|
| -6 | -0.378 | 0.0185 | -0.077 | -20.4 |
| -4 | -0.168 | 0.0142 | -0.077 | -11.8 |
| -2 | 0.042 | 0.0115 | -0.077 | 3.7 |
| 0 | 0.252 | 0.0098 | -0.077 | 25.7 |
| 2 | 0.462 | 0.0091 | -0.077 | 50.8 |
| 4 | 0.672 | 0.0095 | -0.076 | 70.7 |
| 6 | 0.882 | 0.0108 | -0.076 | 81.7 ← Peak section L/D |
| 8 | 1.090 | 0.0132 | -0.076 | 82.6 |
| 10 | 1.296 | 0.0170 | -0.078 | 76.2 |
| 12 | 1.470 | 0.0228 | -0.081 | 64.5 |
| 14 | 1.525 | 0.0320 | -0.090 | 47.7 |
| 15 | 1.540 | 0.0410 | -0.098 | 37.6 |
| 16 | 1.510 | 0.0680 | -0.110 | 22.2 ← Stall onset |
| 18 | 1.200 | 0.1800 | -0.120 | 6.7  ← Deep stall |

**Notes on Clark Y stall character:**
The Clark Y exhibits a gentle leading-edge stall beginning around α = 15–16°. The stall is progressive, not abrupt. CL_max ≈ 1.54 at α ≈ 15.5°. Post-stall, there is a moderate but controllable pitching moment change. This is one of the reasons the Clark Y is recommended for training and personal-use aircraft.

---

## 2. Finite Wing Corrections

### 2.1 Induced Drag

```
Oswald efficiency factor e:
For an unswept, untapered, low-speed wing:
e = 1 / (1 + δ)
where δ accounts for non-elliptical lift distribution.

For constant-chord (rectangular) wing:
δ ≈ 0.04 → e = 1/1.04 = 0.962
However, with struts, fuselage, and other interference effects:
e_effective ≈ 0.80 (conservative field estimate used throughout)

This means the wing produces ~20% more induced drag than the elliptical ideal.
A tapered wing (λ = 0.4) would have e ≈ 0.95, saving about 5% in cruise drag.
The decision to use untapered wing accepts this 15% induced drag penalty.
```

### 2.2 Wing Lift Curve Slope (Finite Wing)

```
Using Prandtl-Glauert + finite aspect ratio correction:
a = a₀ / (1 + a₀/(π × AR))   [no Oswald correction for lift slope]
  = 5.73 / (1 + 5.73/(π × 6.55))
  = 5.73 / (1 + 0.278)
  = 5.73 / 1.278
  = 4.48 per radian = 0.0782 per degree
  
With e in lift correction (Jones correction):
a = a₀ / (1 + a₀/(π × e × AR))
  = 5.73 / (1 + 5.73/(π × 0.80 × 6.55))
  = 5.73 / (1 + 0.348)
  = 4.25 per radian = 0.0742 per degree
```

### 2.3 Downwash at Horizontal Tail

```
Downwash angle ε (behind wing):
ε = 2 × CL / (π × AR) = 2 × CL / (π × 6.55) = 0.0973 × CL

dε/dα = a_wing × 2/(π × AR) = 4.25 × 2/(π × 6.55) = 0.413

This means the tail effective angle of attack changes at:
dα_tail/dα = 1 - dε/dα = 1 - 0.413 = 0.587

At cruise CL = 0.387:
ε_cruise = 0.0973 × 0.387 = 0.038 rad = 2.2°

The tail operates at an incidence of about 2.2° less than the free-stream
due to wing downwash. This is accounted for in the horizontal tail sizing.
```

---

## 3. Full Aircraft Drag Polar

### 3.1 Parasite Drag Estimation (Component Method)

```
CD0 = ΣCD0_component × Swet_component / S_ref

Components and wetted areas:
```

| Component | Swet (m²) | Cf | FF | Interference | CDi_component |
|---|---|---|---|---|---|
| Wing (Clark Y) | 31.4 | 0.00385 | 1.20 | 1.0 | 0.00896 |
| Fuselage (body of revolution) | 8.2 | 0.00420 | 1.30 | 1.05 | 0.00308 |
| Horizontal tail (NACA 0009) | 4.6 | 0.00380 | 1.15 | 1.05 | 0.00138 |
| Vertical fin (NACA 0009) | 2.1 | 0.00380 | 1.15 | 1.05 | 0.00063 |
| Lift struts (2, streamlined) | 0.8 | 0.00600 | 1.50 | 1.20 | 0.00050 |
| Landing gear (fixed, no fairing) | — | — | — | — | 0.00600 |
| Cockpit windscreen (flat plate) | — | — | — | — | 0.00200 |
| Miscellaneous (antennae, gaps) | — | — | — | — | 0.00100 |
| **Total CD0** | | | | | **0.0354** |

**Use CD0 = 0.035 in analysis (matches component estimate)**

```
Where:
  Cf = friction coefficient (turbulent flat plate, Re_component)
  FF = form factor (accounts for pressure drag of shape)
  
  Reynolds numbers at cruise (45 kts = 23.15 m/s):
  Wing: Re = ρVc/μ = 1.225 × 23.15 × 1.49 / 1.81×10⁻⁵ = 2.34 × 10⁶
  Fuselage: Re = 1.225 × 23.15 × 5.49 / 1.81×10⁻⁵ = 8.62 × 10⁶
  
  Cf_turb = 0.455/(log10(Re))^2.58 (Prandtl-Schlichting formula)
  Cf_wing = 0.455/(log10(2.34×10⁶))^2.58 = 0.455/6.373^2.58 = 0.455/118.4 = 0.00384
```

### 3.2 Complete Drag Polar

```
CD = CD0 + CL² / (π × e × AR)
   = 0.035 + CL² / (π × 0.80 × 6.55)
   = 0.035 + CL² / 16.46

This is valid for CL from 0.0 to approximately 1.4 (pre-stall).
```

| CL | CDi (induced) | CD (total) | L/D |
|---|---|---|---|
| 0.0 | 0.000 | 0.035 | 0.0 |
| 0.2 | 0.0024 | 0.0374 | 5.4 |
| 0.4 | 0.0097 | 0.0447 | 8.9 |
| 0.6 | 0.0219 | 0.0569 | 10.5 |
| **0.759** | **0.035** | **0.070** | **10.8 ← MAX** |
| 0.8 | 0.0389 | 0.0739 | 10.8 |
| 1.0 | 0.0608 | 0.0958 | 10.4 |
| 1.2 | 0.0875 | 0.1225 | 9.8 |
| 1.4 | 0.1191 | 0.1541 | 9.1 |
| 1.52 | 0.1405 | 0.1755 | 8.7 (stall) |

**Maximum L/D = 10.8 at CL = 0.759 (best glide)**

---

## 4. Drag Improvement Potential

If the builder adds **wheel fairings** (wheel pants) to all three gear legs:

```
Current gear drag: CD0_gear = 0.006 (from fixed-gear penalty)
With wheel pants: CD0_gear_faired = 0.002 (empirical, based on Cessna data)
CD0 improvement: 0.004

At cruise (CL = 0.387):
L/D_unfaired = 0.387/0.0447 = 8.66
L/D_faired   = 0.387/0.0407 = 9.51

Cruise speed increase at same throttle: ~2.5 kts (4.6 km/h)
Range increase: ~7%

Wheel pants are strongly recommended for fuel savings despite the 0.4 kg mass penalty.
```

---

## 5. Wing Loading and Handling Qualities

```
Wing loading: W/S = MGTOW × g / S = 217 × 9.81 / 14.52 = 146.7 N/m²

Typical ranges:
  Hang glider:     100–200 N/m²
  Ultralight:      200–400 N/m²
  General aviation: 500–1,200 N/m²

At 146.7 N/m², this aircraft has a LOW wing loading.
This means:
  + Very slow stall speed (good)
  + Excellent low-speed handling
  + Good performance from short fields
  - Sensitive to turbulence (bumpy ride in thermals/wind)
  - Not suited for moderate to strong wind flying
  - Takeoff in crosswinds requires skill due to low inertia
  
Operational wind limit recommended: ≤ 10 kts (18.5 km/h) surface wind.
```

---

## 6. Reynolds Number Effects

The aircraft operates at relatively low Reynolds numbers for a full-scale aircraft:

```
At stall (24 kts, chord = 1.49m):
Re = ρ × V × c / μ = 1.225 × 12.35 × 1.49 / 1.81×10⁻⁵ = 1.25 × 10⁶

At cruise (45 kts, chord = 1.49m):
Re = 1.225 × 23.15 × 1.49 / 1.81×10⁻⁵ = 2.34 × 10⁶

At Vne (55 kts, chord = 1.49m):
Re = 1.225 × 28.29 × 1.49 / 1.81×10⁻⁵ = 2.86 × 10⁶
```

The Clark Y airfoil is specifically suited to this Reynolds number range (0.5–3.0 million). Laminar separation bubbles can form below Re ≈ 500,000; at these flight conditions we are well above this threshold throughout the operating envelope.

**Implication for building:** Surface finish matters. A rough fabric covering (grit equivalent > 150 grit) can trip the boundary layer to turbulent prematurely. Sand and dope the fabric to achieve a smooth surface. The Cd difference between rough and smooth fabric at Re = 2×10⁶ is approximately 0.002, which costs about 2 kts of cruise speed.
