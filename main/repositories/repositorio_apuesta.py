from flask.scaffold import F
from .. import db
from main.models import ApuestaModel
from .repositorio_base import Create, Read


class ApuestaRepositorio(Create, Read):
    def __init__(self):
        self.__modelo = ApuestaModel

    def find_all(self):
        objetos = db.session.query(self.__modelo).all()
        return objetos

    def find_one(self, id):
        objeto = db.session.query(self.__modelo).get_or_404(id)
        return objeto

    def create(self, objeto):
        db.session.add(objeto)
        db.session.commit()
        return objeto
