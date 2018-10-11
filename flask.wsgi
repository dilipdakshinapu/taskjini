# flask.wsgi

import sys
import os
sys.path.insert(0,"/home/ubuntu/taskmgr")
from instance.settings import DATABASE_URI, TEST_DATABASE_URI
os.environ["DATABASE_URI"] = DATABASE_URI
os.environ["TEST_DATABASE_URI"] = TEST_DATABASE_URI

from app import create_app
application = create_app(config_name="development")
