from ursina import *
import math

from Core.Formulas import *

from Celestial_Body.SpaceTime import SpaceTimeFabric
from Celestial_Body.StarField import create_starfield, apply_lensing
from Celestial_Body.Black_Hole import BlackHole
from Celestial_Body.Planet import Planet

from Core.camera_setting import setup_camera, camera_update
from Core.Physics import *

app = Ursina(title="black hole", borderless=True)
window.color = color.black

#starfield
starfield = create_starfield()

#lighting
DirectionalLight(direction=(1,-1,-1), color=color.white)
AmbientLight(color=color.rgb(50,50,100,255))

#black_hole
black_hole = BlackHole(mass=1000, position=(0, 0, 0))
black_hole.rotation_x = 15

#planet
orbit_speed = circular_orbit_velocity(black_hole.mass, 40)
planet = Planet(mass=100, black_hole=black_hole, position=(40, 0, 0), velocity=Vec3(0, orbit_speed, 0))

#spacetime
spacetime = SpaceTimeFabric(black_hole)

#camera
setup_camera(black_hole)

absorbed = False

def update():
    global absorbed

    if not absorbed:
        apply_gravity(planet, black_hole, time.dt)
        if Black_hole_physics(planet, black_hole):
            absorbed = True

    apply_lensing(starfield, black_hole)
    camera_update(black_hole)
    spacetime.update()

def input(key):
    if key == 'g':
        spacetime.toggle()

app.run()