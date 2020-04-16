# Python Translator
A small Python script to google translate files or strings
1. 'languages.py' creates a json file of language codes and language names from a table I found online
1. 'translate.py' creates a link from input, makes GET request to mobile version of translate.google.com and using BeautifulSoup parses the output

* Usage: `python3 translate.py <Source Language> <Destination Language> <String>`
* Usage example: `python3 translate.py English Swedish "I love playing footbal"`
`$ Jag älskar att spela fotboll`

## Features to add:
* read from file
* write to file
