input("Welcome to Dollar curency conversion APP")
input("Type 0 if is not currency that you want to convert to")
USD_Euro = input("Convert Dollar to Euro= ")
USD_Riel = input("Convert Dollar to Riel= ")
USD_Yuan = input("Convert Dollar to Yuan= ")
USD_toEuro = float(USD_Euro) * 0.85
USD_toRiel = float(USD_Riel) * 4080.91
USD_toYuan = float(USD_Yuan) * 6.45

Convert=f'''
------------------------
Currency Exchange
USD $ to Euro € = {USD_toEuro}€
USD $ to Riel ៛ = {USD_toRiel}៛
USD $ to Yuan ¥ = {USD_toYuan}¥
------------------------
Thank You for using our app
'''
print(Convert)