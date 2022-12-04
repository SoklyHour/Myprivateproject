from coffee import Db
from prettytable import PrettyTable
import operator

class User(Db):

    def register(self, firstname, lastname, phonenumber):
        sql_register = f"""INSERT INTO customer_tb (customer_first, customer_last, customer_phone) VALUES ('{firstname}', '{lastname}', "{phonenumber}" )"""
        self.cursor.execute(sql_register)
        self.cnx.commit()
        print('\n Thank you for becoming our member.')
        show_member = f"SELECT * FROM customer_tb WHERE customer_phone='{phonenumber}'"
        self.cursor.execute(show_member)
        self.cnx.commit()
        member_data = self.cursor.fetchall()
        p = PrettyTable()
        p.field_names = ["Member ID", "Firstname", "Lastname", "Phone Number"]
        p.add_rows(member_data)
        print(p)
    
    def get_user(self, user_id):
        find_customer = self.cursor
        customer_sql = f"SELECT * FROM customer_tb WHERE customer_id='{user_id}'"
        find_customer.execute(customer_sql)
        customer_data = find_customer.fetchall()
        p = PrettyTable()
        p.field_names = ["Customer ID", "Firstname", "Lastname", "Phone Number"]
        for customer in customer_data:
            p.add_row([customer[0], customer[1], customer[2], customer[3]])
        print(p)

    def is_member(self, phonenumber):
        sql_member = f"SELECT * FROM customer_tb WHERE customer_phone = '{phonenumber}'"
        self.cursor.execute(sql_member)
        member_data = self.cursor.fetchall()
        if member_data == None:
            print('\n No member was found.')
        else:
            print("\n Here is your membership information")
            p = PrettyTable()
            p.field_names = ["Member ID", "Firstname", "Lastname", "Phone Number"]
            p.add_rows(member_data)
            print(p)

    def checkout_member(self, user, coffee_id):   
        self.update_resource(coffee_id=coffee_id)
        sell = self.get_coffee_resource(coffee_id=coffee_id)
        total = sell[3] - (sell[3]*0.1)
        sql_sell = f"""INSERT INTO sell_tb (coffee_id, customer_id, sell_total) VALUES('{coffee_id}','{user}','{total}')"""
        self.cursor.execute(sql_sell)
        self.cnx.commit()

    def checkout_not_member(self, user, coffee_id):
        self.update_resource(coffee_id=coffee_id)
        coffee_price = self.get_coffee_resource(coffee_id=coffee_id)
        sell_total = coffee_price[3]
        sql_sell = f"""INSERT INTO sell_tb (coffee_id, customer_id, sell_total) VALUES('{coffee_id}','{user}','{sell_total}')"""
        self.cursor.execute(sql_sell)
        self.cnx.commit()