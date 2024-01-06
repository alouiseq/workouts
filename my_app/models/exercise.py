from my_app import db
from sqlalchemy import Enum

class Exercise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    weight_type = db.Column(Enum('free', 'body', 'machine', name='weight_type'), nullable=False)

    # Relationships
    workout_plans = db.relationship('WorkoutPlan', secondary='workout_plan_exercise')
    muscle_groups = db.relationship('MuscleGroup', secondary='exercise_muscle_group')

