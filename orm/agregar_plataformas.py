import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# se importa la clase(s) del archivo genera_tablas
from modelo import Pais, Plataforma, Serie, Actor, Premio

# se importa información del archivo de configuración
from config import cadena_base_datos

# se genera el enlace al gestor de base de datos
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()
def leer_csv(ruta):
    with open(ruta, encoding='utf-8') as f:
        lector = csv.DictReader(f)
        return list(lector)
# 1. Plataforma
print("Cargando Plataforma...")
for fila in leer_csv('../data/plataformas.csv'):
    session.add(Serie(
        id=int(fila['id']),
        nombre=(fila['nombre']),
        pais=(fila['pais']),
        suscriptores_millones=(fila['suscriptores_millones'])
    ))
session.commit()
session.close()