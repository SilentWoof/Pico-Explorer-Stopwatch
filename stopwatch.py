from pimoroni import Button
from picographics import PicoGraphics, DISPLAY_PICO_EXPLORER, PEN_P4
import time

# Setup display
display = PicoGraphics(display=DISPLAY_PICO_EXPLORER, pen_type=PEN_P4)
display.set_backlight(1.0)

# Setup buttons
button_x = Button(14)  # Start/Stop
button_y = Button(15)  # Lap
button_b = Button(13)  # Reset
button_a = Button(12)  # Reset

# Stopwatch state
running = False
start_time = 0
lap_start_time = 0
elapsed = 0
lap_elapsed = 0
laps = []

# Colors
WHITE = display.create_pen(255, 255, 255)
BLACK = display.create_pen(0, 0, 0)
GREY = display.create_pen(180, 180, 180)
MID_GREEN = display.create_pen(0, 200, 0)
MID_RED = display.create_pen(200, 0, 0)
DARK_GREEN = display.create_pen(0, 60, 0)
DARK_RED = display.create_pen(60, 0, 0)

def format_time(ms):
    seconds = ms // 1000
    minutes = seconds // 60
    hours = minutes // 60
    tenths = (ms % 1000) // 100
    return "{:02}:{:02}:{:02}.{}".format(hours % 100, minutes % 60, seconds % 60, tenths)

def draw():
    # Set background color based on state
    if running:
        display.set_pen(DARK_GREEN)
    elif not running and elapsed > 0:
        display.set_pen(DARK_RED)
    else:
        display.set_pen(BLACK)
    display.clear()
    display.set_font("bitmap8")

    # Idle screen with button labels
    if not running and elapsed == 0 and len(laps) == 0:
        display.set_pen(MID_RED)
        display.text("STOP", 30, 110, 240, 4)
        display.set_pen(MID_GREEN)
        display.text("WATCH", 115, 110, 240, 4)

        display.set_pen(GREY)
        display.text("Start/Stop", 140, 60, 240, 2)  # Button X
        display.text("Lap", 200, 180, 240, 2)        # Button Y
        display.text("Reset", 10, 60, 240, 2)        # Button A
        display.text("Reset", 10, 180, 240, 2)       # Button B
    else:
        # Main timer
        display.set_pen(WHITE)
        display.text("STOPWATCH", 75, 10, 240, 2)

        if running:
            display.text(format_time(lap_elapsed), 15, 40, 240, 5)
            if len(laps) > 0:
                display.set_pen(WHITE)
                display.text("TOTAL: " + format_time(elapsed), 10, 90, 240, 2)
        else:
            display.text(format_time(elapsed), 10, 40, 240, 5)

        # Lap times
        y = 120
        lap_count = len(laps)
        start_index = max(0, lap_count - 4)
        display.set_pen(GREY)
        for i in range(start_index, lap_count):
            lap_time = laps[i]
            display.text("L{}: {}".format(i + 1, format_time(lap_time)), 10, y, 240, 3)
            y += 40

    display.update()

# Main loop
while True:
    if button_x.read():
        if not running:
            start_time = time.ticks_ms() - elapsed
            lap_start_time = time.ticks_ms()
            running = True
        else:
            elapsed = time.ticks_ms() - start_time
            lap_time = time.ticks_ms() - lap_start_time
            laps.append(lap_time)
            running = False
        time.sleep(0.2)

    if button_y.read() and running:
        lap_time = time.ticks_ms() - lap_start_time
        laps.append(lap_time)
        lap_start_time = time.ticks_ms()
        time.sleep(0.2)

    if button_b.read() or button_a.read():
        running = False
        elapsed = 0
        lap_elapsed = 0
        laps = []
        time.sleep(0.2)

    if running:
        lap_elapsed = time.ticks_ms() - lap_start_time
        elapsed = time.ticks_ms() - start_time

    draw()
    time.sleep(0.05)
