import tkinter as tk

import Styles_Util
from Weather_Backend import get_weather

def show(parent):
    current_temp, tomorrow_forecast, tomorrow_max, tomorrow_min = get_weather()

    # Left Frame: Weather Information
    frame1 = tk.Frame(parent, bg="#1e1e1e", padx=10, pady=10)
    frame1.grid(row=0, column=0, sticky="nsew")
    weather_label = tk.Label(
        frame1,
        text=f"Current Temperature in Stockholm:\n{current_temp}°C\n\n"
             f"Tomorrow's Forecast:\n{tomorrow_forecast}\n"
             f"Max Temp: {tomorrow_max}°C\nMin Temp: {tomorrow_min}°C",
        font=Styles_Util.main_font, bg="#1e1e1e", fg="white", justify="left"
    )
    weather_label.place(relx=0.5, rely=0.5, anchor="center")