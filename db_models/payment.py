from repository.database import db

class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float)
    paid = db.Column(db.Boolean, default=False)
    bank_payment_id = db.Column(db.Integer, nullable=True)
    qr_code = db.Column(db.String(255), nullable=True)
    expiration_date = db.Column(db.DateTime, nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'amount': self.amount,
            'paid': self.paid,
            'bank_payment_id': self.bank_payment_id,
            'qr_code': self.qr_code,
            'expiration_date': self.expiration_date.isoformat() if self.expiration_date else None
        }
