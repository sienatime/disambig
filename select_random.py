import model

if __name__ == "__main__":
    model.connect_to_db()
    tweets = model.select_random_tweets(500)

    for tweet in tweets:
        print tweet[1], tweet[0].encode('ascii','replace')
