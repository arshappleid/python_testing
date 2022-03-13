import gistyc
import json
from functions import *

github_api="https://api.github.com"
github_api_token = "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"
## forming a request url for gists. 

filepath = "./functions.py"

def create_gist(filepath):
	## will return the gist ID, of the new gist created.
	try:
		gist_api = gistyc.GISTyc(auth_token=github_api_token)
		response_data = gist_api.create_gist(file_name=filepath)
		print("New gist created :\n")
		return response_data['id']
	except Exception as e:
		print("Unable to create a new gist , error occured .\n")
		print(e)


def update_gist(filepath,gistId):
	try:
		gist_api = gistyc.GISTyc(auth_token=github_api_token)
		response_data = gist_api.update_gist(file_name=filepath, gist_id = gistId)
		print("Gist Updated :\n")
		return response_data
	except Exception as e:
		print("Unable to update gist , error occured .\n")
		print(e)

def delete_gist(filepath):
	try:
		gist_api = gistyc.GISTyc(auth_token=github_api_token)
		response_data = gist_api.delete_gist(file_name=filepath)
		print("Gist deleted :\n")
		return response_data
	except Exception as e:
		print("Unable to delete gist , error occured .\n")
		print(e)
	
def get_gists_ids():
	try:
		gist_api = gistyc.GISTyc(auth_token=github_api_token)
		response_data = gist_api.get_gists()
		print("Gist deleted :\n")
		ids = []
		for x in response_data:
			ids.append(x['id'])
		return ids
	except Exception as e:
		print("Unable to get gists , error occured .\n")
		print(e)

	



