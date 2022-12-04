from coffee import Db
from user import User
from prettytable import PrettyTable
import os

class Report(User, Db):

    def gen_resource(self):
        resource = self.get_resource()
        p = PrettyTable()
        p.field_names = ["Coffee Bean(kg)", "Water(ml)", "Sugar(kg)"]
        p.add_row([f"{resource[0]}",f"{resource[1]}",f"{resource[2]}"])
        print(p)
         
    def gen_member(self, swap):
        status = True
        while status == True:
            if swap == '1':
                cust_id = input("\n Customer ID: ")
                User().get_user(user_id=cust_id)
                break

            elif swap == '2':
                find_customer = self.cursor
                member_sql = "SELECT * FROM customer_tb"
                find_customer.execute(member_sql)
                member_data = find_customer.fetchall()
                p = PrettyTable()
                p.field_names = ["Customer ID", "Firstname", "Lastname", "Phone Number"]

                for customer in member_data:
                    p.add_row([customer[0], customer[1], customer[2], customer[3]])
                total_member = len(member_data)
                print(f"Total Member: {total_member}")
                print(p)
                break

            elif swap == '3':
                os.system("cls||clear")
                status = False
                continue
            else:
                os.system("cls||clear")
                print("\n Invalid input. Try again.")
                break

    def gen_sale(self, swap):
        status = True
        while status == True:
            if swap == '1': 
                day = input("\n Enter the date: ").split('/')
                day_format = "{year}-{month}-{date}".format(year=day[2], month=day[0], date=day[1])
                sale = self.cursor
                sale_sql = f"SELECT sell_id, customer_first, customer_last, coffee_name, sell_total, sell_date \
                            FROM sell_tb \
                            INNER JOIN customer_tb on sell_tb.customer_id=customer_tb.customer_id \
                            INNER JOIN coffee_tb on sell_tb.coffee_id=coffee_tb.coffee_id \
                            WHERE sell_tb.sell_date='{day_format}' \
                            ORDER BY sell_date DESC"
                sale.execute(sale_sql)
                sale_data = sale.fetchall()
                p = PrettyTable()
                p.field_names = ["Customer ID", "Firstname", "Lastname", "Coffee", "Price", "Date"]
                sell_total=0
                for each_item in sale_data:
                    p.add_row([each_item[0], each_item[1], each_item[2], each_item[3], each_item[4], each_item[5]])
                    sell_total=sell_total+each_item[4]
                round_sell = round(sell_total, 3)
                print(f"\n Total: ${round_sell}")
                print(p)
                break
            
            elif swap == '2':
                start = input("\n Enter start date: ").split('/')
                end = input("\n Enter end date: ").split('/')
                start_format = "{year}-{month}-{date}".format(year=start[2], month=start[0], date=start[1])
                end_format = "{year}-{month}-{date}".format(year=end[2], month=end[0], date=end[1])
                sale = self.cursor
                sale_sql = f"SELECT sell_id, customer_first, customer_last, coffee_name, sell_total, sell_date \
                            FROM sell_tb \
                            INNER JOIN customer_tb on sell_tb.customer_id=customer_tb.customer_id \
                            INNER JOIN coffee_tb on sell_tb.coffee_id=coffee_tb.coffee_id \
                            WHERE sell_date BETWEEN '{start_format}' AND '{end_format}' \
                            ORDER BY sell_date DESC"
                sale.execute(sale_sql)
                sale_data = sale.fetchall()
                p = PrettyTable()
                p.field_names = ["Customer ID", "Firstname", "Lastname", "Coffee", "Price", "Date"]
                sell_total=0
                for each_item in sale_data:
                    p.add_row([each_item[0], each_item[1], each_item[2], each_item[3], each_item[4], each_item[5]])
                    sell_total=sell_total+each_item[4]
                round_sell = round(sell_total, 3)
                print(f"\n Total: ${round_sell}")
                print(p)
                break
            
            elif swap == '3':
                sale = self.cursor
                sale_sql = "SELECT sell_tb.sell_id, customer_tb.customer_first, customer_tb.customer_last, coffee_tb.coffee_name, sell_tb.sell_total, sell_tb.sell_date \
                            FROM sell_tb \
                            INNER JOIN customer_tb on sell_tb.customer_id=customer_tb.customer_id \
                            INNER JOIN coffee_tb on sell_tb.coffee_id=coffee_tb.coffee_id \
                            ORDER BY sell_tb.sell_date DESC"
                sale.execute(sale_sql)
                sale_data = sale.fetchall()
                p = PrettyTable()
                p.field_names = ["Customer ID", "Firstname", "Lastname", "Coffee", "Price", "Date"]
                sell_total=0
                for each_item in sale_data:
                    p.add_row([each_item[0], each_item[1], each_item[2], each_item[3], each_item[4], each_item[5]])
                    sell_total=sell_total+each_item[4]
                round_sell = round(sell_total, 2)
                print(f"\n Total: ${round_sell}")
                print(p)
                break
            
            elif swap == '4':
                os.system("cls||clear")
                status = False
                continue
            
            else:
                os.system("cls||clear")
                print("\n Invalid input. Try again.")
                break