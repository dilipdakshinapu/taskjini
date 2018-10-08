# app/views.py

from flask_restful import reqparse, Resource, fields, marshal
from app import db
from app.models import TaskList

parser = reqparse.RequestParser()
parser.add_argument("title",location=('json', 'args', 'headers', 'form'))
parser.add_argument("description", location=('json', 'args', 'headers', 'form'))
parser.add_argument("priority", location=('json', 'args', 'headers', 'form'))
parser.add_argument("status", type=int, location=('json', 'args', 'headers', 'form'))

task_fields = {
    "title": fields.String,
    "description": fields.String,
    "priority": fields.String,
    "status": fields.Boolean,
    "id": fields.Integer,
}


class Task(Resource):
    """
    Retrieves single task and facilitates
    to delete it
    """
    def get(self, task_id):
        """
        retrieve single task based on task id
        """
        task = TaskList.query.get(int(task_id))
        return {"task": marshal(task, task_fields)}

    def delete(self, task_id):
        """
        Delete the task based on task id
        """
        task = TaskList.query.get(int(task_id))
        db.session.delete(task)
        db.session.commit()
        return {"task": marshal(task, task_fields)}

    def put(self, task_id):
        """
        Update task status based on task id
        """
        args = parser.parse_args()
        task = TaskList.query.get(int(task_id))
        task.status = bool(args["status"])
        db.session.commit()
        return {"task": marshal(task, task_fields)}


class TasksList(Resource):
    """
    Perform operations on multiple tasks
    """
    def get(self, priority=None):
        """
        Retrieve the list of tasks based on priority
        """
        if priority:
            tasks = TaskList.query.filter_by(priority=priority)
        else:
            tasks = TaskList.query.all()
        output = []
        for task in tasks:
            output.append({
                "id": task.id,
                "title": task.title,
                "description": task.description,
                "priority": task.priority,
                "status": task.status,
            })

        return {"tasks": marshal(output, task_fields)}

    def post(self):
        """
        Create a new task
        """
        args = parser.parse_args()
        task = TaskList(
            title = args["title"],
            description = args["description"],
            status = args["status"],
            priority = args["priority"],
        )
        task.save()
        return {"task": marshal(task, task_fields)}, 201
    


