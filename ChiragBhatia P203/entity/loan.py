class Loan:
    def __init__(self, loan_id, customer_id, principal_amount, interest_rate, loan_term, loan_type, loan_status, 
                 property_address=None, property_value=None, car_model=None, car_value=None):
        self.loan_id = loan_id
        self.customer_id = customer_id
        self.principal_amount = principal_amount
        self.interest_rate = interest_rate
        self.loan_term = loan_term
        self.loan_type = loan_type
        self.loan_status = loan_status
        self.property_address = property_address  
        self.property_value = property_value      
        self.car_model = car_model                
        self.car_value = car_value

    def display(self):
        # Basic loan details
        print(f"Loan ID: {self.loan_id}")
        print(f"Customer ID: {self.customer_id}")
        print(f"Principal Amount: {self.principal_amount}")
        print(f"Interest Rate: {self.interest_rate}%")
        print(f"Loan Term: {self.loan_term} months")
        print(f"Loan Type: {self.loan_type}")
        print(f"Loan Status: {self.loan_status}")

        # Additional details based on loan type
        if self.loan_type == "HomeLoan":
            print(f"Property Address: {self.property_address}")
            print(f"Property Value: {self.property_value}")
        elif self.loan_type == "CarLoan":
            print(f"Car Model: {self.car_model}")
            print(f"Car Value: {self.car_value}")
