import nltk
import pandas as pd
import logging, sys, math
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer

logging.basicConfig(format='%(asctime)s | %(levelname)s : %(message)s',
                        level=logging.INFO, stream=sys.stdout)
logging.getLogger().setLevel(logging.INFO)

def sklearn_tf_idf(documents):
    tf_idf_vect = TfidfVectorizer()
    X_train_tf_idf = tf_idf_vect.fit_transform(documents)
    logging.info(X_train_tf_idf)
    
def calc_tf_idf(documents):
    all_documents = ' '.join([str(doc) for doc in documents])
    word_tokens = word_tokenize(all_documents)
    N = len(documents)
    corpus = {}
    doc_freq = {}
    df_tf = pd.DataFrame()
    df_idf = pd.DataFrame()
    col_idx = -1
    for token in word_tokens:
        if token in corpus:
            continue
        corpus[token] = 0
        doc_freq[token] = 0
        col_idx += 1
        df_tf.insert(col_idx, token, None)
        df_idf.insert(col_idx, token, None)

    for document in documents:
        doc_corpus = corpus.copy()
        doc_word_tokens = word_tokenize(document)
        for token in doc_word_tokens:
            doc_corpus[token] += 1
            if doc_corpus[token] == 1:
                doc_freq[token] += 1

        df_tf.loc[len(df_tf)] = doc_corpus.values()

    list_ldf = []
    log_base = 10
    for item in doc_freq.values():
        ldf = math.log(N/item, log_base)
        list_ldf.append(ldf)
    for i in range(N):
        df_idf.loc[i] = list_ldf
    df_tf_idf = df_tf * df_idf
    logging.info(df_tf_idf)

    i = 0

if __name__ == "__main__":
    documents = ["This must be Thursday,' said Arthur to himself, sinking low over his beer. 'I never could get the hang of Thursdays", 
                 "Ford... you're turning into a penguin. Stop it.",
                 "For a moment, nothing happened. Then, after a second or so, nothing continued to happen.",
                 "Would it save you a lot of time if I just gave up and went mad now?",
                 "He felt that his whole life was some kind of dream and he sometimes wondered whose it was and whether they were enjoying it.",
                 "The ships hung in the sky in much the same way that bricks don't.", 
                 "Time is an illusion. Lunchtime doubly so.",
                 "Anyone who is capable of getting themselves made President should on no account be allowed to do the job.",
                 "Arthur: Ah, this is obviously some strange use of the word safe that I wasn't previously aware of.",
                 "and we’ll be saying a big hello to all intelligent life forms everywhere … and to everyone else out there, the secret is to bang the rocks together, guys.",
                 "Here, for whatever reason, is the world. And here it stays. With me on it."
                 ]
    calc_tf_idf(documents)
    sklearn_tf_idf(documents)