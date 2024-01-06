from my_app import db

class WorkoutPlanExercise(db.Model):
    workout_plan_id = db.Column(db.Integer, db.ForeignKey('workout_plan.id'), primary_key=True)
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercise.id'), primary_key=True)
