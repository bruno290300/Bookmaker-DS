from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self, param):
        pass


class Tarea(Command):
    def __init__(self):
        self.lista = []

    def agregar(self, tarea: Command):
        self.lista.append(tarea)

    def execute(self, param):
        for t in self.lista:
            t.execute(param)
