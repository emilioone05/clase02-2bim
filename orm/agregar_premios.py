import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from modelo import Serie, Premio
from config import cadena_base_datos

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

def leer_csv(ruta):
    with open(ruta, encoding='utf-8') as f:
        lector = csv.DictReader(f)
        return list(lector)

print("Cargando Premios...")
for fila in leer_csv('../data/premios.csv'):

    serie_obj = session.query(Serie).filter_by(titulo=fila['serie']).first()

    session.add(Premio(
        id            = int(fila['id']),
        nombre_premio = fila['nombre_premio'],
        categoria     = fila['categoria'],
        anio          = int(fila['anio']),
        serie         = serie_obj
    ))

session.commit()
session.close()
print("Premios cargados correctamente.")