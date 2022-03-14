import pytest
import unittest
from github_functions import *;


class test_GitHub_functions(unittest.TestCase):

	def test_create_gist(self):
		## Test #1
		fileName = "./text_files/testFile1.txt"
		gistId = str(create_gist(fileName)) ## First create a gist Id, we know will exist.
		inList = False
		gist_ids = get_all_gists_ids() ## Then see if it exists, after making a new call.
		for x in gist_ids:
			x = str(x)
			if x == gistId:
				inList = True
		delete_gist(gistId); ## delete the temporary generated list.
		self.assertTrue(True,"New added gist ID did not exist , in retrived lists ID.")
		## Test #2
		fileName = "./text_files/testFile2.txt"
		gistId = str(create_gist(fileName)) ## First create a gist Id, we know will exist.
		inList = False
		gist_ids = get_all_gists_ids() ## Then see if it exists, after making a new call.
		for x in gist_ids:
			x = str(x)
			if x == gistId:
				inList = True
		delete_gist(gistId); ## delete the temporary generated list.
		self.assertTrue(True,"New added gist ID did not exist , in retrived lists ID.")




unittest.main()

