# Incremental Flight Test Plan

**Document:** TEST-F-001  
**Revision:** A  

---

## CRITICAL SAFETY PRINCIPLES

1. **This is an experimental, unproven aircraft.** Every flight is a test flight until the full envelope is cleared.
2. **Expand the envelope one step at a time.** Never skip a test card.
3. **Have an out on every maneuver.** Know where you will land if the engine stops.
4. **Never fly beyond the cleared envelope.** It is not cowardice — it is professionalism.
5. **Brief each test card** with a ground observer before flying. They should know what you plan to do and what a normal outcome looks like.
6. **An EAA Technical Counselor or DAR (Designated Airworthiness Representative) review** before Phase 1 flight is strongly recommended.
7. **If anything feels wrong — land.** Do not press on. The aircraft will be there tomorrow.

---

## Phase 1: First Flights (Hours 0–5)

### Flight Test Card FT-001: First Flight

**Conditions:**  
- Calm wind (≤ 5 kts), light chop only
- Visibility ≥ 8 km, ceiling ≥ 1,500 ft AGL
- Ground observer with radio and binoculars
- Airport or airstrip with at least 600m of usable surface
- Pilot proficient in similar ultralight within last 30 days

**Pilot weight:** Design pilot (80 kg ±10 kg)  
**Fuel:** Full  
**CG:** Confirmed within envelope

**Objective:** First flight. Get airborne, assess basic handling, land safely.

**Profile:**
1. Taxi to threshold, complete pre-takeoff checks (controls, engine instruments)
2. Take off, climb to 150m (500 ft) AGL **DIRECTLY OVER THE AIRFIELD**
3. DO NOT depart the airport boundary on first flight
4. Fly a gentle left-hand pattern at 150m AGL at approximately 40 kts
5. Assess: Does the aircraft feel stable? Does it require constant correction? Can you trim hands-off?
6. One complete circuit, then land

**Data to record after landing:**
- [ ] Did aircraft track straight on takeoff roll?
- [ ] Did aircraft lift off smoothly at approximately expected speed?
- [ ] Did aircraft climb at expected rate?
- [ ] Was pitch control responsive and appropriately stable?
- [ ] Was roll control adequate and symmetric?
- [ ] Any unusual sounds, vibrations, or handling?
- [ ] Approximate trim speed (speed at which hands-off is stable)

**Pass criteria for FT-001:**
- [ ] Aircraft took off and landed safely
- [ ] No abnormal vibration or structural sounds
- [ ] Basic control in pitch, roll, yaw was positive and predictable
- [ ] Engine operated within temperature limits throughout

**Sign-off:** _____________________________ Date: ___________

---

### Flight Test Card FT-002: Handling Assessment

**Prerequisites:** FT-001 passed.  
**Conditions:** Same as FT-001.

**Objective:** Evaluate control responses, trim, and basic stability.

**Profile (at ≥300m AGL, over or adjacent to airfield):**

1. Establish level flight at 40 kts, trim hands-off
   - Record stick position for hands-off flight
   - Does aircraft return to trim speed after small pitch disturbance? (Release and watch)

2. Speed variation:
   - Slow to 30 kts (still above stall — do NOT approach stall yet)
   - Assess: Heavy stick forces? Roll tendency?
   - Accelerate to 45 kts
   - Assess: Stick forces light, medium, heavy?

3. Gentle turns:
   - 15° bank left, hold 10 seconds. Release controls. Does aircraft self-level?
   - 15° bank right, hold 10 seconds. Release controls.
   - Assess: Is roll stability neutral, positive, or negative? Does bank increase without input?

4. Rudder response:
   - Apply brief left rudder pulse, release. Does aircraft yaw and then return?
   - Repeat right. Assess Dutch roll tendency (yaw/roll coupling oscillation).

5. Land and debrief.

**Pass criteria:**
- [ ] Aircraft is longitudinally stable (returns to trim speed within 30 seconds after release)
- [ ] Roll stability is neutral to positive (does not diverge in bank)
- [ ] No Dutch roll oscillation that does not damp within 3 cycles
- [ ] Control forces are acceptable (not excessively heavy or light)

**Sign-off:** _____________________________ Date: ___________

---

### Flight Test Card FT-003: Stall Approach (Buffet Warning)

**Prerequisites:** FT-001 and FT-002 passed, minimum 3 hours on this aircraft.  
**Altitude:** Minimum 600m (2,000 ft) AGL — you need recovery altitude.  
**Location:** Over or near the airfield.  
**Note:** This test approaches but does NOT enter the stall.

**Objective:** Identify the pre-stall buffet warning and note the speed at which it occurs.

**Procedure:**
1. Establish level flight at 45 kts, trim
2. Close throttle to idle
3. Gently and slowly raise the nose (1–2 kts per 5 seconds — very slow deceleration)
4. Note the speed at which buffet (airframe shaking/vibration) begins: **record this speed**
5. As soon as buffet begins, lower the nose immediately and add power
6. DO NOT wait for a full stall break on this first test
7. Return to cruise, repeat 2 more times to confirm the buffet speed

**Data:**
- Buffet onset speed: _______ kts IAS
- Stick position at buffet: _______ (degrees aft of neutral)
- Any roll tendency at buffet: Yes / No / Left / Right

**Pass criteria:**
- [ ] Clear buffet warning occurs at least 3–5 kts above stall speed
- [ ] No violent roll at or near buffet
- [ ] Recovery to normal flight is immediate upon forward stick

**Sign-off:** _____________________________ Date: ___________

---

### Flight Test Card FT-004: Full Stall (Power Off)

**Prerequisites:** FT-003 passed, minimum 5 hours on this aircraft.  
**Altitude:** Minimum 900m (3,000 ft) AGL.  
**Location:** Open area, no obstacles beneath, airfield within gliding distance.  

**Objective:** Determine actual stall speed, verify stall character is benign and recoverable.

**Procedure:**
1. Establish level flight at 45 kts, trim, power off
2. Very slowly raise nose (as in FT-003), past buffet, until stall break occurs
3. Note: the stall break is a significant nose drop and/or roll
4. Immediately upon stall break: relax back pressure, lower nose, add power
5. Record stall speed, stall character, roll tendency, recovery altitude lost
6. Repeat 3 times to verify consistency

**Data:**
| Run | Stall speed (kts IAS) | Roll tendency | Height lost in recovery |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |

**Pass criteria:**
- [ ] Stall speed ≤ 24 kts IAS (FAR Part 103 compliance)
- [ ] Stall has adequate warning (buffet ≥ 3 kts before break)
- [ ] Stall break is not violent (no snap roll or uncontrolled nose-drop exceeding 30°)
- [ ] Recovery completed within 60m altitude loss using standard technique (relax + power)
- [ ] No wing drop exceeding 30° before recovery is initiated

**If any pass criterion fails:**  
STOP TESTING. Return to base. Investigate CG, rigging, or airfoil construction. Do not fly further until resolved.

**Sign-off:** _____________________________ Date: ___________

---

## Phase 2: Envelope Expansion (Hours 5–15)

### Flight Test Card FT-005: Rate of Climb

**Prerequisites:** Phase 1 complete.

**Procedure:**
1. Take off, climb at Vy (45 kts based on analysis) from liftoff to 300m AGL
2. Record time from wheels-off to 300m altitude (use altimeter and watch)
3. Calculate rate of climb: ROC = 300m / time_seconds × 60 (m/min)
4. Compare to predicted ROC of 250 m/min minimum

**Pass criteria:**
- [ ] ROC ≥ 120 m/min (200 fpm) — minimum acceptable
- [ ] ROC ≥ 200 m/min (350 fpm) — expected performance

**Sign-off:** _____________________________ Date: ___________

---

### Flight Test Card FT-006: Cruise Performance Verification

**Prerequisites:** Phase 1 complete.

**Procedure:**
1. Establish level flight at 75% power
2. Allow 5 minutes to stabilize
3. Record: throttle setting, IAS, altitude (note altitude stability — maintains ±30m for 2 minutes)
4. Measure fuel consumption over 20 minutes at cruise: note fuel remaining vs expected

**Pass criteria:**
- [ ] Cruise IAS falls between 40–50 kts at 75% power
- [ ] Fuel consumption consistent with 10–12 L/hr at cruise
- [ ] Aircraft can be trimmed hands-off for ≥2 minutes without significant drift

**Sign-off:** _____________________________ Date: ___________

---

### Flight Test Card FT-007: Speed Limit Approach

**Prerequisites:** Phase 1 complete, FT-005 and FT-006 passed.  
**Altitude:** 600m AGL minimum.  
**Note:** Approach Vne in 2-knot increments. Do NOT exceed 55 kts IAS.

**Procedure:**
1. Enter shallow dive or level flight at max power
2. Stabilize at 48 kts: check for any flutter, vibration, control anomalies
3. If clear: proceed to 50 kts, stabilize, evaluate
4. If clear: proceed to 52 kts, stabilize, evaluate
5. If clear: proceed to 54 kts, stabilize, evaluate — **THIS IS THE LIMIT. DO NOT EXCEED.**
6. Record handling quality at each speed: any flutter, buffet, control heaviness, instability

**Flutter check:** Look at wing, watch for any rapid oscillation of surface or trailing edge. If any flutter is detected at ANY speed: immediately reduce speed by closing throttle, do NOT pull up sharply, return to base immediately and do not fly again until investigated.

**Pass criteria:**
- [ ] No flutter or surface oscillation at any tested speed
- [ ] No abnormal vibration at any tested speed
- [ ] Controls remain effective and predictable throughout
- [ ] Aircraft is comfortable to fly at 54 kts (2 kts below Vne)

**Sign-off:** _____________________________ Date: ___________

---

## Phase 3: Cross-Country Clearance (Hours 15–25)

After successful completion of Phase 2 tests:

### FT-008: Extended Solo Flight
**Objective:** 45-minute flight including departure and return. Verify fuel consumption, navigation, engine endurance.

### FT-009: Engine-Out Practice
- At 600m+ AGL, reduce to idle (simulate engine failure)
- Immediately identify landing area
- Glide to within 150m of intended field, then add power and climb
- Practice this until it is routine
- Know your glide ratio (10:1 — from 300m, you have 3km of glide)

### FT-010: Wind and Crosswind
- Land in crosswind up to 5 kts from 30° off runway centerline
- Verify handling is manageable
- Note maximum demonstrated crosswind component

---

## Phase Completion Sign-off

After completing all flight test cards:

| Phase | Signed by | Date | Remarks |
|---|---|---|---|
| Phase 1 (FT-001 to FT-004) | | | |
| Phase 2 (FT-005 to FT-007) | | | |
| Phase 3 (FT-008 to FT-010) | | | |

**Aircraft cleared for normal recreational flight (within demonstrated envelope):**

Builder/Pilot: _____________________________ Date: ___________

Observer: _____________________________ Date: ___________

---

## Emergency Procedures Reference Card

*(Laminate and keep in cockpit)*

**ENGINE FAILURE IN FLIGHT:**
1. Best glide speed: 40 kts
2. Select landing area (now — you have time only at altitude)
3. Fuel shutoff: CLOSED
4. Ignition: OFF
5. Land in best available field
6. Before touchdown: shoulder harness tight, brace

**ENGINE FIRE:**
1. Fuel shutoff: CLOSED immediately
2. Ignition: OFF
3. Maximum glide, land ASAP
4. After landing: evacuate immediately

**UNCONTROLLED ROLL:**
1. Apply opposite aileron FIRMLY
2. If no response: apply opposite rudder
3. Recover to wings level, then assess altitude and situation

**STRUCTURAL DAMAGE (flutter, unusual vibration):**
1. DO NOT pull up sharply — reduce speed gently
2. Close throttle, maintain controlled descent
3. Land immediately at nearest suitable area
4. Declare emergency on CTAF if radio equipped
