#final code for camera movement



import socket, traceback

import serial

from time import sleep



import RPi.GPIO as GPIO

import time



GPIO.setmode(GPIO.BOARD)

GPIO.setup(38,GPIO.OUT)

GPIO.setup(40,GPIO.OUT)



p=GPIO.PWM(38,50) #horizontal

p1=GPIO.PWM(40,50) #vertical movement

p.start(7.5)

p1.start(7.5)
sleep(0.5)

p1.ChangeDutyCycle(2)
p.ChangeDutyCycle(2)
sleep(0.5)
p1.ChangeDutyCycle(7.5)
p.ChangeDutyCycle(7.5)
sleep(0.5)
p1.ChangeDutyCycle(12)
p.ChangeDutyCycle(12)
sleep(0.5)
p1.ChangeDutyCycle(7.5)
p.ChangeDutyCycle(7.5)

x_duty = 0
y_duty = 0

while 1 :
   try:

        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

        s.bind(('192.168.29.123', 5555))



        print "Listening for broadcasts..."

        time.sleep(0.1)               

        message, address = s.recvfrom(8192)
        print(message)
        no1,no2,x1,y1,z1,no3,x2,y2,z2,no4,m1,m2,m3=message.split(',')

        #print(message)         #whole message signal

        print(m3)

        a1=float(z1)
        print(z2)
        b1=float(m2)
        s.close()

        if a1>=9:                       #bottom
         x_duty=12
        elif a1>=8 and a1<9:
         x_duty=11.8   
        elif a1>=7.5 and a1<8:
         x_duty=11.6
        elif a1>=7 and a1<7.5:
         x_duty=11.2
        elif a1>=6.5 and a1<7:
         x_duty=10.8
        elif a1>=6 and a1<6.5:
         x_duty = 10.4
        elif a1>=5.5 and a1<6:
         x_duty=10
        elif a1>=5 and a1<5.5:
         x_duty=9.6
        elif a1>=4.5 and a1<5:
         x_duty=9.2
        elif a1>=4 and a1<4.5:
         x_duty=8.8
        elif a1>=3.5 and a1<4:
         x_duty=8.5
        elif a1>=3 and a1<3.5:
         x_duty=8.3
        elif a1>=2.5 and a1<3:
         x_duty=8        
        elif a1>=2 and a1<2.5:
         x_duty=7.8
        elif a1>=-0 and a1<2:    #center
         x_duty=7.5
        elif a1>=-1.5 and a1<-1:
         x_duty=7.1
        elif a1>=-2 and a1<-1.5:
         x_duty=6.8
        elif a1>=-2.5 and a1<-2:
         x_duty=6.5
        elif a1>=-3 and a1<-2.5:
         x_duty=6.1 
        elif a1>=-3.5 and a1<-3:
         x_duty=5.8
        elif a1>=-4 and a1<-3.5:
         x_duty=5.5
        elif a1>=-4.5 and a1<-4:
         x_duty=5.1
        elif a1>=-5 and a1<-4.5:
         x_duty=4.8
        elif a1>=-6 and a1<-5:
         x_duty=4.4
        elif a1>=-7 and a1<-6:
         x_duty=3.8 
        elif a1>=-8 and a1<-7:
         x_duty=3.0
        elif a1>=-9 and a1<-8:
         x_duty=2.5
        elif a1<=-10:
         x_duty=2.0                  #top
        else:
        # x_duty=7.5 #center
          pass


        if b1<=-40:
            y_duty=12
        elif b1>-40 and b1<=-35:
            y_duty = 11.5
        elif b1>-35 and b1<=-30:
            y_duty = 11    
        elif b1>-30 and b1<=-25:
            y_duty=10.5
        elif b1>-25 and b1<=-20:
            y_duty=10
        elif b1>-20 and b1<=-15:
            y_duty=9.5
        elif b1>-15 and b1<=-10:
            y_duty=8.8
        elif b1>=-10 and b1<=-5:
            y_duty = 8.2
        elif b1<=6 and b1>-5:
            y_duty=7.5
        elif b1<=12 and b1>6:
            y_duty = 7
        elif b1<=17 and b1>12:
            y_duty = 6.5
        elif b1<=22 and b1>17:
            y_duty = 6
        elif b1<=26 and b1>22:
            y_duty = 5.5
        elif b1<=30 and b1>26:
            y_duty = 4.5             
        elif b1>=30 and b1<=35:
            y_duty = 3.5
        elif b1>35 and b1<=40:
            y_duty = 2.5
        elif b1>40:
            y_duty=2 
        else:
            pass       

        p1.ChangeDutyCycle(x_duty)
        p.ChangeDutyCycle(y_duty)
        sleep(0.05)

   except Exception as e:
       print("error : ",e)

p1.stop()
GPIO.cleanup()

