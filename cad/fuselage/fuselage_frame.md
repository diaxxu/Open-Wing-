# Fuselage Frame — 4130 Steel Tube Welded Structure

**Part number:** FUS-FRAME-001  
**Material:** 4130 chromoly steel tube (normalized)  
**Process:** TIG or MIG welding; TIG preferred for thinner walls  
**Jig:** Required — see `/manufacturing/jigs/fuselage_jig.md`

---

## Structure Overview

The fuselage is a conventional **welded steel tube space frame** covered with thin aluminum sheet (0.4mm) or fabric. The structure carries all primary loads: wing attachment, engine mount, landing gear, and tail loads.

```
Side view (schematic):

     ENGINE        COCKPIT        TAIL SECTION
      MOUNT    
         ↓          
    ══════════════════════════════════════════╗
    ║ A ——————————————————————————————— D    ║ ← Upper longeron
    ║  \         ╱         ╲              ╲   ║
    ║   B———————C           E——————————F  G  ║ ← Frame nodes
    ║  ╱         ╲          ╱              ╲  ║
    ║ ═══════════════════════════════════════ ║ ← Lower longeron
    ══════════════════════════════════════════╝

All tube members shown are specific to 2D; real structure is 3D box section
```

---

## Node Coordinate Table

Origin: Firewall centerline, fuselage datum (FRL), x=0 aft, z=0 at lower longeron.

All coordinates in mm. Positive x is aft, positive z is up.

### Upper Longerons (Port and Starboard, symmetric)

| Node | x (mm) | z (mm) | y ±(mm) | Description |
|---|---|---|---|---|
| UF1 | 0 | 620 | ±145 | Firewall, upper corner |
| UF2 | 350 | 770 | ±145 | Top of cabin front |
| UF3 | 1,050 | 820 | ±145 | Windscreen top / wing attach region |
| UF4 | 1,850 | 820 | ±145 | Aft cabin top |
| UF5 | 2,400 | 780 | ±120 | Begin taper |
| UF6 | 3,200 | 710 | ±90 | Mid-tail |
| UF7 | 4,200 | 620 | ±65 | Aft tail |
| UF8 | 5,050 | 520 | ±40 | Horizontal tail attach |
| UF9 | 5,490 | 490 | ±30 | Tail tip / rudder post |

### Lower Longerons (Port and Starboard, symmetric)

| Node | x (mm) | z (mm) | y ±(mm) | Description |
|---|---|---|---|---|
| LF1 | 0 | 0 | ±145 | Firewall, lower corner |
| LF2 | 500 | 0 | ±145 | Forward seat/gear bulkhead |
| LF3 | 1,300 | 0 | ±145 | Main gear attach point |
| LF4 | 1,900 | 0 | ±145 | Aft seat bulkhead |
| LF5 | 2,600 | 0 | ±120 | Begin taper |
| LF6 | 3,400 | 30 | ±90 | Begin upswept tail |
| LF7 | 4,300 | 120 | ±60 | |
| LF8 | 5,100 | 240 | ±35 | Horizontal tail attach, lower |
| LF9 | 5,490 | 370 | ±25 | Tail tip |

### Cross Members and Diagonals

Cross members connect port-to-starboard at each frame station. Diagonals connect adjacent frame nodes to triangulate the structure.

**Frame stations (x = constant bulkheads):**

| Station | x (mm) | Purpose | Tube spec |
|---|---|---|---|
| FS-00 | 0 | Firewall | 25.4×1.65 4130 |
| FS-05 | 500 | Nose gear / forward bulkhead | 25.4×1.65 4130 |
| FS-13 | 1,300 | Main gear attach | 25.4×1.65 4130 |
| FS-19 | 1,900 | Aft cockpit / wing rear attach | 25.4×1.65 4130 |
| FS-26 | 2,600 | Tail cone front | 19.1×1.24 4130 |
| FS-34 | 3,400 | | 19.1×1.24 4130 |
| FS-43 | 4,300 | | 19.1×1.24 4130 |
| FS-51 | 5,100 | Horizontal tail attach | 19.1×1.24 4130 |

---

## Tube Specification by Member

| Member | Tube Spec | Material | Notes |
|---|---|---|---|
| Upper main longerons | 25.4 OD × 1.65 wall | 4130 normalized | Full length |
| Lower main longerons | 25.4 OD × 1.65 wall | 4130 normalized | Full length |
| Firewall frame | 25.4 OD × 1.65 wall | 4130 normalized | |
| Main gear attach cluster | 25.4 OD × 2.11 wall | 4130 normalized | Heavier at this high-load node |
| Tail cone members | 19.1 OD × 1.24 wall | 4130 normalized | |
| Diagonal bracing | 19.1 OD × 1.24 wall | 4130 normalized | |
| Engine mount sub-frame | 25.4 OD × 1.65 wall | 4130 normalized | Separate sub-assembly |

---

## Wing Attachment Points

The wing attaches to the fuselage at two points per side:

**Forward Fitting (at 25% MAC — primary spar attach):**

```
Location: x = 1,220mm aft of datum (adjusted per final CG calculation)
Both port and starboard: y = ±245mm from centerline (beyond fuselage side)
z = 820mm (top of main fuselage frame, upper longeron height)

Fitting: 6mm 4130 steel plate welded to upper longeron cluster
         2× M10 bolts per side (AN4-20A bolts recommended)
         Bolt pattern: 40mm horizontal, 120mm vertical spacing
         
Bolt torque: 40 N·m, with AN365-1032 locknuts
Inspector: Check torque at each pre-flight
```

**Rear Fitting (at 65% MAC — rear spar attach):**

```
Location: x = 1,690mm aft of datum
Fitting: Single M8 bolt per side (carry tension/compression, not primary bending)
         Slotted hole to allow thermal expansion: 10mm slot, 8.5mm wide
```

**Lift Strut Attach Points (lower fuselage):**

```
Lower strut fitting: x = 1,450mm, z = 0 (lower longeron level), y = ±145mm
Upper strut fitting: at wing, 50% chord, approximately 50% semi-span

Material: 8mm 4130 steel clevis, welded to lower longeron
Pin: M10 AN393 cotter-pinned
```

---

## Welding Requirements

**Pre-weld:**
- De-grease all tube ends with MEK or acetone
- Ensure tight fit-up (gap ≤ 0.25mm before welding)
- Use a proper welding fixture — warping is the enemy

**Weld process:**
- TIG (GTAW) preferred with ER70S-2 filler wire, 1.6mm diameter
- MIG (GMAW) with ER70S-6 wire, 0.9mm, is acceptable for non-critical members
- DO NOT use oxy-acetylene on 4130 for structural welds without proper stress relief

**Post-weld:**
- Allow to cool slowly (do not quench)
- Inspect all welds visually: look for undercut, porosity, cold laps
- Weld throat minimum: 0.7 × tube wall thickness
- Penetration: full-penetration where possible; fillet welds at clusters

**Normalizing:**
4130 normalized requires post-weld stress relief at 870–900°C if welded with significant heat input. For TIG welding thin wall (≤ 2mm), stress relief is not required if the weld heat input is controlled.

**Inspection:**
- [ ] All welds inspected per above criteria
- [ ] Frame jigged true (diagonal measurement within 3mm)
- [ ] All attachment holes drilled and reamed to size
- [ ] Rust-proofing: internal tube treatment with LPS-3 or WD-40 before sealing
- [ ] External: zinc chromate primer, then finish paint

---

## Weight Estimate

```
Total longeron length (2 × upper + 2 × lower + cross members):
Upper longerons: 2 × 5,490 = 10,980mm
Lower longerons: 2 × 5,490 = 10,980mm
Cross members (18 frames × avg 290mm wide): ~5,220mm total
Diagonals (est): ~8,000mm
Total 25.4×1.65 tube: 25,960mm at 0.936 kg/m = 24.3 kg
Total 19.1×1.24 tube: 13,220mm at 0.522 kg/m = 6.9 kg
Fittings and hardware: ~3.0 kg
Total frame weight: ~34.2 kg (vs 32.0 kg design target — 2.2 kg over budget)

Mitigation: Replace tail cone 19.1×1.24 members with 15.9×0.9mm tube.
15.9×0.9 weight: 0.330 kg/m × 8,000mm = 2.64 kg (vs 4.13 kg) → saves 1.5 kg
```
