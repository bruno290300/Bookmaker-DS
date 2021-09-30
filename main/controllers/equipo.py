from flask_restful import Resource
from flask import request
from .. import db
from main.models import EquipoModel
from main.map import EquipoSchema
import logging

equipo_schema = EquipoSchema()
logger = logging.getLogger(__name__)


class Equipo(Resource):
    
    def get(self, id):
        equipo = db.session.query(EquipoModel).get_or_404(id)
        logger.info("Equipo: %s", equipo)
        return equipo_schema.dump(equipo), 201

    def delete(self, id):
        equipo = db.session.query(EquipoModel).get_or_404(id)
        db.session.delete(equipo)
        db.session.commit()
        return '', 204

    def put(self, id):
        equipo = db.session.query(EquipoModel).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(equipo, key, value)
        db.session.add(equipo)
        db.session.commit()
        return equipo_schema.dump(equipo), 201


class Equipos(Resource):
    def get(self):
        equipos = db.session.query(EquipoModel).all()
        return equipo_schema.dump(equipos, many=True)

    def post(self):
        equipo = equipo_schema.load(request.get_json())
        db.session.add(equipo)
        db.session.commit()
        return equipo_schema.dump(equipo), 201
