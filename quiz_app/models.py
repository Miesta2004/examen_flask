from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(300))
    option1 = db.Column(db.String(100))
    option2 = db.Column(db.String(100))
    option3 = db.Column(db.String(100))
    option4 = db.Column(db.String(100))
    correct = db.Column(db.Integer)  # 1-4
    difficulty = db.Column(db.Float)  # 0.5-2.0
    time_limit = db.Column(db.Integer)  # Secondes