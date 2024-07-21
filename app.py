from flask import Flask, render_template,  url_for
from forms import Search

app=Flask(__name__)
app.config['SECRET_KEY']="12345678"
@app.route("/")
def home():
    form=Search()
    return render_template("home.html",form=form)

if __name__=='__main__':
    app.run(debug=True)