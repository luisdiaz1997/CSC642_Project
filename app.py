from flask import Flask, render_template
import scrape

#importing flask into app
app = Flask(__name__)

#route for homepage
@app.route("/")
def home():
    data = scrape.format_data(scrape.get_images('static/images'))
    return render_template("home.html", title="Foodridise",
    data=data)

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
