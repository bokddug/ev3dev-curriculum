
import tkinter
from tkinter import ttk



import mqtt_remote_method_calls as com

import robot_controller as robo



class Point(object):
    def __init__(self,x,y):
        self.x=0
        self.y=0


    def move(self,x,y):
        self.x=self.x+x
        self.y=self.y+y





def main():
    root = tkinter.Tk()
    root.title("MQTT track robot")

    main_frame = ttk.Frame(root, padding=5)
    main_frame.grid()

    instructions = "Track the robot"
    label = ttk.Label(main_frame, text=instructions)
    label.grid(columnspan=2)

    end_x = ttk.Label(main_frame, justify=tkinter.LEFT, text="Position_x")
    end_x.grid(row=1, column=0)

    end_y = ttk.Label(main_frame, justify=tkinter.LEFT, text="Position_y")
    end_y.grid(row=2, column=0)


    """Entry"""
    end_x_entry = ttk.Entry(main_frame, width=8)
    end_x_entry.grid(row=1, column=1)

    end_y_entry = ttk.Entry(main_frame, width=8)
    end_y_entry.grid(row=2, column=1)


    """Buttons"""
    draw1_button = ttk.Button(main_frame, text="Draw")
    draw1_button.grid(row=2, column=3)
    point=Point(0,0)

    draw1_button['command'] = lambda: draw(mqtt_client, end_x_entry, end_y_entry,canvas,point)
    root.bind('<q>', lambda event: draw(mqtt_client, end_x_entry, end_y_entry,canvas,point))



    # Make a tkinter.Canvas on a Frame.
    canvas = tkinter.Canvas(main_frame, background="white", width=800, height=500)
    canvas.grid(column=4)

    clear_button = ttk.Button(main_frame, text="Clear")
    clear_button.grid(row=10, column=0)
    clear_button["command"] = lambda: clear(canvas)
    #
    quit_button = ttk.Button(main_frame, text="Quit")
    quit_button.grid(row=10, column=1)
    quit_button["command"] = lambda: quit_program(mqtt_client)


    mqtt_client=com.MqttClient(robo.Snatch3r)
    mqtt_client.connect_to_ev3()

    root.mainloop()
# ----------------------------------------------------------------------
# Tkinter event handlers
# Left mouse click
# ----------------------------------------------------------------------
def draw(mqtt_client,end_x_entry,end_y_entry, canvas,point):
    color = 'blue'
    inches_x=int(end_x_entry.get())/6
    inches_y=int(end_y_entry.get())/6

    mqtt_client.send_message("drive_to_point", [inches_x, inches_y])

    print("before",point.x,point.y)
    canvas.create_line(point.x,point.y,point.x+int(end_x_entry.get()), point.y+int(end_y_entry.get()), fill=color, width=3)

    point.move(int(end_x_entry.get()),int(end_y_entry.get()))
    print("after",point.x,point.y)
def clear(canvas):
    canvas.delete("all")


def quit_program(mqtt_client):

    if mqtt_client:
        mqtt_client.close()
    exit()


main()
