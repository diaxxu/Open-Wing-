# CAD Documentation

**Toolchain:** FreeCAD 0.21+ (free, open source) or Autodesk Fusion 360 (free tier)  
**Format:** Parametric descriptions with key dimensions; FreeCAD Python scripts where applicable.  
**Units:** All dimensions in millimeters (mm) unless stated.

---

## Philosophy

No proprietary CAD files are distributed. Instead, this directory contains:

1. **Fully dimensioned parametric descriptions** of every part with all key parameters listed
2. **Python scripts** for FreeCAD Part module to generate parts procedurally
3. **Print-scale DXF-compatible coordinate tables** for 2D components (ribs, formers)
4. **Assembly constraint descriptions** that define how parts relate spatially

This approach ensures the design can be reproduced by anyone without a specific CAD application and that all parameters are transparent and modifiable.

---

## Master Parameter Table

These values drive the entire design. All part files reference these as master constants.

```python
# MASTER_PARAMS.py — import this in all FreeCAD scripts
# All dimensions in mm

# Aircraft global
FUSELAGE_LENGTH     = 5490    # mm
WINGSPAN            = 9750    # mm (total, tip-to-tip)
WING_CHORD          = 1490    # mm
WING_AREA_m2        = 14.52   # m² (= 9750 × 1490 / 1e6)

# Wing geometry
WING_SPAR1_CHORD_FRAC  = 0.25   # Main spar at 25% chord
WING_SPAR2_CHORD_FRAC  = 0.65   # Rear spar at 65% chord
WING_SPAR_DEPTH        = 268    # mm (18% × chord)
WING_RIB_SPACING       = 300    # mm center-to-center
WING_RIB_COUNT         = 32     # 16 per panel
DIHEDRAL_DEG           = 2.0    # degrees

# Spar cap dimensions
CAP_WIDTH              = 70     # mm
CAP_HEIGHT             = 25     # mm (2 × 12.5 laminations)
WEB_THICKNESS          = 3      # mm (birch ply)

# Fuselage
FUS_MAIN_TUBE_OD       = 25.4   # mm (1.0 inch)
FUS_MAIN_TUBE_WALL     = 1.65   # mm
FUS_SEC_TUBE_OD        = 19.1   # mm (0.75 inch)
FUS_SEC_TUBE_WALL      = 1.24   # mm
SEAT_ARM_FROM_FW       = 1950   # mm from firewall

# Empennage
HT_SPAN                = 3050   # mm
HT_CHORD               = 720    # mm
HT_SPAR_CHORD_FRAC     = 0.30
VF_HEIGHT              = 1100   # mm
VF_CHORD               = 950    # mm

# Landing gear
MAIN_GEAR_TRACK        = 1830   # mm
NOSE_GEAR_ARM_FROM_FW  = -500   # mm (forward)
MAIN_GEAR_ARM_FROM_FW  = 1300   # mm

# Propulsion
PROP_DIAMETER          = 1520   # mm
PROP_PITCH_IN          = 36     # inches
FIREWALL_TO_PROP       = 350    # mm
```

---

## File Index

### `/cad/wing/`

| File | Contents |
|---|---|
| `wing_rib_clark_y.md` | Clark Y rib geometry, full coordinate table, FreeCAD script |
| `main_spar.md` | I-beam spar: cap + web dimensions, lamination schedule |
| `rear_spar.md` | Rear spar beam dimensions |
| `wing_tip.md` | Tip bow construction |
| `aileron.md` | Aileron structure and hinge points |
| `strut_bracket.md` | Lift strut attachment bracket |

### `/cad/fuselage/`

| File | Contents |
|---|---|
| `fuselage_frame.md` | Full tube-frame geometry, node coordinates, tube sizes |
| `engine_mount.md` | Engine mount sub-frame |
| `seat_pan.md` | Seat pan dimensions |
| `firewall.md` | Firewall dimensions and material |
| `instrument_panel.md` | Instrument panel layout |

### `/cad/empennage/`

| File | Contents |
|---|---|
| `horizontal_tail.md` | HT spar and rib layout |
| `vertical_fin.md` | VF spar and rib layout |
| `elevator.md` | Elevator geometry and balance |
| `rudder.md` | Rudder geometry and horn |

### `/cad/landing_gear/`

| File | Contents |
|---|---|
| `main_gear.md` | Flat spring leg dimensions and attachment |
| `nose_gear.md` | Nose gear strut, steering linkage |
| `wheel_pants.md` | Optional fairing geometry |

### `/cad/propulsion/`

| File | Contents |
|---|---|
| `engine_mount.md` | Mount sub-frame detailed |
| `cowling.md` | Fiberglass cowling plug geometry |
| `exhaust_routing.md` | Exhaust pipe bends and lengths |
