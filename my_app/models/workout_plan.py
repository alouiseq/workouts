from my_app import db

class WorkoutPlan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)

    # Relationships
    exercises = db.relationship('Exercise', secondary='workout_plan_exercise')
