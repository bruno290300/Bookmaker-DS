from .. import db
from sqlalchemy.ext.hybrid import hybrid_property


class Apuesta(db.Model):
    __tablename__ = 'apuestas'
    __id = db.Column('id', db.Integer, primary_key=True, nullable=False)
    __fecha = db.Column('fecha', db.DateTime, nullable=False)
    __monto = db.Column('monto', db.Float('equipo.id'), nullable=False)
    __equipo_ganador = db.Column('equipo_ganador', db.ForeignKey('equipos.id'), nullable=False)

    def __repr__(self):
        return '<Apuesta: %r %r %r %r>' % (self.__id, self.__fecha, self.__monto, self.__eqipo_ganador)

    @hybrid_property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @id.deleter
    def id(self):
        del self.__id

    @hybrid_property
    def fecha(self):
        return self.__fecha

    @fecha.setter
    def fecha(self, fecha):
        self.__fecha = fecha

    @fecha.deleter
    def fecha(self):
        del self.__fecha

    @hybrid_property
    def monto(self):
        return self.__monto

    @monto.setter
    def monto(self, monto):
        self.__monto = monto

    @monto.deleter
    def monto(self):
        del self.__monto

    @hybrid_property
    def equipo_ganador(self):
        return self.__equipo_ganador

    @equipo_ganador.setter
    def equipo_ganador(self, equipo_ganador):
        self.__equipo_ganador = equipo_ganador

    @equipo_ganador.deleter
    def equipo_ganador(self):
        del self.__equipo_ganador
