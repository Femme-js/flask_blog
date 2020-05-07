from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')
    app.run(port=5000, debug=True)

@app.route("/about")
def about():
    return render_template('about.html')
    app.run(port=5000, debug=True)

@app.route("/post")
def post():
    return render_template('post.html')
    app.run(port=5000, debug=True)

@app.route("/contact")
def contact():
    return render_template('contact.html')
    app.run(port=5000, debug=True)





