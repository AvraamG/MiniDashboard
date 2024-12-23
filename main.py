import tkinter as tk
import Quotes_UI
import Styles_Util
import Traffic_UI
import Weather_UI

# Main Application
def main():

    # Create Tkinter root window
    root = tk.Tk()
    root.title("Personal Dashboard")
    root.geometry("900x200")
    root.configure(bg=Styles_Util.dark_background)

    # Configure grid layout
    root.columnconfigure(0, weight=1)  # Left Frame
    root.columnconfigure(1, weight=1)  # Middle Frame
    root.columnconfigure(2, weight=1)  # Right Frame
    root.rowconfigure(0, weight=1)  # Single row

    #Call the views to show their stuff
    Weather_UI.show(root)
    Traffic_UI.show(root)
    Quotes_UI.show(root)

    root.mainloop()

if __name__ == "__main__":
    main()
