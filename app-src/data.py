import numpy as np
import dearpygui.dearpygui as dpg
import serial

NUM_SENSORS = 8
PORT = 'COM5'

data = [np.array([]) for i in range(NUM_SENSORS)]
ser = serial.Serial(port=PORT, baudrate=9600, timeout=1)



def read_data():
    try:
        while dpg.is_dearpygui_running():
            if ser.in_waiting > 0:  # Check if data is available
                line = ser.readline().decode('utf-8').rstrip()
                if line == "S1,S2,S3,S4,S5,S6,S7,S8,AVG_ALL":
                    continue

                for i, val in enumerate(line.split(",")):
                    if i < NUM_SENSORS:
                        data[i] = np.append(data[i], float(val))
                        dpg.set_value( str(i), [np.linspace(0, 1, data[i].size), data[i]])
            
            dpg.render_dearpygui_frame()
    except KeyboardInterrupt:
        print("Closing port...")
    finally:
        ser.close()