# ControlTMPDC

Problema: 
La temperatura recomendada para la correcta conservación de los equipos es entre 17°C y 21°C la cual se sugiere sea mantenida con aire acondicionado, pero los aires acondicionados pueden ser desajustados (manual o por falla mecánica) y la temperatura del datacenter puede aumentar o disminuir poniendo en riesgo los equipos, lo que puede provocar daño en los equipos o disminución en su tiempo de vida útil. Muchas empresas tienen problemas para llevar control de la temperatura en los datacenter, por lo general por falta de equipos para monitoreo.


RECURSOS Hardware y Software
Hardware:
•	ESP32: Creado y desarrollado por Espressif Systems, ESP32, una serie de microcontroladores de bajo costo y de bajo consumo con sistema en chip con Wi-Fi y Bluetooth de modo dual integrados, es un avance para los ingenieros de automatización que no quieren verse envueltos en los matices de la radiofrecuencia (RF) y el diseño inalámbrico. Como una radio combinada Wi-Fi/Bluetooth de bajo costo, la serie ha ganado popularidad no solo entre los aficionados sino también entre los desarrolladores de IoT. Su bajo consumo de energía, sus múltiples entornos de desarrollo de código abierto y sus bibliotecas la hacen perfectamente adecuada para desarrolladores de todo tipo. https://www.digikey.com/es/articles/how-to-select-and-use-the-right-esp32-wi-fi-bluetooth-module 
 
 

•	OLED: Modulo Display LCD OLED 128x64 1.3" I2C Azul 4 Pines compatible con Arduino, el cual podrás acoplarlo a tus pequeños prototipos gracias a su tamaño reducido de solo 35.4 mm x 33.5 mm, perfecto para aplicaciones en Medidores Portátiles, dispositivos Médicos, Reproductores Portátiles, productos como Smart Watch, entre otros. https://ferretronica.com/products/modulo-display-lcd-oled-128x64-1-3-i2c-azul-4-pines 
 
•	DTH11: El DHT11 es un sensor digital de temperatura y humedad relativa de bajo costo y fácil uso. Integra un sensor capacitivo de humedad y un termistor para medir el aire circundante, y muestra los datos mediante una señal digital en el pin de datos (no posee salida analógica). Utilizado en aplicaciones académicas relacionadas al control automático de temperatura, aire acondicionado, monitoreo ambiental en agricultura y más. https://naylampmechatronics.com/sensores-temperatura-y-humedad/57-sensor-de-temperatura-y-humedad-relativa-dht11.html 
 
 
Software: 

•	Thony: Thonny es un entorno de desarrollo integrado para Python diseñado para principiantes. Admite diferentes formas de recorrer el código, evaluación de expresiones paso a paso, visualización detallada de la pila de llamadas y un modo para explicar los conceptos de referencias y montón. https://en.wikipedia.org/wiki/Thonny 

 
•	Librerias:  En informática, una biblioteca o, llamada por vicio del lenguaje librería (del inglés library) es un conjunto de implementaciones funcionales, codificadas en un lenguaje de programación, que ofrece una interfaz bien definida para la funcionalidad que se invoca. https://pythones.net/importar-modulos-en-python/ 

 
•	Fritzing: Fritzing es un programa libre de código abierto que te permite crear y diseñar circuitos. Su interfaz es sencilla e intuitiva, y se complementa con otras iniciativas como Processing y Arduino, formando así un ecosistema que permite a los usuarios documentar y compartir sus prototipos, enseñar electrónica y crear esquemas de circuitos impresos. https://oshl.umh.es/2014/05/30/fritzing-un-programa-open-source-para-el-diseno-electronico/ 
 
IFTTT: IFTTT es una plataforma que se lanzó en 2010 y que permite crear o programar acciones para automatizar diferentes tareas en la Red. Concretamente, su nombre viene de un conjunto de siglas que, en español, significan “Si ocurre esto, haz esto otro” o "IF This Then That".
El objetivo principal de IFTTT es mejorar la productividad del usuario, hasta el punto de que tiene como lema: “Pon a Internet a trabajar para ti”. https://computerhoy.com/noticias/internet/que-es-ifttt-65689 

 
 
ESQUEMA

![image](https://user-images.githubusercontent.com/86392467/127083930-a7beac6a-f3a9-42b3-bf8f-71fe305cb1c5.png)

•	Vista OLED y LED:
o	Temperatura normal y LED verde activo


o	Temperatura subiendo/bajando y LED amarillo activo








o	Temperatura alta/baja y LED verde activo 

 

•	Recepción correo y alimentación Drive: De esta forma se visualiza los datos recibidos por el sensor a cada cambio de temperatura alimentando una hoja de calculo en drive indicándonos la fecha y hora de cada registro, también se puede corroborar que la hora registrada en la tabla coincide con el correo recibido el cual alerta por un cambio de temperatura fuera de los rangos normales:

 


