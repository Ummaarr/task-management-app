from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask app
app = Flask(__name__)

# Database configuration (SQLite database)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Task model (table structure)
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique task ID
    title = db.Column(db.String(100), nullable=False)  # Task title
    description = db.Column(db.String(200))  # Task description

# API route to add a new task
@app.route('/add_task', methods=['POST'])
def add_task():
    data = request.json  # Get JSON data from request
    new_task = Task(title=data['title'], description=data['description'])
    db.session.add(new_task)
    db.session.commit()
    return jsonify({"message": "Task added successfully!"})

# API route to get all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()  # Get all tasks from the database
    task_list = [{"id": task.id, "title": task.title, "description": task.description} for task in tasks]
    return jsonify(task_list)

# Entry point for running the app
if __name__ == '__main__':
    # Create database tables within the application context
    with app.app_context():
        db.create_all()
        print("Database initialized successfully!")
        
    app.run(debug=True)
