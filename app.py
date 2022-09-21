from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy




app = Flask(__name__)
app.secret_key = "Secret Key"

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/crud'

@app.route('/')
def Index():
    return render_template("index.html")




if __name__ == "__main__":
    app.run(debug=True)
