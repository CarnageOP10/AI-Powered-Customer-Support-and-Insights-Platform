from custom import db

class Query(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    mobile_number = db.Column(db.String(10), nullable=False)
    state_name = db.Column(db.String(50), nullable=False)
    city_name = db.Column(db.String(50), nullable=False)
    pincode = db.Column(db.String(6), nullable=False)
    description = db.Column(db.String(5000), nullable=False)