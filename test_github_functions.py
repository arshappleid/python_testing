import pytest
from github_functions import *;


def test_create_gist():
	fileName = "./text_files/testFile1.txt"
	gistId = create_gist(fileName)
	inList = False
	gist_ids = get_gists_ids()
	for x in gist_ids:
		if(x == gistId):
			inList = True

	assert inList == True;

	fileName = "./text_files/testFile2.txt"
	gistId = create_gist(fileName)
	inList = False
	gist_ids = get_gists_ids()
	for x in gist_ids:
		if(x == gistId):
			inList = True

	assert inList == True;



