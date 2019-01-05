from app import db

class Quote(db.Model):
    __tablename__ = "quotes"
    _id = db.Column("id", db.Integer, primary_key=True)
    # From https://stackoverflow.com/questions/386294/what-is-the-maximum-length-of-a-valid-email-address/574698#574698
    email = db.Column(db.String(254), index=True, nullable=False)
    forename = db.Column(db.String(20), nullable=False)
    surname = db.Column(db.String(20), nullable=False)
    telephone = db.Column(db.String(20), nullable=False)
    account_number = db.Column(db.String(20), nullable=False)
    sort_code = db.Column(db.String(20), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    town = db.Column(db.String(100), nullable=False)
    postcode = db.Column(db.String(10), nullable=False)
    _datetime = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f"<Quote {self._id}>"
