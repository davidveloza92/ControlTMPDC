from machine import Pin, I2C, PWM #led,oled
from ssd1306 import SSD1306_I2C #oled
from dht import DHT11 #sensor temperatura
import network, utime, urequests #importa red, tiempo,

#definir medidas OLED
ancho = 128
alto = 64
#declarar variables
i2c = I2C(0, scl=Pin(22), sda=Pin(21))  #Variable OLED
oled = SSD1306_I2C(ancho, alto, i2c)   #Variable OLED
sensor =DHT11(Pin(5))  #Variable sensor DTH11

#variables LED
led_rojo= Pin(14,Pin.OUT)
led_amarillo= Pin(26,Pin.OUT)
led_verde= Pin(33,Pin.OUT)
#impresion por pantalla OLED
print(i2c.scan())
 
oled.text('Sensor de TMP', 0, 0)
oled.text('Areandina', 0, 10)
oled.text('Data Center', 0, 20)
oled.show()
utime.sleep(4)
 

#conectar tarjeta a Wifi
def conectaWifi (red, password):
      global miRed
      miRed = network.WLAN(network.STA_IF)     
      if not miRed.isconnected():              #Si no está conectado…
          miRed.active(True)                   #activa la interface
          miRed.connect(red, password)         #Intenta conectar con la red
          print('Conectando a la red', red +"…")
          timeout = time.time ()
          while not miRed.isconnected():           #Mientras no se conecte..
              if (time.ticks_diff (time.time (), timeout) > 10):
                  return False
      return True
#validacion conexion wifi
if conectaWifi ("FamiliaVelozaValbuena", "YUANDAVA7311"):

    print ("Conexión exitosa!")
    print('Datos de la red (IP/netmask/gw/DNS):', miRed.ifconfig())
      
    url = "https://maker.ifttt.com/trigger/CorreoDTH11/with/key/cZxI2QEPRjGVf2SHnvSSSQ?"
    url2 = "https://maker.ifttt.com/trigger/DTH11/with/key/cZxI2QEPRjGVf2SHnvSSSQ?"



 
    while (True):
    
        utime.sleep(1)
      
        sensor.measure() #toma valores del sensor
        temp=sensor.temperature() #da un valor a temperatura
        hum=sensor.humidity() #da un valor a humedad
    
        if temp < 14:
       
            led_rojo.value(1)
            led_amarillo.value(0)
            led_verde.value(0)
            print("Temperatura baja")
            utime.sleep (1)
        
            oled.fill(0)  
            oled.text("T={:02d} °C".format(temp),0,10) #imprime en oled temp
            oled.text("H={:02d} %".format(hum),0,20)   #imprime en oled Hum
            oled.text("Temperatura",0,40)   #imprime en oled Hum
            oled.text("Baja",0,50)
            oled.show()
            #alimenta documento en drive
            respuesta2 = urequests.get(url2+"&value1="+str(temp)+"&value2="+str(hum)) #variable para URL doc
            print(respuesta2.text)
            print (respuesta2.status_code)
            respuesta2.close ()
            #envia mail
            respuesta = urequests.get(url+"&value1="+str(temp)+"&value1="+str(hum)) #variable envio MAil
            print(respuesta.text)
            print (respuesta.status_code)
            respuesta.close ()
            time.sleep(10)
        
        elif temp > 13 and temp < 17:
    
            led_rojo.value(0)
            led_amarillo.value(1)
            led_verde.value(0)
            print("Temperatura disminuyendo")
            utime.sleep (1)
        
            oled.fill(0)  
            oled.text("T={:02d} °C".format(temp),0,10) #imprime en oled temp
            oled.text("H={:02d} %".format(hum),0,20)   #imprime en oled Hum
            oled.text("Temperatura",0,40)   #imprime en oled Hum
            oled.text("Disminuyendo",0,50)
            oled.show()
            
            respuesta2 = urequests.get(url2+"&value1="+str(temp)+"&value2="+str(hum))
            print(respuesta2.text)
            print (respuesta2.status_code)
            respuesta2.close ()
        
        elif temp > 16 and temp < 25:
    
            led_rojo.value(0)
            led_amarillo.value(0)
            led_verde.value(1)
            print("Temperatura normal")
        
            oled.fill(0)  
            oled.text("T={:02d} °C".format(temp),0,10) #imprime en oled temp
            oled.text("H={:02d} %".format(hum),0,20)   #imprime en oled Hum
            oled.text("Temperatura",0,40)   #imprime en oled Hum
            oled.text("Normal",0,50)
            oled.show()
            
            respuesta2 = urequests.get(url2+"&value1="+str(temp)+"&value2="+str(hum))
            print(respuesta2.text)
            print (respuesta2.status_code)
            respuesta2.close ()
            
       
        
        #oled.fill(0)  
        #oled.text("Temperatura normal",0,40)   #imprime en oled Hum
        #oled.show()
        #utime.sleep (5)
        
        elif temp > 24 and temp < 26:
    
            led_rojo.value(0)
            led_amarillo.value(1)
            led_verde.value(0)
            print("Temperatura aumentando")
            utime.sleep (1)
        
            oled.fill(0)  
            oled.text("T={:02d} °C".format(temp),0,10) #imprime en oled temp
            oled.text("H={:02d} %".format(hum),0,20)   #imprime en oled Hum
            oled.text("Temperatura",0,40)   #imprime en oled Hum
            oled.text("Aumentando",0,50)
            oled.show()
            
            respuesta2 = urequests.get(url2+"&value1="+str(temp)+"&field2="+str(hum))
            print(respuesta2.text)
            print (respuesta2.status_code)
            respuesta2.close ()
            
        elif temp > 25:
    
            led_rojo.value(1)
            led_amarillo.value(0)
            led_verde.value(0)
            print("Temperatura alta")
            utime.sleep (1)
        
            oled.fill(0)  
            oled.text("T={:02d} °C".format(temp),0,10) #imprime en oled temp
            oled.text("H={:02d} %".format(hum),0,20)   #imprime en oled Hum
            oled.text("Temperatura",0,40)   #imprime en oled Hum
            oled.text("Alta",0,50)
            oled.show()
            
            respuesta2 = urequests.get(url2+"&value1="+str(temp)+"&field2="+str(hum))
            print(respuesta2.text)
            print (respuesta2.status_code)
            respuesta2.close ()
            #Envio email
            respuesta = urequests.get(url+"&value1="+str(temp)+"&value1="+str(hum)) #variable envio MAil
            print(respuesta.text)
            print (respuesta.status_code)
            respuesta.close ()
            utime.sleep(10)
            
    
    #oled.fill(0)  
    #oled.text("T={:02d} °C".format(temp),0,10) #imprime en oled temp
    #oled.text("H={:02d} %".format(hum),0,30)   #imprime en oled Hum
    #oled.show()
    
        print("T={:02d} °C, H={:02d} %" .format(temp,hum))   #imprime en thony temp y hum
    
    #print("T={:02d} °C, H={:02d} %" .format(temp,hum))
        utime.sleep(1)
    
else:
       print ("Imposible conectar")
       miRed.active (False)   
if __name__=="__name__":
    main()