from .. import db
from sqlalchemy.ext.hybrid import hybrid_property

class Partido(db.Model):
    __tablename__ = "partidos"
    __id = db.Column('id', db.Integer, primary_key = True)
    __fecha = db.Column('fecha', db.DateTime ,nullable = False)
    __equipo_local = db.Column('equipo_local', db.String)
    __equipo_visitante = db.Column('equipo_visitante', db.String)
    __finalizado = db.Column('finalizado', db.Boolean)
    __ganador = db.Column('ganador', db.String)
    __goles_local = db.Column('goles_local', db.Integer)
    __goles_visitante = db.Column('goles_visitante', db.Integer)
    cuota = db.relationship('Cuota', back_populates='partido', uselist=False)
    

    def __repr__(self):
        return f'< Cuota:  {self.__id}, {self.__fecha}, {self.__finalizado}>'
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
    def fecha(self,fecha):
        self.__fecha = fecha

    @fecha.deleter
    def fecha(self):
        del self.__fecha

    @hybrid_property
    def equipo_local(self):
        return self.__equipo_local
    
    @equipo_local.setter
    def equipo_local(self,equipo_local):
        self.__equipo_local
    
    @equipo_local.deleter
    def equipo_local(self):
        del self.__equipo_local
    
    @hybrid_property

    def equipo_visitante(self):
        return self.__equipo_visitante
    
    @equipo_visitante.setter
    def equipo_visitante(self,equipo_visitante):
        self.__equipo_visitante = equipo_visitante
    
    @equipo_visitante.deleter
    def equipo_visitante(self):
        del self.__equipo_visitante
    
    @hybrid_property

    def finalizado(self):
        return self.__finalizado
    @finalizado.setter
    def finalizado(self,finalizado):
        self.__finalizado = finalizado
    
    @finalizado.deleter
    def finalizado(self):
        del self.__finalizado
    
    @hybrid_property
    
    def ganador(self):
        return self.__ganador
    
    @ganador.setter
    def ganador(self,ganador):
        self.__ganador = ganador
    
    @ganador.deleter
    def ganador(self):
        del self.__ganador

    @hybrid_property
    
    def goles_local(self):
        return self.__goles_local
    @goles_local.setter
    def goles_local(self, goles_local):
        self.__goles_local = goles_local

    @goles_local.deleter
    def goles_local(self):
        del self.__goles_local
    
    @hybrid_property

    def goles_visitante(self):
        return self.__goles_visitante

    @goles_visitante.setter
    def goles_visitante(self, goles_visitante):
        self.__goles_visitante = goles_visitante
    
    @goles_visitante.deleter
    def goles_visitante(self):
        del self.__equipo_visitante
    




