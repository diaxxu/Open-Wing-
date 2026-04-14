# Airfoil Selection — Clark Y Justification

**Document:** DR-002  
**Revision:** A  

---

## 1. Selection Methodology

Airfoil selection was conducted against four weighted criteria:

| Criterion | Weight | Description |
|---|---|---|
| Aerodynamic performance | 30% | CL_max, L/D, stall character |
| Constructional suitability | 35% | Ease of building accurate ribs |
| Data availability | 20% | Tested, documented, known behavior |
| Historical fleet experience | 15% | Proven in similar aircraft classes |

**The constructional suitability criterion is given the highest weight deliberately.** A theoretically superior airfoil built poorly will perform worse than a simpler airfoil built accurately. For a homebuilder, the ability to build the airfoil to profile within ±1mm is more important than 2% better peak L/D.

---

## 2. Candidates Evaluated

### 2.1 Clark Y

**Origin:** Virginius E. Clark, 1922. One of the most widely used low-speed airfoils in history.

**Key constructional advantage:** Flat lower surface from approximately 35–90% chord. This means:
- The rib lower surface cap strip sits on a flat reference datum
- The rib jig lower support is a single flat plane — no complex curving form required
- Dimensional verification is trivial: a flat rule against the lower surface detects any rib defect

**Aerodynamic characteristics at Re = 600,000:**
- CL_max: 1.47–1.61 (confirmed in NACA TN-412 and numerous subsequent tests)
- Max section L/D: ~82 at α = 8° (good for this class)
- Stall: gradual, with ample pre-stall buffet. Leading-edge-type stall initiating near the tip of the nose radius, NOT a sharp trailing-edge separation. Pilot has clear warning.
- Cm_ac: -0.077 (moderate nose-down pitching moment — requires tail download for trim, but this is normal for cambered airfoils)

**Historical record:** Used on the Aeronca C-2, C-3, many early Piper designs, countless homebuilt aircraft in the 1930s–1970s. The fleet experience is unmatched for a cambered, flat-bottom airfoil in this thickness range.

### 2.2 NACA 4412

**Characteristics:** 4% max camber at 40% chord, 12% thickness.  
CL_max ≈ 1.50, well-documented, excellent L/D.  
**Constructional issue:** Both upper and lower surfaces are curved throughout. No flat reference datum. Requires more complex rib jigging.  
**Verdict:** Good aerodynamic performance, but harder to build accurately. Rejected.

### 2.3 NACA 2412

**Characteristics:** 2% max camber, 12% thickness.  
CL_max ≈ 1.43, lower L/D than 4412.  
Lower camber makes CG balance easier (smaller Cm_ac magnitude).  
**Constructional issue:** Same as NACA 4412 — no flat reference surface.  
**Verdict:** Lower CL_max means larger required wing area for the stall limit. Rejected.

### 2.4 Eppler 193

**Characteristics:** Laminar-flow airfoil designed for low-speed motorgliders.  
CL_max ≈ 1.60, excellent L/D at low CL (≈16:1 section).  
**Constructional issue:** Laminar-flow airfoils are extremely sensitive to surface finish. At the expected Re (600,000–2,400,000), any surface roughness (typical of fabric-covered ribs) will trigger premature boundary layer transition, eliminating the laminar benefit. The airfoil designed for polished composite surfaces performs no better than Clark Y when built in fabric-covered wood.  
**Verdict:** Theoretical advantage evaporates in fabric construction. Rejected.

### 2.5 NACA 4415

**Characteristics:** More cambered (4%) and thicker (15%), giving CL_max ≈ 1.56.  
Good performance, but thicker spar (15% vs 11.7%) increases structural height unnecessarily.  
**Verdict:** Marginally competitive with Clark Y but no flat-bottom advantage. Rejected.

---

## 3. Scoring Matrix

| Airfoil | Aero (30%) | Construct (35%) | Data (20%) | History (15%) | Total |
|---|---|---|---|---|---|
| **Clark Y** | 7.5/10 (2.25) | **9.5/10 (3.33)** | 10/10 (2.00) | 10/10 (1.50) | **9.08** |
| NACA 4412 | 8.0/10 (2.40) | 6.5/10 (2.28) | 9.5/10 (1.90) | 7.5/10 (1.13) | 7.71 |
| NACA 2412 | 7.0/10 (2.10) | 6.5/10 (2.28) | 9.5/10 (1.90) | 8.0/10 (1.20) | 7.48 |
| Eppler 193 | 9.0/10 (2.70)* | 4.0/10 (1.40) | 7.0/10 (1.40) | 3.0/10 (0.45) | 5.95 |
| NACA 4415 | 7.8/10 (2.34) | 7.0/10 (2.45) | 9.5/10 (1.90) | 7.0/10 (1.05) | 7.74 |

*Eppler 193 aero score assumes ideal conditions; practical score is closer to 6.5 in fabric construction.

**Winner: Clark Y with a clear margin.**

---

## 4. Clark Y — Key Design Data Summary

```
Designation:      Clark Y (no NACA designation — predates NACA series system)
Year:             1922
Thickness:        11.7% of chord
Max camber:       3.3% at 42% chord
Zero-lift angle:  -4.0°
Lift slope:       0.105 per degree (section), 0.0742 per degree (finite wing, AR 6.55)
CL at 0°:         0.42 (approximate, based on zero-lift angle)
CL_max:           1.55 (conservative design value)
CL at max L/D:    ≈ 0.66
Max section L/D:  ≈ 82 (at α = 8°, Re = 600,000)
Cm_ac:            -0.077 (nose-down, stable with respect to pitch)
Flat bottom from: x/c = 0.35 to x/c = 0.90
```

---

## 5. Wing Incidence Setting

The Clark Y is installed at **+2° incidence** relative to the fuselage reference line (FRL).

**Rationale:**
At cruise CL = 0.387, the geometric angle of attack of the finite wing is:
```
α_cruise = (CL - CL_at_0°) / a = (0.387 - 0.42) / 0.0742 = ... 
Actually: α_cruise from zero lift: α = α₀ + CL/a
          α₀ = -4.0° (zero lift angle), a = 0.0742 deg⁻¹
          α_cruise = -4.0 + 0.387/0.0742 = -4.0 + 5.2 = +1.2° 
          (angle of attack relative to zero-lift line at cruise)
          
With wing incidence +2° relative to FRL:
  Wing angle to zero-lift line at cruise = 1.2°
  Fuselage pitch attitude at cruise = 1.2° - 2° = -0.8°
  (Fuselage is slightly nose-down at cruise — normal and comfortable for pilot)
```

A 2° incidence keeps the fuselage near-level at cruise, which is ergonomically correct and reduces parasite drag from the fuselage at a non-zero attitude.

---

## 6. Upper vs Lower Surface Finish

The Clark Y upper surface does most of the lifting. Surface finish affects transition from laminar to turbulent flow.

**At Re = 600,000–2,400,000 (our operating range):**

- Natural transition occurs at approximately 25–40% chord on the upper surface for a smooth airfoil
- Dacron fabric with dope finish has an equivalent roughness of approximately 0.2–0.4mm
- This triggers transition near the leading edge (turbulent from the start, essentially)
- The Clark Y is tolerant of this: its section drag at turbulent flow conditions is CD_section ≈ 0.010–0.012, compared to 0.007–0.008 at natural transition

**Practical implication:** Sand and dope to the smoothest finish achievable. Each order-of-magnitude improvement in surface roughness saves approximately 0.001 in CD0, which translates to ~1.5 kts at cruise.

The effort of achieving a glass-smooth finish on a fabric-covered wing is high. Two smooth coats of dope plus wet-sanding with 400-grit achieves a good result within 3× the laminar-flow ideal.
