import json

list = open(r"list", "r")
array = list.readlines()
langs = []
codes = []
i = 0
for x in array:
	langs.append(x.split('\t')[0])
	codes.append(x.split('\t')[1])
codes = [x.replace('\n', '') for x in codes]
lang_dict = dict(zip(codes, langs))
with open('langs.json', 'w') as fp:
    json.dump(lang_dict, fp, sort_keys=True, indent=4)