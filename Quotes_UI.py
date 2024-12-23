import tkinter as tk
import Quotes_Backend
import Styles_Util

def update_quote(label):
    # Fetch and display a new quote
    new_quote =  Quotes_Backend.fetch_random_quote()
    label.config(text=new_quote)

    # Schedule the next update after x ms
    label.after(50000, update_quote, label)

def show(parent):
    frame3 = tk.Frame(parent, bg="#4c4c4c", padx=10, pady=10)
    frame3.grid(row=0, column=2, sticky="nsew")
    # Create a label to display the quote
    quote_label = tk.Label(
        frame3,
        text="Loading a quote...",
        font=Styles_Util.main_font,
        bg="#4c4c4c",
        fg="white",
        wraplength=250,
        justify="center",
    )
    quote_label.place(relx=0.5, rely=0.5, anchor="center")

    # Start updating the quote
    update_quote(quote_label)