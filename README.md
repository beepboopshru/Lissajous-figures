# Lissajous Figures Visualizer

A desktop application built in Python using Tkinter that visualizes Lissajous figures in real time. Adjust the x/y frequencies and phase shift with intuitive sliders, and watch the dynamic, oscilloscope-like display update instantly.

## Features

- **Real-Time Visualization:** See the Lissajous figures update live as you change parameters.
- **Adjustable Parameters:** Modify the frequency along the x-axis, y-axis, and the phase shift.
- **Optimized Rendering:** Efficient drawing using a persistent line object and a reduced number of points.
- **User-Friendly Interface:** A simple UI that mimics a physical oscilloscope display.

## Getting Started

### Prerequisites

- Python 3.x (Tkinter is included with most Python installations)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/lissajous-visualizer.git
   cd lissajous-visualizer
   ```

2. **Run the application:**

   ```bash
   python lissajous_app.py
   ```

## How It Works

The app uses a Tkinter canvas to render the Lissajous figure. It:
- Calculates the coordinates using sine functions with adjustable parameters.
- Updates the figure by modifying an existing line object to reduce overhead.
- Uses the `after()` method for a smooth refresh loop.
