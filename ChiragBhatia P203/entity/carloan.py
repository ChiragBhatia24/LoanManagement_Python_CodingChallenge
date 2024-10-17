import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

sys.path.append(os.path.dirname(SCRIPT_DIR))

from entity.loan import Loan

class CarLoan(Loan):
    def __init__(self, loan_id, customer_id, principal_amount, interest_rate, loan_term, loan_type, loan_status, car_model, car_value):
        super().__init__(loan_id, customer_id, principal_amount, interest_rate, loan_term, loan_type, loan_status)
        self.car_model = car_model
        self.car_value = car_value

    def __str__(self):
        return f"CarLoan [CarModel={self.car_model}, CarValue={self.car_value}]"
