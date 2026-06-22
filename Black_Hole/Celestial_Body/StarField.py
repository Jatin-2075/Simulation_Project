from ursina import *
import random

def create_starfield(num_stars=500):
    stars = []
    for i in range(num_stars):
        x = random.uniform(-300, 300)
        y = random.uniform(-300, 300)
        z = random.uniform(-300, 300)

        brightness = random.uniform(0.3, 1.0)

        star = Entity(
            model='sphere',
            color=color.rgb(
                int(brightness * 255),
                int(brightness * 255),
                int(brightness * 255)
            ),
            scale=random.uniform(0.1, 0.5),
            position=(x, y, z)
        )

        star.original_position = Vec3(x, y, z)
        stars.append(star)

    return stars


def apply_lensing(stars, black_hole, lensing_radius=80, strength=5):
    for star in stars:
        dx = black_hole.x - star.original_position.x
        dy = black_hole.y - star.original_position.y
        dz = black_hole.z - star.original_position.z

        dist = (dx**2 + dy**2 + dz**2) ** 0.5

        if dist < lensing_radius and dist > 0.1:
            bend_factor = (1 - dist / lensing_radius) ** 2 * strength

            nx, ny, nz = dx / dist, dy / dist, dz / dist

            star.x = star.original_position.x + nx * bend_factor
            star.y = star.original_position.y + ny * bend_factor
            star.z = star.original_position.z + nz * bend_factor
        else:
            star.position = star.original_position