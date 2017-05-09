from gpiozero import Motor
from time import sleep

motor = Motor(4, 14)

while True:
	motor.fordward()
	sleep(5)
	motor.backward()
	sleep(5)