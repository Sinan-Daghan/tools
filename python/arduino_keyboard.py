import serial, sys

port = '/dev/ttyACM0'

if len(sys.argv) >= 2:
    port = sys.argv[1]

print(f"You are connected to the port: {port}")

with serial.Serial(port, 9600) as ser:
    try:
        while True:
            line = ser.readline().decode("utf-8", errors='replace').strip()
            if (line == "1"):
                print("ON")

    except KeyboardInterrupt:
        ser.close() 
        print("Serial port closed.")