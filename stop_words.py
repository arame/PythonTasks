import nltk
import logging, sys
nltk.download("stopwords")
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

logging.basicConfig(format='%(asctime)s | %(levelname)s : %(message)s',
                        level=logging.INFO, stream=sys.stdout)
logging.getLogger().setLevel(logging.INFO)

def remove_stopwords(sentence):
    logging.info(f"Sentence with stop words")
    logging.info(sentence)
    word_tokens = word_tokenize(sentence)
    stop_words = set(stopwords.words("english"))
    sentence_with_no_stopwords_tokens = \
        [word for word in word_tokens if word.casefold() not in stop_words]

    new_sentence = ' '.join([str(word) for word in sentence_with_no_stopwords_tokens])
    logging.info(f"Sentence * without * stop words")
    logging.info(new_sentence)

if __name__ == "__main__":
    sentence = "A towel, [The Hitchhiker's Guide to the Galaxy] says, is about the most massively useful thing an interstellar hitchhiker can have. Partly it has great practical value. You can wrap it around you for warmth as you bound across the cold moons of Jaglan Beta; you can lie on it on the brilliant marble-sanded beaches of Santraginus V, inhaling the heady sea vapors; you can sleep under it beneath the stars which shine so redly on the desert world of Kakrafoon; use it to sail a miniraft down the slow heavy River Moth; wet it for use in hand-to-hand-combat; wrap it round your head to ward off noxious fumes or avoid the gaze of the Ravenous Bugblatter Beast of Traal (such a mind-boggingly stupid animal, it assumes that if you can't see it, it can't see you); you can wave your towel in emergencies as a distress signal, and of course dry yourself off with it if it still seems to be clean enough."
    remove_stopwords(sentence)