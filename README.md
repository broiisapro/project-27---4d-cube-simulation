---

# Rotating Cube with Full RGB Gradient

This project creates a 3D rotating cube using Pygame and NumPy, where the cube is drawn with a full RGB gradient. The cube continuously rotates in 3D space while the color smoothly transitions through the entire RGB spectrum.

## Features

- A rotating 3D cube.
- RGB gradient color effects on the cube.
- Opposite gradient background for a dynamic visual experience.
- Adjustable rotation speed and gradient cycle duration.

## Code Overview

- **Cube Generation**: The cube is created with 8 vertices, and the edges between these vertices are defined.
- **Rotation**: The cube rotates around the X and Y axes using simple 3D rotation matrices.
- **Projection**: The 3D coordinates of the cube are projected onto a 2D plane for display.
- **Color Gradient**: The cube's color cycles through the entire RGB spectrum. The background color is the inverse of the cube’s color for contrast.
- **Main Loop**: The main loop handles the continuous rendering of the cube, its rotation, and the RGB color transitions.

## Customization

- You can adjust the size of the cube by modifying the scaling factor in the `draw_cube` function (currently `100`).
- Change the `angle_x` and `angle_y` increments to control how fast the cube rotates.
- The gradient cycle speed can be changed by modifying the `max_time` variable.

---
