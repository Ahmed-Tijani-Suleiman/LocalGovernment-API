import sys
from flask import Flask, request, jsonify, make_response, abort
from flask_sqlalchemy import SQLAlchemy
from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from flask_moment import Moment
from flask_migrate import Migrate
from sqlalchemy.orm import relationship, backref
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine import URL 


app = Flask(__name__)
moment = Moment(app)
app.config.from_object('config')
db = SQLAlchemy(app)
db.Model.metadata.reflect(db.engine)
migrate = Migrate(app, db)

## MODELS
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



## CONTROLLERS ##

@app.route('/api/state', methods=['GET'])
def index():
    get_todos = State.query.order_by('name').all()
    state_schema = StateSchema(many=True)
    todos = state_schema.dump(get_todos)
    return make_response(jsonify({"state": todos}))

@app.route('/api/lga', methods=['GET'])
def index1():
    get_todos = LGA.query.join(State).all()
    value=[]
    for data in get_todos:
        value.append({
     "id": data.id,
     "name": data.name,
     "state_id": data.state_id,
    
        })
    return jsonify(value)


@app.route('/api/state/<id>', methods=['GET'])
def get_state_by_id(id):
    get_state = State.query.get(id)
    state_schema = StateSchema()
    state = state_schema.dump(get_state)
    return make_response(jsonify({"todo":state}))


@app.route('/api/state/<id>', methods=['DELETE'])
def delete_state_by_id(id):
    get_todo = State.query.get(id)
    db.session.delete(get_todo)
    db.session.commit()
    return make_response("", 204)


@app.route('/api/state', methods=['POST'])
def create_state():
    error = False
    body = {}
    try:
        description = request.get_json()['name']
        todo = State(name=description)
        db.session.add(todo)
        db.session.commit()
        body['name'] = todo.name
    except:
        error = True
        db.session.rollback()
        print(sys.exc_info())
    finally:
        db.session.close()
    if error:
        abort(500)
    else:
        return jsonify(body)

@app.route('/api/lga', methods=['POST'])
def create_lga():
    error = False
    body = {}
    try:
        description = request.get_json()['name']
        desc = request.get_json()['state_id']
        todo = LGA(name=description, state_id=desc)
        db.session.add(todo)
        db.session.commit()
        body['name'] = todo.name
        body['state_id'] = todo.state_id
    except:
        error = True
        db.session.rollback()
        print(sys.exc_info())
    finally:
        db.session.close()
    if error:
        abort(500)
    else:
        return jsonify(body)


@app.route('/api/lga/<stateId>', methods=['GET'])

def get_lga_by_id(stateId):
    get_todos = State.query.get(stateId)
    get_todos1 = LGA.query.join(State).filter(LGA.state_id==get_todos.id).all()

    value=[]
    for i in get_todos1:
    
        value.append({
        "id": i.id,
        "name": i.name,
        "state_id": i.state_id
        })
    
    return jsonify(value)


if __name__ == '__main__':
    app.run(debug=True)