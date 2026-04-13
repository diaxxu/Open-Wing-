# OpenWing ULA-1

**Open-Source Ultralight Aircraft — FAR Part 103 Compliant**

> *"Build it. Fly it. Fix it yourself."*

---

## Project Overview

OpenWing ULA-1 is a fully documented, open-source ultralight aircraft designed for construction by a single skilled builder using basic workshop tools, a CNC router (optional), and a 3D printer for brackets and jigs. Every design decision prioritizes **repairability, affordability, and engineering rigor** over aesthetic novelty.

This repository contains everything required to reproduce the aircraft from raw materials: aerodynamic analysis, structural calculations, CAD descriptions, manufacturing procedures, electronics schematics, simulation software, and an incremental flight test plan.

**This is not a toy. This is a real aircraft. Building and flying it requires skill, judgment, and compliance with all applicable regulations in your jurisdiction.**

---

## Aircraft Specifications (Design Point)

| Parameter | Value | Notes |
|---|---|---|
| Configuration | High-wing monoplane, tractor prop | |
| Wingspan | 9.75 m (32.0 ft) | |
| Wing chord (constant) | 1.49 m (4.89 ft) | Untapered for buildability |
| Wing area | 14.52 m² (156.3 ft²) | |
| Aspect ratio | 6.55 | |
| Airfoil | Clark Y | Flat-bottom, proven, easy to build |
| Fuselage length | 5.49 m (18.0 ft) | |
| Empty weight (target) | 113 kg (249 lbs) | FAR Part 103 ≤ 115 kg |
| Max gross weight | 217 kg (478 lbs) | Pilot 90 kg + 14 kg fuel |
| Wing loading | 14.7 kg/m² (3.01 lb/ft²) | |
| Propulsion | Rotax 447 UL (40 hp) | Budget alt: Hirth F33, Kawasaki 440 |
| Propeller | 152 cm × 91 cm (60×36") wooden 2-blade | |
| Fuel capacity | 13.2 L (3.5 US gal) | FAR Part 103 ≤ 5 gal |
| Cruise speed | 45 kts (83 km/h) | At 75% power |
| Never exceed (Vne) | 55 kts (102 km/h) | FAR Part 103 limit |
| Stall speed (Vs) | ≤ 24 kts (44 km/h) | FAR Part 103 requirement |
| Rate of climb (Vy) | ~152 m/min (500 fpm) | MGTOW, sea level, ISA |
| Endurance | ~1.5 hr | At cruise, 45-min reserve |
| Range | ~105 km (57 nm) | No reserve |
| Glide ratio | ~9.5:1 | At best glide speed |
| Occupants | 1 | FAR Part 103 |

---

## Design Philosophy

### Why High-Wing?

A parasol/high-wing configuration provides inherent roll stability through pendulum effect, excellent downward visibility, easy access to the wing structure for inspection and repair, and a lower center of gravity. For a single-seat ultralight with a novice-adjacent builder profile, this configuration is the most forgiving.

### Why Clark Y Airfoil?

The Clark Y was selected for four reasons:
1. Its **flat lower surface** makes rib construction and jig setup trivial
2. It has a well-documented, predictable stall behavior (gentle leading-edge stall)
3. Extensive historical data exists from NACA TN-412 and wind tunnel tests
4. It performs well in the Reynolds number range (Re ≈ 500,000–800,000) of this aircraft

### Why Untapered Wing?

A constant-chord (Hershey bar) wing is chosen deliberately:
- All ribs are **identical** → single jig, minimal waste
- Spar caps can be routed from uniform stock
- No twist correction needed at root vs tip during assembly
- Structural analysis is simpler and more conservative

### Why a 2-Stroke Engine?

The Rotax 447 (or budget equivalents) offers the best power-to-weight ratio in the accessible market for Part 103 aircraft. A 40 hp, ~25 kg engine is difficult to match with electric propulsion without exceeding the 115 kg empty weight limit. Electric propulsion is addressed as a variant in `/docs/design_report.md`.

---

## Repository Structure

```
openwing-ula1/
├── README.md                        ← You are here
├── DISCLAIMER.md                    ← Safety and legal notice (READ FIRST)
├── LICENSE                          ← MIT License
│
├── docs/
│   ├── design_report.md             ← Full design report
│   ├── airfoil_selection.md         ← Airfoil analysis and justification
│   ├── weight_and_balance.md        ← Mass breakdown and CG calculation
│   ├── performance_estimates.md     ← Range, endurance, V-speeds
│   └── figures/                     ← Diagrams referenced in docs
│
├── cad/
│   ├── README.md                    ← CAD philosophy and toolchain
│   ├── wing/                        ← Wing components
│   ├── fuselage/                    ← Fuselage frame
│   ├── empennage/                   ← Tail surfaces
│   ├── landing_gear/                ← Main and nose/tail gear
│   └── propulsion/                  ← Engine mount and cowling
│
├── analysis/
│   ├── aero/                        ← Lift/drag, polar curves
│   ├── structures/                  ← Spar sizing, spar loads
│   └── stability/                   ← Static margin, trim, derivatives
│
├── electronics/
│   ├── avionics_overview.md         ← Instrument suite description
│   ├── schematics/                  ← Wiring diagrams
│   └── firmware/                    ← Arduino EFI/telemetry code
│
├── software/
│   ├── performance/                 ← Python performance calculators
│   └── simulation/                  ← Flight envelope simulation
│
├── manufacturing/
│   ├── build_guide.md               ← Master build sequence
│   ├── materials_list.md            ← BOM with pricing and alternatives
│   ├── tool_requirements.md         ← Required and optional tools
│   ├── jigs/                        ← Jig descriptions and setup
│   └── cutting_templates/           ← Print-scale templates
│
├── testing/
│   ├── ground/                      ← Static load tests, engine runs
│   └── flight/                      ← Incremental flight test cards
```

---

## Regulatory Compliance

This aircraft is designed to comply with **FAR Part 103 (Ultralight Vehicles)** in the United States:

- ✅ Single occupant
- ✅ Unpowered empty weight ≤ 115 kg (target: 113 kg)
- ✅ Fuel capacity ≤ 5 US gallons (3.5 gal specified)
- ✅ Maximum airspeed ≤ 55 knots (Vne = 55 kts)
- ✅ Power-off stall ≤ 24 knots

**Non-US builders must verify compliance with local regulations (EASA ULM, CASA RAAus, DGAC, etc.).**

No airworthiness certificate is required under Part 103. **However**, the builder assumes full responsibility for airworthiness. The documents in `/testing/` describe the validation protocol this team recommends before any flight.

---

## Cost Estimate

| Category | Low Estimate (USD) | High Estimate (USD) |
|---|---|---|
| Airframe materials (wood, fabric, hardware) | $1,800 | $3,200 |
| Engine (used Rotax 447 / budget alt.) | $1,500 | $4,500 |
| Avionics (basic) | $300 | $900 |
| Propeller | $200 | $600 |
| Instruments and controls | $400 | $1,000 |
| Consumables (glue, dope, paint) | $300 | $600 |
| **Total** | **~$4,500** | **~$10,800** |

A skilled builder with access to a workshop can complete this aircraft in **600–900 hours** of labor.

---

## Critical Warnings

1. **Do not fly without completing all ground tests** described in `/testing/ground/`
2. **Do not extend the flight envelope** beyond what the incremental test plan authorizes
3. **This design has not been certified by any aviation authority.** It is your responsibility to ensure your build meets the standards described herein
4. **Modifications to structure, propulsion, or control surfaces invalidate all analysis in this repository** and require independent engineering review
5. **Seek dual instruction** in a similar aircraft before solo flight in this design

---

## Contributing

Pull requests for error corrections, additional analysis, or build variant documentation are welcomed. All structural changes must include updated analysis files. See `CONTRIBUTING.md`.

---

## License

MIT License. See `LICENSE`. You may build, modify, and distribute freely. Attribution appreciated. **Do not remove DISCLAIMER.md.**
