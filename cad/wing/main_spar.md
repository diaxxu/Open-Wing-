# Main Wing Spar — I-Beam, Spruce

**Part number:** WG-SPAR-001  
**Material:** Sitka spruce caps + 3mm birch aircraft plywood web  
**Adhesive:** Aeropoxy PR2032/PH3660 or T-88 structural epoxy  
**Quantity:** 2 (one per wing panel)

---

## Overview

The main spar is a built-up I-beam: two spruce rectangular caps bonded to a thin plywood shear web. This is the standard construction used in wooden ultralight and homebuilt aircraft since the 1920s. It is strong, light, and repairable.

---

## Spar Geometry

```
Cross-section view (at mid-span):

    ←——— 70mm ———→
    ┌─────────────┐  ─┐
    │  Cap (top)  │   │ 25mm
    └──────┬──────┘  ─┤
           │          │
           │  Web     │ 268mm
           │  3mm ply │
           │          │
    ┌──────┴──────┐  ─┤
    │ Cap (bottom)│   │ 25mm
    └─────────────┘  ─┘
    ←— 70mm —→
    
Total height: 318mm
Total width: 70mm (cap), 3mm (web)
```

**Taper:** The spar caps are NOT tapered in this design for simplicity. The constant cross-section is conservative and adds approximately 600g per panel vs a tapered spar.

**Reason for no taper:** At the builder's experience level targeted, a tapered spar introduces joinery risk. The uniform spar with constant cap dimensions is structurally analyzed conservatively throughout.

---

## Bill of Materials (Per Wing Panel, 4.875m span)

| Item | Specification | Length/Size | Qty | Source |
|---|---|---|---|---|
| Spar cap (upper) | Sitka spruce, clear, straight grain | 25mm × 70mm × 4900mm | 2 laminations | Aircraft spruce supplier |
| Spar cap (lower) | Sitka spruce, clear, straight grain | 25mm × 70mm × 4900mm | 2 laminations | Aircraft spruce supplier |
| Web | Aircraft birch ply, 3mm | 318mm × 4900mm | 1 sheet | Aircraft supplier |
| Web doublers (at root) | Aircraft birch ply, 6mm | 318mm × 600mm | 2 pieces | Aircraft supplier |
| Spar root fitting | 4130 steel plate, 6mm | 120mm × 250mm | 1 | Steel supplier |
| Gussets (web-to-cap) | Aircraft birch ply, 3mm | 50mm × 75mm | 18 | Offcuts |
| Bond adhesive | T-88 or Aeropoxy | 250mL mixed | 1 kit | Aircraft supplier |

### Material Substitutions (Budget)

- **Sitka spruce → Douglas fir:** Douglas fir has ~85% of spruce's specific strength-to-weight. Increase cap to 28mm × 75mm to compensate. Not preferred but acceptable.
- **Aircraft birch ply → domestic hardwood ply (poplar face):** Verify shear modulus; poplar-core ply varies widely. Use 4mm domestic in place of 3mm aircraft.
- **T-88 → West System 105/205:** Both are acceptable. West System is more available. Mix ratio critical — 5:1 by volume. DO NOT substitute white glue, yellow carpenter's glue, or polyurethane glue.

---

## Lamination Schedule

Each spar cap is made from **two laminations** of 12.5mm × 70mm spruce:

**Why laminate?**
1. Easier to source clear grain in thinner stock
2. Laminated caps are approximately 15% stronger than single-piece equivalent due to defect probability reduction
3. Any grain deviation in one lamination is compensated by the adjacent one

**Lamination procedure:**
1. Select stock with grain running as close to parallel to the long axis as possible (max 1:15 slope of grain)
2. Surface-plane both mating faces flat to within 0.1mm per 300mm
3. Apply T-88 epoxy to both mating faces (spread to ~0.15mm wet film)
4. Clamp at 75mm spacing with minimum 70 kPa clamping pressure
5. Allow 24 hours at 20°C minimum before removing clamps
6. Scrape excess epoxy flush

---

## Spar Assembly Sequence

### Step 1: Cut web panels

```
Web dimensions:
  Full length: 4,875mm (panel span)
  Height: 268mm (between inner cap faces)
  
  From 3mm birch ply (standard sheet 1220×2440mm):
  Two pieces 268 × 2440mm, one piece 268 × 2000mm → scarf-join
  
  Web scarf joint:
  - 12:1 scarf ratio minimum → overlap = 12 × 3mm = 36mm (use 40mm)
  - Cut on bandsaw with a sled at the correct angle
  - Bond with T-88, clamp flat on a straight reference surface
  - Scarf location: DO NOT place within 500mm of root fitting or within 200mm of a rib station
```

### Step 2: Groove web for cap bonding

Using a router table with straight bit:
- Cut a 3mm × 3mm groove in each cap lamination at the web location
- This groove acts as a glue reservoir and self-aligning feature
- Groove depth: 3mm, width: 3mm (+0.2/-0.0 tolerance)

### Step 3: Dry-fit assembly

Dry-fit without glue:
- Web sits in grooves of both cap laminations
- Check spar is straight on assembly jig (see `/manufacturing/jigs/spar_jig.md`)
- Check web perpendicularity to caps: ≤ 0.5° deviation

### Step 4: Bond assembly

1. Mix T-88 per manufacturer instructions (equal parts by volume)
2. Apply to web faces, groove faces, and mating surfaces of cap laminations
3. Assemble in jig with web locating on center
4. Apply clamps at 50mm intervals (minimum 40 clamps per spar)
5. Check spar for twist: lay straight edge across caps at multiple points
6. Allow to cure 48 hours at 20°C

### Step 5: Root doublers

At the root 600mm, bond 6mm plywood doublers to both faces of the 3mm web:

```
Doubler dimensions: 318mm × 600mm × 6mm each side

Root shear force = 6,387 N (from structural analysis)
Web shear stress with single 3mm web: 6387/(268×3) = 7.94 MPa
Birch ply Fs_allow = 5.5 MPa → FAIL at root, hence doublers

With doublers (total web at root = 3+6+6 = 15mm):
Shear stress = 6387/(268×15) = 1.59 MPa ✓ (SF = 3.5)
```

### Step 6: Root fitting

The root fitting is a 6mm 4130 steel plate, laser-cut or plasma-cut, drilled for 2× M10 bolts through the fuselage main spar carry-through.

```
Root fitting dimensions:
  Material: 4130 steel, 6mm
  Width: 120mm (covers both spar caps + 25mm each side)
  Height: 250mm (covers full spar depth + 10mm each side)
  
  Bolt holes: 2× M10 clearance (10.5mm dia)
              Spacing: 180mm vertical
              Center to outboard face: 15mm
              
  Weld to spar: NO — bolt and bondfit only
  Attachment: M10 AN bolts, AN960-1016 washers, AN365 nylon-insert lock nuts
              Torque: 40 N·m (30 ft-lbs)
```

---

## Inspection Points

Before installing spar:

- [ ] No delaminations visible (tap test along entire length — hollow sound indicates void)
- [ ] No voids in glue line (inspect all joints with bright light)
- [ ] Spar is straight within 3mm over full length (check on flat surface)
- [ ] Web is perpendicular to caps within 1° over full length
- [ ] Root doublers are fully bonded with no edge separation
- [ ] Root fitting bolt holes are perpendicular to spar face within 0.5°
- [ ] All spruce is clear grade with no knots, checks, or diagonal grain exceeding 1:15

**Failed inspection → Do not install. Rebuild spar.**
