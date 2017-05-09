from gpiozero import LightSensor, LED

ldr = LightSensor(4)
led = LED(4)

while True:
	print (ldr.value)
	if ldr.value > ldr.threshold:
		led.off()
		print("light")
	else:
		led.on()
		print("dark")