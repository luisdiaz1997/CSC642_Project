from flask import Flask, render_template
import json
import scrape
import pandas as pd
app = Flask(__name__)


@app.route("/")
def home():

    try:
        df = pd.read_csv('static/data.csv')
    except:
        df = scrape.construct_data('static/images')
        df.to_csv('static/data.csv', index=False)

    df_json = df.to_json(orient='records')

    return render_template("home.html", title="Foodridise",
    data=json.loads(df_json))


if __name__ == "__main__":
    app.run(debug=True, port=5000)
