import machine
import network
import ubinascii
from machine import SoftI2C
from machine import Pin
from utime import sleep, sleep_ms
import mpu6050
import utime
import uasyncio as asyncio

uart = machine.UART(1, baudrate=9600, tx=12, rx=13 , parity=None, stop=1, timeout=5000, rxbuf=1024)


def printDataGps(time_utc,latitude,longitude,speed):
    
    gps = """
                
                #########################
                ######### GPS ###########
                #########################
                # Hora UTC: """+ time_utc + """   #'
                # Latitud:  """+ latitude + """'  #'
                # Longitud: """+ longitude +"""   #'
                # Velocidad:"""+ speed  +"""   #'
                #########################               

    """
    return gps

async def getDataGPS():
    temp = True
    while temp:
     if uart.any():
         data = uart.readline()
         if data.startswith(b'$GPRMC'):
            # Procesa los datos NMEA y extrae la información necesaria
            data_str = data.decode('utf-8')
            fields = data_str.split(',')
            if len(fields) >= 8 and fields[2] == 'A':
                time_utc = float(fields[1])
                latitude = float(fields[3])
                longitude = float(fields[5])
                latitud_decimal = latitude // 100 + (latitude % 100) / 60
                longitud_decimal = longitude // 100 + (longitude % 100) / 60
                speed = fields[7]
                
                #gps = printDataGps(time_utc,latitude,longitude,speed)
                latitud_decimal = latitude // 100 + (latitude % 100) / 60
                longitud_decimal = (longitude // 100 + (longitude % 100) / 60) * -1
                #print(gps)
                gps2 = {"latitud":latitud_decimal, "longitud":longitud_decimal, "velocidad":speed, "hora":time_utc}
                temp = False
                return gps2
print(asyncio.run(getDataGPS()))
            
#while True:
    #getDataGPS()


                

                # Realiza acciones con los datos obtenidos (por ejemplo, imprimirlos)

    
                                                                                               