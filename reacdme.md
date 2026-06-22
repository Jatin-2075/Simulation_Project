# 🕳️ Black Hole Simulation

An interactive 3D black hole simulation built from scratch in Python using Ursina Engine. Features real Newtonian gravity, Keplerian accretion disk, gravitational lensing, photon ring, and a spacetime fabric visualization.

![Python](https://img.shields.io/badge/Python-3.13-blue) ![Ursina](https://img.shields.io/badge/Ursina-8.3.0-purple) ![Physics](https://img.shields.io/badge/Physics-Newtonian-orange)

---

## Features

- ⚫ **Black Hole** — Visual scale derived from mass, pure black event horizon
- 🌀 **Keplerian Accretion Disk** — 3000 particles with real orbital speeds (inner disk faster than outer)
- 💫 **Photon Ring** — Bright glowing ring sitting just outside the event horizon
- 🌌 **Gravitational Lensing** — Background stars bend toward the black hole based on proximity
- 🕸️ **Spacetime Fabric** — Warping grid visualization (toggle with `G`)
- 🪐 **Planetary Orbit** — Planet orbits the black hole using calculated circular orbit velocity
- 💥 **Absorption** — Objects get destroyed when they cross the Schwarzschild radius

---

## Project Structure

```
Black_Hole/
├── Main.py                        # Entry point
├── Celestial_Body/
│   ├── Black_Hole.py              # BlackHole entity + accretion disk + photon ring
│   ├── Planet.py                  # Planet entity with gravity update
│   ├── StarField.py               # Starfield generation + lensing
│   └── SpaceTime.py               # Spacetime fabric grid
├── Core/
│   ├── Formulas.py                # Pure physics/math functions
│   ├── Physics.py                 # Gravity simulation logic
│   └── camera_setting.py          # Camera controls
└── README.md
```

---

## Physics

All physics is implemented from scratch in `Core/Formulas.py`:

| Formula | Description |
|---|---|
| `F = GMm/r²` | Newtonian gravitational force |
| `v = √(GM/r)` | Circular orbit velocity |
| `v_e = √(2GM/r)` | Escape velocity |
| `r_s = 2GM/c²` | Schwarzschild radius |
| `r_ph = 3GM/c²` | Photon sphere radius |

Gravity is applied using Euler integration every frame via `apply_gravity()` in `Core/Physics.py`.

---

## Controls

| Key | Action |
|---|---|
| `A / D` | Orbit camera left / right |
| `W / S` | Orbit camera up / down |
| `Q` | Zoom in |
| `E` | Zoom out |
| `G` | Toggle spacetime fabric |

---

## Installation

```bash
# Clone the repo
git clone https://github.com/Jatin-2075/black-hole-sim

# Install dependencies
pip install ursina

# Run
python Main.py
```

---

## Configuration

You can tweak these values in `Main.py` to change the simulation behavior:

```python
# Black hole mass — affects gravity strength and visual size
black_hole = BlackHole(mass=1000, position=(0, 0, 0))

# Planet starting position and orbital velocity (auto-calculated)
orbit_speed = circular_orbit_velocity(black_hole.mass, 40)
planet = Planet(mass=100, black_hole=black_hole, position=(40, 0, 0), velocity=Vec3(0, orbit_speed, 0))
```

And in `Core/Formulas.py`:
```python
G = 10  # Gravitational constant (scaled for game units)
```

---

## Built With

- [Python 3.13](https://python.org)
- [Ursina Engine 8.3.0](https://www.ursinaengine.org/)
- Newtonian gravity + Keplerian orbital mechanics
- Custom vector math (no external physics library)

---

## What I Learned

- Implementing Newtonian gravity and stable orbital mechanics from scratch
- Why real SI units break game simulations (and how to scale G correctly)
- Keplerian disk dynamics — why inner orbits are faster than outer ones
- Fake gravitational lensing using star position offsets
- Structuring a physics simulation with clean separation (Formulas → Physics → Entities)

---

## Roadmap

- [ ] Shader-based gravitational lensing (GLSL)
- [ ] Ray-traced accretion disk
- [ ] Multiple black holes with mutual gravity
- [ ] RK4 integration for more stable long-term orbits
- [ ] Time dilation visualization near the event horizon

---

*Built in 2 weeks as a personal learning project. No tutorials — just physics, math, and a lot of debugging.*