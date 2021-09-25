from flask import Flask,render_template
from flask_moment import Moment
from flask_bootstrap import Bootstrap
from datetime import datetime

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html',name = name,current_time = datetime.utcnow())

if __name__ == "__main__":
    app.run(debug=True)