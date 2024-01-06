from datetime import datetime
from my_app import db

class UserProgress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercise.id'))
    # current_weight in pounds (lbs)
    current_weight = db.Column(db.Integer, nullable=True)
    current_reps = db.Column(db.Integer, nullable=True)
    # current_duration in seconds (s)
    current_duration = db.Column(db.Integer, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
