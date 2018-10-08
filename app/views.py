# app/views.py

from flask_restful import reqparse, Resource
from app import db
from app.models import TaskList

parser = reqparse.RequestParser()
parser.add_argument("title")
parser.add_argument("description")
parser.add_argument("priority")
parser.add_argument("status")


class Task(Resource):
    """
    Retrieves single task and facilitates
    to delete it
    """
    def get(self, task_id):
        """
        retrieve single task based on task id
        """
        task = TaskList.query.filter_by(id=task_id)
        return task

    def delete(self, task_id):
        """
        Delete the task based on task id
        """
        task = TaskList.query.filter_by(id=task_id)
        db.session.delete(task)
        db.session.commit()
        return task

    def put(self, task_id):
        """
        Update task status based on task id
        """
        args = parser.parse_args()
        task = TaskList.query.filter_by(id=task_id)
        task.status = args["status"]
        db.session.commit()
        return task


class TasksList(Resource):
    """
    Perform operations on multiple tasks
    """
    def get(self, priority):
        """
        Retrieve the list of tasks based on priority
        """
        args = parser.parse_args()
        tasks = TaskList.query.filter_by(priority=args["priority"])
        return tasks

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
        return task
    


