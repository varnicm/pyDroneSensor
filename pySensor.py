import serial
import csv
import time

# Configure the serial connection to the Arduino
ser = serial.Serial('COM3', 9600, timeout=1)  # Replace 'COM3' with your actual port

# Open the CSV file where data will be stored
with open('data_log.csv', 'w', newline='') as csvfile:
    data_writer = csv.writer(csvfile)
    
    # Write a header row
    data_writer.writerow(['Timestamp', 'Sensor Value'])
    
    # Keep reading data from serial and write to the CSV
    while True:
        try:
            # Read a line from serial and decode it
            line = ser.readline().decode('utf-8').rstrip()
            
            # If the line has data, write it to CSV
            if line:
                timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
                data_writer.writerow([timestamp, line])
                print(f"Logged data: {line}")
        
        except KeyboardInterrupt:
            print("Exiting...")
            break
        except Exception as e:
            print(f"An error occurred: {e}")

# Close the serial connection
ser.close()