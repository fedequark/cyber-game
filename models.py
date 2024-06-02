from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Scenario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(255), nullable=False)
    options = db.relationship('Option', backref='scenario', lazy=True)

class Option(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(255), nullable=False)
    scenario_id = db.Column(db.Integer, db.ForeignKey('scenario.id'), nullable=False)
    next_scenario_id = db.Column(db.Integer, db.ForeignKey('scenario.id'), nullable=True)
    conclusion = db.Column(db.String(255), nullable=True)