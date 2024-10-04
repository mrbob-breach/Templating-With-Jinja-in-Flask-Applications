from flask import Flask, render_template
import requests


app = Flask(__name__)


@app.route('/guess/<string:name>')
def guess_name(name):
    name = name.title()
    guessed_age = requests.get(f"https://api.agify.io?name={name}").json()['age']
    guessed_gender = requests.get(f"https://api.genderize.io?name={name}").json()['gender']
    return render_template("index.html", name=name, age=guessed_age, gender=guessed_gender)


@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    all_posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
    return render_template("blog.html", posts=all_posts)


@app.route('/')
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)

