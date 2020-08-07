from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def dataView():
    return render_template('data.html')
