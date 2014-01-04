import sqlite3
import model
import pdb

def count_words():
    #used initially to just sum up the number of times a word appeared in a given set (either relevant or irrelevant tweets)
    rows = model.get_relevant_tweets()

    d = {}

    for row in rows:
        tweet = row[0]
        tokens = tweet.split()
        for token in tokens:
            lc = token.lower()
            lc = lc.strip(".,!?()[]\":;'")
            count = d.get(lc, 0)
            count += 1
            d[lc] = count

    sorted_d = sorted(d.items(), key=lambda score: score[1])

    for key, val in sorted_d:
        # I'm just ignoring Unicode characters that Python doesn't know how to print, as this is just for my information and we are only interested in tweets in English anyway.
        print str(val) + ":", key.encode('ascii','replace')

    print len(rows)

def has_word(word_list, tweet):
    tweet = tweet.lower()

    for word in word_list:
        # important to remember to strip out the newline character in the word list
        # however some terms have spaces in them (e.g. "on survivor" should not match on "abduction survivor")
        if word.strip("\n") in tweet:
            print word
            return True
    return False

def classify_tweets(include, exclude):
    #rates 100 tweets at a time. 
    tweets = model.get_unrated_tweets(100)

    for tweet_data in tweets:
        t_id, tweet = tweet_data
        if has_word(exclude, tweet):
            model.rate_tweet(t_id, 0)
        elif has_word(include, tweet):
            model.rate_tweet(t_id, 1)
        else:
            model.rate_tweet(t_id, 0)

if __name__ == "__main__":
    model.connect_to_db()

    include = open("include.txt").readlines()
    exclude = open("exclude.txt").readlines()

    classify_tweets(include, exclude)