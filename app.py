from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Set up the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///messages.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Create the database model
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)

# Create the database tables if they don't exist
with app.app_context():
    db.create_all()

# Route for home page, renders the contact form
@app.route('/')
def home():
    return render_template('index.html')  # The HTML file where the form is

# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Create a new message record in the database
        new_message = Message(name=name, email=email, message=message)
        db.session.add(new_message)
        db.session.commit()

        return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
