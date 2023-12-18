import os
import openai


OAI_ORGANIZATION_ID = str(os.getenv("OAI_ORGANIZATION_ID"))
OAI_SECRET_KEY_ACCESS = str(os.getenv("OAI_SECRET_KEY_ACCESS"))

openai.organization = OAI_ORGANIZATION_ID
openai.api_key = OAI_SECRET_KEY_ACCESS


def resume_comments(comments):

	completion = openai.ChatCompletion.create(
		model="gpt-3.5-turbo",
		max_tokens=20, #40
		temperature=0.3,
		messages=[
		{"role": "system", "content": "Your role is to resume the main topics of a list of comments in input. You must respond with a few words without introduction"},
		{"role": "user", "content": f"analyse this list of comments : {comments}"}
	]
	)
	return(completion["choices"][0]['message']['content'])

def	fill_media_sentiment(account):

	for media_key, media_value in account['medias'].items():

		comments = []

		for comment_key, comment_value in media_value['comments'].items():

			comments.append(comment_value['text'])

		media_value['media_sentiment'] = resume_comments(comments)


def	analyse_comment(comment):

	completion = openai.ChatCompletion.create(
		model="gpt-3.5-turbo",
		max_tokens=15, #25
		temperature=0.3,
		messages=[
		{"role": "system", "content": "You are a sentiment analyst. Your role is to analyse the sentiment in the comment in input. You must respond with a few words without introduction."},
		{"role": "user", "content": f"what's the sentiment in it : {comment}"}
	]
	)
	return(completion["choices"][0]['message']['content'])

def fill_comment_sentiment(account):

	for media_key, media_value in account['medias'].items():

		for comment_key, comment_value in media_value['comments'].items():

			comment_value['sentiment'] = analyse_comment(comment_value['text'])
