

import tkinter
from tkinter import ttk

import mqtt_remote_method_calls as com


class MyDelegate(object):

    def print_message(self, message):
        print("Message received:", message)


def main():
    root = tkinter.Tk()
    root.title = "MQTT Talking to yourself"

    main_frame = ttk.Frame(root, padding=20, relief='raised')
    main_frame.grid()

    msg_entry = ttk.Entry(main_frame, width=40)
    msg_entry.grid(row=1, column=0)

    msg_button = ttk.Button(main_frame, text="Send")
    msg_button.grid(row=1, column=1)
    msg_button['command'] = lambda: send_message(mqtt_client, msg_entry)
    root.bind('<Return>', lambda event: send_message(mqtt_client, msg_entry))

    q_button = ttk.Button(main_frame, text="Quit")
    q_button.grid(row=1, column=2)
    q_button['command'] = (lambda: quit_program(mqtt_client))

    # Create an MQTT connection
    my_delegate = MyDelegate()
    mqtt_client = com.MqttClient(my_delegate)
    mqtt_client.connect("topic_name", "topic_name")
    # mqtt_client.connect("topic_name", "topic_name", "35.194.247.175")  # Off campus IP address of a GCP broker

    root.mainloop()


def send_message(mqtt_client, msg_entry):
    msg = msg_entry.get()
    msg_entry.delete(0, 'end')
    mqtt_client.send_message("print_message", [msg])


def quit_program(mqtt_client):
    mqtt_client.close()
    print("Closed connection")
    exit()


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
