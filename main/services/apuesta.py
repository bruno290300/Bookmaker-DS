from .. import db
from main.models import ApuestaModel
from .command import Command, Tarea


class ApuestaService:
    def registrar_apuestas(self, apuesta):
        tarea = Tarea()
        tarea.agregar(ValidarPartido())
        tarea.agregar(ValidarMontos())
        tarea.agregar(GuardarApuesta())
        tarea.agregar(EnviarMail())
        tarea.execute(apuesta)
        return


class ValidarPartido(Command):
    def execute(self, param):
        #lógica para validar apuesta del partido
        pass


class ValidarMontos(Command):
    def execute(self, param):
        #lógica para validar montos de apuesta
        pass


class GuardarApuesta(Command):
    def execute(self, param):
        #lógica para guardar apuesta
        pass


class EnviarMail(Command):
    def execute(self, param):
        #lógica para enviar mail de confirmación de apuesta
        pass
