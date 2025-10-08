# Pico Explorer Stopwatch ⏱️

A compact, lap-enabled stopwatch built for the [Pimoroni Pico Explorer Base](https://shop.pimoroni.com/products/pico-explorer-base), using MicroPython and the `picographics` display library. Designed for clarity, tactile control, and segmented lap tracking with visual feedback.

## Features

- 🟢 **Start/Stop** with Button X (GPIO 14)
- 🟡 **Lap** with Button Y (GPIO 15)
- 🔴 **Reset** with Button B (GPIO 13) or Button A (GPIO 12)
- 📺 **Large main timer** showing lap time while running
- 🕓 **Secondary timer** shows total race time after first lap
- 📋 **Lap history** displays last 4 laps in soft grey
- 🧠 **Final lap auto-recorded** when stopwatch is stopped

## Display Behavior

- **Running**: Main timer shows lap time; secondary timer shows total time (after first lap)
- **Stopped**: Main timer shows total time; secondary timer disappears
- **Lap Pressed**: Lap time is recorded and lap timer resets
- **Stop Pressed**: Final lap is recorded automatically

## Hardware Requirements

- Raspberry Pi Pico (or Pico W)
- Pimoroni Pico Explorer Base
- MicroPython firmware with `picographics` and `pimoroni` libraries installed

## Setup

1. Flash your Pico with [Pimoroni's custom MicroPython firmware](https://github.com/pimoroni/pimoroni-pico/releases)
2. Copy `stopwatch.py` to your Pico using Thonny or your preferred IDE
3. Run the script and interact using the onboard buttons

## Button Mapping

| Button | GPIO | Function     |
|--------|------|--------------|
| A      | 12   | Reset        |
| B      | 13   | Reset        |
| X      | 14   | Start/Stop   |
| Y      | 15   | Lap          |

## License

MIT License. See `LICENSE.md` for details.

