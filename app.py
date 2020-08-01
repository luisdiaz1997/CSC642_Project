from flask import Flask, render_template
import scrape
app = Flask(__name__)


@app.route("/")
def home():
    data = scrape.format_data(scrape.get_images('static/images'))
    return render_template("home.html", title="Foodridise",
    data=data)

@app.route("/lorempizzeria")
def lorempizzeria():
    data = scrape.format_data(scrape.get_images('static/images2'))
    return render_template("lorempizzeria.html", title="Lorem Pizzeria",
    data=data)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
