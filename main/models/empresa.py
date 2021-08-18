from main import db

class Empresa(db.Model):
    __id = db.Column(db.Integer, primary_key=True)
    __razon_social = db.Column(db.String(100), nullable=False)
    __email = db.Column(db.String(120), nullable=False)

    def __init__(self):
        pass

    def __repr__(self):
        return '<Empresa: %r %r >' % (self.razon_social, self.email)

    def set_id(self, id):
        self.__id = id

    def get_id(self):
        return self.__id

    def set_razon_social(self, razon_social):
        self.__razon_social = razon_social

    def get_razon_social(self):
        return self.__razon_social


    def set_mail(self, email):
        self.__email = email

    def get_mail(self):
        return self.__email