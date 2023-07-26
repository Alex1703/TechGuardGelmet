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
    
    #print("Temperatura en °C:", temp_data)
    #print(datos_alecerometro)

    #sleep_ms(1000)

