from prettytable import PrettyTable
mytable=PrettyTable(['coffee name', 'coffee bean(kg)','water(ml)','sugar(kg)'])
mytable.add_row(['Americano',20,15,5])
mytable.add_row(['Latte',10,30,20])
mytable.add_row(['Cappuccino',22,10,10])
print(mytable)

table=PrettyTable(['sell id','firstname','lastname','coffee','sale'])
table.add_row([1,'Joe','Chea','Latte','$2'])
table.add_row([2,'Jack','Soun','Cappuccino','$2.5'])
print(table)