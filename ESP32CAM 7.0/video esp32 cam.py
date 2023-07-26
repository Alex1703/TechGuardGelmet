import uvc
import machine
import time

# Configuración de la cámara
dev = uvc.CaptureDevice()
dev.product = "ESP32-CAM"
dev.vendor = "Espressif"
dev.width = 640
dev.height = 480
dev.framerate = 10

# Inicialización de la cámara
dev.open()

# Esperar a que la cámara se estabilice
time.sleep(2)

# Configuración del archivo de video
filename = "video.mp4"
fourcc = "mp4v"
fps = 10
video = machine.VideoWriter(filename, fourcc, fps, (dev.width, dev.height))

# Inicio de la grabación
video.open()

# Grabación del video
for i in range(100):  # Grabar durante 10 segundos (100 frames a 10 fps)
    img = dev.getImage()
    video.write(img)

# Fin de la grabación
video.close()

# Cerrar la conexión con la cámara
dev.close()
