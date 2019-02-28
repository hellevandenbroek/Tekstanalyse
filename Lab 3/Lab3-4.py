from nltk import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.feature_extraction.text import CountVectorizer

def readFromFile():
    # trying without SW
    f = open("twitterCorpusSW.txt", "r", encoding="utf-8")
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


# own_texts = ['This is my text. I own the text.',
#              'Someone stole my text.',
#              'Hey, stop that!',
#              'Fine, I give up..',
#              'And now for the credits']


def count_vectorizer(account, comp_tweet):
    # Adding the account tweets to the list first,
    # then adding the input tweet last [-1]
    list_tweets = [tweet for tweet in account]
    list_tweets.append(comp_tweet)

    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(list_tweets)
    # print("gtf:", vectorizer.get_feature_names())
    return X.toarray()


def dist(matrix):
    euc = euclidean_distances(matrix)
    return euc


def compute_similarity(account, new_tweet):
    mean_value = 0
    sum_new = sum(new_tweet)

    for line in account:
        vec_sum = sum(line)
        dist_euc = dist([line, new_tweet])[1][0]
        print("dist:", dist_euc)
        sim = (vec_sum + sum_new/
                       dist_euc)
        print("similarity:", sim)
        mean_value += sim
    mean_value /= len(account)
    print("mean value:", mean_value)
    return mean_value


input_tweet = "this is a great wall and the animals are doing perfectly fine reportingly vegan peta vegetarian good! We need the wall"
results = readFromFile()
tweets = results[0]
names = results[1]

print('\n---------------TWEETS---------------')
print("tweets:", tweets)
print('Input tweet: ', input_tweet)

print('\n---------------CORPORA---------------')
print(names[0], ': ', tweets[0])
print(names[1], ': ', tweets[1])

print('\n---------------VECTORS---------------')
vectorized = count_vectorizer(tweets[0], input_tweet)
print(vectorized)

sum_vect = [sum(vec) for vec in vectorized]
print("sum:", sum_vect)

# sim = compute_similarity(vectorized[0], vectorized[1])


# vectorized2 = count_vectorizer(tweets[1], input_tweet)


print('\n---------------COMPARED---------------')
compared = [sum(line) for line in dist(vectorized)]
# compared2 = compare(vectorized2)


compute_similarity(vectorized[:len(vectorized) - 1], vectorized[-1])

print('\n---------------CREDITS---------------')
print("Helle van den Broek - Author")
print("Truls Andreas Berglund - Author")
