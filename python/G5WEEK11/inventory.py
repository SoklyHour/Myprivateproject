import mysql.connector
from prettytable import PrettyTable
from coffee import Db

class Inventory(Db):
    
    def refill (self, user, adding):
        if user == "1":
            update_water = f'UPDATE resource_tb \
            SET water = water + {adding} \
            WHERE resource_id = 1'
            select_water = "SELECT * from resource_tb"
            self.cursor.execute(update_water)
            self.cnx.commit()
            self.cursor.execute(select_water)
            water_result = self.cursor.fetchall()
            p = PrettyTable()
            p.field_names = ["Resource ID", "Water(ml)", "Coffee Beans (kg)", "Sugar(kg)"]
            p.add_rows(water_result)
            print(p.get_string())
            print("\n SUCESSFULLY REFILLED")
        
        elif user == '2':
            sugar_sql = f'UPDATE resource_tb \
            SET sugar = sugar + {adding} \
            WHERE resource_id = 1'
            select_sugar = "SELECT * from resource_tb"
            self.cursor.execute(sugar_sql)
            self.cnx.commit()
            self.cursor.execute(select_sugar)
            result = self.cursor.fetchall()
            p = PrettyTable()
            p.field_names = ["Resource ID", "Water(ml)", "Coffee Beans (kg)", "Sugar(kg)"]
            p.add_rows(result)
            print(p.get_string())
            print("\n SUCESSFULLY REFILLED ")

        elif user == "3":
            coffee_sql = f'UPDATE resource_tb \
            SET coffee_bean = coffee_bean + {adding} \
            WHERE resource_id = 1'
            select_coffee = "SELECT * from resource_tb"
            self.cursor.execute(coffee_sql)
            self.cnx.commit()
            self.cursor.execute(select_coffee)
            coffee_result = self.cursor.fetchall()
            p = PrettyTable()
            p.field_names = ["Resource ID", "Water(ml)", "Coffee Beans (kg)", "Sugar(kg)"]
            p.add_rows(coffee_result)
            print(p.get_string())
            print("\n SUCESSFULLY REFILLED")
        
        else:
            print("\n DATA NOT FOUND")