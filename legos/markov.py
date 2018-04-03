import logging
import markovify
from Legobot.Lego import Lego
from nltk.tokenize import RegexpTokenizer

logger = logging.getLogger(__name__)


class MarkovListener(Lego):
    def __init__(self, baseplate, lock, redis, *args, **kwargs):
        super().__init__(baseplate, lock)
        self.r = redis

    @staticmethod
    def listening_for(message):
        if message['metadata']['source_user'] is not None \
                and message['text'] is not None:
            return True

    def handle(self, message):
        # Exclude bot commands from model input
        if not message['text'].startswith("!"):
            self.append_text(message['metadata']['display_name'],
                             message['text'])

    def append_text(self, user, text):
        key = "text/" + user
        resp = self.r.rpush(key, text)
        logger.debug(resp)

    @staticmethod
    def get_name():
        return None

    @staticmethod
    def get_help():
        return None


class MarkovGenerator(Lego):
    def __init__(self, baseplate, lock, redis, *args, **kwargs):
        super().__init__(baseplate, lock)
        self.r = redis
        self.t = RegexpTokenizer(r'\w+')

    @staticmethod
    def listening_for(message):
        if message['text'] is not None:
            return message['text'].split()[0] == "!markov"

    def handle(self, message):
        opts = self.set_opts(message)
        try:
            key = "text/" + message['text'].split()[1]
        except IndexError as e:
            err = "MarkovGenerator called without specifying a user.\
                Usage: !markov username"
            logger.error(e)
            self.reply(message, err, opts)
        if self.r.exists(key):
            model = self.make_model(key)
            self.reply(message, model.make_sentence(), opts)
        else:
            self.reply(message, "No data exists for that user. Sorry.", opts)

    @staticmethod
    def set_opts(message):
        try:
            target = message['metadata']['source_channel']
            opts = {'target': target}
            return opts
        except IndexError:  # This should raise an error too
            logger.error('Could not identify message source in message: %s'
                         % str(message))

    def make_model(self, key):
        combined_model = None
        for msg in self.r.lrange(key, 0, -1):
            try:
                msg = " ".join(self.t.tokenize(msg)) + "."
                model = markovify.Text(msg, retain_original=False)
                if combined_model:
                    combined_model = markovify.combine(
                        models=[combined_model, model])
                else:
                    combined_model = model
            except Exception as e:
                logger.error("Failed when processing the following message: \
                             {}\n{}".format(msg, e))
        return combined_model

    @staticmethod
    def get_name(self):
        return None

    @staticmethod
    def get_help(self):
        return None
