from datetime import datetime
from my_app import db

class ExerciseHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_progress_id = db.Column(db.Integer, db.ForeignKey('user_progress.id'))
    # weight in pounds (lbs)
    weight = db.Column(db.Integer, nullable=True)
    reps = db.Column(db.Integer, nullable=True)
    # duration in seconds (s)
    duration = db.Column(db.Integer, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

