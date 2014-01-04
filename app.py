from flask import Flask, render_template, request
import model

app = Flask(__name__)

@app.route("/classify")
def classify():
    model.connect_to_db()
    sample_tweet = model.get_tweet()
    return render_template("classify.html", tweet_data=sample_tweet)

@app.route("/rate", methods=["POST"])
def rate_tweet():
    model.connect_to_db()
    t_id = request.form.get("tweet_id")
    relevant = request.form.get("relevant")
    model.rate_tweet(t_id, relevant)
    return "ok"

if __name__ == "__main__":
    app.run(debug=True)