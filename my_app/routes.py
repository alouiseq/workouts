from flask import render_template, request, jsonify
from my_app import create_app, db
from my_app.models import WorkoutPlan  # Import your models here

app = create_app()

# Define a route for the home page
@app.route('/')
def home():
    return "Welcome to the Workout Planner!"

# Define a route to list all workout plans
@app.route('/workout_plans')
def list_workout_plans():
    workout_plans = WorkoutPlan.query.all()
    return render_template('workout_plans.html', workout_plans=workout_plans)

# Define a route to create a new workout plan
@app.route('/workout_plans/create', methods=['POST'])
def create_workout_plan():
    # Process the data from the request and create a new workout plan
    # (You'll need to implement this logic)

    # Example:
    # plan_name = request.form.get('name')
    # new_plan = WorkoutPlan(name=plan_name)
    # db.session.add(new_plan)
    # db.session.commit()

    return jsonify({'message': 'Workout plan created successfully!'})

# Define a route to view a specific workout plan
@app.route('/workout_plans/<int:plan_id>')
def view_workout_plan(plan_id):
    plan = WorkoutPlan.query.get_or_404(plan_id)
    return render_template('workout_plan.html', plan=plan)

# ... Add more routes as needed

# if __name__ == '__main__':
#     app.run()

