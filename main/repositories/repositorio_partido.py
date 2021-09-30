from flask.scaffold import F
from .. import db
from main.models import PartidoModel
from .repositorio_base import Create, Read, Update, Delete
#from .main.utils import Logger
import logging


logger = logging.getLogger(__name__)


class PartidoRepositorio(Create, Read, Update, Delete):
    def __init__(self):
        self.__modelo = PartidoModel

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

    def delete(self, id):
        try:
            objeto = db.session.query(self.__modelo).get_or_404(id)
            db.session.delete(objeto)
            db.session.commit()
        except Exception as err:
            logger.error("No se pudo borrar %s", id)
            db.session.rollback()


    def update(self, data, id):
        objeto = db.session.query(self.__modelo).get_or_404(id)
        for key, value in data:
            setattr(objeto, key, value)
        db.session.add(objeto)
        db.session.commit()
        return objeto
