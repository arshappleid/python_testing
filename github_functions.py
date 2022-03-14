import gistyc
import json
from functions import *

github_api="https://api.github.com"
json_file = open('login_info.json','r')
github_api_token = json.load(json_file)['github_api_token']
## forming a request url for gists. 

filepath = "./text_files/testFile1.txt"

def create_gist(filepath):
	## will return the gist ID, of the new gist created.
	try:
		# Initiate the GISTyc class with the auth token
		gist_api = gistyc.GISTyc(auth_token=github_api_token)
		# get the gist information , of the gist created.
		response_data = gist_api.create_gist(file_name=filepath)
		return response_data['id']
	except Exception as e:
		print("Unable to create a new gist , error occured .")
		print(e)


def update_gist(filepath,gistId):
	try:
		gist_api = gistyc.GISTyc(auth_token=github_api_token)
		# This time , we need to give the fileName , and the gistId . Just in case there is 
		response_data = gist_api.update_gist(file_name=filepath, gist_id = gistId)
		print("Gist Updated :")
		return response_data
	except Exception as e:
		print("Unable to update gist , error occured .")
		print(e)

def delete_gist(gistID):
	try:
		gist_api = gistyc.GISTyc(auth_token=github_api_token)
		## give the api , the ID of the gist that we want to delete.
		response_data = gist_api.delete_gist(gist_id = gistID)
		print("Gist deleted :")
		return response_data
	except Exception as e:
		print("Unable to delete gist , error occured .")
		print(e)
	
def get_all_gists_ids():
	try:
		# Initiate the GISTyc class with the auth token
		gist_api = gistyc.GISTyc(auth_token=github_api_token)
		# Get a list of GISTs
		print("trying to get gist ids..")
		response_data = gist_api.get_gists()
		print("got all gist ids...")
		ids = []
		for x in response_data:
			ids.append(x['id'])
		return ids
	except Exception as e:
		print("Unable to get gists , error occured .")
		print(e)

def delete_all_gists():
	try:
		listIds = get_all_gists_ids()
		for x in listIds:
			print(x +" deleted")
			delete_gist(x);
		return ("All gists deleted.")
	except Exception as e:
		print("Unable to delete all gists, error occured .")
		print(e)

	



