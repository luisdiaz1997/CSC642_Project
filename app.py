from flask import Flask, render_template

app = Flask(__name__)


data = [
        {"name": "Lorum Pizzeria", "src": "https://image.freepik.com/free-photo/pork-boat-noodles-classic-thai-food-popular-menus-ready-eat-soups-there-is-also-basil-bowl_1150-24194.jpg"},
        {"name": "Lorum Pizzeria", "src": "https://image.freepik.com/free-photo/pork-boat-noodles-classic-thai-food-popular-menus-ready-eat-soups-there-is-also-basil-bowl_1150-24194.jpg"},
        {"name": "Lorum Pizzeria", "src": "https://image.freepik.com/free-photo/pork-boat-noodles-classic-thai-food-popular-menus-ready-eat-soups-there-is-also-basil-bowl_1150-24194.jpg"},
        {"name": "Lorum Pizzeria", "src": "https://image.freepik.com/free-photo/pork-boat-noodles-classic-thai-food-popular-menus-ready-eat-soups-there-is-also-basil-bowl_1150-24194.jpg"},
        {"name": "Lorum Pizzeria", "src": "https://image.freepik.com/free-photo/pork-boat-noodles-classic-thai-food-popular-menus-ready-eat-soups-there-is-also-basil-bowl_1150-24194.jpg"},
        {"name": "Lorum Pizzeria", "src": "https://image.freepik.com/free-photo/pork-boat-noodles-classic-thai-food-popular-menus-ready-eat-soups-there-is-also-basil-bowl_1150-24194.jpg"},
        {"name": "Lorum Pizzeria", "src": "https://image.freepik.com/free-photo/pork-boat-noodles-classic-thai-food-popular-menus-ready-eat-soups-there-is-also-basil-bowl_1150-24194.jpg"},
        {"name": "Lorum Pizzeria", "src": "https://image.freepik.com/free-photo/pork-boat-noodles-classic-thai-food-popular-menus-ready-eat-soups-there-is-also-basil-bowl_1150-24194.jpg"},
        {"name": "Lorum Pizzeria", "src": "https://image.freepik.com/free-photo/pork-boat-noodles-classic-thai-food-popular-menus-ready-eat-soups-there-is-also-basil-bowl_1150-24194.jpg"},
        ]

@app.route("/")
def home():
    return render_template("home.html", title="Foodridise", data=data)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
