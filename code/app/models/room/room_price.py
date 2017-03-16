from app import app, db


class Room_Price(db.Model):
    '''
    Database representation of room prices
    '''
    __tablename__ = 'room_price'

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(120), nullable=False)
    price_weekday = db.Column(db.Float, nullable=False)
    price_weekend = db.Column(db.Float, nullable=False)

    def __init__(self, type, price_weekday, price_weekend):
        self.type = type
        self.price_weekday = price_weekday
        self.price_weekend = price_weekend

    def set_price_weekend(self, price_weekend):
        self.price_weekend = price_weekend
 
    def set_price_weekday(self, price_weekday):
        self.price_weekday = price_weekday

    def set_type(self, type):
        self.type = type


    def __repr__(self):
        return '<Room %r>' % self.type