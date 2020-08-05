from flask import Flask, render_template

import json
import scrape
import pandas as pd

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

    df = df.sort_values(by='rating', ascending=False) #We sort by rating before sending
    df_json = df.to_json(orient='records')

    return render_template("home.html", title="Foodridise",
    data=json.loads(df_json))



#route for login
@app.route("/login")
def login():
    return render_template("starter.html", title="Login")

#route for registration
@app.route("/register" , methods=['GET', 'POST'])
def register():

    #if account exist, send to login
    userExists = False
    if userExists:
        redirect("/login")
    
    #start grabbing data 
    if request.method == 'POST':
        firstName = request.form['firstName']
        lastName = request.form['lastName']
        email = request.form['email']
        password = request.form['password']

    data = request.json

    return render_template("register.html", title = "Registration")


#route for registering ones restaurant
#might need to append endpoint to register
#TODO indicator on register if individual is making a account with a restaurant as well
#TODO once someone enters resteraunt take them directly to menu route
@app.route("/restaurant_reg", methods=['GET', 'POST'])
def resteraunt_reg():
    return render_template("restaurant_reg.html", title = "Register you Resteraunt!")

#route for restaurant to input menu images
@app.route
def menu_input():
    return render_template("menu_input.html", title = "Menu Input")

#route for placing order
@app.route("/place_order")
def order():
    return render_template("starter.html", title = "Place Order")





@app.route("/lorempizzeria")
def lorempizzeria():
    data = scrape.format_data(scrape.get_images('static/images2'))
    print(data)
    return render_template("lorempizzeria.html", title="Lorem Pizzeria",
    data=data)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
