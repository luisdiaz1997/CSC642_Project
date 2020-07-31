from flask import Flask, render_template
import json
import scrape

import pandas as pd
app = Flask(__name__)


#importing flask into app
app = Flask(__name__)

#route for homepage
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



#route for login 
@app.route("/login")
def login():
    return render_template("starter.html", title="Login")

#route for registration
@app.route("/register")
def register():
    return render_template("starter.html", title = "Registration")
    

#route for registration
@app.route("/place_order")
def order():
    return render_template("starter.html", title = "Place Order")






if __name__ == "__main__":
    app.run(debug=True, port=5000)
