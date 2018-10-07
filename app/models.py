# app/models.py

from app import db


class TaskList(db.Model):
    """
    Table structure for the task list
    """

    __tablename__ = "tasks"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    description = db.Column(db.Text)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(
        db.DateTime,
        default = db.func.current_timestamp(),
        onupdate = db.func.current_timestamp()
    )

    def __init__(self):
        """
        Initialize the object with title
        """
        self.title = title

    def save(self):
        db.session.add(self)
        db.session.commit()

    