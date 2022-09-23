from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy




app = Flask(__name__)
app.secret_key = "Secret Key"

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/crud'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100))
    author = db.Column(db.String(100))
    year = db.Column(db.String(100))

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year




@app.route('/')
def Index():
    all_data = Book.query.all()

    return render_template("index.html", books = all_data)





@app.route('/insert', methods = ['POST'])
def insert():

    if request.method == 'POST':

        title = request.form['title']
        author = request.form['author']
        year = request.form['year']



        my_data = Book(title, author, year)
        db.session.add(my_data)
        db.session.commit()

        flash("Book Added Successfully!")

        return redirect(url_for('Index'))


@app.route('/update', methods = ['GET', 'POST'])
def update():

    if request.method == 'POST':
        my_data = Book.query.get(request.form.get('id'))

        my_data.title = request.form['title']
        my_data.author= request.form['author']
        my_data.year = request.form['year']

        db.session.commit()
        flash("Book Updated Successfully")

        return redirect(url_for('Index'))

@app.route('/delete/<id>/', methods = ['GET', 'POST'])
def delete(id):
    my_data = Book.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Book Deleted Successfully")

    return redirect(url_for('Index'))



if __name__ == "__main__":
    app.run(debug=True)
