from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Step 1: Create the Flask app instance
app = Flask(__name__)

# Step 2: Configure the app to use a SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

# Step 3: Initialize the SQLAlchemy object with the app instance
db = SQLAlchemy(app)

# Example route
@app.route('/')
def home():
    return "Database connected!"

# Run the app
if __name__ == '__main__':
    app.run(debug=True)

