# pySensor

## Introduction

This project involves a Python script for logging data from an Arduino to a CSV file. The script establishes a serial connection with the Arduino and continuously reads sensor data, which it then logs along with a timestamp to a CSV file.

## Requirements

- Python 3.x
- `pyserial` library
- `csv` library
- Arduino (or similar microcontroller)
- Serial connection to the Arduino (USB, etc.)

## Installation

1. Install Python 3.x from [python.org](https://www.python.org/).
2. Install the `pyserial` library using pip:

   ```bash
   pip install pyserial
   ```

3. Connect your Arduino to the computer and note the COM port it's connected to.

## Usage

1. Open the script in a Python editor or IDE.
2. Modify the line `ser = serial.Serial('COM3', 9600, timeout=1)` to match the COM port of your Arduino.
3. Run the script. It will start logging data from the Arduino to `data_log.csv`.
4. To stop logging, use `Ctrl+C` in the terminal or console.

## Script Overview

- `serial.Serial`: Establishes a serial connection with the Arduino.
- `csv.writer`: Opens a CSV file and prepares it for writing data.
- `while True`: A loop that continuously reads data from the Arduino.
- `ser.readline()`: Reads a line of data from the Arduino.
- `time.strftime`: Adds a timestamp to each data entry.

## Error Handling

- The script includes basic error handling for common issues such as interruptions or serial connection errors.

## Closing the Connection

- The script ensures the serial connection is closed properly when the script is stopped.

## Disclaimer

- Ensure the Arduino is connected properly.
- The COM port and baud rate in the script should match the Arduino's configuration.
- This script is a basic example and might need modifications for specific use cases.

## Contributing

Feel free to fork this project and contribute. If you find any issues or have suggestions, please open an issue or a pull request.

