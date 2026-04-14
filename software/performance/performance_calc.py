#!/usr/bin/env python3
"""
OpenWing ULA-1 Performance Calculator
======================================
Computes key performance parameters for the OpenWing ULA-1 ultralight aircraft.
All SI units unless stated otherwise.

Usage:
    python3 performance_calc.py
    python3 performance_calc.py --altitude 1500 --temp 30 --pilot-mass 85

Requires: Python 3.8+, numpy, matplotlib
Install:  pip install numpy matplotlib
"""

import argparse
import math
import sys

try:
    import numpy as np
    import matplotlib.pyplot as plt
    HAS_PLOT = True
except ImportError:
    print("Warning: numpy/matplotlib not found. Text output only.")
    HAS_PLOT = False

# ─────────────────────────────────────────────────
# AIRCRAFT MASTER PARAMETERS
# ─────────────────────────────────────────────────

class AircraftParams:
    """Master parameter block — all values from design documents."""
    
    # Geometry
    wingspan        = 9.75          # m
    chord           = 1.490         # m
    wing_area       = 14.52         # m²
    aspect_ratio    = 6.55
    oswald_e        = 0.80          # Oswald efficiency
    
    # Aerodynamics
    CD0             = 0.035         # Zero-lift drag coefficient
    CL_max          = 1.55          # Max lift coefficient (Clark Y)
    CL_alpha        = 4.25          # Wing lift curve slope, rad⁻¹
    alpha_0         = -4.0          # Zero-lift angle of attack, deg
    
    # Weights
    empty_mass      = 105.8         # kg
    fuel_mass_full  = 9.50          # kg (13.2 L × 0.72 kg/L)
    
    # Propulsion
    P_max_kW        = 29.4          # kW (Rotax 447 max)
    P_cont_kW       = 26.5          # kW (continuous rating)
    BSFC            = 0.38          # kg/(kW·hr) specific fuel consumption
    eta_prop_climb  = 0.65          # Propeller efficiency in climb
    eta_prop_cruise = 0.72          # Propeller efficiency at cruise
    
    # Limits
    Vne_kts         = 55.0          # Never-exceed speed, knots
    n_max           = 4.0           # Maximum positive load factor
    n_min           = -2.0          # Maximum negative load factor


class Atmosphere:
    """ISA atmosphere model with temperature offset."""
    
    def __init__(self, altitude_m=0, delta_T_C=0):
        self.h   = altitude_m
        self.dT  = delta_T_C
        
        T_sl     = 288.15            # K, sea level ISA
        L        = -0.0065           # K/m lapse rate (troposphere)
        P_sl     = 101325            # Pa
        rho_sl   = 1.2250            # kg/m³
        g        = 9.80665           # m/s²
        R        = 287.058           # J/(kg·K)
        
        T_isa    = T_sl + L * altitude_m
        self.T   = T_isa + delta_T_C  # K, actual temperature
        self.P   = P_sl * (T_isa / T_sl) ** (g / (-L * R))
        self.rho = self.P / (R * self.T)
        self.sigma = self.rho / rho_sl  # density ratio
    
    def density_altitude(self):
        """Return density altitude in meters."""
        T_sl  = 288.15
        L     = -0.0065
        R     = 287.058
        g     = 9.80665
        P_sl  = 101325
        # From definition: density altitude is the ISA altitude where ρ = actual ρ
        h_DA = (T_sl / L) * (1 - (self.rho * R * T_sl / P_sl) ** (L * R / g))
        return h_DA


def knots_to_ms(v_kts):
    return v_kts * 0.514444

def ms_to_kts(v_ms):
    return v_ms / 0.514444

def ms_to_fpm(v_ms):
    return v_ms * 196.85


def compute_performance(pilot_mass_kg, fuel_fraction=1.0, atmo=None, verbose=True):
    """
    Compute performance at given loading condition and atmosphere.
    
    Args:
        pilot_mass_kg:  Pilot weight in kg
        fuel_fraction:  Fraction of full fuel load (0.0–1.0)
        atmo:           Atmosphere object (default: sea level ISA)
        verbose:        Print results to stdout
    
    Returns:
        Dictionary of performance parameters
    """
    if atmo is None:
        atmo = Atmosphere()
    
    ac = AircraftParams()
    
    # ── Weights ──
    fuel_mass  = ac.fuel_mass_full * fuel_fraction
    MGTOW      = ac.empty_mass + pilot_mass_kg + fuel_mass
    W          = MGTOW * 9.80665                 # N
    
    rho        = atmo.rho
    
    # ── Aerodynamics ──
    k          = 1.0 / (math.pi * ac.oswald_e * ac.aspect_ratio)  # induced drag factor
    
    # Stall speed (power off)
    Vs_ms      = math.sqrt(2 * W / (rho * ac.wing_area * ac.CL_max))
    Vs_kts     = ms_to_kts(Vs_ms)
    
    # Best glide speed (min power required per unit speed)
    CL_bg      = math.sqrt(ac.CD0 / k)          # CL at max L/D
    CD_bg      = 2 * ac.CD0                      # CD at max L/D (CDi = CD0)
    LD_max     = CL_bg / CD_bg
    Vbg_ms     = math.sqrt(2 * W / (rho * ac.wing_area * CL_bg))
    Vbg_kts    = ms_to_kts(Vbg_ms)
    
    # Min sink speed (for maximum endurance glide)
    CL_ms_sink = math.sqrt(3 * ac.CD0 / k)
    Vms_ms     = math.sqrt(2 * W / (rho * ac.wing_area * CL_ms_sink))
    Vms_kts    = ms_to_kts(Vms_ms)
    
    # Sink rate at best glide
    sink_bg    = Vbg_ms / LD_max                 # m/s
    
    # ── Power Curves ──
    V_range    = [v * 0.1 for v in range(int(Vs_ms * 10), 
                                          int(knots_to_ms(ac.Vne_kts) * 10) + 1)]
    
    T_req_list = []
    P_req_list = []
    T_avail_list = []
    P_avail_list = []
    
    for V in V_range:
        CL   = 2 * W / (rho * V**2 * ac.wing_area)
        CDi  = k * CL**2
        CD   = ac.CD0 + CDi
        D    = 0.5 * rho * V**2 * ac.wing_area * CD
        T_req_list.append(D)
        P_req_list.append(D * V / 1000)          # kW
        
        # Available power (simplified: linear taper from max at low speed to 85% at Vne)
        fraction = 0.90 - 0.05 * (V - Vs_ms) / (knots_to_ms(ac.Vne_kts) - Vs_ms)
        P_avail  = ac.P_max_kW * ac.eta_prop_climb * max(0.5, fraction)
        T_avail_list.append(P_avail * 1000 / V)
        P_avail_list.append(P_avail)
    
    # ── Climb Performance ──
    # Find Vy: speed of maximum excess power
    excess_P   = [pa - pr for pa, pr in zip(P_avail_list, P_req_list)]
    max_excess = max(excess_P)
    Vy_idx     = excess_P.index(max_excess)
    Vy_ms      = V_range[Vy_idx]
    Vy_kts     = ms_to_kts(Vy_ms)
    
    ROC_ms     = max_excess * 1000 / W             # m/s
    ROC_fpm    = ms_to_fpm(ROC_ms)
    
    # ── Cruise Performance ──
    # At 75% power (continuous)
    P_cruise   = 0.75 * ac.P_cont_kW              # kW
    
    # Find cruise speed: where P_req = P_cruise × eta_prop
    P_cruise_eff = P_cruise * ac.eta_prop_cruise   # kW effective thrust power
    
    # Iterate for cruise speed
    Vcr_ms = Vbg_ms  # Initial guess
    for _ in range(100):
        CL   = 2 * W / (rho * Vcr_ms**2 * ac.wing_area)
        CDi  = k * CL**2
        CD   = ac.CD0 + CDi
        D    = 0.5 * rho * Vcr_ms**2 * ac.wing_area * CD
        P_r  = D * Vcr_ms / 1000                   # kW thrust power
        if abs(P_r - P_cruise_eff) < 0.01:
            break
        Vcr_ms += (P_cruise_eff - P_r) / (P_cruise_eff + P_r) * 0.5
    
    Vcr_kts    = ms_to_kts(Vcr_ms)
    CL_cr      = 2 * W / (rho * Vcr_ms**2 * ac.wing_area)
    CD_cr      = ac.CD0 + k * CL_cr**2
    LD_cr      = CL_cr / CD_cr
    
    # ── Fuel and Range ──
    fuel_flow_kghr = ac.BSFC * P_cruise            # kg/hr
    fuel_flow_Lhr  = fuel_flow_kghr / 0.72         # L/hr (at 0.72 kg/L)
    
    endurance_hr   = fuel_mass / fuel_flow_kghr    # total endurance
    reserve_hr     = 0.75                          # 45-min reserve
    useful_hr      = max(0, endurance_hr - reserve_hr)
    range_km       = useful_hr * Vcr_ms * 3.6      # km
    range_nm       = range_km / 1.852
    
    # ── Takeoff Estimate ──
    V_liftoff      = 1.10 * Vs_ms
    T_static       = 450 * math.sqrt(atmo.sigma)   # N, estimated static thrust (sea-level scaled)
    mu_r           = 0.04                          # Rolling resistance
    F_net          = T_static - mu_r * W
    accel          = F_net / MGTOW                 # m/s²
    ground_roll    = V_liftoff**2 / (2 * accel) if accel > 0 else float('inf')
    
    # ── V-Speeds ──
    Va_kts         = Vs_kts * math.sqrt(ac.n_max)  # Maneuver speed
    Vno_kts        = min(ac.Vne_kts * 0.85, 47)    # Normal operating limit
    
    results = {
        'MGTOW_kg':         MGTOW,
        'W_N':              W,
        'rho':              rho,
        'density_alt_m':    atmo.density_altitude(),
        'Vs_kts':           Vs_kts,
        'Vs_ms':            Vs_ms,
        'Vbg_kts':          Vbg_kts,
        'Vms_kts':          Vms_kts,
        'Vy_kts':           Vy_kts,
        'Va_kts':           Va_kts,
        'Vno_kts':          Vno_kts,
        'Vne_kts':          ac.Vne_kts,
        'LD_max':           LD_max,
        'LD_cruise':        LD_cr,
        'CL_bg':            CL_bg,
        'sink_bg_ms':       sink_bg,
        'ROC_fpm':          ROC_fpm,
        'ROC_ms':           ROC_ms,
        'Vcruise_kts':      Vcr_kts,
        'fuel_flow_Lhr':    fuel_flow_Lhr,
        'endurance_hr':     endurance_hr,
        'range_km':         range_km,
        'range_nm':         range_nm,
        'ground_roll_m':    ground_roll,
        'V_range':          V_range,
        'P_req_kW':         P_req_list,
        'P_avail_kW':       P_avail_list,
        'excess_P_kW':      excess_P,
    }
    
    if verbose:
        print_results(results, pilot_mass_kg, fuel_fraction, atmo)
    
    return results


def print_results(r, pilot_mass, fuel_fraction, atmo):
    """Print formatted performance summary."""
    line = "─" * 55
    print(f"\n{'═'*55}")
    print(f"  OpenWing ULA-1 Performance Summary")
    print(f"{'═'*55}")
    print(f"  Pilot mass:    {pilot_mass:.0f} kg")
    print(f"  Fuel:          {fuel_fraction*100:.0f}% ({fuel_fraction * 9.50:.1f} kg)")
    print(f"  MGTOW:         {r['MGTOW_kg']:.1f} kg ({r['MGTOW_kg']*2.2046:.0f} lbs)")
    print(f"  Altitude:      {atmo.h:.0f} m ({atmo.h*3.281:.0f} ft)")
    print(f"  Density alt:   {r['density_alt_m']:.0f} m ({r['density_alt_m']*3.281:.0f} ft)")
    print(f"  Air density:   {r['rho']:.4f} kg/m³ ({r['rho']/1.225:.3f} σ)")
    print(f"\n{line}")
    print(f"  SPEEDS")
    print(f"{line}")
    print(f"  Stall  (Vs):   {r['Vs_kts']:.1f} kts  ({r['Vs_ms']*3.6:.1f} km/h)")
    
    part103_ok = "✓ COMPLIANT" if r['Vs_kts'] <= 24.0 else "✗ EXCEEDS LIMIT"
    print(f"                 FAR Part 103 limit: 24 kts — {part103_ok}")
    
    print(f"  Best glide:    {r['Vbg_kts']:.1f} kts  ({r['Vbg_kts']*1.852:.1f} km/h)")
    print(f"  Min sink:      {r['Vms_kts']:.1f} kts  ({r['Vms_kts']*1.852:.1f} km/h)")
    print(f"  Best climb(Vy): {r['Vy_kts']:.1f} kts ({r['Vy_kts']*1.852:.1f} km/h)")
    print(f"  Cruise (75%P): {r['Vcruise_kts']:.1f} kts ({r['Vcruise_kts']*1.852:.1f} km/h)")
    print(f"  Maneuver (Va): {r['Va_kts']:.1f} kts")
    print(f"  Max normal(Vno): {r['Vno_kts']:.1f} kts")
    print(f"  Never exceed(Vne): {r['Vne_kts']:.1f} kts")
    
    print(f"\n{line}")
    print(f"  CLIMB PERFORMANCE")
    print(f"{line}")
    print(f"  Rate of climb: {r['ROC_fpm']:.0f} fpm  ({r['ROC_ms']:.2f} m/s)")
    
    print(f"\n{line}")
    print(f"  GLIDE PERFORMANCE")
    print(f"{line}")
    print(f"  Max L/D:       {r['LD_max']:.1f}:1  at {r['Vbg_kts']:.1f} kts")
    print(f"  Sink rate:     {r['sink_bg_ms']*196.85:.0f} fpm at best glide")
    print(f"  Cruise L/D:    {r['LD_cruise']:.1f}:1")
    
    print(f"\n{line}")
    print(f"  RANGE & ENDURANCE")
    print(f"{line}")
    print(f"  Fuel flow:     {r['fuel_flow_Lhr']:.1f} L/hr at cruise")
    print(f"  Total endurance: {r['endurance_hr']:.2f} hr ({r['endurance_hr']*60:.0f} min)")
    print(f"  With 45-min reserve:")
    print(f"    Range:       {r['range_km']:.0f} km  ({r['range_nm']:.0f} nm)")
    
    print(f"\n{line}")
    print(f"  TAKEOFF (estimate)")
    print(f"{line}")
    print(f"  Ground roll:   {r['ground_roll_m']:.0f} m  ({r['ground_roll_m']*3.281:.0f} ft)")
    print(f"{'═'*55}\n")


def plot_power_curves(results, title="Power Required vs. Available"):
    """Plot power required and available curves."""
    if not HAS_PLOT:
        print("Matplotlib not available — skipping plot.")
        return
    
    V_kts = [ms_to_kts(v) for v in results['V_range']]
    
    fig, axes = plt.subplots(2, 1, figsize=(10, 8))
    
    # Power curves
    ax1 = axes[0]
    ax1.plot(V_kts, results['P_req_kW'], 'b-', linewidth=2, label='Power Required')
    ax1.plot(V_kts, results['P_avail_kW'], 'r--', linewidth=2, label='Power Available (climb)')
    ax1.fill_between(V_kts, results['P_req_kW'], results['P_avail_kW'],
                     where=[pa > pr for pa, pr in zip(results['P_avail_kW'], results['P_req_kW'])],
                     alpha=0.2, color='green', label='Excess Power (climb)')
    ax1.axvline(x=results['Vs_kts'], color='orange', linestyle=':', label=f"Vs = {results['Vs_kts']:.1f} kts")
    ax1.axvline(x=results['Vbg_kts'], color='purple', linestyle=':', label=f"Vbg = {results['Vbg_kts']:.1f} kts")
    ax1.set_xlabel('Airspeed (knots)')
    ax1.set_ylabel('Power (kW)')
    ax1.set_title(title)
    ax1.legend(fontsize=8)
    ax1.grid(True, alpha=0.3)
    ax1.set_xlim([results['Vs_kts'] - 2, 60])
    ax1.set_ylim([0, max(results['P_avail_kW']) * 1.2])
    
    # Excess power (rate of climb)
    ax2 = axes[1]
    W = results['W_N']
    roc_fpm = [ep * 1000 / W * 196.85 for ep in results['excess_P_kW']]
    ax2.plot(V_kts, roc_fpm, 'g-', linewidth=2)
    ax2.axhline(y=0, color='k', linewidth=0.5)
    ax2.axvline(x=results['Vy_kts'], color='r', linestyle='--', 
                label=f"Vy = {results['Vy_kts']:.1f} kts")
    ax2.fill_between(V_kts, roc_fpm, 0,
                     where=[r >= 0 for r in roc_fpm],
                     alpha=0.2, color='green')
    ax2.set_xlabel('Airspeed (knots)')
    ax2.set_ylabel('Rate of Climb (fpm)')
    ax2.set_title('Rate of Climb vs. Airspeed')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    ax2.set_xlim([results['Vs_kts'] - 2, 60])
    
    plt.tight_layout()
    plt.savefig('performance_curves.png', dpi=150, bbox_inches='tight')
    print("Saved: performance_curves.png")
    plt.show()


def main():
    parser = argparse.ArgumentParser(
        description='OpenWing ULA-1 Performance Calculator',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 performance_calc.py
  python3 performance_calc.py --pilot-mass 90 --altitude 1500 --temp 35
  python3 performance_calc.py --pilot-mass 56 --fuel 0.5 --no-plot
        """
    )
    parser.add_argument('--pilot-mass', type=float, default=80.0,
                        help='Pilot mass in kg (default: 80)')
    parser.add_argument('--altitude', type=float, default=0.0,
                        help='Altitude in meters MSL (default: 0, sea level)')
    parser.add_argument('--temp', type=float, default=0.0,
                        help='Temperature offset from ISA in °C (default: 0)')
    parser.add_argument('--fuel', type=float, default=1.0,
                        help='Fuel fraction, 0.0–1.0 (default: 1.0 = full)')
    parser.add_argument('--no-plot', action='store_true',
                        help='Skip plotting (text output only)')
    
    args = parser.parse_args()
    
    if not 40 <= args.pilot_mass <= 120:
        print(f"Warning: Pilot mass {args.pilot_mass} kg is outside the design range (40–120 kg)")
    
    if args.pilot_mass > 102:
        print(f"Warning: Pilot mass {args.pilot_mass} kg exceeds 95th percentile (102 kg).")
        print("  Verify stall speed ≤ 24 kts before flight.")
    
    atmo = Atmosphere(altitude_m=args.altitude, delta_T_C=args.temp)
    
    print(f"\nAtmosphere: {args.altitude:.0f}m, ISA+{args.temp:.0f}°C")
    print(f"  T = {atmo.T - 273.15:.1f}°C, ρ = {atmo.rho:.4f} kg/m³, σ = {atmo.rho/1.225:.3f}")
    
    results = compute_performance(
        pilot_mass_kg=args.pilot_mass,
        fuel_fraction=args.fuel,
        atmo=atmo,
        verbose=True
    )
    
    # FAR Part 103 compliance check
    print("\n--- FAR Part 103 Compliance Check ---")
    vs_ok   = results['Vs_kts'] <= 24.0
    vne_ok  = results['Vne_kts'] <= 55.0
    ew_ok   = AircraftParams.empty_mass <= 115.0
    
    print(f"  Stall ≤ 24 kts:   {results['Vs_kts']:.1f} kts — {'✓ PASS' if vs_ok else '✗ FAIL'}")
    print(f"  Vne ≤ 55 kts:     {results['Vne_kts']:.1f} kts — {'✓ PASS' if vne_ok else '✗ FAIL'}")
    print(f"  Empty ≤ 115 kg:   {AircraftParams.empty_mass:.1f} kg — {'✓ PASS' if ew_ok else '✗ FAIL'}")
    
    if all([vs_ok, vne_ok, ew_ok]):
        print("  Overall: ✓ COMPLIANT (at this loading)")
    else:
        print("  Overall: ✗ ONE OR MORE PARAMETERS EXCEED LIMITS")
    
    if not args.no_plot:
        plot_power_curves(results, 
                          title=f"Power Curves — {args.pilot_mass}kg pilot, "
                                f"ISA+{args.temp}°C, {args.altitude:.0f}m")


if __name__ == "__main__":
    main()
