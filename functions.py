## all the functions that we create, or would want to use for our project. Would be added here.
import math
import json


def add(num1, num2): ## will return int type
	return (num1+num2);

def add_Strings(str1,str2): ## will return string
	return (str1+" "+str2);

def read_file(fileName):
	## will return the data in a file as a string
	try:
		file = open(fileName,'r')
		line = file.readline()
		data = "";
		while line:
			data += line
			line = file.readline()
		file.close()
		return data;
	except Exception as e:
		print(e)
		return "Could not read from file"

def write_file(writeStr , fileName):
	## this will write the writeStr to the fileName. 
	## here fileName is supposed to be be the dynamic address to the file.
	try:
		if(type(writeStr) is dict):
			with open(fileName, 'w') as json_file:
  				json.dump(writeStr, json_file)
			json_file.close();
		else:
			file = open(fileName,'w')
			file.write(writeStr)
			file.close()
	except Exception as e:
		print(e)
		print("Could not write to file.")








	
