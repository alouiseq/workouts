from my_app import db
from sqlalchemy import Enum

class ExerciseMuscleGroup(db.Model):
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercise.id'), primary_key=True)
    muscle_group_id = db.Column(db.Integer, db.ForeignKey('muscle_group.id'), primary_key=True)
    target_type = db.Column(Enum('primary', 'secondary', name='target_type'), nullable=False)

