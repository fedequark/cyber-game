from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Scenario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    situations = db.relationship('Situation', backref='scenario', lazy=True)

class Situation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(255), nullable=False)
    scenario_id = db.Column(db.Integer, db.ForeignKey('scenario.id'), nullable=False)
    options = db.relationship('Option', backref='situation', lazy=True)

class Option(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(255), nullable=False)
    situation_id = db.Column(db.Integer, db.ForeignKey('situation.id'), nullable=False)
    next_situation_id = db.Column(db.Integer, db.ForeignKey('situation.id'), nullable=True)
    conclusion = db.Column(db.String(255), nullable=True)
