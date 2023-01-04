#archivo donde se convertiran en diccionario lo retornado en el archivo .yaml

import yaml

__config=None

def config():
    global __config
    if not __config:
        with open("config.yaml",mode="r") as f:
#se recibe archivo como parametro y retorna diccionario
            __config=yaml.load(f,Loader=yaml.FullLoader)

    return __config

