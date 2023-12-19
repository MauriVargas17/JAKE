# Cooking Pal: AI Voice Assistant

Un asistente de voz personalizable y facil de implementar en una Raspberry Pi 4, gracias a las librerias y modelos de Whisper C++ y Piper, ambas herramientas para convertir voz a texto y texto a voz de manera local, asi como la API de OpenAI para el procesamiento de las peticiones.

## Mauricio Vargas Escobar: 56224

## ¿Como ejecutar?

### Requisitos de software

Despues de clonar el repositorio en la placa Raspberry Pi 4, se debe descomprimir los archivos de piper y voice-en-us-amy-low para poder utilizarlos.

Asi mismo se debe clonar el repositorio https://github.com/ggerganov/whisper.cpp.git en alguna carpeta.

El ultimo requisito es contar con una OPENAI-KEY de una cuenta con fondos para hacer uso de los modelos necesarios como GPT-4.

### Requisitos de hardware

Es necesario contar con la placa Raspberry Pi, recomendablemente de la 4 para arriba. El programa hace un uso intensivo de CPU por lo que placa se calienta, asi que tambien se recomienda usarla en un lugar fresco.

Se debe conectar un microfono USB y en caso de no reconocerse por parte de la placa, se deben hacer las configuraciones pertinentes. Mas detalles en este repositorio: https://github.com/microsoft/IoT-For-Beginners/blob/main/6-consumer/lessons/1-speech-recognition/pi-microphone.md

Se puede usar un parlante USB asi como conectarlo mediante bluetooth, usando la herramienta bluetoothctl desde terminal, haciendo un ==scan on== y al encontrar el dispositivo, hacer ==connect MAC:ADDRESS ==.

### Comandos principales

Primero que nada, nos situamos en la raiz de este repositorio para poder ejecutar los siguientes comandos:

Para activar un entorno virtual (Se debe crear uno si no existe)

```
source ~/ruta/al/entorno/bin/activate
```

Instalar los requerimientos

```
pip install -r requirements.txt
```

Ejecutar el Cooking Pal

```
python cooking_pal.py
```

> [!IMPORTANT]
> Ahora el cooking pal, a quien nos referiremos como _Jake_ en cualquier interaccion que tengamos con el asistente (es obligatorio mencionar su nombre para que la interaccion sea procesada), estara escuchando en el puerto 12345 por datos para hacer decodificacion y procesamiento.

Para ejecutar el reconocimiento de voz de Whisper C++ (habiendo ejecutado el cooking pal primero), estando en el root del repositorio clonado ejecutamos:

```
./stream -m models/ggml-tiny.en.bin --length 2000 -c 0 -t 4 -ac 512 | nc localhost 12345
```

¡Listo! Ahora podras interactuar con el cooking pal (UNICAMENTE EN INGLES por el momento).

> [!TIP]
> Para monitorear el rendimiento y la temperatura de la placa, se puede usar una herramienta llamada _btop_. Si no la tienes, puedes descargarla con:

```
sudo apt update
sudo apt upgrade
sudo apt install btop
```
