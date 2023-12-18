import os
import json
from utils import graph_data
from utils import oai_treatment


ACCESS_TOKEN = str(os.getenv("GRAPH_ACCESS_TOKEN"))


if __name__ == "__main__":

	account = {}

	ig_id = graph_data.get_ig_id(ACCESS_TOKEN)
	account['medias'] = graph_data.get_medias_and_comments(ig_id, ACCESS_TOKEN)

	oai_treatment.fill_comment_sentiment(account)
	oai_treatment.fill_media_sentiment(account)

	with open('./outputs/output_test.json', 'w') as f:
		json.dump(account, f, indent=4)
