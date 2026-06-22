from ursina import *
import math

class SpaceTimeFabric:
    def __init__(self, black_hole, grid_size=40, spacing=5):
        self.black_hole = black_hole
        self.grid_size = grid_size
        self.spacing = spacing
        self.visible = True
        self.points = []

        half = (grid_size // 2) * spacing
        for i in range(grid_size):
            row = []
            for j in range(grid_size):
                x = -half + i * spacing
                z = -half + j * spacing
                y = -60

                point = Entity(
                    model='sphere',
                    color=color.rgba(100, 100, 255, 150),
                    scale=0.3,
                    position=(x, y, z)
                )
                row.append(point)
            self.points.append(row)

        self.lines = []
        for i in range(grid_size):
            for j in range(grid_size):
                if j < grid_size - 1:
                    line = Entity(
                        model='cube',
                        color=color.rgba(100, 100, 255, 100),
                        scale=(0.1, 0.1, spacing),
                        position=self.points[i][j].position
                    )
                    self.lines.append({'entity': line, 'i': i, 'j': j, 'axis': 'z'})
                if i < grid_size - 1:
                    line = Entity(
                        model='cube',
                        color=color.rgba(100, 100, 255, 100),
                        scale=(spacing, 0.1, 0.1),
                        position=self.points[i][j].position
                    )
                    self.lines.append({'entity': line, 'i': i, 'j': j, 'axis': 'x'})

    def update(self):
        if not self.visible:
            return

        bh = self.black_hole
        half = (self.grid_size // 2) * self.spacing

        for i in range(self.grid_size):
            for j in range(self.grid_size):
                x = -half + i * self.spacing
                z = -half + j * self.spacing

                dx = x - bh.x
                dz = z - bh.z
                dist = math.sqrt(dx**2 + dz**2)

                warp = -20 / (dist / 10 + 1)

                self.points[i][j].position = Vec3(x, -30 + warp, z)

    def toggle(self):
        self.visible = not self.visible
        for row in self.points:
            for point in row:
                point.enabled = self.visible
        for line in self.lines:
            line['entity'].enabled = self.visible