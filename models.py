from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class Pet(db.Model):
    """Model for a pet in the adoption agency."""

    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    species = db.Column(db.String, nullable=False)
    photo_url = db.Column(db.String, nullable=True)
    age = db.Column(db.Integer, nullable=True)
    notes = db.Column(db.String, nullable=True)
    available = db.Column(db.Boolean, nullable=False, default=True)

    def image_url(self):
        """Return image for pet, actual or generic."""
        GENERIC_IMAGE = "https://cdn.pixabay.com/photo/2024/01/22/15/36/cat-8525662_1280.png"
        return self.photo_url or GENERIC_IMAGE
    
def connect_db(app):
    """Connect this database to provided Flask app."""
    db.app = app
    db.init_app(app)

        
