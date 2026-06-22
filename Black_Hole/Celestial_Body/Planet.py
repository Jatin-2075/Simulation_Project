from ursina import *
from Core.Formulas import *
from Core.Physics import *


class Planet(Entity):
    def __init__(
        self,
        mass,
        black_hole,
        position=(50, 0, 0),
        velocity=Vec3(0, 0, 0)
    ):
        super().__init__(
            model='sphere',
            color=color.blue,
            
            scale=2,
            position=position
        )

        self.mass = mass
        self.velocity = velocity
        self.black_hole = black_hole
        self.absorbed = False

