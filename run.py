from app import app
from db import db

@app.before_first_request # Remember
def create_tables():
    db.create_all()

db.init_app(app)
