from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

import os


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:rawnak88@localhost:5432/test"
db = SQLAlchemy(app)
migrate = Migrate(app, db)
# app.config.from_object(os.environ['APP_SETTINGS'])
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# from models import Loading
class Loading(db.Model):
    __tablename__ = 'floor_loading'

    id = db.Column(db.Integer, primary_key=True)
    loading_type = db.Column(db.String())
    loading = db.Column(db.String)

    def __init__(self, loading_type, loading):
        self.loading_type = loading_type
        self.loading = loading

    def __repr__(self):
        return '<id {}>'.format(self.id)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/floor_loading', methods=['POST', 'GET'])
def handle_loading():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            new_loading = Loading(loading_type=data['loading_type'], loading=data['loading'])
            db.session.add(new_loading)
            db.session.commit()
            return {"message": f"loading {new_loading.loading_type} has been created successfully."}
        else:
            return {"error": "The request payload is not in JSON format"}

    elif request.method == 'GET':
        floor_loading = Loading.query.all()
        results = [
            {
                "loading_type": loading.loading_type,
                "loading": loading.loading
            } for loading in floor_loading]

        return {"count": len(results), "loading": results}

if __name__ == '__main__':
    app.run()