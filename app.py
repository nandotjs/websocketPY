from flask import Flask, jsonify
from repository.database import db
from db_models.payment import Payment

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'secret_key_websocket'

db.init_app(app)

@app.route('/payments/pix', methods=['POST'])
def create_pix_payment():
    return jsonify({'message': 'Pix payment created successfully'}), 201

@app.route('/payments/pix/confirm', methods=['POST'])
def confirm_pix_payment():
    return jsonify({'message': 'Pix payment confirmed successfully'}), 200

@app.route('/payments/pix/<int:payment_id>', methods=['GET'])
def get_pix_payment(payment_id):
    return jsonify({'message': f'Pix payment {payment_id}'}), 200

if __name__ == '__main__':
    app.run(debug=True)