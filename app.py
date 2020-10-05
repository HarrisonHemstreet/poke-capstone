# pokemon search engine
from flask import Flask, request, redirect, render_template
from flask_debugtoolbar import DebugToolbar
from jinja2 import Template

app = Flask(__name__)

@app.route('/')
def home():
    """return homepage"""
    return render_template('base.html')


if __name__ == "__main__":
    app.run()

# have users sign in and add pokemon to their favorites to incorporate databases
#maybe consider puting the site in 8bit
# user favortites page
