import time
from instagram import InstagramScraper


class SleeperAgent:

    def __init__(self):
        self.agent_shutdown = False
        self.current_order = 'default'

    @staticmethod
    def identify_hashtag(textexcerpts):
        for x in textexcerpts[0]:
            string = x
            hashtags = tuple([i for i in string.split() if i.startswith("#")])
        return hashtags

    def identify_orders(self, hashtags):
        for x in hashtags:
            if x == '#alpha' or x == '#beta' or x == '#gama':
                self.current_order = x
                break
            else:
                self.current_order = 'default'
                pass

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
            data = self.identify_hashtag(results)
            self.identify_orders(data)
            self.parse_data(self.current_order)
