from ursina import Vec3, destroy
from Core.Formulas import *


def apply_gravity(planet, black_hole, dt):
    ax, ay, az = gravity_acceleration_vector(
        black_hole.x, black_hole.y, black_hole.z,
        planet.x, planet.y, planet.z,
        black_hole.mass
    )
    
    vx, vy, vz = update_velocity(
        planet.velocity.x, planet.velocity.y, planet.velocity.z,
        ax, ay, az,
        dt
    )

    planet.velocity = Vec3(vx, vy, vz)

    x, y, z = update_position(
        planet.x, planet.y, planet.z,
        planet.velocity.x, planet.velocity.y, planet.velocity.z,
        dt
    )

    planet.position = Vec3(x, y, z)



def Black_hole_physics(planet, black_hole):
    absorb_radius = black_hole.visual_radius
    dista = distance(planet.x, planet.y, planet.z, black_hole.x, black_hole.y, black_hole.z)


    if dista < absorb_radius:
        planet.velocity = Vec3(0,0,0)
        destroy(planet)
        return True