from my_app.models import MuscleGroup
from my_app import db

main_muscle_groups = [
    MuscleGroup(name="Chest"),
    MuscleGroup(name="Triceps"),
    MuscleGroup(name="Biceps"),
    MuscleGroup(name="Back"),
    MuscleGroup(name="Abs"),
    MuscleGroup(name="Legs"),
    MuscleGroup(name="Glutes"),
]

for muscle_group in main_muscle_groups:
    db.session.add(muscle_group)

db.session.commit()

