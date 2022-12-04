input('Welcome to myAPP(waf waf)registration, press any key to start')
firstname = input('First Name:')
lastname = input('Last Name:')
date_of_birth = input('Date of Birth:')
dog_age = input('Your dog age:')
dog_age_human = int(dog_age) * 7 

user_info = f'''

Registration Information

First Name : {firstname}
Last Name : {lastname}
was born on {date_of_birth}
----------------------------------------------------------
Owning a dog which age equivalent of {dog_age_human} age
----------------------------------------------------------

'''
print(user_info)