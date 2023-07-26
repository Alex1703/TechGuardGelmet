from utime import sleep, sleep_ms
import network, time, urequests
from machine import Pin
from utelegram import Bot, ReplyKeyboardMarkup, KeyboardButton
import json
import urequests as requests
from config.demo import wifi_config
from gps import getDataGPS
import uasyncio as asyncio
from acelerometro import detect_golpes#datos_alecerometro


# Definir los Chats Ids
chat_ids = ['1591218956','1489867926']

# Definir el token de acceso del bot de Telegram
bot_token = "6379582908:AAHIOH39toWMC3jz8rlfXn9r9ZQzqnokyy8"
# Iniciar las instacia de la clase
bot = Bot(bot_token)


#KEYBOARD DEFINED AS ARRAY OF ARRAYS OF KEYBOARDBUTTONS
keyboard = [[KeyboardButton('ON'), KeyboardButton('OFF')], [KeyboardButton('Toggle')]]
replyKeyboard = ReplyKeyboardMarkup(keyboard)

boton = Pin(15, Pin.IN)



def conectaWifi ():
      global miRed
      miRed = network.WLAN(network.STA_IF)     
      if not miRed.isconnected():              #Si no está conectado…
          miRed.active(True)                   #activa la interface
          miRed.connect(wifi_config['ssid'], wifi_config['password'])         #Intenta conectar con la red
          print('Conectando a la red')
          timeout = time.time ()
          while not miRed.isconnected():           #Mientras no se conecte..
              if (time.ticks_diff (time.time (), timeout) > 10):
                  return False
      return True


def initBot():

    @bot.add_command_handler('help')
    def help(update):
        update.reply('Write /start to get a custom keyboard or /value to get the current led status')

    @bot.add_command_handler('start')
    def start(update):
        print(json.dumps(update))
        update.reply('Led control keyboard enabled', reply_markup=replyKeyboard)

    @bot.add_command_handler('value')
    def value(update):
        if led.value():
            update.reply('LED is on')
        else:
            update.reply('LED is off')

    @bot.add_message_handler('^on|On|ON$')
    def on(update):
        led.on()

    @bot.add_message_handler('^off|Off|OFF$')
    def off(update):
        led.off()

    @bot.add_message_handler('^Toggle|TOGGLE|toggle$')
    def toggle(update):
        old_status = bool(led.value())
        led.value(not old_status)

    bot.start_loop()

def sendMessegeWithGps(isButton = False):

    resultadogps = asyncio.run(getDataGPS())
    message = ''
    for i in chat_ids:
        
        
        if isButton:
            message = """ ¡Atención! El botón de pánico del sistema ha sido ejecutado. \n Por favor, contáctese de inmediato con el operador que porta el prototipo para verificar su seguridad. \n Si no responde, reportar el incidente a las autoridades. """
        else :            
            message =  """¡Alerta! Nuestro sistema ha detectado fuertes y bruscos movimientos en el prototipo. \n Por favor, contáctese de inmediato con el operador que porta el prototipo para verificar su seguridad. \n Si no responde, reportar el incidente a las autoridades."""
        
        bot.send_message(i,message)
        bot.send_location(i, float(resultadogps['latitud']), float(resultadogps['longitud']))
        
                


def main():
    if conectaWifi():

        print ("Conexión exitosa!")
        print('Datos de la red (IP/netmask/gw/DNS):', miRed.ifconfig())
        
        print(boton.value())
        if boton.value() ==0:
            sendMessegeWithGps(isButton=True)
        
        print("-- Deteccion de Golpes")        
        if asyncio.run(detect_golpes(test=True)):
            sendMessegeWithGps(isButton = False)
                   
    else:
        print ("Imposible conectar")
        miRed.active (False)
        
        
        

while True:
    main()
    
    

