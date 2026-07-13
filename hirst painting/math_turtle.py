"""
╔══════════════════════════════════════════════════════════╗
║   🐢 MATHEMATICAL TURTLE — Rose Curve & Spirograph       ║
║   Draws r = cos(k·θ) rose curves + animated spirograph   ║
╚══════════════════════════════════════════════════════════╝

Run with:  python math_turtle.py
Press SPACE to switch between equations!
"""

import turtle
import math
import colorsys
import time

# ── Setup ──────────────────────────────────────────────────
screen = turtle.Screen()
screen.setup(width=900, height=900)
screen.bgcolor("#0a0a0f")
screen.title("🐢 Mathematical Turtle — Press SPACE to switch curves")
screen.tracer(0)  # Manual updates for speed

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.pensize(1.5)

label = turtle.Turtle()
label.hideturtle()
label.penup()

hue_offset = [0]
current_eq = [0]
running = [True]

# ── Equations ──────────────────────────────────────────────
EQUATIONS = [
    {
        "name": "Rose Curve  r = cos(3θ)",
        "fn": lambda theta: math.cos(3 * theta),
        "scale": 300,
        "steps": 1000,
        "theta_max": 2 * math.pi,
        "style": "polar",
    },
    {
        "name": "Rose Curve  r = cos(5θ)",
        "fn": lambda theta: math.cos(5 * theta),
        "scale": 300,
        "steps": 2000,
        "theta_max": 2 * math.pi,
        "style": "polar",
    },
    {
        "name": "Lissajous  x=sin(3t), y=sin(2t)",
        "fn": lambda t: (math.sin(3 * t), math.sin(2 * t)),
        "scale": 300,
        "steps": 1500,
        "theta_max": 2 * math.pi,
        "style": "parametric",
    },
    {
        "name": "Butterfly Curve  r = e^(sin θ) − 2cos(4θ)",
        "fn": lambda theta: math.exp(math.sin(theta)) - 2 * math.cos(4 * theta),
        "scale": 120,
        "steps": 3000,
        "theta_max": 12 * math.pi,
        "style": "polar",
    },
    {
        "name": "Spirograph  (hypotrochoid)",
        "fn": lambda t_val: (
            (7 - 2) * math.cos(t_val) + 2 * math.cos((7 - 2) / 2 * t_val),
            (7 - 2) * math.sin(t_val) - 2 * math.sin((7 - 2) / 2 * t_val),
        ),
        "scale": 60,
        "steps": 3000,
        "theta_max": 4 * math.pi,
        "style": "parametric",
    },
    {
        "name": "Maclaurin's Trisectrix  r = cos(θ/3)",
        "fn": lambda theta: math.cos(theta / 3),
        "scale": 280,
        "steps": 2000,
        "theta_max": 6 * math.pi,
        "style": "polar",
    },
]

# ── Draw helpers ────────────────────────────────────────────
def hsv_color(h, s=1.0, v=1.0):
    r, g, b = colorsys.hsv_to_rgb(h % 1.0, s, v)
    return (r, g, b)


def draw_grid():
    """Faint grid lines for mathematical feel."""
    t.pencolor(0.08, 0.08, 0.15)
    t.pensize(0.5)
    for x in range(-400, 401, 50):
        t.penup(); t.goto(x, -450); t.pendown(); t.goto(x, 450)
    for y in range(-400, 401, 50):
        t.penup(); t.goto(-450, y); t.pendown(); t.goto(450, y)
    # Axes
    t.pencolor(0.15, 0.15, 0.3)
    t.pensize(1)
    t.penup(); t.goto(-450, 0); t.pendown(); t.goto(450, 0)
    t.penup(); t.goto(0, -450); t.pendown(); t.goto(0, 450)


def draw_label(eq):
    label.clear()
    label.pencolor("#ffffff")
    label.goto(-430, 380)
    label.write(eq["name"], font=("Courier", 14, "bold"))
    label.goto(-430, -420)
    label.pencolor("#555577")
    label.write("SPACE → next curve   |   Q → quit", font=("Courier", 10, "normal"))


def draw_equation(eq, hue_start=0):
    steps = eq["steps"]
    scale = eq["scale"]
    theta_max = eq["theta_max"]
    style = eq["style"]

    t.penup()
    first = True

    for i in range(steps + 1):
        theta = theta_max * i / steps
        h = (hue_start + i / steps * 0.75) % 1.0

        if style == "polar":
            r = eq["fn"](theta)
            x = r * math.cos(theta) * scale
            y = r * math.sin(theta) * scale
        else:  # parametric
            result = eq["fn"](theta)
            x = result[0] * scale
            y = result[1] * scale

        t.pencolor(hsv_color(h, 0.9, 1.0))

        if first:
            t.goto(x, y)
            t.pendown()
            first = False
        else:
            t.goto(x, y)

        # Refresh every 30 steps for smooth animation
        if i % 30 == 0:
            screen.update()


def render(eq_index):
    t.clear()
    label.clear()
    eq = EQUATIONS[eq_index % len(EQUATIONS)]
    draw_grid()
    draw_label(eq)
    screen.update()
    draw_equation(eq, hue_offset[0])
    hue_offset[0] = (hue_offset[0] + 0.15) % 1.0
    screen.update()


# ── Key bindings ────────────────────────────────────────────
def next_eq():
    current_eq[0] = (current_eq[0] + 1) % len(EQUATIONS)
    render(current_eq[0])

def quit_app():
    running[0] = False
    screen.bye()

screen.listen()
screen.onkey(next_eq, "space")
screen.onkey(quit_app, "q")
screen.onkey(quit_app, "Q")

# ── Main loop ───────────────────────────────────────────────
print("\n🐢  Mathematical Turtle is running!")
print("   SPACE  →  next equation")
print("   Q      →  quit\n")

render(0)

# Cycle through all equations automatically then hand off to user
turtle.mainloop()