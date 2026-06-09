import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from modelo import Pais, Plataforma, Serie, Actor, Premio
from config import cadena_base_datos

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

def leer_csv(ruta):
    with open(ruta, encoding='utf-8') as f:
        lector = csv.DictReader(f)
        return list(lector)

print("Cargando Series...")
for fila in leer_csv('../data/series.csv'):

    # Buscar el objeto Plataforma por nombre
    plataforma_obj = session.query(Plataforma).filter_by(nombre=fila['plataforma']).first()

    # Buscar el objeto Pais por nombre
    pais_obj = session.query(Pais).filter_by(nombre=fila['pais']).first()

    session.add(Serie(
        id           = int(fila['id']),
        titulo       = fila['titulo'],
        genero       = fila['genero'],
        anio_estreno = int(fila['anio_estreno']),
        temporadas   = int(fila['temporadas']),
        plataforma   = plataforma_obj,  # objeto ORM, puede ser None si no existe
        pais         = pais_obj         # objeto ORM, puede ser None si no existe
    ))

session.commit()
session.close()
print("Series cargadas correctamente.")