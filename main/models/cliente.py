from main import db

class Cliente(db.Model):
    __id = db.Column(db.Integer, primary_key=True)
    __nombre = db.Column(db.String(100), nullable=False)
    __apellido = db.Column(db.String(100), nullable=False)
    __email = db.Column(db.String(120), nullable=False)

    def __init__(self):
        pass

    def __repr__(self):
        return '<Cliente: %r %r %r >' % (self.nombre, self.apellido, self.email)

    def set_id(self, id):
        self.__id = id

    def get_id(self):
        return self.__id

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_nombre(self):
        return self.__nombre

    def set_apellido(self, apellido):
        self.__apellido = apellido

    def get_apellido(self):
        return self.__apellido

    def set_email(self, email):
        self.__email = email

    def get_email(self):
        return self.__email