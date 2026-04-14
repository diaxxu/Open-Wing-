# Ground Testing Procedures

**Document:** TEST-G-001  
**Revision:** A  

---

## GROUND TEST OVERVIEW

All ground tests must be completed and signed off **before any flight attempt**.  
No exceptions. These tests exist because they catch issues that cannot be safely discovered in the air.

Complete tests in sequence. A failed test requires corrective action and re-test from that point.

| Test Card | Description | Required | Sign-off |
|---|---|---|---|
| TC-G-001 | Engine ground run procedure | YES | [ ] |
| TC-G-002 | Wing static load test | YES | [ ] |
| TC-G-003 | Control surface deflection and rigging | YES | [ ] |
| TC-G-004 | Fastener torque check (all primary structure) | YES | [ ] |
| TC-G-005 | Weight and balance confirmation | YES | [ ] |
| TC-G-006 | Taxi tests | YES | [ ] |
| TC-G-007 | Flight control interference check | YES | [ ] |

---

## TC-G-001: Engine Ground Run

**Purpose:** Verify engine operation, fuel system, cooling system, and kill switch.  
**Required equipment:** Tachometer, EGT/CHT gauges connected, fire extinguisher (ABC, 2.5kg minimum), assistant.  
**Location:** Open area, aircraft secured to anchor points with tie-down ropes.  
**Wind:** Calm to 5 kts, aligned with aircraft heading.

### Pre-run Checklist

- [ ] Aircraft secured: tie-down rope on each main gear leg, nose gear, and tail — rope at 45° to fuselage
- [ ] Fuel quantity: full (first run)
- [ ] Fuel shutoff: OPEN
- [ ] Oil level: check per Rotax manual
- [ ] Coolant level: check per Rotax manual
- [ ] Propeller area: clear of all persons (≥5m in front, ≥3m to each side)
- [ ] Fire extinguisher: accessible, safety pin removed
- [ ] Assistant stationed: at fire extinguisher, NOT in propeller arc
- [ ] EGT/CHT gauges: powered on, reading ambient temperature (approx. 15–25°C if cold)

### Start Procedure (Rotax 447)

1. Prime: choke on (if cold), prime bulb 3–5 strokes
2. Ignition: BOTH ignitions ON (both switches up)
3. Throttle: idle position
4. Start: pull cord or electric start
5. After start: warm-up at 1,500–2,000 RPM for 3–5 minutes
6. Choke: gradually off as engine warms

### Ground Run Test Points

| Step | Action | Expected Result | Limit | Pass/Fail |
|---|---|---|---|---|
| 1 | Idle (1,500–2,000 RPM) for 5 min | Smooth idle, CHT rising | CHT < 120°C | [ ] |
| 2 | Increase to 3,000 RPM, hold 2 min | Smooth acceleration | EGT < 700°C | [ ] |
| 3 | Increase to 4,500 RPM, hold 1 min | No vibration | CHT < 180°C | [ ] |
| 4 | Increase to full throttle (max RPM), hold 15 sec | Strong thrust | CHT < 230°C | [ ] |
| 5 | Reduce to idle | Smooth deceleration | No stumble | [ ] |
| 6 | Test mag 1 only (kill mag 2): idle | Engine continues running | RPM drop < 200 | [ ] |
| 7 | Test mag 2 only (kill mag 1): idle | Engine continues running | RPM drop < 200 | [ ] |
| 8 | Both mags ON | Engine running normally | — | [ ] |
| 9 | Kill switch TEST: idle | Engine stops within 3 sec | < 3 seconds | [ ] |
| 10 | Restart, idle | Clean restart | — | [ ] |
| 11 | Idle 2 min, then shut down via kill switch | Clean shutdown | — | [ ] |

### Post-run Inspection

- [ ] Inspect entire engine for oil leaks (visual)
- [ ] Inspect all cooling hose connections for seepage
- [ ] Check exhaust clamps for tightness (may loosen on first heat cycle)
- [ ] Check propeller for cracks, delamination, nicks (visual, handle carefully)
- [ ] Check engine mount bolts for looseness (feel for movement by hand)
- [ ] Record max CHT, max EGT, and idle RPM in aircraft log

**Sign-off:** _____________________________ Date: ___________

---

## TC-G-002: Wing Static Load Test

**Purpose:** Verify the wing structure can withstand at least 2× design load.  
**Note:** This test is a sandbag load test to verify construction quality. It does not replace the structural analysis but confirms the analysis assumptions are met in the actual build.

### Method: Distributed Load Test

```
Test load: 2× MGTOW across both wings = 2 × 217 kg = 434 kg
Per wing panel: 217 kg (concentrated representation of distributed load)

Load application: sandbags placed at 1/4 span and 3/4 span positions
(1/4 span represents the approximate centroid of a triangular distribution)

Sandbag arrangement:
  Each panel: 109 kg at 1.2m from root + 109 kg at 3.6m from root
  (approximates triangular lift distribution centroid)
  
Alternative: apply load at 33% semi-span (effective centroid for uniform distribution)
  Single point: 217 kg at y = 1.6m from root per panel
```

### Procedure

1. Disconnect wing from lift struts (test wing attachment only)
2. Support aircraft fuselage rigidly (block up on sawhorses under main spar attach points)
3. Attach sandbags to wing using wide straps — **DO NOT concentrate load at single rib**
   - Spread strap across 3 rib bays minimum
4. Add weight incrementally: 50% load first, hold 30 seconds
5. Inspect: look for cracking sounds, any visible deformation at spar root
6. If no issue: add remaining 50% to full test load
7. Hold full test load for 60 seconds
8. Inspect all spar joints, root fittings, rib bonds
9. Remove load gradually
10. Inspect again after load removal

### Pass Criteria

- [ ] No cracking sounds during loading (occasional wood settling is acceptable)
- [ ] No visible deformation of spar exceeding 15mm tip deflection (mark tip with tape before test)
- [ ] No disbonding of spar caps, ribs, or root fittings
- [ ] No permanent deformation remaining after load removal
- [ ] Both panels tested (port and starboard)

**IMPORTANT:** If you observe cracking sounds or visible delamination, **stop the test immediately**, remove the load, and inspect thoroughly. Rebuild the affected assembly before retesting.

**Sign-off:** _____________________________ Date: ___________

---

## TC-G-003: Control Surface Deflection and Rigging

**Purpose:** Confirm all control surfaces move through full range, correct direction, without binding, and with correct cable tensions.

### Required Tools
- Protractor or digital angle finder (0.1° resolution)
- Cable tensiometer (1–50 kg range)
- 2m straight edge

### Elevator

| Check | Method | Limit | Pass/Fail |
|---|---|---|---|
| Full up deflection | Protractor at hinge, full back stick | 25° ±2° | [ ] |
| Full down deflection | Protractor, full forward stick | 20° ±2° | [ ] |
| Neutral position | No stick input, elevator aligns with stabilizer | ±1° | [ ] |
| Cable tension | Tensiometer both cables | 6–8 kg | [ ] |
| No binding | Move stick slowly full travel, both directions | No hard spots | [ ] |
| No vibration | Wiggle elevator at trailing edge: no slop in hinges | <1mm slop | [ ] |

### Ailerons

| Check | Method | Limit | Pass/Fail |
|---|---|---|---|
| Right aileron up | Stick right, right aileron up | 20° ±2° | [ ] |
| Right aileron down | Stick right, right aileron down | 20° ±2° | [ ] |
| Left aileron opposite | Confirm differential — both sides equal | Symmetric | [ ] |
| Neutral position | Stick centered — both ailerons aligned with wing | ±1° | [ ] |
| Cable tension | 6–8 kg each side | 6–8 kg | [ ] |

### Rudder

| Check | Method | Limit | Pass/Fail |
|---|---|---|---|
| Left rudder | Left pedal forward, rudder deflects left | 25° ±2° | [ ] |
| Right rudder | Right pedal forward, rudder deflects right | 25° ±2° | [ ] |
| Neutral | Pedals neutral, rudder aligned with fin | ±1° | [ ] |

### Combined Movement Check

Move all controls simultaneously:
- [ ] Full right aileron + full up elevator + full right rudder: no binding, no fouling
- [ ] Full left aileron + full down elevator + full left rudder: no binding, no fouling
- [ ] Full back stick + full left aileron + right rudder: no binding
- [ ] Any combination: no jamming anywhere in the envelope

**Sign-off:** _____________________________ Date: ___________

---

## TC-G-004: Fastener Torque Check

All primary structural fasteners must be torqued and marked with torque seal (torque sealing paint/pen) to detect movement.

### Primary Structural Fasteners

| Location | Fastener | Torque | Checked |
|---|---|---|---|
| Wing main spar root bolts (×4 per side) | AN4 M10 | 40 N·m | [ ] |
| Wing rear spar attach (×2 per side) | AN3 M8 | 22 N·m | [ ] |
| Lift strut clevis pins (×4) | Cotter pin (not torqued — check security) | — | [ ] |
| Engine mount bolts (×4) | M8 × 8.8 | 22 N·m | [ ] |
| Propeller bolts (×6) | M8 with Loctite 243 | 25 N·m | [ ] |
| Horizontal tail attach (×2) | AN4 | 40 N·m | [ ] |
| Vertical fin attach (×2) | AN4 | 40 N·m | [ ] |
| Main gear attach (×4 per side) | AN4 | 40 N·m | [ ] |
| Nose gear attach (×2) | AN4 | 40 N·m | [ ] |
| Seat attach (×4) | AN3 | 22 N·m | [ ] |

After torquing, apply torque seal stripe across fastener head to structure. If stripe is broken at pre-flight, re-torque before flight.

**Sign-off:** _____________________________ Date: ___________

---

## TC-G-005: Weight and Balance Confirmation

**Purpose:** Verify the actual empty weight and CG are within the design envelope.

### Equipment
- Three scales, minimum 100 kg capacity each (aircraft scales, or verified bathroom scales × 3)
- Plumb bob and chalk line
- Level (to verify aircraft is level during weighing)

### Procedure

1. Weigh aircraft empty (no fuel, no pilot, but with all installed equipment)
2. Place one scale under each main gear wheel and one under nose gear
3. Level aircraft longitudinally and laterally using reference marks on fuselage
4. Record weight on each scale: W_nose, W_left, W_right
5. Total empty weight: W_empty = W_nose + W_left + W_right

```
CG calculation:
Arms from datum:
  Nose gear at x = -500mm from datum (500mm forward of firewall)
  Main gear at x = +1,300mm from datum

CG_x = (W_nose × (-500) + (W_left + W_right) × 1300) / W_empty

MAC leading edge: x = 1,220mm (or as per final assembly)
MAC length: 1,490mm

CG as % MAC = (CG_x - 1220) / 1490 × 100
```

### Pass Criteria

- [ ] Empty weight ≤ 115 kg (FAR Part 103 limit)
- [ ] Empty CG within -5% to +15% MAC (acceptable range for empty aircraft)
- [ ] Loaded CG (with design pilot 80 kg + full fuel) falls within 27%–38% MAC

**Sign-off:** _____________________________ Date: ___________

---

## TC-G-006: Taxi Tests

**Purpose:** Verify ground handling, steering, brakes, and structural integrity at ground speeds.

⚠️ **Perform on a grass or paved runway/taxiway only. Not on public roads.**  
⚠️ **Have an observer stationed to one side, not in propeller arc.**

| Step | Action | Speed | Expected | Pass |
|---|---|---|---|---|
| T-1 | Power on, taxi straight at idle | 5–10 km/h | Straight tracking, no vibration | [ ] |
| T-2 | Left turn, full nose gear deflection | Walking pace | Smooth turn, no tip or rock | [ ] |
| T-3 | Right turn, full deflection | Walking pace | Symmetric with left | [ ] |
| T-4 | Brake test: accelerate to 20 km/h, full brakes | 20 km/h | Straight stop, no pull | [ ] |
| T-5 | Accelerate to 30 km/h, hold briefly | 30 km/h | No vibration, no flutter | [ ] |
| T-6 | Power up to 60% throttle, taxi straight | ~40 km/h | No wing rock, nose stays down | [ ] |

After taxi tests:
- [ ] Check all fasteners (feel for movement — do not fully re-torque unless found loose)
- [ ] Check tire pressures (main: 18–22 PSI, nose: 15–18 PSI)
- [ ] Inspect landing gear attachment points for cracks or movement

**Sign-off:** _____________________________ Date: ___________

---

## TC-G-007: High-Speed Taxi and Lift-off Test

⚠️ **This test must be observed by a qualified aviation person (EAA Tech Counselor or A&P mechanic).**  
⚠️ **Do not perform this test alone.**

**Purpose:** Verify the aircraft tracks straight, lifts off predictably, and returns to ground safely before committing to a flight.

### Straight runs to lift-off speed (DO NOT CLIMB)

1. Taxi to runway threshold
2. Advance throttle to 75%, maintain runway centerline
3. As the aircraft approaches takeoff speed (~14 m/s, 27 kts), allow the nosewheel to rise naturally
4. DO NOT apply back pressure — let the aircraft find its own attitude
5. If the aircraft feels like it wants to fly: close throttle, hold forward stick, allow to settle on all wheels
6. Roll out to stop, review

**Evaluate on each run:**
- [ ] Aircraft tracks straight without excessive rudder
- [ ] Nosewheel rises at approximately correct speed (~22 kts)
- [ ] No wing rock or yaw tendency during roll
- [ ] Directional control is responsive and adequate
- [ ] Brakes effective for rollout

Repeat 3 times. After three satisfactory runs without anomalies, the aircraft is ready for the Phase 1 flight test.

**Sign-off:** _____________________________ Date: ___________

---

## Pre-Flight Inspection Checklist (Daily Use)

Use this checklist before every flight after completion of build testing:

**Airframe:**
- [ ] All access panels secure
- [ ] Wing attach bolts — torque seal intact
- [ ] Lift struts: pins cotter-pinned, no cracks
- [ ] Control surface hinges: no excessive slop (< 2mm)
- [ ] Fabric: no tears, no delamination from structure
- [ ] Fuel: quantity checked, cap sealed, no odor of fuel in cockpit

**Engine:**
- [ ] Oil level: 2-stroke premix ratio correct for today's fuel fill
- [ ] Coolant level: full (Rotax 447)
- [ ] Propeller: no cracks, no delamination, no nicks >1mm deep
- [ ] Exhaust: clamps secure, no blue/black oxidation indicating air leak
- [ ] Kill switch: test function before taxi

**Controls:**
- [ ] Elevator: full travel, correct direction
- [ ] Ailerons: full travel, symmetric
- [ ] Rudder: full travel, correct direction
- [ ] Trim: set to neutral for takeoff

**Personal:**
- [ ] Pilot is current and proficient (fly similar aircraft within last 90 days)
- [ ] Weather: wind ≤ 10 kts, visibility ≥ 5 km, ceiling ≥ 1,000 ft AGL
- [ ] Someone knows your flight plan and expected return time
