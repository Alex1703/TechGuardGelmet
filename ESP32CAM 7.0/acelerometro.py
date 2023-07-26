import random
import time

#Librerias originales 
#from machine import SoftI2C
#from machine import Pin
#from utime import sleep, sleep_ms
#import mpu6050

#/////////////////////////////////////////Librerias para prueba William despues de la linea 53////////////////////
from machine import SoftI2C
from machine import Pin
from utime import sleep, sleep_ms
from MPU6050 import MPU6050
import uasyncio as asyncio

#///////////////////////////////////////////Codigo original
i2c = SoftI2C(scl=Pin(14), sda=Pin(2))      #initializing the I2C method for ESP32
mpu= MPU6050(i2c)

#string = ""

async def detect_golpes(threshold=1000,test=True):
    count = test
    print(count)
    while count:
        valsAcX, valsAcY, valsAcZ= get_values()#mpu.get_values()
        total_accel = abs(valsAcX) + abs(valsAcY) + abs(valsAcZ)
        print(total_accel)
        if total_accel > threshold:
            print("¡Golpe detectado!")
            #print(detect_golpes)
            sleep_ms(1000)
            return True
        count = False            
        

# Llamar a la función para detectar golpes

# (True):
     #print(mpu.get_values()) #-- > Glaficar    variables
     #print(mpu.get_raw_values()) 
     #string = str(mpu.get_values())
    
     #print("")
     #print(string[1:12])
     #print(string[14:25])
     #print(string[27:38])
     #print(string[40:51])

     #inversa =string[52:64]
     #print(inversa[5:11]+ " " + inversa[0:3])
     
     #inversa =string[65:77]
     #print(inversa[5:11]+ " " + inversa[0:3])
     
     #inversa =string[80:99]
     #print(inversa[5:11]+ " " + inversa[0:3])
     
     #print("")
     #print(string)
     #sleep_ms(1000)
#////////////////////////Fin codigo original

#####################################Prueba William

#from machine import SoftI2C
#from machine import Pin
#from utime import sleep, sleep_ms
#from MPU6050 import MPU6050

#i2c = SoftI2C(scl=Pin(14), sda=Pin(2))     #initializing the I2C method for ESP32
#mpu= MPU6050(i2c)


#while (True):
    #accel_data = mpu.read_accel_data()
    #gyro_data = mpu.read_gyro_data()
    #temp_data = mpu.read_temp_data()
    #datos_alecerometro = accel_data
    
    #print("Aceleración en X:", accel_data['x'])
    #print("Aceleración en Y:", accel_data['y'])
    #print("Aceleración en Z:", accel_data['z'])

    #print("Giro en X:", gyro_data['x'])
    #print("Giro en Y:", gyro_data['y'])
    #print("Giro en Z:", gyro_data['z'])

    #print(datos_alecerometro)
    #print(datos_alecerometro)
    #print(temp_data)
#FIn prueba 



# Función para generar valores de aceleración simulados en el rango [-1000, 1000]
def get_values():
    return random.randint(-1000, 1000),random.randint(-1000, 1000),random.randint(-1000, 1000)

