# Wing Rib — Clark Y Airfoil

**Part number:** WG-RIB-001  
**Material:** 3mm aircraft birch plywood (ribs) or shaped foam (EPS 40 kg/m³)  
**Quantity:** 32 (16 per wing panel)  
**Spacing:** 300 mm center-to-center  

---

## Clark Y Scaled Coordinates

Chord = 1,490 mm. Coordinates below are (x, y) in mm from leading edge.

The Clark Y has a **flat lower surface from approximately x = 520 mm to x = 1,340 mm** (35% to 90% chord). This is the key constructional advantage.

### Upper Surface (x_mm, y_upper_mm)

| Station | x (mm) | y_upper (mm) |
|---|---|---|
| 0 | 0.0 | 0.0 |
| 1.25% | 18.6 | 29.3 |
| 2.5% | 37.3 | 39.4 |
| 5.0% | 74.5 | 52.8 |
| 7.5% | 111.8 | 61.1 |
| 10% | 149.0 | 67.0 |
| 15% | 223.5 | 75.5 |
| 20% | 298.0 | 80.7 |
| 25% | 372.5 | 83.4 |
| 30% | 447.0 | 83.6 |
| 35% | 521.5 | 81.9 |
| 40% | 596.0 | 78.4 |
| 45% | 670.5 | 73.7 |
| 50% | 745.0 | 67.9 |
| 55% | 819.5 | 61.4 |
| 60% | 894.0 | 54.1 |
| 65% | 968.5 | 46.5 |
| 70% | 1043.0 | 38.6 |
| 75% | 1117.5 | 30.8 |
| 80% | 1192.0 | 22.8 |
| 85% | 1266.5 | 15.2 |
| 90% | 1341.0 | 8.2 |
| 95% | 1415.5 | 3.0 |
| 100% | 1490.0 | 0.7 |

### Lower Surface (x_mm, y_lower_mm)

| Station | x (mm) | y_lower (mm) |
|---|---|---|
| 0 | 0.0 | 0.0 |
| 1.25% | 18.6 | 8.9 |
| 2.5% | 37.3 | 15.5 |
| 5.0% | 74.5 | 24.6 |
| 7.5% | 111.8 | 30.3 |
| 10% | 149.0 | 33.6 |
| 15% | 223.5 | 37.3 |
| 20% | 298.0 | 39.6 |
| 25% | 372.5 | 40.6 |
| **30%** | **447.0** | **41.4** |
| **35%** | **521.5** | **41.6** ← flat begins |
| **40%** | **596.0** | **41.6** ← flat |
| **45%** | **670.5** | **41.6** ← flat |
| **50%** | **745.0** | **41.6** ← flat |
| **55%** | **819.5** | **41.6** ← flat |
| **60%** | **894.0** | **41.6** ← flat |
| **65%** | **968.5** | **41.6** ← flat |
| **70%** | **1043.0** | **41.6** ← flat |
| **75%** | **1117.5** | **41.6** ← flat |
| **80%** | **1192.0** | **41.6** ← flat |
| **85%** | **1266.5** | **41.6** ← flat |
| **90%** | **1341.0** | **41.6** ← flat ends |
| 95% | 1415.5 | 27.6 |
| 100% | 1490.0 | 13.0 |

> **Note:** The flat lower surface from 35–90% chord sits at y = 41.6 mm above the chord datum. When the chord line is the reference, the flat lower surface is not at y=0 — this is because the chord line is drawn between the leading edge and trailing edge, and the Clark Y has a cambered chord line. **The construction reference datum is the flat lower surface itself.** All rib dimensions should be measured from the lower flat surface.

---

## Rib Construction (Plywood Ribs)

### 3mm Birch Plywood Rib (Primary Method)

**Cutting method:** CNC router (preferred) or hand scroll saw with template.

1. **Template:** Print the rib profile at 100% scale (or plot to full size from coordinates above). Template is 1,490 mm long.

2. **Layout:** Mark on 3mm birch ply with template and sharp pencil.

3. **Spar cutouts:**
   - Main spar (25% chord): rectangular cutout, 75 mm wide × 80 mm tall, centered at x = 372 mm
   - Rear spar (65% chord): rectangular cutout, 25 mm wide × 55 mm tall, centered at x = 968 mm

4. **Lightening holes:** 
   - 4× holes, ∅ 65 mm, distributed between spar cutouts
   - 2× holes, ∅ 40 mm, between rear spar and trailing edge
   - Minimum rib material width at any cutout edge: 15 mm

5. **Cap strips:**
   - 6mm × 8mm spruce cap strips glued to both faces of the rib along the profile
   - Cap strips are cut to the profile using the jig (see `/manufacturing/jigs/`)
   - Butt-joint at spar locations

### Alternative: Foam Ribs (EPS 40 kg/m³)

For builders without CNC capability:

1. Hot-wire cut from full-density EPS (expanded polystyrene, 40 kg/m³ minimum density)
2. Wire template: 1.6mm stainless wire bent to upper and lower profiles
3. Lower surface is flat → clamp foam blank to flat work surface, use template on upper only
4. Sand with 80-grit foam sanding block to final profile
5. Apply 1-layer 49 g/m² fiberglass + West System 105/207 to all surfaces
6. Sand glass smooth, cut spar pockets with sharp knife

**Foam rib weight:** ~95 g per rib (vs ~120 g for plywood rib)

---

## Spar Pocket Dimensions

The main spar I-beam fits into the rib pocket:

```
Main spar I-beam cross-section:
  Cap width:   70 mm
  Cap height:  25 mm (each cap)
  Web height: 268 mm
  Web thickness: 3 mm (+ 6mm at root 500mm)
  
  Overall I-beam height: 25 + 268 + 25 = 318 mm
  Width at cap: 70 mm

Rib main spar cutout:
  Height: 322 mm (4mm clearance for glue)
  Width: 74 mm (4mm clearance)
  
Rear spar cutout (19mm × 38mm spruce beam):
  Height: 44 mm
  Width: 23 mm
```

---

## FreeCAD Python Script (Rib Profile Generation)

```python
# freecad_rib.py
# Run in FreeCAD Python console to generate Clark Y rib profile
# Requires FreeCAD 0.21+

import FreeCAD as App
import Part, Draft
import math

# Clark Y coordinates (x/c, y_upper/c, y_lower/c)
clark_y_upper = [
    (0.000, 0.000), (0.0125, 0.0197), (0.025, 0.0264), (0.050, 0.0354),
    (0.075, 0.0410), (0.100, 0.0450), (0.150, 0.0507), (0.200, 0.0542),
    (0.250, 0.0560), (0.300, 0.0561), (0.350, 0.0550), (0.400, 0.0526),
    (0.450, 0.0495), (0.500, 0.0456), (0.550, 0.0412), (0.600, 0.0363),
    (0.650, 0.0312), (0.700, 0.0259), (0.750, 0.0207), (0.800, 0.0153),
    (0.850, 0.0102), (0.900, 0.0055), (0.950, 0.0020), (1.000, 0.0005),
]

clark_y_lower = [
    (0.000, 0.000), (0.0125, 0.0060), (0.025, 0.0104), (0.050, 0.0165),
    (0.075, 0.0203), (0.100, 0.0226), (0.150, 0.0250), (0.200, 0.0266),
    (0.250, 0.0272), (0.300, 0.0278), (0.350, 0.0279), (0.400, 0.0279),
    (0.450, 0.0279), (0.500, 0.0279), (0.550, 0.0279), (0.600, 0.0279),
    (0.650, 0.0279), (0.700, 0.0279), (0.750, 0.0279), (0.800, 0.0279),
    (0.850, 0.0279), (0.900, 0.0279), (0.950, 0.0185), (1.000, 0.0087),
]

CHORD = 1490  # mm

def make_rib_profile(doc, chord_mm):
    pts_upper = [App.Vector(x * chord_mm, y * chord_mm, 0) for x, y in clark_y_upper]
    pts_lower = [App.Vector(x * chord_mm, y * chord_mm, 0) for x, y in reversed(clark_y_lower)]
    
    all_pts = pts_upper + pts_lower[1:]  # Close the loop
    
    wire = Part.makePolygon(all_pts + [all_pts[0]])
    face = Part.Face(wire)
    
    rib = doc.addObject("Part::Feature", "ClarkY_Rib")
    rib.Shape = face
    return rib

doc = App.newDocument("OpenWing_Rib")
rib = make_rib_profile(doc, CHORD)
doc.recompute()
print(f"Rib created: {CHORD}mm chord, Clark Y airfoil")
print("Next: Add spar cutouts and lightening holes using Part::Cut")
```

---

## Quality Control — Rib Template Check

After cutting ribs, verify each one against the master template:
- Maximum allowable deviation from template: ±1.5 mm at any station
- Spar pocket squareness: ±0.5° (check with combination square)
- All ribs must be identical within these tolerances

Rejected ribs should be set aside for test pieces, not used in the aircraft.
