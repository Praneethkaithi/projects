# quote_display.py
import tkinter as tk
import random

# List of quotes
quotes = [
    "quote 1 ",
    "quote 2",
    "quote n",
    
    # Add more quotes here
]

def get_random_quote():
    return random.choice(quotes)

def show_quote():
    quote = get_random_quote()
    root = tk.Tk()
    root.title("Daily Quote")
    label = tk.Label(root, text=quote, wraplength=400, font=("Helvetica", 14))
    label.pack(pady=20)
    root.mainloop()

if __name__ == "__main__":
    show_quote()
