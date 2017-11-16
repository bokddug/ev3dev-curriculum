"""
  Library of EV3 robot functions that are useful in many different applications. For example things
  like arm_up, arm_down, driving around, or doing things with the Pixy camera.

  Add commands as needed to support the features you'd like to implement.  For organizational
  purposes try to only write methods into this library that are NOT specific to one tasks, but
  rather methods that would be useful regardless of the activity.  For example, don't make
  a connection to the remote control that sends the arm up if the ir remote control up button
  is pressed.  That's a specific input --> output task.  Maybe some other task would want to use
  the IR remote up button for something different.  Instead just make a method called arm_up that
  could be called.  That way it's a generic action that could be used in any task.

  Commands for the Snatch3r robot that might be useful in many different programs.
"""

import ev3dev.ev3 as ev3
import time
import math


class Snatch3r(object):

    def __init__(self):
        self.left_motor = ev3.LargeMotor(ev3.OUTPUT_B)
        self.right_motor = ev3.LargeMotor(ev3.OUTPUT_C)

        assert self.left_motor.connected
        assert self.right_motor.connected
        self.arm_motor = ev3.MediumMotor(ev3.OUTPUT_A)

        assert self.arm_motor.connected

        self.touch_sensor = ev3.TouchSensor()
        assert self.touch_sensor.connected

        self.color_sensor = ev3.ColorSensor()
        assert self.color_sensor

        self.ir_sensor = ev3.InfraredSensor()
        assert self.ir_sensor

        self.pixy = ev3.Sensor()
        assert self.pixy

        self.x=0
        self.y=0
        self.angle=0


        """ Moves the robot forward the requested number of inches at a speed in degrees / second."""
        print("abc")
        degrees_per_inch = 90
        degrees = inches * degrees_per_inch
        self.left_motor.run_to_rel_pos(position_sp=degrees, speed_sp=speed, stop_action=ev3.Motor.STOP_ACTION_BRAKE)
        self.right_motor.run_to_rel_pos(position_sp=degrees, speed_sp=speed, stop_action=ev3.Motor.STOP_ACTION_BRAKE)


    def drive(self, left_sp, right_sp):
        self.left_motor.run_forever(speed_sp=left_sp)
        self.right_motor.run_forever(speed_sp=right_sp)


    def drive_to_point(self, x, y):
        d_x=x
        d_y=y
        destangle= math.atan2(y,x)
        d_angle=destangle-self.angle
        degrees_turn= d_angle*(180/math.pi)
        self.turn_degree(degrees_turn,300)
        distance=math.sqrt((d_x**2)+(d_y**2))
        self.drive_inches(distance,300)
        self.angle=destangle
        self.x= x
        self.y= y



    def turn_degree(self, degree, speed):
        """Moves the robot to a given degree at a given speed."""
        self.left_motor.run_to_rel_pos(position_sp=degree*5, speed_sp=speed)
        self.right_motor.run_to_rel_pos(position_sp=-degree*5, speed_sp=speed)
        self.left_motor.wait_while(ev3.Motor.STATE_RUNNING)
        self.right_motor.wait_while(ev3.Motor.STATE_RUNNING)
        ev3.Sound.beep().wait()

    def stop(self):
        self.right_motor.stop()
        self.left_motor.stop()

    def arm_calibration(self):
        """Moves the arm up and then back down to recalibrate it."""
        touch_sensor = ev3.TouchSensor()
        self.arm_motor.run_forever(speed_sp=900)
        while not touch_sensor.is_pressed:
            time.sleep(0.01)
        self.arm_motor.stop(stop_action=ev3.Motor.STOP_ACTION_BRAKE)
        ev3.Sound.beep().wait()

        self.arm_motor.run_to_rel_pos(position_sp=-5112, speed_sp=900)
        self.arm_motor.wait_while(ev3.Motor.STATE_RUNNING)
        ev3.Sound.beep().wait()

        self.arm_motor.position = 0

    def arm_up(self):
        """Moves arm up to the MAX position."""
        touch_sensor = ev3.TouchSensor()
        self.arm_motor.run_to_abs_pos(position_sp=14.2 * 360, speed_sp=900)
        while not touch_sensor.is_pressed:
            time.sleep(0.01)
        self.arm_motor.stop(stop_action=ev3.Motor.STOP_ACTION_BRAKE)
        self.arm_motor.wait_while(ev3.Motor.STATE_RUNNING)
        ev3.Sound.beep().wait()

    def arm_down(self):
        """Moves the arms down back to the MIN position."""
        self.arm_motor.run_to_abs_pos(position_sp=0, speed_sp=-900)
        self.arm_motor.wait_while(ev3.Motor.STATE_RUNNING)
        ev3.Sound.beep().wait()

    def shutdown(self):
        """Shutdown the program"""
        btn = ev3.Button()
        while btn.backspace:
            ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.GREEN)
            ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.GREEN)
            ev3.Sound.speak('goodbye').wait()
            print('Goodbye')

    def loop_forever(self):
        # This is a convenience method that is only useful if the only input to the robot is coming via mqtt.
        btn = ev3.Button()
        self.running = True
        while not btn.backspace and self.running:
            # Do nothing while waiting for commands
            time.sleep(0.01)
        self.shutdown()

    def seek_beacon(self):
        forward_speed = 300
        turn_speed = 100
        beacon_seeker = ev3.BeaconSeeker(channel=1)

        while not self.touch_sensor.is_pressed:
            current_heading = beacon_seeker.heading
            current_distance = beacon_seeker.distance
            if current_distance == -128:
                print("IR Remote not found. Distance is -128")
                self.drive(turn_speed,-turn_speed)
            else:

                if math.fabs(current_heading) < 2:
                    if current_distance == 1:
                        self.drive_inches(4, forward_speed)
                        self.stop()
                        print("Found the beacon!")
                        return True
                    print("On the right heading. Distance: ", current_distance)
                    if current_distance > 1:
                        self.drive(forward_speed, forward_speed)
                        time.sleep(0.1)
                if 2 < math.fabs(current_heading) < 10:
                    if current_heading > 0:
                        self.drive(turn_speed, -turn_speed)
                        time.sleep(0.1)
                        print("Adjusting heading right: ", current_heading)

                    if current_heading < 0:
                        self.drive(-turn_speed, turn_speed)
                        time.sleep(0.1)
                        print("Adjusting heading left: ", current_heading)

                if math.fabs(current_heading) > 10:
                    self.drive(forward_speed,-forward_speed)
                    time.sleep(0.1)
                    print("Heading is too far off to fix: ", current_heading)

            time.sleep(0.2)
        print("Abandon ship!")
        self.stop()
        return False

    def both_red(self):
        ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.RED)
        ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.RED)

    def both_green(self):
        ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.GREEN)
        ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.GREEN)

    def both_black(self):
        ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.BLACK)
        ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.BLACK)

    def follow_black_line(self, left_speed, right_speed, color_to_seek):
        while True:
            self.drive(left_speed,right_speed)
            current_color = self.color_sensor.color
            time.sleep(0.1)
            if current_color == color_to_seek:
                self.right_motor.stop(speed_sp=0)
                self.left_motor.stop(speed_sp=0)
                ev3.Sound.speak("Stop").wait()
                break
        self.stop()
        self.drive_inches(2.8,left_speed)
        self.turn_degree(90,left_speed)

        while not self.color_sensor.color == ev3.ColorSensor.COLOR_RED:
            if self.color_sensor.reflected_light_intensity < 50:
                self.drive(left_speed, right_speed)
            if self.color_sensor.reflected_light_intensity >= 50:
                self.drive(left_speed,-right_speed)
                time.sleep(0.01)
            if self.color_sensor.color == ev3.ColorSensor.COLOR_RED:
                break
        self.stop()
        ev3.Sound.speak("Done")
        self.arm_down()
        self.arm_up()
        time.sleep(1)
        self.drive_inches(21,left_speed)
        self.arm_down()







