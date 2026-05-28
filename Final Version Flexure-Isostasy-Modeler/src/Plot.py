import matplotlib.pyplot as plt
import os


def plot_flexure_model(plot_filename, x_km, surface_load, deflection, Original_Te_km):
    os.makedirs("outputs", exist_ok=True)
    plt.figure(figsize=(10, 5), facecolor="white", dpi=100)

    plt.plot(x_km, surface_load, label="Surface Load / Topography")
    plt.plot(x_km, deflection, label=f"Lithosphere Deflection, Te = {Original_Te_km:.0f} km")

    plt.axhline(0, color="black", linewidth=2, linestyle="--", alpha=0.9)
    plt.axvline(0, color="gray", linewidth=1, linestyle=":", alpha=0.8)

    plt.xlabel("Distance (km)")
    plt.ylabel("Elevation / Deflection (m)")
    plt.title("1D Lithospheric Flexure Model")

    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    plt.savefig(plot_filename, dpi=150)
    


def plot_comparison_model(comparison_results, plot_filename):
    os.makedirs("outputs", exist_ok=True)

    plt.figure(figsize=(10, 5), facecolor="white", dpi=100)

    for result in comparison_results:
        Te_km = result["Te"] / 1000

        plt.plot(result["x_km"], result["deflection"],label=f"Te = {Te_km:.0f} km")

    plt.axhline(0, color="black", linewidth=2, linestyle="--", alpha=0.9)
    plt.axvline(0, color="gray", linewidth=1, linestyle=":", alpha=0.8)

    plt.xlabel("Distance (km)")
    plt.ylabel("Lithosphere Deflection (m)")
    plt.title("Lithosphere Deflection Comparison by Elastic Thickness")

    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()