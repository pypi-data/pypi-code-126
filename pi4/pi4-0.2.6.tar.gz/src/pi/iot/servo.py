import sys
import os.path
if sys.platform == 'win32' or not __package__:
    sys.path.append(os.path.dirname(__file__))
    from simulator import GPIO
else:
	from RPi import GPIO

if __package__:
    from . import Adafruit_PWM_Servo_Driver as servo_drv # Adafruit Industries 是纽约的一家开源硬件公司
else:
    import Adafruit_PWM_Servo_Driver as servo_drv
import time

RUNNING = True
DELTA = 5 # degrees to to correct servo direction. 
STEP = 5
IIC_SERVO = 0x40

# Initialise the servo PWM using the default address
servo_pwm = servo_drv.PWM(IIC_SERVO, debug = False)
servoMin = 150  # Min pulse length out of 4096
servoMax = 600  # Max pulse length out of 4096

def setServoPulse(channel, pulse):
    pulseLength = 1000000.0                   # 1,000,000 us per second
    pulseLength /= 50.0                       # 60 Hz
    # print ("%d us per period", pulseLength)
    pulseLength /= 4096.0                     # 12 bits of resolution
    # print ("%d us per bit", pulseLength)
    pulse *= 1000.0
    pulse /= (pulseLength*1.0)
    # pwmV=int(pluse)
    # print ("pluse: %f  ", pulse)
    servo_pwm.setPWM(channel, 0, int(pulse))

#Angle to PWM
def turn_direction(servonum,x):
    x = x + DELTA
    y=x/90.0+0.5
    y=max(y,0.5)
    y=min(y,2.5)
    setServoPulse(servonum,y)

def pan_tilt_right():
    global PT_LR
    PT_LR = PT_LR - STEP
    if (PT_LR < 0):
        PT_LR = 0
    turn_direction(1,PT_LR)

def pan_tilt_left():
    global PT_LR
    PT_LR = PT_LR + STEP
    if (PT_LR > 180):
        PT_LR = 180
    turn_direction(1,PT_LR)

def pan_tilt_up():
    global PT_UD
    PT_UD = PT_UD - STEP
    if (PT_UD < 0):
        PT_UD = 0
    turn_direction(2,PT_UD)

def pan_tilt_down():
    global PT_UD
    PT_UD = PT_UD + STEP
    if (PT_UD > 135):
        PT_UD = 135
    turn_direction(2,PT_UD)

def pan_tilt(status): # Pan-Tilt
    '''
    'up3x', 'up2x', 'up1x', \
	'down3x', 'down2x', 'down1x', \
	'left3x', 'left2x', 'left1x', \
	'right3x', 'right2x', 'right1x', \
	'pressed'
    '''    

    if 'up' in status:
        pan_tilt_up()
    if 'down' in status:
        pan_tilt_down()
    if 'left' in status:
        pan_tilt_left()
    if 'right' in status:
        pan_tilt_right()
   
    # time.sleep(0.5)


def ra_right():
    global RA_LR
    RA_LR = RA_LR - STEP
    if (RA_LR < 0):
        RA_LR = 0
    turn_direction(4,RA_LR)

def ra_left():
    global RA_LR
    RA_LR = RA_LR + STEP
    if (RA_LR > 180):
        RA_LR = 180
    turn_direction(4, RA_LR)

def ra_down():
    global RA_UD
    RA_UD = RA_UD - STEP
    if (RA_UD < 45):
        RA_UD = 45
    print(RA_UD)
    turn_direction(5,RA_UD)

def ra_up():
    global RA_UD
    RA_UD = RA_UD + STEP
    if (RA_UD > 180):
        RA_UD = 180
    print(RA_UD)
    turn_direction(5,RA_UD)

def ra_b():
    global RA_FB
    RA_FB = RA_FB - STEP
    if (RA_FB < 50):
        RA_FB = 50
    print(RA_FB)
    turn_direction(6,RA_FB)

def ra_f():
    global RA_FB
    RA_FB = RA_FB + STEP
    if (RA_FB > 180):
        RA_FB = 180
    print(RA_FB)
    turn_direction(6,RA_FB)

def ra_clamp():
    global RA_CLAMP
    if (RA_CLAMP <= 80):
        RA_CLAMP = 90  # open
    elif (RA_CLAMP > 80):
        RA_CLAMP = 65 # close
    print(RA_CLAMP)
    turn_direction(7,RA_CLAMP)

def test_servo():

    for ch in range(8): # 4,5,6,7 are for robotic arms
        for ang in [70, 90]: # [30,60,90,120,150,90]:
            turn_direction(ch,ang)
            time.sleep(0.5)

def reset_tilt():
    turn_direction(1,90)
    time.sleep(0.5)
    turn_direction(2,75)

def test_ra():

    ra_clamp()
    ra_clamp()
    time.sleep(0.5)

    ra_left()
    time.sleep(0.5)

    ra_right()
    time.sleep(0.5)

    ra_up()
    time.sleep(0.5)

    ra_down()
    time.sleep(0.5)   

    ra_f()
    time.sleep(0.5)

    ra_b()
    time.sleep(0.5)
    
def setup():
    servo_pwm.setPWMFreq(50)   # Set frequency

    global PT_LR, PT_UD, RA_LR, RA_UD, RA_FB, RA_CLAMP
    PT_LR = 90 # curretn tilt left-right angle
    PT_UD = 90 # current tilt up-down angle

    RA_LR = 90 # current robotic arm left-right angle
    RA_UD = 90 # current robotic arm up-down angle
    RA_FB = 90 # current robotic arm front-back angle

    RA_CLAMP = 90

def destroy():
	GPIO.cleanup()  # 释放资源

if __name__ == "__main__":
	try:  
		setup()      
		test_servo()        
	except KeyboardInterrupt:                             
		destroy()