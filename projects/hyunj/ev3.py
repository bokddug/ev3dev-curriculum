import mqtt_remote_method_calls as com
import robot_controller as robo
import ev3dev.ev3 as ev3
import time

class DataContainer(object):

    def __init__(self):
        self.running = True

def main():
    robot = robo.Snatch3r()
    mqtt_client = com.MqttClient(robot)
    mqtt_client.connect_to_pc()
    robot.loop_forever()
    dc = DataContainer()
    btn = ev3.Button()
    btn.on_backspace = lambda state:handle_shutdown(state,dc)
    while dc.running:
        btn.process()
        time.sleep(0.01)

    print("Goodbye!")
    ev3.Sound.speak("Goodbye").wait()
def handle_shutdown(button_state, dc):
    if button_state:
        print("back")
        dc.running = False

main()
