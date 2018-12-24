import time
from instagram import InstagramScraper


class SleeperAgent:

    def __init__(self):
        self.agent_shutdown = False

    @staticmethod
    def identify_last_hashtag(textexcerpts):
        for x in textexcerpts[0]:
            string = x
            hashtags = tuple([i for i in string.split() if i.startswith("#")])
        return hashtags

    def parse_data(self, data):
        dispatcher = {'#alpha': self.alpha,
                      '#beta': self.beta,
                      '#gamma': self.gama,
                      'default': self.sleep}

        selected_option = data
        try:
            dispatcher[selected_option]()
        except KeyError:
            selected_option = 'default'
            dispatcher[selected_option]()

    def alpha(self):
        print('alpha')
        time.sleep(5)

    def beta(self):
        print('beta')
        time.sleep(5)

    def gama(self):
        print('gama')
        time.sleep(5)

    def sleep(self):
        print("Let's sleep")
        time.sleep(60*60*24)

    def main_loop(self, connection):
        while not self.agent_shutdown:
            k = InstagramScraper()
            results = k.get_texts_from_posts(connection)
            data = self.identify_last_hashtag(results)
            currentorder = data[0]
            self.parse_data(currentorder)
