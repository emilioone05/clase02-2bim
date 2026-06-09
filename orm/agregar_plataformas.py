import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from modelo import Pais, Plataforma
from config import cadena_base_datos

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

def leer_csv(ruta):
    with open(ruta, encoding='utf-8') as f:
        lector = csv.DictReader(f)
        return list(lector)

print("Cargando Plataformas...")
for fila in leer_csv('../data/plataformas.csv'):

    pais_obj = session.query(Pais).filter_by(nombre=fila['pais']).first()

    session.add(Plataforma(
        id                    = int(fila['id']),
        nombre                = fila['nombre'],
        pais                  = pais_obj,
        suscriptores_millones = round(float(fila['suscriptores_millones']))
    ))

session.commit()
session.close()
print("Plataformas cargadas correctamente.")