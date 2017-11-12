import robot_controller
import ev3dev.ev3 as ev3
import time
import tkinter
import math

import mqtt_remote_method_calls as com
from tkinter import ttk

def main():
    root = tkinter.Tk()
    root.title("Piano Robot")

    mqtt_client = com.MqttClient()
    mqtt_client.connect_to_ev3()

    frame = ttk.Frame(root, padding=20)
    frame.grid()

    forward_button = ttk.Button(frame, text="Forward")
    forward_button.grid(row=2, column=1)
    forward_button['command'] = lambda: drive_inches(mqtt_client,20, 100)
    root.bind('<Up>', lambda event: drive_inches(mqtt_client, 20, 100))

    back_button = ttk.Button(frame, text="Back")
    back_button.grid(row=4, column=1)
    back_button['command'] = lambda: drive_inches(mqtt_client, -20,100)
    root.bind('<Down>', lambda event: drive_inches(mqtt_client, -20,100))


    print ("Hi doctor fisher")
    robot = robot_controller.Snatch3r()
    while True:
        playing_piano(robot)
        time.sleep(1)

def drive_inches(self, inches, speed):
    """ Moves the robot forward the requested number of inches at a speed in degrees / second."""
    degrees_per_inch = 90
    degrees = inches * degrees_per_inch

    self.left_motor.run_to_rel_pos(position_sp=degrees, speed_sp=speed, stop_action=ev3.Motor.STOP_ACTION_BRAKE)
    self.right_motor.run_to_rel_pos(position_sp=degrees, speed_sp=speed, stop_action=ev3.Motor.STOP_ACTION_BRAKE)

    self.left_motor.wait_while(ev3.Motor.STATE_RUNNING)
    self.right_motor.wait_while(ev3.Motor.STATE_RUNNING)
    ev3.Sound.beep().wait()
    playing_piano()

def playing_piano(robot):
    # Reference from internet
    # C_note = 262
    # D_note = 294
    # Eflat_note = 311
    # E_note = 330
    # F_note = 349
    # G_note = 392
    # A_note = 440
    # B_note = 494
    # Chigh_note = 523

    # Reference 2
    No_color = 0
    Black = 1
    Blue = 2
    Green = 3
    Yellow = 4
    Red = 5
    White = 6
    Brown = 7

    sensor = ev3.ColorSensor()
    time.sleep(0.1)

    if sensor.color == No_color:
        ev3.Sound.tone("262", 300).wait()
    if sensor.color == Black:
        ev3.Sound.tone("294", 300).wait()
    if sensor.color == Blue:
        ev3.Sound.tone("330", 300).wait()
    if sensor.color == Green:
        ev3.Sound.tone("349", 300).wait()
    if sensor.color == Yellow:
        ev3.Sound.tone("392", 300).wait()
    if sensor.color == Red:
        ev3.Sound.tone("440", 300).wait()
    if sensor.color == White:
        ev3.Sound.tone("494.3", 300).wait()
    if sensor.color == Brown:
        ev3.Sound.tone("523", 300).wait()

main()