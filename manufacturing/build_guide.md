# Master Build Guide

**Document:** MFG-001  
**Revision:** A  
**Estimated Build Time:** 600–900 hours for an experienced builder  

---

## BEFORE YOU START — READ THIS ENTIRE DOCUMENT

Building an aircraft is not like any other woodworking or metalworking project. Decisions made early in the build have consequences that cannot be undone without scrapping major assemblies. Read this entire guide, the design report, and all structural analysis documents before cutting a single piece of material.

**Every step has a sign-off checkbox. These are not bureaucratic theater. They exist because aircraft have crashed due to a single overlooked step.**

---

## Phase Overview

| Phase | Major Tasks | Est. Hours | Sign-off |
|---|---|---|---|
| 0 | Shop setup, materials procurement | 20–40 hr | [ ] |
| 1 | Jig fabrication | 40–60 hr | [ ] |
| 2 | Wing spars | 60–80 hr | [ ] |
| 3 | Wing ribs and panels | 80–120 hr | [ ] |
| 4 | Fuselage welding | 60–90 hr | [ ] |
| 5 | Empennage (tail surfaces) | 40–60 hr | [ ] |
| 6 | Landing gear | 15–25 hr | [ ] |
| 7 | Control systems | 30–50 hr | [ ] |
| 8 | Engine installation | 20–30 hr | [ ] |
| 9 | Fabric covering | 60–80 hr | [ ] |
| 10 | Avionics and electrical | 15–25 hr | [ ] |
| 11 | Final assembly and rigging | 30–50 hr | [ ] |
| 12 | Ground testing | 20–40 hr | [ ] |

---

## Phase 0: Shop Setup and Materials Procurement

### 0.1 Required Tools

**Essential (cannot proceed without):**
- [ ] Workbench, flat and rigid, minimum 3m × 0.9m
- [ ] Band saw with fine-tooth blade (10 TPI minimum for wood)
- [ ] Table saw or track saw for ripping lumber
- [ ] Router table with straight bit (for spar cap grooves)
- [ ] Drill press
- [ ] Hand drill with bits: 2mm to 12mm
- [ ] Combination square, 300mm and 600mm
- [ ] Straight edge, 2m aluminum
- [ ] Clamps: minimum 40× F-clamps (spring clamps not sufficient for spar bonding)
- [ ] TIG or MIG welder (for fuselage; can outsource to certified welder)
- [ ] Angle grinder with cutting and grinding discs
- [ ] Pipe/tube cutter or cold saw
- [ ] Rivet gun (for aluminum skin panels)
- [ ] Digital calipers
- [ ] Protractor or digital angle finder

**Recommended:**
- [ ] CNC router (for ribs — can substitute with scroll saw + template)
- [ ] Vacuum pump (for vacuum bagging epoxy joints)
- [ ] 3D printer (for jig components and brackets)
- [ ] Laser level (for fuselage alignment)

### 0.2 Materials Procurement Checklist

All quantities include approximately 15% waste allowance.

**Wood:**
- [ ] Sitka spruce, 70mm × 19mm, 50m total (spar caps)
- [ ] Aircraft birch plywood 3mm, 4× 1220×2440mm sheets (spar webs, gussets)
- [ ] Aircraft birch plywood 6mm, 2× 1220×2440mm sheets (spar root doublers, bulkheads)
- [ ] Spruce dimensional lumber, 38mm × 38mm, 20m (ribs, formers)
- [ ] Balsa wood, 3mm sheet, 5× 600×900mm (trailing edge and tip fill)

**Metal:**
- [ ] 4130 chromoly tube, 25.4mm OD × 1.65mm wall, 30m (fuselage main structure)
- [ ] 4130 chromoly tube, 19.1mm OD × 1.24mm wall, 15m (fuselage diagonals, tail)
- [ ] 6061-T6 aluminum tube, 50.8mm OD × 3mm wall, 2× 500mm (main gear legs) **← WRONG for flat spring — see below**
- [ ] 6061-T6 aluminum flat bar, 50mm × 25mm, 2× 500mm (flat spring main gear legs)
- [ ] 6061-T6 aluminum tube, various, for struts and fittings: 10m mixed
- [ ] 4130 steel plate, 6mm, 500×500mm (root fittings, attach plates)
- [ ] AN hardware kit (bolts, nuts, washers, cotter pins) — see hardware list in materials_list.md

**Adhesives and Consumables:**
- [ ] T-88 structural epoxy, 2× 1-pint kits
- [ ] West System 105 resin + 205 or 207 hardener, 1.4L kit
- [ ] MIL-SPEC contact cement (for fabric application) — Poly-Tak or equivalent
- [ ] Fabric dope (polyester dope for Dacron): 4L
- [ ] Dacron polyester fabric (aircraft grade, 56g/m²): 60m²
- [ ] 60-grit, 120-grit, 220-grit sandpaper, 10 sheets each
- [ ] Zinc chromate primer (rattle can or brush-on): 4 cans/1L
- [ ] Aircraft enamel or polyurethane topcoat: 2L
- [ ] MEK solvent (for degreasing): 1L

---

## Phase 1: Jig Fabrication

**Before building the aircraft, build the jigs. Time spent on accurate jigs saves many times that in rework.**

### 1.1 Wing Assembly Jig

The wing jig holds ribs perpendicular to the spar during assembly.

```
Jig construction:
1. Obtain a 5m × 0.6m sheet of 19mm MDF or 18mm OSB (not ideal — use MDF)
2. Draw the spar centerline along the length
3. At each rib station (every 300mm), mark a perpendicular line
4. Cut rib saddle blocks from 38mm spruce:
   - Lower face: cut to match the lower surface profile of Clark Y at spar location
   - This ensures each rib sits at the correct angle to the spar
5. Nail/screw saddle blocks at each station
6. Check with a straight edge that all saddle blocks are coplanar (within 1mm)
7. Check squareness with combination square at each station

Dihedral setting:
  At the root (y=0): rib saddle is level
  At y = 4.875m (tip): rib saddle is elevated by:
    Δz = tan(2°) × 4.875m = 0.0349 × 4.875 = 170mm
  
  Build a shim under each saddle block proportional to its position:
  Shim height = 170 × (station / 4875) mm
  Example: at y=2000mm: shim = 170 × 2000/4875 = 69.7mm ≈ 70mm
```

### 1.2 Fuselage Assembly Jig

The fuselage jig holds all tube nodes at the correct positions for welding.

```
Material: 50mm × 50mm square steel tubing (borrow from local welding shop)
Process:
1. Lay out two straight 6m base rails, parallel, 580mm apart (fuselage width)
2. Weld cross-members at each frame station (x = 0, 500, 1300, 1900, 2600, 3400, 4300, 5100mm)
3. At each station, weld a short vertical pin of the correct height for each longeron node
   (Refer to fuselage node table in fuselage_frame.md)
4. Cut the pin lengths carefully — this is what determines fuselage geometry
5. Verify the jig is straight: diagonals of each rectangular frame should be equal
6. Check that base rails are parallel: measure across at 4 points

The jig will be distorted by welding heat. Tack-weld first, verify geometry, 
then complete the welds and re-verify. Correct before proceeding.
```

---

## Phase 2: Wing Spar Fabrication

**Reference document:** `/cad/wing/main_spar.md`

### Step 2.1: Select and Inspect Spruce

- [ ] Unwrap all spruce stock and inspect each piece individually
- [ ] Reject any piece with: knot (any size), check, split, diagonal grain >1:15
- [ ] Measure moisture content: target 8–12% (use a wood moisture meter)
  - Below 7%: Acclimate in the shop for 2 weeks before use
  - Above 15%: Do not use — dry to 12% minimum
- [ ] Mark each accepted piece with chalk

### Step 2.2: Mill Spar Caps

- [ ] Run all cap laminations through table saw to 70mm width (±0.5mm)
- [ ] Run through planer to exactly 19.0mm thickness (±0.3mm)
- [ ] Cut to 4,900mm length (25mm extra for trimming)
- [ ] Rout the 3mm × 3mm groove for web alignment (router table, straight bit)
  - Groove centered on the 70mm face, 3mm from one edge
  - One edge only per lamination (the inner face)

### Step 2.3: Cut Spar Webs

- [ ] Cut birch ply into strips: 268mm × 2,440mm (from 3mm sheet)
- [ ] Scarf-join two strips end-to-end to reach 4,875mm:
  - Cut 12:1 scarf (40mm overlap) on bandsaw with sled
  - Sand mating surfaces flat
  - Bond with T-88, clamp flat on glass plate (ensures no warping)
  - Cure 48 hours
- [ ] After curing, verify scarf joint is flat within 0.5mm

### Step 2.4: Bond Spar Assembly

- [ ] Set up assembly jig (straight surface, wax paper to prevent sticking)
- [ ] Dry fit all components — check web sits in both grooves simultaneously
- [ ] Mark web position on inner faces of both cap laminations
- [ ] Mix T-88 epoxy (equal volumes, stir 3 minutes minimum until uniform color)
- [ ] Brush epoxy onto:
  - Both faces of web (thin coat, ~0.15mm)
  - Groove surfaces on both cap inner faces
  - Contact faces of cap laminations (two inner faces between laminations)
- [ ] Assemble: lower cap laminations → web → upper cap laminations
- [ ] Clamp at 50mm intervals — squeeze until small epoxy bead appears at joint line
- [ ] Verify spar is straight: place on flat surface, check with straight edge at 500mm intervals
- [ ] Mark any high spots and weight down, reclamp if needed before epoxy gels (~30 min)
- [ ] Cure minimum 48 hours at 18°C or above
- [ ] [ ] **Inspection: No voids, straight within 3mm, perpendicular web ±0.5°**

### Step 2.5: Root Doublers and Fittings

- [ ] Cut 6mm ply doublers: 344mm × 600mm (2 pieces per spar)
- [ ] Scuff-sand doubler and web mating surfaces with 60-grit
- [ ] Bond doublers to both sides of web at root using T-88
- [ ] Drill root fitting bolt holes (2× 10.5mm) through full spar assembly:
  - Clamp steel root fitting to spar
  - Drill through all layers simultaneously (2-flute bit, lubricate with cutting oil)
  - Deburr all layers
- [ ] [ ] **Inspection: Doublers fully bonded, holes perpendicular to spar face**

---

## Phase 3: Wing Ribs and Panel Assembly

### Step 3.1: Rib Fabrication (32 ribs total — one jig, all identical)

Option A (CNC):
- [ ] Export rib profile to DXF (from freecad_rib.py)
- [ ] CNC-route from 3mm birch ply, including all lightening holes and spar pockets
- [ ] Sand cut edges with 120-grit to remove router fuzz

Option B (hand cut):
- [ ] Print rib template at full scale (1,490mm long): print on 4× A4 sheets, align and tape
- [ ] Transfer to 3mm ply with pencil and sharp marking knife
- [ ] Cut with scroll saw, keeping inside the line; sand to line with drum sander
- [ ] Stack 4 ribs at a time with double-sided tape for gang sanding: ensures uniformity

Rib assembly (all methods):
- [ ] Glue 6mm × 8mm spruce cap strips to both faces of each rib with aliphatic resin
  - Use a curved clamping form matching the upper surface profile
  - The lower surface is straight (flat) — clamp against the flat work surface
- [ ] Cure overnight, remove clamps, trim cap strip flush at spar cutouts
- [ ] [ ] **Check fit: Each rib should slide onto the spar without forcing and without slop (>0.5mm each side)**

### Step 3.2: Rib Installation

- [ ] Set up wing jig with spar supported in saddle blocks at correct dihedral angle
- [ ] Dry-fit all 16 ribs on spar (port panel), check spacing: 300mm ±2mm
- [ ] Mark rib positions on spar with pencil
- [ ] Remove ribs, apply T-88 to rib spar pocket faces
- [ ] Reinstall ribs onto spar, clamp (use rubber-band clamping to spar if needed)
- [ ] Check rib perpendicularity to spar at each location (right angle)
- [ ] Allow to cure 24 hours in jig — DO NOT MOVE THE PANEL
- [ ] Install rear spar (19mm × 38mm spruce) through rear spar cutout of each rib
  - Bond with T-88 at each rib notch
  - Check rear spar is parallel to main spar in the vertical plane (use laser level)

### Step 3.3: Leading Edge and Trailing Edge

- [ ] Form the leading edge from 3mm birch ply bent over the nose of the first 4 ribs
  - Wet the ply with water, bend gently over a 75mm diameter former
  - Allow to dry in the bent position before bonding
  - Bond with T-88 to rib nose blocks and first forward rib bay
- [ ] Install trailing edge: 6mm × 25mm spruce trailing edge strip
  - Bond to the rear face of all rib trailing edge notches
  - Fairness check: run a straight edge along the trailing edge — any kink or bump must be sanded fair before covering

---

## Phase 4: Fuselage Welding

**IMPORTANT: If you are not a certified welder or have not welded 4130 tubing before, hire a certified welder with experience in aircraft fuselage construction. The entire structural integrity of the aircraft depends on weld quality.**

### Step 4.1: Tube Preparation

- [ ] Cut all tubes to length using cold saw or abrasive chop saw (not torch)
- [ ] File all notch fits (fishmouth cuts) to tight fit-up — gap ≤ 0.25mm
- [ ] Degrease all joints with acetone or MEK — gloves required
- [ ] Mark tube positions on jig nodes

### Step 4.2: Tack Welding

- [ ] Mount all tubes in jig, clamp securely
- [ ] Tack weld at each joint: two tacks per joint, 180° apart, minimum
- [ ] After all tacks complete: **VERIFY GEOMETRY**
  - Measure all diagonals at each frame station
  - Diagonals of a frame must be equal ±3mm
  - Overall fuselage length within 5mm of nominal
- [ ] Correct any distortion before completing welds (heat opposite side to correct a bend)
- [ ] [ ] **Geometry check sign-off before completing welds**

### Step 4.3: Complete Welding

- [ ] Complete all joint welds
- [ ] Allow to cool naturally (do not quench)
- [ ] Visually inspect all welds: look for undercut, porosity, cold starts
- [ ] Touch up any defective welds (grind back, re-weld)
- [ ] [ ] **Weld quality inspection sign-off**

### Step 4.4: Fuselage Finishing

- [ ] Remove from jig
- [ ] Internal rust prevention: pour LPS-3 or linseed oil into each tube, rotate to coat, drain
- [ ] External: blast with 60-grit to remove mill scale from weld areas, or use phosphoric acid etch
- [ ] Apply zinc chromate primer to entire external surface within 4 hours of prep
- [ ] [ ] **Corrosion protection sign-off**

---

## Phase 5: Empennage

Construction method is identical to wing panels (spruce spar, foam or ply ribs, Dacron covering), scaled to smaller dimensions.

Key dimensions:
- Horizontal stabilizer: 3,050mm span × 720mm chord
- Elevator: 45% of HT chord, full span minus 75mm per side at tips
- Vertical fin: 1,100mm height × 950mm chord
- Rudder: 35% of fin chord, full height minus 75mm top and bottom

Hinge installation:
- [ ] Use MS20001 piano hinge (continuous) or 3× AN257 hinge plates per surface
- [ ] Hinges must be aligned within 0.5° to prevent binding
- [ ] Test each hinge before covering: full travel, no binding, no side-play exceeding 1mm

---

## Phase 6: Landing Gear

### Main Gear (Flat Spring, 6061-T6)

- [ ] Obtain 6061-T6 flat bar: 50mm × 25mm × 500mm per leg (2 pieces)
- [ ] Drill 2× M10 clearance holes at top of each leg (gear-to-fuselage attach)
- [ ] Drill 1× 12mm hole at bottom for axle
- [ ] Deburr all holes thoroughly
- [ ] Install with AN4 bolts to fuselage main gear cluster (FS-13 frame station)
- [ ] Install wheels with AN3 axle bolts, AN970 large-area washers
- [ ] Safety-wire or cotter-pin all axle hardware
- [ ] Test: sit full body weight on the gear legs — they should deflect no more than 15mm
- [ ] [ ] **Load test sign-off**

---

## Phase 7: Control Systems

### Control Surface Connections

All control surfaces connect via push-pull tubes or aircraft cable with swaged (or nicopress) end fittings. **Wire rope clips (U-bolt type) are NOT acceptable for control cables. Use swaged or nicopressed thimble-and-eye assemblies only.**

- [ ] Elevator: 3mm aircraft cable, 1×19 stainless, through nylon-lined fairleads
- [ ] Aileron: 3mm cable, both wings cross-connected to single stick
- [ ] Rudder: 3mm cable to rudder pedals
- [ ] Cable tension: 5–8 kgs on elevator and aileron (measured with tensiometer)
- [ ] Turnbuckle lock: safety-wire all turnbuckles after final rigging adjustment

### Control Travel Verification

With aircraft fully assembled and on gear:
- [ ] Elevator up: 25° ±2° (measure with protractor at hinge line)
- [ ] Elevator down: 20° ±2°
- [ ] Aileron up: 20° ±2°, down: 20° ±2° (both sides equal)
- [ ] Rudder: 25° ±2° each direction

### Control Interference Check

Move all controls simultaneously through full deflection:
- [ ] No jamming or excessive friction
- [ ] No cable/tube fouling on structure
- [ ] No control reversal (up elevator = stick back)
- [ ] Aileron roll direction correct (stick right = right wing drops)

---

## Phase 8: Engine Installation

### Rotax 447 Installation

- [ ] Mount engine on mount sub-frame with 4× M8 rubber isolation mounts (Lord J-9613 or equivalent)
- [ ] Torque engine mount bolts: 22 N·m
- [ ] Connect exhaust system: do not tighten until all joints aligned cold; retighten after first hot run
- [ ] Connect cooling hoses: use Oetiker ear clamps or stainless worm-drive clamps, not plastic
- [ ] Install propeller: see Rotax installation manual for torque values (prop bolts: 25–30 N·m with Loctite 243)
- [ ] Balance propeller before installation (dynamic balance recommended; static balance acceptable for first run)
- [ ] [ ] **Engine installation sign-off per Rotax Installation Manual**

---

## Phase 9: Fabric Covering

Dacron polyester fabric covering is applied using the heat-shrink and dope method:

1. **Apply fabric:** Cut panels with 25mm overlap on all structure. Apply with Poly-Tak cement to all wood and metal edges.
2. **Shrink:** Heat-shrink gun at 120°C, working from center outward to remove wrinkles.
3. **First coat dope:** Apply 2-part polyester dope, thinned 20%, brush coat. Allow to dry 4 hours.
4. **Second coat:** Unthinned, brush. Sand with 220-grit when dry.
5. **Third coat (finishing):** Brush or spray.
6. **Color coat:** Polyurethane aircraft enamel, 2 coats.

**Inspection between each coat:**
- [ ] No bubbles or delaminations from structure
- [ ] Fabric is drum-tight, no ripples
- [ ] All leading and trailing edges fully bonded

---

## Phase 10: Avionics and Electrical

See `/electronics/avionics_overview.md` for full wiring details.

- [ ] Install instrument panel
- [ ] Route all wiring with minimum 50mm radius bends, secured with adel clamps every 150mm
- [ ] Test each circuit before connecting to aircraft
- [ ] Verify kill switch function: engine stops within 3 seconds when switched to KILL
- [ ] [ ] **Electrical system sign-off**

---

## Phase 11: Final Assembly and Rigging

### Wing Attachment

- [ ] Attach wings to fuselage at main and rear spar fittings
- [ ] Torque main spar bolts: 40 N·m (AN4-20A, M10)
- [ ] Install lift struts: M10 clevis pins, cotter-pinned
- [ ] Check wing incidence: 2° ±0.25° on both wings relative to fuselage datum
- [ ] Check dihedral: 2° ±0.5° (measure with digital level at mid-span, compare port and starboard)

### Rigging

- [ ] Tension all control cables per Phase 7 specifications
- [ ] Set elevator neutral trim tab to provide cruise trim at 33% MAC CG, 45 kts
- [ ] Set aileron neutral: both ailerons in neutral when stick is centered (verify with level)
- [ ] Set horizontal tail incidence: -1.5° relative to FRL (set at factory, verify with digital angle finder)

### Weight and Balance

- [ ] Weigh the completed aircraft on a flat, level surface using three scales (one per wheel)
- [ ] Record empty weight and CG
- [ ] Verify: empty weight ≤ 115 kg
- [ ] Verify: CG falls within 27–38% MAC envelope when loaded with representative pilot

---

## Phase 12: Pre-Flight Ground Testing

**See `/testing/ground/` for detailed test cards.**

- [ ] Engine ground run: start, idle, full power test (see TC-G-001)
- [ ] Static load test on wing spar: sandbag test to 2× empty weight (see TC-G-002)
- [ ] Control surface deflection verification (see TC-G-003)
- [ ] All fasteners checked and torqued (see TC-G-004)
- [ ] Weight and balance confirmed (see TC-G-005)
- [ ] **EAA Technical Counselor inspection (strongly recommended)**

**Do not proceed to flight without completing all ground test cards.**
