import serial

# Configure the serial port
# Windows: 'COM1', 'COM2', etc.
# Linux/macOS: '/dev/ttyUSB0', '/dev/ttyACM0', etc.
ser = serial.Serial(port='COM5', baudrate=9600, timeout=1)

try:
    while True:
        if ser.in_waiting > 0:  # Check if data is available in the buffer
            line = ser.readline().decode('utf-8').rstrip()
            print(f"Received: {line}")
except KeyboardInterrupt:
    print("Closing connection.")
finally:
    ser.close()  # Always close the port to free resources