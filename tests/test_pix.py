import sys
sys.path.append("../")
import pytest
import os
from payments.pix import Pix

def test_pix_create_payment():
    pix_instance = Pix()
    payment_info = pix_instance.create_pix_payment(base_path='../')

    assert payment_info is not None
    assert 'qr_code' in payment_info
    assert 'qr_code_path' in payment_info
    assert 'bank_payment_id' in payment_info

    qr_code_path = payment_info['qr_code_path']
    assert os.path.isfile(qr_code_path)

