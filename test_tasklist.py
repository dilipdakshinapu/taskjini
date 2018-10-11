# test_tasklist.py

import os
import unittest
import json
from app import create_app, db


class TaskListTestCase(unittest.TestCase):
    """
    This class represents tasklist testcase
    """

    def setUp(self):
        """
        Define test variables
        initialize the app
        """
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        self.tasklist = {"title": "sample task", "description": "test task", "priority": "high", "status": 0}

        # Bind the app to current context
        with self.app.app_context():
            # create all the tables
            db.create_all()

    def test_tasklist_create(self):
        """
        Test case for create
        """
        res = self.client().post('/tasks', data=self.tasklist)
        self.assertEqual(res.status_code, 201)
        self.assertIn('sample', str(res.data))

    def test_api_can_get_all_tasklists(self):
        """Test API can get a tasklist (GET request)."""
        res = self.client().post('/tasks', data=self.tasklist)
        self.assertEqual(res.status_code, 201)
        res = self.client().get('/tasks')
        self.assertEqual(res.status_code, 200)
        self.assertIn('sample', str(res.data))

    def test_api_can_get_tasklist_by_id(self):
        """Test API can get a single task by using it's id."""
        rv = self.client().post('/tasks', data=self.tasklist)
        self.assertEqual(rv.status_code, 201)
        result_in_json = json.loads(rv.data.decode('utf-8').replace("'", "\""))
        result = self.client().get(
            '/task/{}'.format(result_in_json["task"]['id']))
        self.assertEqual(result.status_code, 200)
        self.assertIn('sample', str(result.data))

    def test_tasklist_can_be_edited(self):
        """Test API can edit an existing tasklist. (PUT request)"""
        rv = self.client().post(
            '/tasks',
            data={'title': "beautiful", "description": "ooty", "status": 0, "priority": "low"})
        self.assertEqual(rv.status_code, 201)
        rv = self.client().put(
            '/task/1',
            data={
                "status": 1
            })
        self.assertEqual(rv.status_code, 200)
        results = self.client().get('/task/1')
        self.assertIn('beautiful', str(results.data))

    def test_tasklist_deletion(self):
        """Test API can delete an existing task. (DELETE request)."""
        rv = self.client().post(
            '/tasks',
            data={'title': "beautiful", "description": "ooty", "status": 0, "priority": "low"})
        self.assertEqual(rv.status_code, 201)
        res = self.client().delete('/task/1')
        self.assertEqual(res.status_code, 200)

    def tearDown(self):
        """teardown all initialized variables."""
        with self.app.app_context():
            # drop all tables
            db.session.remove()
            db.drop_all()


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
