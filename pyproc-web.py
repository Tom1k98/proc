#!/usr/bin/env python3
from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def vypis():
    with open('procstat.txt', 'r') as f:
        text = f.readlines()
    return render_template('index.html', lines=text)
if __name__ == "__main__":
    app.run()