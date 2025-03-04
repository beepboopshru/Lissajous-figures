import tkinter as tk
import math

# Define canvas dimensions and center coordinates
WIDTH = 600
HEIGHT = 400
center_x = WIDTH // 2
center_y = HEIGHT // 2

# Amplitudes for x and y (with padding)
A = WIDTH // 2 - 10  
B = HEIGHT // 2 - 10  

# Global variable to store the line object
line_item = None

def draw_curve():
    global line_item
    # Get current slider values for frequencies and phase shift
    freq_x = slider_x.get()
    freq_y = slider_y.get()
    phase = slider_phase.get()
    
    # Use fewer steps for efficiency (300 instead of 1000)
    steps = 300
    points = []
    for i in range(steps):
        t = 2 * math.pi * i / steps
        x = center_x + A * math.sin(freq_x * t + phase)
        y = center_y + B * math.sin(freq_y * t)
        points.extend([x, y])
    
    # If the line hasn't been created, create it; otherwise, update its coordinates.
    if line_item is None:
        # smooth=True gives a nicer curve; remove it if you need more performance.
        line_item = canvas.create_line(points, fill="cyan", smooth=True, width=2)
    else:
        canvas.coords(line_item, *points)
    
    # Schedule next update (50 ms refresh rate)
    root.after(50, draw_curve)

# Create the main window
root = tk.Tk()
root.title("Lissajous Figures Visualizer")

# Create a canvas mimicking an oscilloscope display
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()

# Create a frame for the sliders
frame = tk.Frame(root)
frame.pack(pady=10)

# Frequency X slider
label_x = tk.Label(frame, text="Frequency X:")
label_x.grid(row=0, column=0, padx=5)
slider_x = tk.Scale(frame, from_=1, to=10, orient=tk.HORIZONTAL)
slider_x.set(3)  # Default value
slider_x.grid(row=0, column=1, padx=5)

# Frequency Y slider
label_y = tk.Label(frame, text="Frequency Y:")
label_y.grid(row=1, column=0, padx=5)
slider_y = tk.Scale(frame, from_=1, to=10, orient=tk.HORIZONTAL)
slider_y.set(2)  # Default value
slider_y.grid(row=1, column=1, padx=5)

# Phase Shift slider
label_phase = tk.Label(frame, text="Phase Shift:")
label_phase.grid(row=2, column=0, padx=5)
slider_phase = tk.Scale(frame, from_=0, to=2 * math.pi, resolution=0.1, orient=tk.HORIZONTAL)
slider_phase.set(0)  # Default value
slider_phase.grid(row=2, column=1, padx=5)

# Start the drawing loop
draw_curve()

# Run the application
root.mainloop()
