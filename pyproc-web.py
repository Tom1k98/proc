#!/usr/bin/env python3
from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def vypis():
    with open('test.txt', 'r') as f:
        content = f.read()
    return render_template('index.html', text=content)
if __name__ == "__main__":
    app.run()
