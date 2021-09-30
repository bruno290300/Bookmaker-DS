from marshmallow import Schema, fields, validate, post_load
from main.models import CuotaModel


class CuotaSchema(Schema):
    id = fields.Int(dump_only=True)
    probabilid
