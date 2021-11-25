from flask import Flask, render_template, request
from SentimentAnalysis import SentimentAnalysis

sentiment_obj = SentimentAnalysis()
app = Flask(__name__)


@app.route('/')
def Home():
    return render_template(
        '/index.html',
        phrase_output="",
        pos_average=0,
        neg_average=0,
        isSubmit=False
    )

@app.route('/predict', methods=['POST'])
def predict():
    result = ""
    pos_str = 0
    neg_str = 0
    if request.method == "POST":
        phrase = request.form['phrase']

        type, pos_ave, neg_ave  = sentiment_obj.predict_phrase(phrase)
        pos_per = pos_ave * 100
        neg_per = neg_ave * 100
        pos_str = "{0:.1f}".format(pos_per)
        neg_str = "{0:.1f}".format(neg_per)
        if type=="Positive":
            result = "POSITIVE 😄"
        elif type=="Negative":
            result = "NEGATIVE 🤨"
        return render_template(
            'index.html',
            phrase_output=result,
            pos_average=pos_str,
            neg_average=neg_str,
            isSubmit=True
        )
if __name__ == '__main__':
    app.run(debug=True)

