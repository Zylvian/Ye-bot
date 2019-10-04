

from fetching import Fetcher
import logging as log
from wikibot import RedditBot
from constants import  Constants
from parse_helper import NameParser

#names = ["grandpa garp", "luccy", "asdasdasdasdasd", "future king of pirates"]
#names = ["sugoii"]
#names = ["Luffy","Marco"]

# Parse the comment
text = "Btw, I created a bot that takes excerpts of the One Piece wiki and neatly arranges them. Just write any name like ::Shiki:: or ::Bakkins:: in double colons. :)"
# Finds all text within brackets.
parser = NameParser()
names = parser.parse_text(text)
print(names)

# Did Luffy meet Marco pre-war?

#log.basicConfig(filename='bot_logging.log', level=log.INFO)

const = Constants()

pages = Fetcher().get_wiki_info(const.sub_to_wiki("onepiece"),names)
print(pages)
response_string = RedditBot().create_response_string(pages)

print(response_string)
log.debug("Yeehaw")
# asdasd

#print(Fetcher().fetch_summary())