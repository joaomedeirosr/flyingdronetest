from djitellopy import tello
import time

# Make variable to call the class Tello of the
# library tello
drone = tello.Tello()

# Call the method "connect" of library Tello
# for conect the drone to the wireless network to PC
#for the drone receive the commands

drone.connect()

#print on the console the method to show level of baterry
#before start fly
print(drone.get_battery())

#Move Drone using distance in cm
#drone.takeoff this method is to the drone fly
drone.takeoff()

#Call the method "move_up" and give for
# the atribute 80 for the drone get up 80 cm
drone.move_up(80)

# Move using speed
drone.send_rc_control(0, 0, 0, 20)

time.sleep(5)

drone.send_rc_control(0,0,0,0)

drone.land()





