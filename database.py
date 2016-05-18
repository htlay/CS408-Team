#!/usr/bin/python

import MySQLdb

# Connect to database

# set up database
DB_HOST = "localhost"
DB_USER = "cs408_user"
DB_PW = "cs408"
DB_DB = "game"

# Open databse connection
db = MySQLdb.connect(DB_HOST, DB_USER, DB_PW, DB_DB)

