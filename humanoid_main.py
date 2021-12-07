import sqlite3
import serial
import os
import time
import RPi.GPIO as GPIO
import Adafruit_PCA9685
def robomove():
    pwm = Adafruit_PCA9685.PCA9685()
    servo_min = 150  
    servo_max = 600
    con=sqlite3.connect('robodata.db')
    con.row_factory=sqlite3.Row
    cu=con.cursor()
    pwm.set_pwm_freq(60)
    

    def dbaccess(move):
        cu.execute("SELECT * FROM Movements WHERE action=?",(move,))
        for row in cu:
            m1=row['m1']
            m2=row['m2']
            m3=row['m3']
            m4=row['m4']
            m5=row['m5']
            m6=row['m6']
            m7=row['m7']
            m8=row['m8']
            m9=row['m9']
            M=[m1,m2,m3,m4,m5,m6,m7,m8,m9]
            return M
        
    def positions(M):        
        pwm.set_pwm(1,0,M[0])
        pwm.set_pwm(2,0,M[1])
        pwm.set_pwm(3,0,M[2])
        pwm.set_pwm(4,0,M[3])
        pwm.set_pwm(5,0,M[4])
        pwm.set_pwm(6,0,M[5])
        pwm.set_pwm(7,0,M[6])
        pwm.set_pwm(8,0,M[7])
        pwm.set_pwm(9,0,M[8])
        
        
        return 0

    os.system('echo "enter the movement" | festival --tts')
    while True:
        GPIO.output(12,True)
        print("enter the movement")
        time.sleep(2)
        GPIO.output(12,False)
        text=s.readline()
        text=text.decode('UTF-8')
        text=text.strip()
        text=text.lower()
        movement=text
        print(text)
        if movement=="quit":
            M1=dbaccess("initial")
            positions(M1)
            time.sleep(3)
            break
        elif movement=="swing":
            a=0
            while a<4:
                M1=dbaccess("swing1")
                positions(M1)
                time.sleep(3)
                M2=dbaccess("swing2")
                positions(M2)
                time.sleep(3)
                a+=1
            M3=dbaccess("initial")
            positions(M3)
        elif movement=="fly":
            a=0
            while a<4:
                M1=dbaccess("fly1")
                positions(M1)
                time.sleep(3)
                M2=dbaccess("fly2")
                positions(M2)
                time.sleep(3)
                a+=1
            M3=dbaccess("initial")
            positions(M3)
        else:
            try:
                M=dbaccess(movement)
                positions(M)
                time.sleep(1)
            except:
                print("wrong movement")
                os.system('echo "wrong movement" | festival --tts')
        

try:
    con=sqlite3.connect('/home/pi/Documents/robodata.db')
    cu=con.cursor()
    s=serial.Serial('/dev/rfcomm0')
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(7,GPIO.OUT)
    GPIO.setup(11,GPIO.OUT)
    GPIO.setup(12,GPIO.OUT)
    GPIO.output(11,False)
    while True:
        errorMessage="sorry"
        quitMessage="ok thankyou"
        GPIO.output(7,True)
        time.sleep(2)
        GPIO.output(7,False)
        print("listening")
        text=s.readline()
        text=text.decode('UTF-8')
        text=text.strip()
        text=text.lower()
        print(text)
        if text!="quit":
            if text=="move":
                print(text)
                robomove()
            else:    
                cu.execute('SELECT output FROM Talkback WHERE input=?',(text,))
                rows=cu.fetchone()
                if rows!=None:
                    for row in rows:
                        info=str(row)
                        print(info)
                        os.system('echo %s | festival --tts' %info)
                else:
                    print(errorMessage)
                    os.system('echo %s | festival --tts' %errorMessage)
                
        else:
            print(quitMessage)
            os.system('echo %s | festival --tts' %quitMessage)
            break
    con.close()   
except:
    print("error try again")
