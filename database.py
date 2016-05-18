#!/usr/bin/python

import MySQLdb
import board

# Connect to database

# set up database
DB_HOST = "localhost"
DB_USER = "cs408_user"
DB_PW = "cs408"
DB_DB = "game"

# Open databse connection
db = MySQLdb.connect(DB_HOST, DB_USER, DB_PW, DB_DB)

# prepare cursor object
cursor = db.cursor()

def sort():

	# get names
	sql = "SELECT name FROM score"
	cursor.execute(sql)
	name = cursor.fetchall()

	# convert to values
	nameList = []
	for i in name:
		nameList.append(i[0])

	# get scores
	sql = "SELECT score FROM score"
	cursor.execute(sql)
	score = cursor.fetchall()

	# convert to values
	scoreList = []
	for i in score:
		scoreList.append(i[0])

	# map score to id
	idList = list(xrange(len(scoreList)))
	rankingScore = dict(zip(idList, scoreList))

	# map name to id
	rankingName = dict(zip(idList, nameList))

	# sort by score
	sorted(rankingScore.values())

	print rankingScore
	print rankingName

	for i in range(0, len(rankingName)):

		sql = "UPDATE score SET rank = '%d' WHERE name = '%s' AND score = '%d'" % (i + 1, rankingName[i], rankingScore[i])
		cursor.execute(sql)

def addScore(name, score):
	# store new score
	sql = "INSERT INTO score (rank, name, score) VALUES (0, '%s', '%d')" % (name, score)
	cursor.execute(sql)

	# sort database
	sort()

def resetScore():

	# delete table
	cursor.execute("DROP TABLE IF EXISTS score")

	# add empty table
	sql = "CREATE TABLE score (rank int, name VARCHAR(3), score int)"
	cursor.execute(sql)

def displayScore():

	# get ranks
	sql = "SELECT rank FROM score"
	cursor.execute(sql)
	rankList = cursor.fetchall()

	# get names
	sql = "SELECT name FROM score"
	cursor.execute(sql)
	nameList = cursor.fetchall()

	# get scores
	sql = "SELECT score FROM score"
	cursor.execute(sql)
	scoreList = cursor.fetchall()

	# print
	if not rankList:
		print "No Scores"
	else:
		print "Rank: %d\nName: %s\nScore: %s\n" % (rankList[0][0], nameList[0][0], scoreList[0][0])
		print "Rank: %d\nName: %s\nScore: %s\n" % (rankList[1][0], nameList[1][0], scoreList[1][0])

resetScore()
addScore("AAA", 0)
addScore("AAA", 1)
displayScore()

# commit changes
db.commit()

# disconnect from server
db.close()