from main.models import EmpresaModel
from main.repositories import EmpresaRepositorio


repositorio = EmpresaRepositorio


class EmpresaService():
    def obtener_empresas(self):
        return repositorio.obtener_todos()

    def obtener_empresa_por_id(self, id):
        return repositorio.obtener_por_id(id)
