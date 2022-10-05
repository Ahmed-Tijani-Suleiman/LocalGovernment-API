import os
import urllib
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database
connection_string = "DRIVER={ODBC Driver 17 for SQL Server};SERVER=PHEDETSLT33666\SQLEXPRESS;DATABASE=staff_db;Trusted_Connection=yes"

params = urllib.parse.quote_plus(connection_string)
SQLALCHEMY_DATABASE_URI = "mssql+pyodbc:///?odbc_connect=%s" % params
SQLALCHEMY_TRACK_MODIFICATIONS = False