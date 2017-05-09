from gpiozero import Motor
from gpiozero import PWMOutputDevice
from time import sleep

motor = Motor(4, 14)
speed = PWMOutputDevice(17, frecuency=1000)
speed.value = 0.5
while True:
	motor.fordward()
	sleep(5)
	motor.backward()
	sleep(5)