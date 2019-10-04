import json
import random
import re

class Util:

    # Class is created for the files to load only once.

    def __init__(self, constantJSON='data/constants.json'):
        with open(constantJSON, 'r', encoding='utf8') as file:
            constants = json.load(file)

        self.keywords = constants["triggers"]
        self.quotes = constants["quotes"]


    def is_keyword_mentioned(self, text):
        """ Checks if the trigger words to call the bot are present in the string """

        for keyword in self.keywords:

            # Do a case insensitive search
            if re.search(keyword, text, re.IGNORECASE):
                return True

        return False

    def get_random_quote(self):
        """ Returns random quote from quotes file"""

        return random.choice(self.quotes)