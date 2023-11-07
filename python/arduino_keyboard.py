import serial

with serial.Serial('/dev/ttyACM0', 9600) as ser:
    try:
        while True:
            line = ser.readline().decode("utf-8", errors='replace').strip()
            if (line == "1"):
                print("ON")

    except KeyboardInterrupt:
        ser.close() 
        print("Serial port closed.")