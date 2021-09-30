from datetime import datetime
from colorama import init, Fore
from abc import ABC, abstractmethod

init(autoreset=True)


class Logger(ABC):
    @abstractmethod
    def info(self, mensaje, valor):
        pass

    @abstractmethod
    def warning(self, mensaje, valor):
        pass

    @abstractmethod
    def error(self, mensaje, valor):
        pass

    @abstractmethod
    def debug(self, mensaje, valor):
        pass


class LoggerFactory(ABC):
    @abstractmethod
    def getLogger(self, tipo):
        pass


class LoggerFactoryImpl(LoggerFactory):
    def getLogger(self, tipo):
        diccionario = {
            'c': LoggerConsole(),
            'f': LoggerFile(),
            'e': LoggerEmail()
        }
        return diccionario[tipo]


class LoggerConsole(Logger):
    def info(self, mensaje, valor):
        print(datetime.now(), Fore.CYAN+" INFO: ", mensaje, valor)

    def warning(self, mensaje, valor):
        print(datetime.now(), Fore.YELLOW+" WARN: ", mensaje, valor)

    def error(self, mensaje, valor):
        print(datetime.now(), Fore.RED+" ERR:  ", mensaje, valor)

    def debug(self, mensaje, valor):
        print(datetime.now(), Fore.GREEN+" DEB:  ", mensaje, valor)


class LoggerFile(Logger):
    def info(self, mensaje, valor):
        with open("file_log.txt", "a") as file:
            out = str(datetime.now()) + " INFO: " + mensaje + " " +  str(valor) +  "\n"
            file.writelines(out)

    def warning(self, mensaje, valor):
        with open("file_log.txt", "a") as file:
            out = str(datetime.now()) + " WARN: " + mensaje + " " + str(valor) +  "\n"
            file.writelines(out)

    def error(self, mensaje, valor):
        with open("file_log.txt", "a") as file:
            out = str(datetime.now()) + " ERR:  " + mensaje + " " + str(valor) +  "\n"
            file.writelines(out)

    def debug(self, mensaje, valor):
        with open("file_log.txt", "a") as file:
            out = str(datetime.now()) + " DEB:  " + mensaje + " " + str(valor) +  "\n"
            file.writelines(out)


class LoggerEmail(Logger):
    def info(self, mensaje, valor):
        print("Enviando email info")

    def warning(self, mensaje, valor):
        print("Enviando email warning")

    def error(self, mensaje, valor):
        print("Enviando email error")

    def debug(self, mensaje, valor):
        print("Enviando email debug")


if __name__ == "__main__":

    type_log = input("Ingrese la letra 'c' para salida por consola, la letra 'f' ara salida por archivo log o 'e' para salida por email: ")

    logger = LoggerFactoryImpl().getLogger(tipo=type_log)
    logger.info("Valor de variable", 1234)
    logger.warning("Valor de warning", 2345)
    logger.error("Valor de error", 7896)
    logger.debug("Valor de debug", 9999)
