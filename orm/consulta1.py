from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker

from modelo import Serie, Actor, Premio
from config import cadena_base_datos

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

resultados = (
    session.query(
        Serie.titulo,
        func.avg(Actor.edad).label('promedio_edad'),
        func.count(Premio.id).label('num_premios')
    )
    .outerjoin(Actor, Actor.serie_id == Serie.id)
    .outerjoin(Premio, Premio.serie_id == Serie.id)
    .group_by(Serie.id, Serie.titulo)
    .all()
)

print(f"{'Titulo':<40} {'Prom. Edad':>12} {'Premios':>10}")
print("-" * 65)
for titulo, prom_edad, num_premios in resultados:
    prom_str = f"{prom_edad:.1f}" if prom_edad else "N/A"
    print(f"{titulo:<40} {prom_str:>12} {num_premios:>10}")

session.close()