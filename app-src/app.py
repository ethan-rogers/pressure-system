import dearpygui.dearpygui as dpg
import data

dpg.create_context()
dpg.create_viewport(title='Pressure System', width=650, height=350)

with dpg.window(label="Graph Data", width=600, height=300):
    with dpg.plot(label="Sensor Reading", height=-1, width=-1):
        dpg.add_plot_legend()
        
        # Create X and Y Axes
        x_axis = dpg.add_plot_axis(dpg.mvXAxis, label="X Axis")
        y_axis = dpg.add_plot_axis(dpg.mvYAxis, label="Y Axis")

        dpg.set_axis_limits(y_axis, 0, 1024)
        dpg.set_axis_limits(x_axis, 0,1)
        
        
        # Add second line to the SAME y_axis
        dpg.add_line_series([1,2,3], [1,2,3], label="Sensor 1", parent=y_axis, tag = "0")
        dpg.add_line_series([], [], label="Sensor 2", parent=y_axis, tag = "1")
        dpg.add_line_series([], [], label="Sensor 3", parent=y_axis, tag = "2")
        dpg.add_line_series([], [], label="Sensor 4", parent=y_axis, tag = "3")
        dpg.add_line_series([], [], label="Sensor 5", parent=y_axis, tag = "4")
        dpg.add_line_series([], [], label="Sensor 6", parent=y_axis, tag = "5")
        dpg.add_line_series([], [], label="Sensor 7", parent=y_axis, tag = "6")
        dpg.add_line_series([], [], label="Sensor 8", parent=y_axis, tag = "7")


dpg.setup_dearpygui()
dpg.show_viewport()

data.read_data()
    

dpg.destroy_context()
