import tkinter as tk
from tkinter import ttk
import pandas as pd

# Load the dataset
file_path = "500713128_submissions-vs-hires-3790691742579723.xlsx"
data = pd.read_excel(file_path)

# Data Preprocessing
total_submissions = data['# Submissions'].sum()
client_submissions = data['# Client Submissions'].sum()
interviews = data['# Interviews'].sum()
hires = data['# Hires'].sum()

# Placeholder values for other KPIs
internal_rejections = 0
end_client_submissions = 0
offer_sent = 0
no_show = 0
joined_count = 0

# Create a dictionary for KPI data
kpis = {
    "Submissions": total_submissions,
    "Internal Rejections": internal_rejections,
    "Client Submissions": client_submissions,
    "End Client Submissions": end_client_submissions,
    "End Client Interviews": interviews,
    "Offer Sent": offer_sent,
    "No Show": no_show,
    "Joined Count": joined_count,
}

# Initialize Tkinter Window
root = tk.Tk()
root.title("Healthcare Staffing Dashboard")
root.geometry("800x400")
root.configure(bg="white")

# Create a title label
title_label = tk.Label(root, text="Dashboards KPIs", font=("Arial", 20, "bold"), bg="white")
title_label.pack(pady=10)

# Create a frame for the KPI tiles
kpi_frame = ttk.Frame(root)
kpi_frame.pack(pady=10)

# Tile Colors
tile_colors = ["#FFF2CC", "#DDEBF7", "#EAD1DC", "#D4E6D5", "#F8D7DA", "#FFF3CD", "#CCE5FF", "#E2D1F9"]

# Create KPI Tiles
for i, (kpi, value) in enumerate(kpis.items()):
    tile = tk.Frame(
        kpi_frame,
        bg=tile_colors[i % len(tile_colors)],
        width=150,
        height=100,
        relief="ridge",
        borderwidth=2,
    )
    tile.grid(row=0, column=i, padx=10, pady=10)
    tile.pack_propagate(False)

    kpi_label = tk.Label(tile, text=kpi, font=("Arial", 10, "bold"), bg=tile_colors[i % len(tile_colors)])
    kpi_label.pack(pady=5)

    value_label = tk.Label(tile, text=str(value), font=("Arial", 16, "bold"), fg="black", bg=tile_colors[i % len(tile_colors)])
    value_label.pack()

# Run the Tkinter event loop
root.mainloop()
