# import praw
# import re
#
# from fetching import Fetcher
#
# reddit = praw.Reddit('bot1')
#
#
# """class Fetcher:
#
#     def __init__(self):
#         #self._apistartstring = ''
#         test = {("xxxx","xdd"):"asd"}
#         self._getim = test.get("xxxx")
#         self._querystartlink = self._getim + " MUSTAFA"
#
#         #self._endlink = self._startlink+'query&'
#
#         # '&prop=info&inprop=url&generator=allpages&gapfrom='
#
#     def testing(self, api_string):
#         self._apistartstring = api_string
#         print(self._querystartlink)
#
#
# Fetcher().testing("xd")"""
#
# """look for [[cardname]]s in text and collect them"""
# names = [Fetcher("asd")]
# text = "i want to --dance-- boy and also [[xdddd]] and [asd[adasdasd]]"
#
# if Fetcher("asd") in names:
#     print("the fuuuck")
#
# for name in re.finditer(r'\\?\-\\?\-([^\]\\]{1,30})\\?\-\\?\-', text):
#     name = name.group(1)
#     if name not in names:
#         names.append(name)
#     else:
#         #log.info("duplicate name: %s", name)
#         print("ah fuck")
#
# print(names)
#
# """subreddit = reddit.subreddit("onepiece+memepiece+Rickandorty")
#
# for comment in subreddit.stream.comments(skip_existing=True):
#     print("yay")
#     print(comment.subreddit.display_name)
#     print("ay")
#     print(comment.subreddit.fullname)
#     print("way")
#     print(comment.subreddit.id)"""

import itertools

dictlol = {
"sub_to_wiki":{
    "rickandmorty":"rickandmorty",
    "onepiece":["onepiece","memepiece"],
    "gameofthrones": "gameofthrones"
  }
}

listman = dictlol["sub_to_wiki"].values()
print(list(itertools.chain.from_iterable(listman)))
