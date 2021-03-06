from marshmallow import Schema, fields, post_load
from main.models import EquipoModel


class EquipoSchema(Schema):
    id = fields.Int(dump_only=True)
    nombre = fields.String(required=True)
    escudo = fields.String(required=True)
    pais = fields.String(required=True)
    puntaje = fields.Int(required=True)

    @post_load
    def make_equipo(self, data, **kwargs):
        return EquipoModel(**data)
