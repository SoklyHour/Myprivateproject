from prettytable import PrettyTable
import mysql.connector, datetime, operator

class Db:

    def __init__(self):
        self.cnx = mysql.connector.connect(host="127.0.0.1",port="3307", user="root", password="", database="cs_coffee") 
        self.cursor = self.cnx.cursor(buffered=True)

    def show_coffee (self):
        coffees_cursor = self.cursor
        coffees_sql = "SELECT coffee_tb.coffee_id, coffee_tb.coffee_name, coffee_tb.coffee_price \
                From coffee_tb"
        coffees_cursor.execute(coffees_sql)
        coffees_data = coffees_cursor.fetchall()
        p = PrettyTable()
        p.field_names = ["Coffee ID", "Coffee Name", "Price"]
        p.add_rows(coffees_data)
        print(p.get_string())

    def get_coffee_resource (self, coffee_id):
        coff_sql = f"SELECT material_tb.mat_coffee_bean, material_tb.mat_water, material_tb.mat_sugar, coffee_tb.coffee_price \
        FROM coffee_tb \
        INNER JOIN material_tb ON coffee_tb.mat_id = material_tb.mat_id \
        WHERE coffee_id={coffee_id}"        
        self.cursor.execute(coff_sql)
        self.cnx.commit()
        coffee_data = self.cursor.fetchone()
        return coffee_data

    def get_resource(self):
        resource_cursor = self.cursor
        resource_sql = "SELECT resource_tb.coffee_bean, resource_tb.water, resource_tb.sugar \
                From resource_tb"
        resource_cursor.execute(resource_sql)
        self.cnx.commit()
        resource_data = resource_cursor.fetchone()
        return resource_data
    
    def check_material(self, resources, coffee):
        coffee = coffee[0], coffee[1], coffee[2]
        if resources >= coffee:
            self.make_coffee(valid=True)
        elif resources < coffee:
             self.make_coffee(valid=False)
        else:
            return "\n The coffee gods have decided you are unworthy."

    def make_coffee(self, valid):
        while True:
            if valid == True:
                print("\n Your order has processed successfully.")
                break
            elif valid == False:
                print("\n Try adding to our inventory to order successfully.")
                break
            else:
                print("\n The coffee gods have decided you are unworthy.")
                quit()


    def update_resource(self, coffee_id):
        coffee_material = self.get_coffee_resource(coffee_id=coffee_id)
        coffee_mat_list = coffee_material[0], coffee_material[1], coffee_material[2]
        table_resource = self.get_resource()
        self.check_material(resources=table_resource, coffee=coffee_material)
        update_resource = list(map(operator.sub, table_resource, coffee_mat_list))
        resource_sql = "UPDATE resource_tb \
                        SET water= %s, coffee_bean= %s, sugar= %s \
                        WHERE resource_id =1"
        self.cursor.execute(resource_sql, update_resource)
        self.cnx.commit()