import math

G = 10
c = 299792458


# Vector Math

def vector_magnitude(x: float, y: float, z: float) -> float:
    return math.sqrt(x**2 + y**2 + z**2)


def unit_vector(component: float, magnitude: float) -> float:
    if magnitude == 0:
        return 0
    return component / magnitude


def dot_product(x1: float, y1: float, z1: float,x2: float, y2: float, z2: float) -> float:
    return x1*x2 + y1*y2 + z1*z2


def vector_add(x1: float, y1: float, z1: float,x2: float, y2: float, z2: float):
    return (x1 + x2,y1 + y2,z1 + z2)


def vector_subtract(x1: float, y1: float, z1: float,x2: float, y2: float, z2: float):
    return (x1 - x2,y1 - y2,z1 - z2)


def scalar_multiply(x: float, y: float, z: float,scalar: float):
    return (x * scalar,y * scalar,z * scalar)


def normalize_vector(x: float,y: float,z: float):
    mag = vector_magnitude(x, y, z)

    if mag == 0:
        return 0, 0, 0

    return (x / mag,y / mag,z / mag )



# Basic Mechanics

def velocity(displacement: float, time: float) -> float:
    return displacement / time


def acceleration(delta_v: float, time: float) -> float:
    return delta_v / time


def second_law(mass: float, acceleration_value: float) -> float:
    return mass * acceleration_value


def momentum(mass: float, velocity_value: float) -> float:
    return mass * velocity_value


# Gravity

def gravity_force(m1: float, m2: float, distance: float) -> float:
    return (G * m1 * m2) / (distance**2)


def gravity_potential_energy(m1: float, m2: float, r: float) -> float:
    return -(G * m1 * m2) / r


def escape_velocity(M: float, r: float) -> float:
    return math.sqrt((2 * G * M) / r)


def circular_orbit_velocity(M: float, r: float) -> float:
    return math.sqrt((G * M) / r)


def centripetal_force(mass: float, velocity_value: float, radius: float) -> float:
    return (mass * velocity_value**2) / radius


def gravitational_acceleration(M: float, r: float) -> float:
    return (G * M) / (r**2)


def gravity_acceleration_vector(bh_x: float, bh_y: float, bh_z: float,p_x: float, p_y: float, p_z: float,M: float, softening: float = 1.0):
    dx, dy, dz = vector_subtract(bh_x, bh_y, bh_z, p_x, p_y, p_z)

    r = vector_magnitude(dx, dy, dz)
    r_safe = max(r, softening)

    accel_magnitude = gravitational_acceleration(M, r_safe)

    dir_x, dir_y, dir_z = normalize_vector(dx, dy, dz)

    return scalar_multiply(dir_x, dir_y, dir_z, accel_magnitude)


# Black Hole Physics

def schwarzschild_radius(M: float) -> float:
    return (2 * G * M) / (c**2)


def photon_sphere_radius(M: float) -> float:
    return (3 * G * M) / (c**2)


# Simulation Helpers

def distance(x1: float, y1: float, z1: float, x2: float, y2: float, z2: float) -> float:
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)


def update_velocity(vx: float, vy: float, vz: float,ax: float, ay: float, az: float,dt: float) -> tuple:
    return vx + ax * dt, vy + ay * dt, vz + az * dt


def update_position(x: float, y: float, z: float,vx: float, vy: float, vz: float,dt: float) -> tuple:
    return x + vx * dt, y + vy * dt, z + vz * dt
