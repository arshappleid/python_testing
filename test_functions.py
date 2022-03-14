## This file is supposed to carry out all the tests for our functions in functions.py file.


from functions import *;

def test_add():
	## this will test our simple add funciton.
	assert add(3,4) == 7
	assert add(6,4) == 10
	assert add(1,2) == 3
	assert add(74,11) == 85

def test_add_Strings():
	## we expect our original function to add a 1 space between the two strings given.
	str1 = "HELLO"
	str2 = "WORLD"
	assert add_Strings(str1, str2) == "HELLO WORLD"

	str1 = "good"
	str2 = "apple"
	assert add_Strings(str1, str2) == "good apple"

	str1 = "!@#$%^&"
	str2 = "*()"
	assert add_Strings(str1, str2) == "!@#$%^& *()"

def test_write_file():
	fileName = "./text_files/testFile1.txt"
	writeStr = "UBC IRP Student QA!"
	write_file(writeStr, fileName)
	assert read_file(fileName) == writeStr

	fileName = "./text_files/testFile2.txt"
	writeStr = "How was your Day"
	write_file(writeStr, fileName)
	assert read_file(fileName) == writeStr
