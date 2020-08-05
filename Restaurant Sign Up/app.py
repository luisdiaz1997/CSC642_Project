from flask import Flask, render_template, request, redirect
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
@app.route("/register")
def register():

    #if account exist, send to login
    userExists = False
    if userExists:
        redirect("/login")

    return render_template("register.html", title = "Registration")


#route for registering ones restaurant
#might need to append endpoint to register
#TODO indicator on register if individual is making a account with a restaurant as well
#TODO once someone enters resteraunt take them directly to menu route
@app.route("/restaurant_reg")
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
    return render_template("lorempizzeria.html", title="Lorem Pizzeria",
    data=data)


#Route to first page of restaurant registration
@app.route("/restaurantsignup")
def test():
    return render_template("register.html", title = "Place Order")

#Restaurant step 1 to step 2
@app.route("/step1", methods=["GET","POST"])
def step1():
    if request.method == 'POST':
        firstName = request.form.get("firstName")
        lastName = request.form.get("lastName")
        password = request.form.get("password")
        confirmPassword = request.form.get("confirmPassword")
        email = request.form.get("email")

        if password != confirmPassword:
            feedback = "Passwords do not match!"
            return render_template("register.html", feedback = feedback)

        if numValidation(firstName) == True:
            feedback = "Invalid name!"
            return render_template("register.html", feedback = feedback)

        if numValidation(lastName) == True:
            feedback = "Invalid name!"
            return render_template("register.html", feedback = feedback)

    #return redirect(request.url)
    return render_template("restaurant_reg.html")

#Step 2 to 3
@app.route("/step2", methods=["GET","POST"])
def step2():

    if request.method == 'POST':
        city = request.form.get("city")
        restaurantName = request.form.get("restaurantName")
        zip = request.form.get("zip")
        country = request.form.get("country")
        phoneNum = request.form.get("phoneNum")
        hours = request.form.get("hours")
        state = request.form.get("state")
        street = request.form.get("street")
        type = request.form.get("type")

        if numValidation(city) == True:
            feedback = "Invalid city name!"
            return render_template("restaurant_reg.html", feedback = feedback)

        if numValidation(type) == True:
            feedback = "Invalid type of restaurant!"
            return render_template("restaurant_reg.html", feedback = feedback)

        if numValidation(restaurantName) == True:
            feedback = "Invalid restaurant name!"
            return render_template("restaurant_reg.html", feedback = feedback)

        if zip.isdigit() == False or len(zip) != 5:
            feedback = "Invalid zip code!"
            return render_template("restaurant_reg.html", feedback = feedback)

        if phoneNum.isdigit() == False or len(phoneNum) != 7:
            feedback = "Invalid phone number!"
            return render_template("restaurant_reg.html")


    return render_template("menu_input.html")

#step 3 to 4
@app.route("/step4")
def step3():
    return render_template("/reg_login/step4.html", title = "Place Order")

#step 4 to 5
@app.route("/step5")
def step4():
    return render_template("/reg_login/step5.html", title = "Place Order")

@app.route("/thanks", methods=["GET","POST"])
def thankyou():
    if request.method == "POST":
        accountNum = request.form.get("accountNum")
        confirmRoutingNum = request.form.get("confirmRoutingNum")
        year = request.form.get("year")
        month = request.form.get("month")
        routingNum = request.form.get("routingNum")
        legalName = request.form.get("legalName")
        businessOwner = request.form.get("businessOwner")
        day = request.form.get("day")
        confirmAccountNum = request.form.get("confirmAccountNum")
        ein = request.form.get("ein")

        if numValidation(legalName) == True:
            feedback = "Invalid legal restaurant name!"
            return render_template("/reg_login/step5.html", feedback = feedback)

        if numValidation(businessOwner) == True:
            feedback = "Invalid owner name!"
            return render_template("/reg_login/step5.html", feedback = feedback)

        if routingNum != confirmRoutingNum:
            feedback = "Routing numbers don't match. "
            return render_template("/reg_login/step5.html", feedback = feedback)

        if len(routingNum) != 9 or len(confirmRoutingNum) !=9:
            feedback = "Routing number is not valid!"
            return render_template("/reg_login/step5.html", feedback = feedback)

        if len(accountNum) < 9 or len(confirmAccountNum) < 9:
            feedback = "Account number is not valid, too short!"
            return render_template("/reg_login/step5.html", feedback = feedback)

        if len(accountNum) > 16 or len(confirmAccountNum) > 16:
            feedback = "Account number is not valid, too long!"
            return render_template("/reg_login/step5.html", feedback = feedback)

        if len(ein) != 9 or numValidation(ein) == False:
            feedback = "EIN number is not valid!"
            return render_template("/reg_login/step5.html", feedback = feedback)

    return render_template("thankyou.html", businessOwner = businessOwner, legalName = legalName)

#Check for digits where they shouldnt be
def numValidation(s):
    return any(i.isdigit() for i in s)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
