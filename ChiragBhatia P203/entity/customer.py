import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

sys.path.append(os.path.dirname(SCRIPT_DIR))

from util.db_conn_util import DBConnUtil

class Customer:
    def __init__(self, customer_id, name, email, phone, address, credit_score):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        self.credit_score = credit_score

    def get_customer_id(self):
        return self.customer_id

    def get_name(self):
        return self.name

    def get_email_address(self):
        return self.email

    def get_phone_number(self):
        return self.phone

    def get_address(self):
        return self.address

    def get_credit_score(self):
        return self.credit_score

    def set_customer_id(self, customer_id):
        self.customer_id = customer_id

    def set_name(self, name):
        self.name = name

    def set_email_address(self, email):
        self.email_address = email

    def set_phone_number(self, phone):
        self.phone_number = phone

    def set_address(self, address):
        self.address = address

    def set_credit_score(self, credit_score):
        self.credit_score = credit_score

    def display_customer_details(self):
        print()
        print(f"Customer ID: {self.customer_id}")
        print(f"Name: {self.name}")
        print(f"Email Address: {self.email}")
        print(f"Phone Number: {self.phone}")
        print(f"Address: {self.address}")
        print(f"Credit Score: {self.credit_score}")
        print()


    def insert_new_customer(self):
        try:
            conn = DBConnUtil.get_db_conn()  # Get the connection
            cursor = conn.cursor()  # Create a cursor

            # Insert the customer record
            cursor.execute(
                """
                INSERT INTO Customer (name, email, phone, address, credit_score) 
                VALUES (?, ?, ?, ?, ?)
                """,
                (self.name, self.email, self.phone, self.address, self.credit_score)
            )
            conn.commit()  # Commit the transaction

            # Fetch the newly inserted customer_id using SCOPE_IDENTITY()
            cursor.execute("SELECT count(customer_id) from Customer;")
            result = cursor.fetchone() 

            if result and result[0] is not None:
                self.customer_id = int(result[0])  # Store the customer_id
                print(f"Customer '{self.name}' added to the database with ID: {self.customer_id}")
            else:
                print("Error: Could not fetch customer_id.")
            
            return self.customer_id 
        
        except Exception as e:
            print("Error inserting customer:", e)
            return None
        
        finally:
            cursor.close()  # Ensure the cursor is closed
            conn.close()  # 