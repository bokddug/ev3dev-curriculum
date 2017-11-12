import tkinter
from tkinter import ttk
import ev3dev.ev3 as ev3
import mqtt_remote_method_calls as com
import robot_controller as robo



def main():
    mqtt_client = com.MqttClient()
    mqtt_client.connect_to_ev3()
    root = tkinter.Tk()
    root.title("Color Selection & Drive motor & LED on ev3")
    main_frame = ttk.Frame(root, padding=100, relief='raised')
    main_frame.grid()
    left_speed_label = ttk.Label(main_frame, text="Left")
    left_speed_label.grid(row=0, column=0)
    left_speed_entry = ttk.Entry(main_frame, width=10)
    left_speed_entry.insert(0, "900")
    left_speed_entry.grid(row=1, column=0)
    right_speed_label = ttk.Label(main_frame, text="Right")
    right_speed_label.grid(row=0, column=2)
    right_speed_entry = ttk.Entry(main_frame, width=10)
    right_speed_entry.insert(0, "900")
    right_speed_entry.grid(row=1, column=2)
    forward_button = ttk.Button(main_frame, text="Forward")
    forward_button.grid(row=2, column=1)
    forward_button['command'] = lambda: send_forward(mqtt_client, left_speed_entry, right_speed_entry)
    left_button = ttk.Button(main_frame, text="Left")
    left_button.grid(row=3, column=0)
    left_button['command'] = lambda: send_left(mqtt_client, left_speed_entry, right_speed_entry)
    stop_button = ttk.Button(main_frame, text="Stop")
    stop_button.grid(row=3, column=1)
    stop_button['command'] = lambda: send_stop(mqtt_client)
    right_button = ttk.Button(main_frame, text="Right")
    right_button.grid(row=3, column=2)
    right_button['command'] = lambda: send_right(mqtt_client, left_speed_entry, right_speed_entry)
    back_button = ttk.Button(main_frame, text="Back")
    back_button.grid(row=4, column=1)
    back_button['command'] = lambda: send_backward(mqtt_client, left_speed_entry, right_speed_entry)
    down_button = ttk.Button(main_frame, text="Down")
    down_button.grid(row=6, column=0)
    down_button['command'] = lambda: send_down(mqtt_client)
    q_button = ttk.Button(main_frame, text="Quit")
    q_button.grid(row=5, column=2)
    q_button['command'] = (lambda: quit_program(mqtt_client, False))
    e_button = ttk.Button(main_frame, text="Exit")
    e_button.grid(row=6, column=2)
    e_button['command'] = (lambda: quit_program(mqtt_client, True))
    led_red_both_sides = ttk.Button(main_frame,text='LED RED')
    led_red_both_sides.grid(row=8, column=2)
    led_red_both_sides['command'] = lambda :send_both_red(mqtt_client)
    led_green_both_sides = ttk.Button(main_frame, text='LED GREEN')
    led_green_both_sides.grid(row=9, column=2)
    led_green_both_sides['command'] = lambda: send_both_green(mqtt_client)
    led_black_both_sides = ttk.Button(main_frame, text='TURN OF LED')
    led_black_both_sides.grid(row=10, column=2)
    led_black_both_sides['command'] = lambda: send_both_black(mqtt_client)
    find_object_button = ttk.Button(main_frame, text = 'Find the object')
    find_object_button.grid(row=7, column=0)
    find_object_button['command'] = lambda:send_find_object(mqtt_client,left_speed_entry,right_speed_entry)


    root.mainloop()



def send_up(mqtt_client):
    print("arm_up")
    mqtt_client.send_message("arm_up")


def send_down(mqtt_client):
    print("arm_down")
    mqtt_client.send_message("arm_down")


def send_forward(mqtt_client, left_speed_entry, right_speed_entry):
    print("forward")
    mqtt_client.send_message("drive", [int(left_speed_entry.get()), int(right_speed_entry.get())])


def send_backward(mqtt_client, left_speed_entry, right_speed_entry):
    print("backward")
    mqtt_client.send_message("drive", [-int(left_speed_entry.get()), -int(right_speed_entry.get())])


def send_left(mqtt_client, left_speed_entry, right_speed_entry):
    mqtt_client.send_message("drive", [-int(left_speed_entry.get()), int(right_speed_entry.get())])


def send_right(mqtt_client, left_speed_entry, right_speed_entry):
    mqtt_client.send_message("drive", [int(left_speed_entry.get()), -int(right_speed_entry.get())])


def send_stop(mqtt_client):
    print("stop")
    mqtt_client.send_message("stop")


def quit_program(mqtt_client, shutdown_ev3):
    if shutdown_ev3:
        print("shutdown")
        mqtt_client.send_message("shutdown")
    mqtt_client.close()
    exit()


def send_both_red(mqtt_client):
    print('LEDs---red')
    mqtt_client.send_message('both_red')


def send_both_green(mqtt_client):
    print('LEDs---green')
    mqtt_client.send_message('both_green')


def send_both_black(mqtt_client):
    print('LEDs turn off')
    mqtt_client.send_message('both_black')

def send_find_object(mqtt_client, left_speed_entry, right_speed_entry):
    print('Find the object')
    mqtt_client.send_message('find_object',[left_speed_entry.get,right_speed_entry.get])







main()

