from flask import Flask, render_template
import requests
from datetime import datetime


app = Flask(__name__)

@app.route('/')
def home():
    current_year = datetime.now().year
    return render_template('index.html', year=current_year)


@app.route('/blog/<num>')
def blog_post(num):
    blog_url = "https://api.npoint.io/7bb7d1b262b40d632b71"
    response = requests.get(url=blog_url)
    all_posts = response.json()
    return render_template('blog.html', posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)



