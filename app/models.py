# app/models.py

import enum
from app import db

class Priorities(enum.Enum):
    """
    Fixed values for the priorities
    """
    low = "Low"
    medium = "Medium"
    high = "High"


class TaskList(db.Model):
    """
    Table structure for the task list
    """

    __tablename__ = "tasks"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    description = db.Column(db.Text)
    priority = db.Column(db.Enum(Priorities))
    status = db.Column(db.Boolean, default=False)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(
        db.DateTime,
        default = db.func.current_timestamp(),
        onupdate = db.func.current_timestamp()
    )

    def __init__(self, title, description, status, priority):
        """
        Initialize the object with title
        """
        self.title = title
        self.description = description
        self.priority = priority
        self.status = status

    def save(self):
        db.session.add(self)
        db.session.commit()