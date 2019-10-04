import os
import time

import praw
from prawcore import PrawcoreException
from utils import Util
import logging as log


class RedditBot:

    def __init__(self):
        self.LOCK_FILE = 'lockfile.lock'

        log.basicConfig(filename='bot_logging.log', level=log.INFO
                        )

        self.util = Util()

    def _comment_responder(self):
        reddit = praw.Reddit('bot1')

        # Yeezus bot only needs one sub, FOOL!
        subreddit_name = "Kanye"
        subreddit = reddit.subreddit(subreddit_name)

        for comment in subreddit.stream.comments(skip_existing=True):

            if os.path.isfile(self.LOCK_FILE):

                # Parse the comment
                text = comment.body
                # Checks if the keyword is in the comment.
                keyword_mentioned_bool = self.util.is_keyword_mentioned(text)

                # If a triggerword is in the string...
                if keyword_mentioned_bool:
                    response_string = self.util.get_random_quote()

                    try:
                        comment.reply(response_string)
                    except praw.exceptions.APIException as e:
                        log.info(str(e))


            else:
                return

    def run(self):
        with open(self.LOCK_FILE, 'w'): pass
        print("Lock file made (presumably)")
        log.info("STARTED")
        # remove to kill

        self.run_cont()

    def run_cont(self):

        try:
            self._comment_responder()
        except PrawcoreException as e:
            log.info(e)
            log.info("Sleeping for 1 minute...")
            time.sleep(60)
            self.run_cont()
        except KeyboardInterrupt:
            raise
        except:
            log.info("Something random happened, sleeping for 10 sec.")
            time.sleep(60)
            self.run_cont()

if __name__ == '__main__':
    RedditBot().run()
