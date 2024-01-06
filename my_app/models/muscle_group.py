from my_app import db

class MuscleGroup(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    parent_id = db.Column(db.Integer, nullable=True)

    exercises = db.relationship('Exercise', secondary='exercise_muscle_group')
