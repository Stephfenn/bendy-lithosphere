import numpy as np

def run_Calculations(Te, load_height, load_width):
    # -----------------------------
    # Constants
    # -----------------------------
    E = 1.0e11          # Young's modulus (Pa)
    v = 0.25            # Poisson's ratio
    rho_m = 3300        # mantle density (kg/m^3)
    rho_c = 2800        # crust/load density (kg/m^3)
    g = 9.81            # gravity (m/s^2)

    # -----------------------------
    # Flexural Rigidity
    # -----------------------------
    D = (E * Te**3) / (12 * (1 - v**2))

    # -----------------------------
    # Distance Profile
    # -----------------------------
    x = np.linspace(-500e3, 500e3, 1000)
    x_km = x / 1000

    # -----------------------------
    # Surface Load / Topography
    # -----------------------------
    surface_load = load_height * np.exp(-((x / load_width)**2))

    # -----------------------------
    # Flexural Parameter
    # -----------------------------
    alpha = (4 * D / ((rho_m - rho_c) * g))**0.25

    # -----------------------------
    # Lithosphere Deflection
    # -----------------------------
    deflection = -load_height * np.exp(-(np.abs(x) / alpha)) * np.cos(x / alpha)

    return x_km, surface_load, deflection, D, alpha

def run_comparison_Calculations(Te_values, load_height, load_width):
    comparison_results = []

    for Te in Te_values:
        x_km, surface_load, deflection, D, alpha = run_Calculations(Te,load_height,load_width)
        comparison_results.append({"Te": Te, "x_km": x_km, "surface_load": surface_load, "deflection": deflection, "D": D, "alpha": alpha})
    return comparison_results