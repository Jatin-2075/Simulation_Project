from ursina import *
import math

def setup_camera(target):
    camera.position = (0, 10, -60)
    camera.look_at(target)

def camera_update(target):
    orbit_speed = 80
    zoom_speed = 50

    if held_keys['a']:
        camera.position = rotate_around_y(camera.position, -orbit_speed * time.dt)
    if held_keys['d']:
        camera.position = rotate_around_y(camera.position, orbit_speed * time.dt)
    if held_keys['w']:
        camera.position = rotate_around_x(camera.position, -orbit_speed * time.dt)
    if held_keys['s']:
        camera.position = rotate_around_x(camera.position, orbit_speed * time.dt)

    if held_keys['q']:
        camera.position += camera.forward * zoom_speed * time.dt
    if held_keys['e']:
        camera.position -= camera.forward * zoom_speed * time.dt

    camera.look_at(target)


def rotate_around_y(pos, degrees):
    angle = math.radians(degrees)
    x = pos.x * math.cos(angle) - pos.z * math.sin(angle)
    z = pos.x * math.sin(angle) + pos.z * math.cos(angle)
    return Vec3(x, pos.y, z)


def rotate_around_x(pos, degrees):
    angle = math.radians(degrees)
    y = pos.y * math.cos(angle) - pos.z * math.sin(angle)
    z = pos.y * math.sin(angle) + pos.z * math.cos(angle)
    return Vec3(pos.x, y, z)