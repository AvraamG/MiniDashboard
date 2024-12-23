import tkinter as tk

import QuotesAPI
from Google import get_traffic_info
from Weather import get_weather

main_font:tuple[str,int] = ("Montserrat", 12)
dark_background:str = "#202020"
def update_quote(label):
    # Fetch and display a new quote
    new_quote =  QuotesAPI.fetch_random_quote()
    label.config(text=new_quote)

    # Schedule the next update after x ms
    label.after(50000, update_quote, label)
# Main Application
def main():
    # Fetch data
    current_temp, tomorrow_forecast, tomorrow_max, tomorrow_min = get_weather()
    duration, duration_in_traffic = get_traffic_info()

    # Create Tkinter window
    root = tk.Tk()
    root.title("Personal Dashboard")
    root.geometry("900x200")
    root.configure(bg=dark_background)  # Dark background

    # Configure grid layout
    root.columnconfigure(0, weight=1)  # Left Frame
    root.columnconfigure(1, weight=1)  # Middle Frame
    root.columnconfigure(2, weight=1)  # Right Frame
    root.rowconfigure(0, weight=1)  # Single row

    # Left Frame: Weather Information
    frame1 = tk.Frame(root, bg="#1e1e1e", padx=10, pady=10)
    frame1.grid(row=0, column=0, sticky="nsew")
    weather_label = tk.Label(
        frame1,
        text=f"Current Temperature in Stockholm:\n{current_temp}°C\n\n"
             f"Tomorrow's Forecast:\n{tomorrow_forecast}\n"
             f"Max Temp: {tomorrow_max}°C\nMin Temp: {tomorrow_min}°C",
        font=main_font, bg="#1e1e1e", fg="white", justify="left"
    )
    weather_label.place(relx=0.5, rely=0.5, anchor="center")

    # Middle Frame: Traffic Information
    frame2 = tk.Frame(root, bg="#333333", padx=10, pady=10)
    frame2.grid(row=0, column=1, sticky="nsew")
    traffic_label = tk.Label(
        frame2,
        text=f"Traffic Information:\nDuration: {duration}\nDuration in Traffic: {duration_in_traffic}",
        font=main_font, bg="#333333", fg="white", justify="center"
    )
    traffic_label.place(relx=0.5, rely=0.5, anchor="center")

    # Right Frame: Quotes
    frame3 = tk.Frame(root, bg="#4c4c4c", padx=10, pady=10)
    frame3.grid(row=0, column=2, sticky="nsew")

    # Create a label to display the quote
    quote_label = tk.Label(
        frame3,
        text="Loading a quote...",
        font=main_font,
        bg="#4c4c4c",
        fg="white",
        wraplength=250,
        justify="center",
    )
    quote_label.place(relx=0.5, rely=0.5, anchor="center")

    # Start updating the quote
    update_quote(quote_label)

    root.mainloop()


if __name__ == "__main__":
    main()
