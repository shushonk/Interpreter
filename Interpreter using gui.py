import tkinter as tk
from tkinter import scrolledtext
import sys
from io import StringIO

# Function to execute Python code
def execute_code():
    # Get the Python code from the text widget
    code = code_input.get("1.0", tk.END)

    # Redirect standard output to capture print statements
    old_stdout = sys.stdout
    result = StringIO()
    sys.stdout = result

    try:
        # Execute the code entered in the input box
        exec(code)
    except Exception as e:
        result.write(f"Error: {e}")

    # Update the output display with the result
    sys.stdout = old_stdout
    output_display.config(state=tk.NORMAL)  # Enable editing to update text
    output_display.delete(1.0, tk.END)  # Clear previous output
    output_display.insert(tk.END, result.getvalue())  # Insert new output
    output_display.config(state=tk.DISABLED)  # Disable editing after updating output

# Create main window
root = tk.Tk()
root.title("Python Code Executor")

# Create a text widget for inputting Python code
code_input = scrolledtext.ScrolledText(root, width=60, height=15)
code_input.pack(padx=10, pady=10)

# Create a button to execute the code
execute_button = tk.Button(root, text="Execute Code", command=execute_code)
execute_button.pack(pady=5)

# Create a text widget to display output
output_display = scrolledtext.ScrolledText(root, width=60, height=10, state=tk.DISABLED)
output_display.pack(padx=10, pady=10)

# Start the GUI loop
root.mainloop()
