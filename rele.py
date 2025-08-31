import RPi.GPIO as GPIO
import datetime
import spidev 
import time

# create SPI connection
spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz = 1000000 # 1 MHz

# function to read out data from MCP3008
def readData(channel):
      adc = spi.xfer2([1,(8+channel)<<4,0])
      data = ((adc[1]&3) << 8) + adc[2]
      return data

pinPump = 4                               # GPIO pin of pump

# general GPIO settings
GPIO.setwarnings(False)                   # ignore warnings (unrelevant here)
GPIO.setmode(GPIO.BCM)                    # refer to GPIO pin numbers
GPIO.setup(pinPump, GPIO.OUT)             # Pi can send voltage to pump
GPIO.output(pinPump, GPIO.LOW)            # turn pump off

f = open("/home/brunocasas/raspberry-watering/WateringStats.txt", "a") 
currentTime = datetime.datetime.now() 
f.write(str(currentTime) + ":\n")


t_end = time.time() + 4               # pump runs 4 seconds
    
# actual pumping
while (time.time() < t_end):                 
    GPIO.output(pinPump, GPIO.HIGH)               

GPIO.output(pinPump, GPIO.LOW)        # turn pump off

f.write("End - rele stopped\n")                             # line break for next log entry
f.close()                                 # close file
GPIO.cleanup()                            # proper clean up of used pins
