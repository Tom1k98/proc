#!/usr/bin/env python3
from flask import Flask, render_template
import re
from types import SimpleNamespace
app = Flask(__name__)
@app.route('/')
def vypis():
    with open('procstat.txt', 'r') as f:
        text = f.read().replace(' ', '')
        text = re.split('[\n-]', text)
        tmp = iter(text)
        slovnik = dict(zip(tmp, tmp))
        n = SimpleNamespace(**slovnik)
        return render_template('index.html', ansa=n.ansa, meta=n.meta, animator=n.animator)
if __name__ == "__main__":
    app.run()
