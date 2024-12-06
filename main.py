import pygame
import numpy as np
import math

pygame.init()

WIDTH, HEIGHT = 1920, 1080
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rotating Cube with Full RGB Gradient")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def generate_cube():
    vertices = np.array([
        [-1, -1, -1],
        [ 1, -1, -1],
        [ 1,  1, -1],
        [-1,  1, -1],
        [-1, -1,  1],
        [ 1, -1,  1],
        [ 1,  1,  1],
        [-1,  1,  1]
    ])
    return vertices

def rotate_cube(vertices, angle_x, angle_y):
    rotation_matrix_x = np.array([
        [1, 0, 0],
        [0, np.cos(angle_x), -np.sin(angle_x)],
        [0, np.sin(angle_x), np.cos(angle_x)]
    ])
    
    rotation_matrix_y = np.array([
        [np.cos(angle_y), 0, np.sin(angle_y)],
        [0, 1, 0],
        [-np.sin(angle_y), 0, np.cos(angle_y)]
    ])
    
    rotated_vertices = np.dot(vertices, rotation_matrix_x.T)
    rotated_vertices = np.dot(rotated_vertices, rotation_matrix_y.T)
    
    return rotated_vertices

def project_3d_to_2d(vertices):
    return vertices[:, :2]

def get_full_rgb_gradient_color(time, max_time):
    progress = (time / max_time) % 1
    
    if 0 <= progress < 1/3:
        red = int(255 * (1 - 3 * progress))
        green = int(255 * (3 * progress))
        blue = 0
    elif 1/3 <= progress < 2/3:
        progress -= 1/3
        red = 0
        green = int(255 * (1 - 3 * progress))
        blue = int(255 * (3 * progress))
    else:
        progress -= 2/3
        red = int(255 * (3 * progress))
        green = 0
        blue = int(255 * (1 - 3 * progress))
    
    return (red, green, blue)

def get_opposite_gradient_color(cube_color):
    return (255 - cube_color[0], 255 - cube_color[1], 255 - cube_color[2])

def draw_cube(vertices, edges, cube_color, background_color):
    screen.fill(background_color)
    
    for edge in edges:
        start, end = vertices[edge[0]], vertices[edge[1]]
        start_pos = (int(start[0] * 100 + WIDTH // 2), int(start[1] * 100 + HEIGHT // 2))
        end_pos = (int(end[0] * 100 + WIDTH // 2), int(end[1] * 100 + HEIGHT // 2))
        pygame.draw.line(screen, cube_color, start_pos, end_pos, 3)
    
    pygame.display.flip()

edges = [
    [0, 1], [1, 2], [2, 3], [3, 0],
    [4, 5], [5, 6], [6, 7], [7, 4],
    [0, 4], [1, 5], [2, 6], [3, 7]
]

def main():
    clock = pygame.time.Clock()
    angle_x, angle_y = 0, 0
    running = True
    time = 0
    max_time = 600

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        vertices = generate_cube()
        rotated_vertices = rotate_cube(vertices, angle_x, angle_y)
        projected_vertices = project_3d_to_2d(rotated_vertices)

        cube_color = get_full_rgb_gradient_color(time, max_time)
        background_color = get_opposite_gradient_color(cube_color)

        draw_cube(projected_vertices, edges, cube_color, background_color)

        angle_x += 0.02
        angle_y += 0.02
        time += 1
        if time > max_time:
            time = 0

        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
