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
# 1. Paises
print("Cargando Paises...")
for fila in leer_csv('../data/paises.csv'):
    session.add(Pais(
        id=int(fila['id']),
        nombre=(fila['nombre']),
        continente=(fila['continente']),
        
    ))
session.commit()
session.close()