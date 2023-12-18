import json
import requests


def	data_requests(endpoint, params):

	response = requests.get(endpoint, params=params)

	if response.status_code == 200:
		return response.json()


def	get_ig_id(access_token):

	temp_data = {}

	temp_data = data_requests('https://graph.facebook.com/v16.0/me', {'access_token':access_token, 'fields':'accounts'})
	fb_id = temp_data['accounts']['data'][0]['id']

	temp_data = data_requests(f'https://graph.facebook.com/v16.0/{fb_id}', {'access_token':access_token, 'fields':'instagram_business_account'})
	ig_id = temp_data['instagram_business_account']['id']

	return (ig_id)


def	get_medias_and_comments(ig_id, access_token):

	medias = {}
	temp_data = {}

	temp_data = data_requests(f'https://graph.facebook.com/v16.0/{ig_id}/media', {'access_token':access_token, 'fields':''})
	medias = {f'media{str(i)}': {'id': id['id']} for i, id in enumerate(temp_data['data'])}

	for media_key, media_value in medias.items():

		temp_data = data_requests(f'https://graph.facebook.com/v16.0/{media_value["id"]}/comments', {'access_token':access_token, 'fields':''})
		media_value['comments'] = {}

		for i, comment in enumerate(temp_data['data']):

			media_value['comments'][f'{i}'] = comment

	return(medias)
