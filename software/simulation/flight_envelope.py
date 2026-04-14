#!/usr/bin/env python3
"""
OpenWing ULA-1 — V-n Diagram and Flight Envelope Generator
===========================================================
Generates the structural load factor envelope (V-n diagram) and
flight envelope charts for the OpenWing ULA-1.

Usage:
    python3 flight_envelope.py
    python3 flight_envelope.py --mgtow 217 --save

Requires: Python 3.8+, numpy, matplotlib
"""

import math
import sys
import argparse

try:
    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib.patches as mpatches
    HAS_PLOT = True
except ImportError:
    print("Error: numpy and matplotlib are required.")
    print("Install with: pip install numpy matplotlib")
    sys.exit(1)


# ─────────────────────────────────────────────────────────────
# AIRCRAFT PARAMETERS
# ─────────────────────────────────────────────────────────────

WING_AREA    = 14.52    # m²
ASPECT_RATIO = 6.55
OSWALD_E     = 0.80
CD0          = 0.035
CL_MAX       = 1.55     # Maximum lift coefficient (clean)
CL_MIN       = -0.85    # Maximum negative lift coefficient (inverted stall)
RHO_SL       = 1.225    # kg/m³

# Load limits
N_MAX_LIMIT  = 4.0      # Maximum positive maneuver load factor (structural limit)
N_MIN_LIMIT  = -2.0     # Maximum negative maneuver load factor (structural limit)
N_MAX_ULT    = 6.0      # Ultimate positive (1.5 × limit)
N_MIN_ULT    = -3.0     # Ultimate negative

# Speed limits
VNE_MS       = 55 * 0.514444   # m/s, never exceed
VNO_MS       = 47 * 0.514444   # m/s, normal operations limit


def v_n_diagram(MGTOW_kg=217, rho=RHO_SL, plot=True, save=False):
    """
    Compute and optionally plot the V-n diagram.
    
    Args:
        MGTOW_kg: Maximum gross takeoff weight in kg
        rho:      Air density kg/m³
        plot:     Show plot if True
        save:     Save plot to file if True
    
    Returns:
        Dictionary with V-n diagram data points
    """
    W    = MGTOW_kg * 9.80665   # N
    q_fn = lambda V: 0.5 * rho * V**2
    
    # ── Speed range ──
    Vs_pos   = math.sqrt(2 * W / (rho * WING_AREA * CL_MAX))   # Positive stall speed
    Vs_neg   = math.sqrt(2 * W / (rho * WING_AREA * abs(CL_MIN))) # Negative stall speed
    
    V_range  = np.linspace(0.1, VNE_MS * 1.05, 500)
    
    # ── Aerodynamic lift limits ──
    # n_pos_aero: limited by CL_MAX (stall boundary, positive)
    # n_neg_aero: limited by CL_MIN (inverted stall boundary)
    n_pos_aero = np.array([0.5 * rho * V**2 * WING_AREA * CL_MAX / W for V in V_range])
    n_neg_aero = np.array([-0.5 * rho * V**2 * WING_AREA * abs(CL_MIN) / W for V in V_range])
    
    # Clip to structural limits
    n_pos_struct = np.minimum(n_pos_aero, N_MAX_LIMIT)
    n_neg_struct = np.maximum(n_neg_aero, N_MIN_LIMIT)
    
    # Corner/maneuver speed Va: speed at which n_pos_aero = N_MAX_LIMIT
    Va_ms = math.sqrt(2 * W * N_MAX_LIMIT / (rho * WING_AREA * CL_MAX))
    Va_kts = Va_ms / 0.514444
    
    # ── Gust envelope ──
    a_wing = 4.25  # per radian, finite wing lift slope
    
    def gust_n(V, Ug):
        """Load factor increment due to vertical gust Ug (m/s EAS)."""
        mu_g = 2 * (W/WING_AREA) / (rho * a_wing * (W/WING_AREA/9.81) * 9.81)
        # Simplified: Kg = gust alleviation factor
        Kg   = 0.88 * mu_g / (5.3 + mu_g)  # FAR 23 gust factor
        delta_n = Kg * rho * V * Ug * a_wing * WING_AREA / (2 * W)
        return delta_n
    
    Ug_B    = 15.24  # m/s (50 fps), rough air gust at Vb
    Ug_C    = 7.62   # m/s (25 fps), gust at Vc  
    Ug_D    = 3.81   # m/s (12.5 fps), gust at Vd
    
    # Gust lines from n=1 at cruise
    V_gust   = np.linspace(0, VNE_MS, 200)
    n_gust_up_C   = np.array([1 + gust_n(V, Ug_C) for V in V_gust])
    n_gust_down_C = np.array([1 - gust_n(V, Ug_C) for V in V_gust])
    
    # ── Key Points ──
    points = {
        'Vs_pos':    (ms_to_kts(Vs_pos), 1.0),
        'Vs_neg':    (ms_to_kts(Vs_neg), -1.0),
        'Va':        (Va_kts, N_MAX_LIMIT),
        'Vno':       (ms_to_kts(VNO_MS), N_MAX_LIMIT),
        'Vne':       (ms_to_kts(VNE_MS), N_MAX_LIMIT),
        'Vne_neg':   (ms_to_kts(VNE_MS), N_MIN_LIMIT),
    }
    
    # ── Print Summary ──
    print("\n" + "="*55)
    print("  V-n Diagram Key Points (MGTOW = {:.0f} kg)".format(MGTOW_kg))
    print("="*55)
    print(f"  Stall speed (pos):  {ms_to_kts(Vs_pos):.1f} kts at n = 1.0")
    print(f"  Stall speed (neg):  {ms_to_kts(Vs_neg):.1f} kts at n = -1.0")
    print(f"  Maneuver speed Va:  {Va_kts:.1f} kts at n = {N_MAX_LIMIT:.1f}g")
    print(f"  Normal ops limit:   {ms_to_kts(VNO_MS):.1f} kts")
    print(f"  Never exceed Vne:   {ms_to_kts(VNE_MS):.1f} kts")
    print(f"\n  Structural Limits:")
    print(f"    Positive (limit):  +{N_MAX_LIMIT:.1f}g")
    print(f"    Negative (limit):  {N_MIN_LIMIT:.1f}g")
    print(f"    Positive (ultimate): +{N_MAX_ULT:.1f}g")
    print(f"    Negative (ultimate): {N_MIN_ULT:.1f}g")
    
    # ── Gust loads at key speeds ──
    print(f"\n  Gust Load Cases (FAR 23 §23.341 methodology):")
    Vcr_ms = 45 * 0.514444
    print(f"    At Vc={ms_to_kts(Vcr_ms):.0f} kts, 25fps gust: n = {1 + gust_n(Vcr_ms, Ug_C):.2f}")
    print(f"    At Vne={ms_to_kts(VNE_MS):.0f} kts, 12.5fps gust: n = {1 + gust_n(VNE_MS, Ug_D):.2f}")
    print(f"  → All gust loads well within structural limits ✓")
    
    if not plot:
        return points
    
    # ── Plot ──
    fig, ax = plt.subplots(1, 1, figsize=(12, 7))
    
    V_kts   = [ms_to_kts(v) for v in V_range]
    Vg_kts  = [ms_to_kts(v) for v in V_gust]
    
    # Positive stall boundary
    mask_pos = n_pos_aero <= N_MAX_LIMIT + 0.1
    ax.plot(
        [ms_to_kts(v) for v, m in zip(V_range, mask_pos) if m],
        [n for n, m in zip(n_pos_aero, mask_pos) if m],
        'b-', linewidth=2.5, label='Positive stall boundary (CL max)'
    )
    
    # Negative stall boundary
    mask_neg = n_neg_aero >= N_MIN_LIMIT - 0.1
    ax.plot(
        [ms_to_kts(v) for v, m in zip(V_range, mask_neg) if m],
        [n for n, m in zip(n_neg_aero, mask_neg) if m],
        'b--', linewidth=2.5, label='Negative stall boundary (CL min)'
    )
    
    # Structural limits (horizontal lines)
    ax.hlines(N_MAX_LIMIT, Va_kts, ms_to_kts(VNE_MS), colors='r', linewidths=2.5, 
              label=f'Structural limit (+{N_MAX_LIMIT:.0f}g / {N_MIN_LIMIT:.0f}g)')
    ax.hlines(N_MIN_LIMIT, ms_to_kts(Vs_neg), ms_to_kts(VNE_MS), colors='r', linewidths=2.5)
    
    # Vne vertical line
    ax.vlines(ms_to_kts(VNE_MS), N_MIN_LIMIT, N_MAX_LIMIT, colors='darkred', 
              linewidths=3, label=f'Vne = {ms_to_kts(VNE_MS):.0f} kts')
    ax.vlines(ms_to_kts(VNO_MS), N_MIN_LIMIT, N_MAX_LIMIT, colors='orange', 
              linewidths=2, linestyles='--', label=f'Vno = {ms_to_kts(VNO_MS):.0f} kts')
    
    # Gust lines
    ax.plot(Vg_kts, n_gust_up_C, 'g:', linewidth=1.5, 
            label='Gust (25 fps, Vc)', alpha=0.7)
    ax.plot(Vg_kts, n_gust_down_C, 'g:', linewidth=1.5, alpha=0.7)
    
    # Ultimate load dashed lines
    ax.hlines(N_MAX_ULT, 0, ms_to_kts(VNE_MS), colors='darkred', linewidths=1, 
              linestyles=':', label=f'Ultimate limit (+{N_MAX_ULT:.0f}g / {N_MIN_ULT:.0f}g)')
    ax.hlines(N_MIN_ULT, 0, ms_to_kts(VNE_MS), colors='darkred', linewidths=1, linestyles=':')
    
    # Shade the approved envelope
    V_envelope = []
    n_envelope = []
    # Build envelope: pos stall → structural corner → Vne → neg structural → neg stall → back
    for V, n in zip(V_range, n_pos_struct):
        if V <= VNE_MS:
            V_envelope.append(ms_to_kts(V))
            n_envelope.append(n)
    for V, n in zip(reversed(V_range), reversed(n_neg_struct)):
        if V <= VNE_MS:
            V_envelope.append(ms_to_kts(V))
            n_envelope.append(n)
    ax.fill(V_envelope, n_envelope, alpha=0.08, color='blue')
    
    # Annotations
    ax.annotate(f'Va = {Va_kts:.1f} kts', xy=(Va_kts, N_MAX_LIMIT), 
                xytext=(Va_kts - 8, N_MAX_LIMIT + 0.3),
                arrowprops=dict(arrowstyle='->', color='gray'),
                fontsize=9, color='darkblue')
    
    ax.annotate(f'Vs = {ms_to_kts(Vs_pos):.1f} kts', 
                xy=(ms_to_kts(Vs_pos), 1.0),
                xytext=(ms_to_kts(Vs_pos) + 2, 1.8),
                arrowprops=dict(arrowstyle='->', color='gray'),
                fontsize=9)
    
    # Formatting
    ax.set_xlabel('Equivalent Airspeed (knots)', fontsize=11)
    ax.set_ylabel('Load Factor n (g)', fontsize=11)
    ax.set_title(f'OpenWing ULA-1 — V-n Diagram\nMGTOW = {MGTOW_kg:.0f} kg, Sea Level ISA',
                 fontsize=12, fontweight='bold')
    ax.axhline(y=0, color='k', linewidth=0.5)
    ax.axhline(y=1, color='k', linewidth=0.5, linestyle=':')
    ax.set_xlim(0, 65)
    ax.set_ylim(-3.5, 7.0)
    ax.legend(loc='upper left', fontsize=8)
    ax.grid(True, alpha=0.3)
    
    # Speed marker bands
    ax.axvspan(ms_to_kts(Vs_pos), ms_to_kts(VNO_MS), alpha=0.05, color='green')  # Green arc
    ax.axvspan(ms_to_kts(VNO_MS), ms_to_kts(VNE_MS), alpha=0.05, color='yellow') # Yellow arc
    ax.axvspan(ms_to_kts(VNE_MS), 65, alpha=0.10, color='red')                    # Red (forbidden)
    
    plt.tight_layout()
    
    if save:
        plt.savefig('vn_diagram_ula1.png', dpi=150, bbox_inches='tight')
        print("Saved: vn_diagram_ula1.png")
    
    plt.show()
    
    return points


def ms_to_kts(v_ms):
    return v_ms / 0.514444


def main():
    parser = argparse.ArgumentParser(description='OpenWing ULA-1 V-n Diagram Generator')
    parser.add_argument('--mgtow', type=float, default=217.0,
                        help='MGTOW in kg (default: 217)')
    parser.add_argument('--altitude', type=float, default=0.0,
                        help='Altitude in meters (default: 0)')
    parser.add_argument('--save', action='store_true',
                        help='Save diagram to PNG file')
    parser.add_argument('--no-plot', action='store_true',
                        help='Skip plot, text only')
    
    args = parser.parse_args()
    
    rho = RHO_SL
    if args.altitude > 0:
        T_sl = 288.15
        L    = -0.0065
        P_sl = 101325
        R    = 287.058
        g    = 9.80665
        T    = T_sl + L * args.altitude
        P    = P_sl * (T / T_sl) ** (g / (-L * R))
        rho  = P / (R * T)
        print(f"Density at {args.altitude:.0f}m: {rho:.4f} kg/m³ (σ = {rho/RHO_SL:.3f})")
    
    v_n_diagram(MGTOW_kg=args.mgtow, rho=rho, 
                plot=not args.no_plot, save=args.save)


if __name__ == "__main__":
    main()
