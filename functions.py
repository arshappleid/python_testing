## all the functions that we create, or would want to use for our project. Would be added here.
import math


def add(num1, num2): ## will return int type
	return (num1+num2);

def add_Strings(str1,str2): ## will return string
	return (str1+" "+str2);

def read_file(fileName):
	## will return the data in a file as a string
	try:
		file = open(fileName)
		line = myfile.readline()
		data = "";
		while line:
			data += myline
			line = myfile.readline()
		file.close()
	except:
		return "Could not read from file"

def write_file(writeStr , fileName):
	## this will write the writeStr to the fileName. 
	## here fileName is supposed to be be the dynamic address to the file.
	try:
		file = open(fileName)
		file.write(writeStr)
		file.close()
	except:
		print("Could not write to file.")








	
