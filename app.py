"""

"""
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def this():
    return render_template('test.html',
                           info=[1, 2, 3, 4])

if __name__ == '__main__':
    app.run()