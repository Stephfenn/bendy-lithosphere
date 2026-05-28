from datetime import datetime as time
from src.Calculations import run_Calculations as Calculations, run_comparison_Calculations as ComparisonCalculations
from src.Database import create_database as Database_Creation, save_model_run as Database_Saving
from src.Plot import plot_flexure_model as Plot, plot_comparison_model as PlotComparison

# -----------------------------
# Inputs
# -----------------------------
print("--------------------------")
print("Stimulator For Flexure & Isostasy")
print("--------------------------")
Te = float(input("Enter elastic thickness Te in meters, example 30000: "))
print("--------------------------")
load_height = float(input("Enter load height in meters, example 3000: "))
print("--------------------------")
load_width = float(input("Enter load width in meters, example 80000: "))
print("--------------------------")
print("Assign Te Values for Comparison Results")
print("--------------------------")
TeComparisonOne = float(input("Enter elastic thickness Te in meters, example 10000: "))
print("--------------------------")
TeComparisonTwo = float(input("Enter elastic thickness Te in meters, example 30000: ")) 
print("--------------------------")
TeComparisonThree = float(input("Enter elastic thickness Te in meters, example 60000: ")) 
print("Processing Plots")

# -----------------------------
# Assigning Time To Saved Files
# -----------------------------

run_time = time.now().strftime("%Y-%m-%d_%H-%M-%S")
database_filename = f"data/model_runs_{run_time}.db"
plot_filename = f"outputs/flexure_model_{run_time}.png"

# -----------------------------
# Doing Calculations
# -----------------------------
x_km, surface_load, deflection, D, alpha = Calculations(Te, load_height, load_width)
Original_Te_km = Te / 1000

# -----------------------------
#  Data Creation and Saving
# -----------------------------
Database_Creation(database_filename)
Database_Saving(database_filename, run_time, Te, load_height, load_width, deflection, D)

# -----------------------------
#  Plotting Data
# -----------------------------
Plot(plot_filename, x_km, surface_load, deflection, Original_Te_km)

# -----------------------------
# Plotting Comparison Data
# -----------------------------


Te_values = [TeComparisonOne, TeComparisonTwo, TeComparisonThree]
comparison_results = ComparisonCalculations(Te_values,load_height,load_width)

comparison_plot_filename = f"outputs/flexure_comparison_{run_time}.png"
PlotComparison(comparison_results, comparison_plot_filename)

