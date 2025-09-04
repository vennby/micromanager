from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class EventDocumentations(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    date = db.Column(db.String(50), nullable=False)
    participants = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=False)
    image_filename = db.Column(db.String(300), nullable=True)

class Contributions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    month = db.Column(db.String(20), nullable=False)
    year = db.Column(db.String(4), nullable=False)
    points = db.Column(db.Text, nullable=False)

    def unique_key(self):
        return f"{self.month.lower()}-{self.year}"