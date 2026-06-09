import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from modelo import Pais, Serie, Actor
from config import cadena_base_datos

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

def leer_csv(ruta):
    with open(ruta, encoding='utf-8') as f:
        lector = csv.DictReader(f)
        return list(lector)

print("Cargando Actores...")
for fila in leer_csv('../data/actores.csv'):

    pais_obj = session.query(Pais).filter_by(nombre=fila['pais']).first()

    serie_obj = session.query(Serie).filter_by(titulo=fila['serie']).first()

    session.add(Actor(
        id     = int(fila['id']),
        nombre = fila['nombre'],
        edad   = int(fila['edad']),
        pais   = pais_obj,
        serie  = serie_obj
    ))

session.commit()
session.close()
print("Actores cargados correctamente.")