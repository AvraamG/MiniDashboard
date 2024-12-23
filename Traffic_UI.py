import tkinter as tk
import Styles_Util
from Traffic_Backend import get_traffic_info


def show(parent):
    duration, duration_in_traffic = get_traffic_info()
    frame2 = tk.Frame(parent, bg="#333333", padx=10, pady=10)
    frame2.grid(row=0, column=1, sticky="nsew")
    traffic_label = tk.Label(
        frame2,
        text=f"Traffic Information:\nDuration: {duration}\nDuration in Traffic: {duration_in_traffic}",
        font=Styles_Util.main_font, bg="#333333", fg="white", justify="center"
    )
    traffic_label.place(relx=0.5, rely=0.5, anchor="center")

