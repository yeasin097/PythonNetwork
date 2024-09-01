import tkinter as tk

# Function to add two numbers
def add_numbers():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 + num2
        result_label.config(text=f"Result: {result}")
    except ValueError:
        result_label.config(text="Please enter valid numbers!")

# Create the main window
window = tk.Tk()
window.title("Addition Calculator")

# Create input fields for the numbers
entry1 = tk.Entry(window, width=10)
entry2 = tk.Entry(window, width=10)

# Create a button to perform the addition
add_button = tk.Button(window, text="Add", command=add_numbers)

# Create a label to display the result
result_label = tk.Label(window, text="Result: ")

# Place the widgets in the window
entry1.pack(pady=5)
entry2.pack(pady=5)
add_button.pack(pady=10)
result_label.pack(pady=10)

# Start the Tkinter event loop
window.mainloop()
