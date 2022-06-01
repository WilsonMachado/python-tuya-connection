from importlib.resources import open_binary
import logging
from env import * # Archivo donde se encuentran las llaves de tuya

#from tuya_iot import TuyaOpenAPI, TUYA_LOGGER
from tuya_connector import (
	TuyaOpenAPI,
	TuyaOpenPulsar,
	TuyaCloudPulsarTopic,
    TUYA_LOGGER,
) 

# Enable debug log
#TUYA_LOGGER.setLevel(logging.DEBUG)

# Conexión a la OpenAPI de Tuya
openapi = TuyaOpenAPI(API_ENDPOINT, ACCESS_ID, ACCESS_KEY,)
openapi.connect()



# Obtener el estado del dispositivo
status = openapi.get("/v1.0/iot-03/devices/{}/status".format(DEVICE_ID), dict())
get_plug_status = status["result"][0]['value']

flag = not get_plug_status
while True:
    input("Presione enter para encender o apagar el dispositivo")
    commands = {'commands': [{'code': 'switch_1', 'value': flag}]}
    flag = not flag
    openapi.post('/v1.0/iot-03/devices/{}/commands'.format(DEVICE_ID), commands)