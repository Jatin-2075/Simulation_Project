from ursina import *
import math
import random
from Core.Formulas import circular_orbit_velocity

class BlackHole(Entity):
    def __init__(self, mass, position=(0,0,0)):

        self.mass = mass
        self.visual_radius = max(8, math.log10(mass) * 2.5)

        super().__init__(
            model='sphere',
            color=color.black,
            scale=self.visual_radius * 2,
            position=position
        )

        self.disk_particles = []

        inner = self.visual_radius + 1
        outer = self.visual_radius + 17

        for i in range(3000):
            radius = random.uniform(inner, outer)
            angle = random.uniform(0, 2 * math.pi)

            x = math.cos(angle) * radius
            z = math.sin(angle) * radius
            y = random.uniform(-1.5, 1.5) * (1 - (radius - inner) / (outer - inner))

            if radius < inner + 4:
                r, g, b = 255, 255, int(200 * random.uniform(0.8, 1.0))
                scale = random.uniform(0.1, 0.25)
            elif radius < inner + 10:
                r, g, b = 255, int(120 * random.uniform(0.7, 1.0)), 0
                scale = random.uniform(0.15, 0.35)
            else:
                r, g, b = int(180 * random.uniform(0.5, 1.0)), 30, 0
                scale = random.uniform(0.2, 0.45)

            speed = circular_orbit_velocity(self.mass, radius)

            particle = Entity(
                parent=self,
                model='sphere',
                color=color.rgb(r, g, b),
                scale=scale,
                position=(x, y, z)
            )

            self.disk_particles.append({
                'entity': particle,
                'angle': angle,
                'radius': radius,
                'speed': speed,
                'y': y
            })

        photon_radius = self.visual_radius * 0.1
        for i in range(300):
            angle = random.uniform(0, 2 * math.pi)
            x = math.cos(angle) * photon_radius
            z = math.sin(angle) * photon_radius
            y = random.uniform(-0.1, 0.1)

            brightness = random.uniform(0.8, 1.0)

            Entity(
                parent=self,
                model='sphere',
                color=color.rgb(
                    int(255 * brightness),
                    int(220 * brightness),
                    int(100 * brightness)
                ),
                scale=random.uniform(0.05, 0.15),
                position=(x, y, z)
            )

    def update(self):
        dt = time.dt
        for p in self.disk_particles:
            p['angle'] += p['speed'] * dt
            x = math.cos(p['angle']) * p['radius']
            z = math.sin(p['angle']) * p['radius']
            p['entity'].position = (x, p['y'], z)