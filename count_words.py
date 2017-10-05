import os,json
def countPronouns():
	pronouns = {'han':0,'hon':0,'hen':0,'den':0,'det':0,'denna':0,'denne':0}
	for twitterFile in os.listdir('./data'):
		with open('./data/' + twitterFile,'rw') as file:
			for line in file:
				if not line.isspace():
					data = json.loads(line)
					if not data['retweeted']:
						words = data['text'].lower().split()
						for word in words:
							if word in pronouns:
								pronouns[word]+=1
	return(pronouns)
