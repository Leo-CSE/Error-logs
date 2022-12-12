# Import the Tkinter library, the csv module, and the datetime module
import tkinter as tk
import csv
import datetime

# Set the font size, font color, and font style
font_size = 40
font_color = "white"
font_style = "bold"
font_name = "Helvetica"

# Set the space between buttons
button_spacing = 15

# Create the main window
root = tk.Tk()

# Set the window name
root.title("Machine Error Log - TG-NAI B-2")

# Set the size of the window to 600 pixels by 600 pixels
root.geometry("800x800")

# Set the path of the file where the user's input will be saved
file_path = "Machine_Errors_Log.csv"

# Set the background color of the window to black
root.config(bg="black")

# Create a function that will be called when the user clicks on one of the options
def on_click(value):
    # Get the current time and date
    now = datetime.datetime.now()
    # Open the file in append mode
    with open(file_path, "a", newline="") as f:
        # Create a CSV writer
        writer = csv.writer(f)
        # Write the selected option and the time and date to the file
        writer.writerow([value, now.strftime("%Y-%m-%d %H:%M:%S")])

# Create a label that explains what the user should do
label = tk.Label(root, text="Please select the reason for the machine error:")
label.pack()

# Create buttons for the different options
button1 = tk.Button(root, text="Missing screw", command=lambda: on_click("Missing screw"))
button2 = tk.Button(root, text="Screw Placement", command=lambda: on_click("Screw Placement"))
button3 = tk.Button(root, text="Missing clip", command=lambda: on_click("Missing clip"))
button4 = tk.Button(root, text="Robot won't home", command=lambda: on_click("Robot won't home"))

# Set the background color of the button/s and font color/size/style
button1.config(background="RoyalBlue3", foreground=font_color, font=(font_name, font_size, font_style))
button2.config(background="RoyalBlue3", foreground=font_color, font=(font_name, font_size, font_style))
button3.config(background="RoyalBlue3", foreground=font_color, font=(font_name, font_size, font_style))
button4.config(background="RoyalBlue3", foreground=font_color, font=(font_name, font_size, font_style))

# Set the width and height of the button/s to fill the available space
button1.pack(fill=tk.BOTH, expand=True, padx=button_spacing, pady=button_spacing)
button2.pack(fill=tk.BOTH, expand=True, padx=button_spacing, pady=button_spacing)
button3.pack(fill=tk.BOTH, expand=True, padx=button_spacing, pady=button_spacing)
button4.pack(fill=tk.BOTH, expand=True, padx=button_spacing, pady=button_spacing)


# Start the main loop
root.mainloop()
