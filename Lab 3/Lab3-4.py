from nltk import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.feature_extraction.text import CountVectorizer

def readFromFile():
    f = open("twitterCorpus.txt", "r", encoding="utf-8")
    tweets = []
    names = []
    for line in f.readlines():
        tweeter = line

        colon = tweeter.index(":")
        name = tweeter[0:colon]
        names.append(name)
        tweeter = line.split('-,-')
        tweets.append(tweeter[colon + 1:])
    return tweets, names


def count_vectorizer(corpus):
    list_tweets = []
    for tweet in corpus:
        list_tweets.append(' '.join(tweet))
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(list_tweets)
    print(vectorizer.get_feature_names())
    return(X.toarray())


def count_vec_example():
    corpus = [
        'This is the first document.',
         'This is the second second document.',
         'And the third one.',
         'Is this the first document?'
    ]
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    return(X.toarray())

def compare(matrix) :
    return (euclidean_distances(matrix, matrix))

results = readFromFile()
tweets = results[0]
names = results[1]
vectorized = count_vectorizer(tweets)
compared = compare(vectorized)

print('\n---------------TWEETS---------------')
print("tweets:", tweets)

print('\n---------------CORPORA---------------')
print(names[0], ': ', tweets[0])
print(names[1], ': ', tweets[1])

print('\n---------------VECTORS---------------')
print(vectorized)

print('\n---------------COMPARED---------------')
print(compared)
