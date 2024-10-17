import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

sys.path.append(os.path.dirname(SCRIPT_DIR))
import pyodbc
from util.db_property_util import DBPropertyUtil

class DBConnUtil:
    @staticmethod
    def get_db_conn():
        conn_str = DBPropertyUtil.get_db_conn_str()
        return pyodbc.connect(conn_str)

