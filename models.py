
from flask import Flask, request, jsonify, make_response, abort
from flask_sqlalchemy import SQLAlchemy
from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from flask_moment import Moment
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy



class State(db.Model):
    __table__ = db.Model.metadata.tables['state']
class LGA(db.Model):
    __table__ = db.Model.metadata.tables['local_government']

class StateSchema(SQLAlchemySchema):
    class Meta(SQLAlchemySchema.Meta):
        model = State
        sqla_session = db.session

    id = fields.Number(dump_only=True)
    name = fields.String(required=True)

class LGASchema(SQLAlchemySchema):
    class Meta(SQLAlchemySchema.Meta):
        model = LGA
        sqla_session = db.session

    id = fields.Number(dump_only=True)
    name = fields.String(required=True)
    state_id = fields.Nested(StateSchema, many=True)
