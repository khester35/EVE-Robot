import board
import busio
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

TRIG = 23
ECHO = 24

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

GPIO.output(TRIG, False)
time.sleep(2)

# GPIO.output(TRIG, True)
# time.sleep(0.00001)
# GPIO.output(TRIG, False)

# while GPIO.input(ECHO)==0:
#	pulse_start = time.time()

# while GPIO.input(ECHO)==1:
# 	pulse_end = time.time()

# pulse_duration = pulse_end - pulse_start
# distance = pulse_duration * 17150
# distance = round(distance, 2)
# print(distance)

from adafruit_is31fl3731.matrix import Matrix as Display

i2c = busio.I2C(board.SCL, board.SDA)

display = Display(i2c)

r1=[0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,]
r2=[0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,]
r3=[0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,]
r4=[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,]
r5=[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,]
r6=[0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,]
r7=[0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,]
r8=[0,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,]
r9=[0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,]

cols1 = [r1,r2,r3,r4,r5,r6,r7,r8,r9]

r1=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
r2=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
r3=[0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,]
r4=[0,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,]
r5=[0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,]
r6=[0,0,1,1,1,0,0,0,0,0,1,1,1,1,0,0,]
r7=[0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,]
r8=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
r9=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]

cols2 = [r1,r2,r3,r4,r5,r6,r7,r8,r9]

r1=[1,1,1,0,1,0,1,0,1,1,1,0,1,0,1,0,]
r2=[1,0,0,0,1,0,1,0,1,0,0,0,1,0,1,0,]
r3=[1,0,0,0,1,1,1,0,1,1,1,0,1,0,1,0,]
r4=[1,0,0,0,1,0,1,0,0,0,1,0,0,0,0,0,]
r5=[1,1,1,0,1,0,1,0,1,1,1,0,1,0,1,0,]
r6=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
r7=[1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,]
r8=[0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,]
r9=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]

cols3 = [r1,r2,r3,r4,r5,r6,r7,r8,r9]

r1=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
r2=[0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,0,]
r3=[0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,]
r4=[0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,]
r5=[0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,]
r6=[0,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,]
r7=[0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0,]
r8=[0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,]
r9=[0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,]

cols4 = [r1,r2,r3,r4,r5,r6,r7,r8,r9]

def displayPixels(arr):
	for y,c in enumerate(arr):
		for x,p in enumerate(c):
			if p:
				display.pixel(x,y,50)
			else:
				display.pixel(x,y,0)

while True:
	GPIO.output(TRIG, True)
	time.sleep(0.00001)
	GPIO.output(TRIG, False)

	while GPIO.input(ECHO)==0:
		pulse_start = time.time()

	while GPIO.input(ECHO)==1:
		pulse_end = time.time()

	pulse_duration = pulse_end - pulse_start
	distance = pulse_duration * 17150
	distance = round(distance, 2)

	if distance > 20:
		displayPixels(cols1)
		time.sleep(3)
		displayPixels(cols2)
		time.sleep(.1)
		displayPixels(cols1)
	elif distance <= 35: 
		displayPixels(cols2)
		time.sleep(3)
	
	else: 	
		displayPixels(cols4)
		time.sleep(3)

#	displayPixels(cols3)
#	time.sleep(3)

GPIO.cleanup()
