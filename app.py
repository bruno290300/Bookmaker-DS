from main import create_app
import os

app = create_app()

app.app_context().push()

from main import db
from faker import Faker
from main.models import ClienteModel, EquipoModel, CuotaModel, PartidoModel
import csv
from datetime import datetime


def load_clientes():
    fake = Faker('es_ES')
    for _ in range(10):
        cliente = ClienteModel(nombre=fake.first_name(), apellido=fake.name(), email=fake.email(), activado=fake.boolean())
        db.session.add(cliente)
        db.session.commit()

    


def load_equipos():
    with open('./docs/equipo.csv', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            equipo = EquipoModel(nombre=row[0], escudo=row[1], pais=row[2], puntaje=float(row[3]))

            db.session.add(equipo)

            db.session.commit()
        

def load_partidos():
    formato = "%d/%m/%Y %H:%M"
    with open('./docs/partidos.csv', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            partido = PartidoModel(fecha=datetime.strptime(row[0], formato), equipo_local=row[1], equipo_visitante=row[2], finalizado=False, goles_local=0, goles_visitante=0)
            cuota = CuotaModel(probabilidad_local=float(row[3]), probabilidad_empate=float(row[4]), probabilidad_visitante=float(row[5]))

            partido.cuota = cuota
            db.session.add(partido)

            db.session.commit()
        


if __name__ == '__main__':
    db.drop_all()
    db.create_all()
    load_equipos()
    load_clientes()
    load_partidos()
    app.run(debug=True, port=os.getenv("PORT"))
