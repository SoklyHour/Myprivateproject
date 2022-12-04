from Covid19class import covid
import smtplib as smtp
import datetime as dt
time = dt.datetime.now()
now = time.strftime("%w-%m-%Y ")
Covid_track= True
while Covid_track:
    Input = int(input('Press 1 to get lastest record, Press 2 to filter specific date range: '))
    country = input('Enter The country Name: ')
    if Input == 1:
        content = covid.get_data_1(country)
        print(content)
        #Sent = input('Do you want to send to your email? Y or N: ')
    elif Input == 2:
        content = covid.get_data_2(country)
        print(content)    
        #if Y enter the email
    Sent = input('Do you want to send to your email? Y or N: ')
    if Sent == 'Y':
        username = 'hoursokly011@gmail.com'
        password = 'Hoursokly13092002' 
        subject = (f"Covid in {country}  ")
        defualt = 'hoursokly007@gmail.com'
        email = input('Enter Your Email: ') or 'hoursokly007@gmail.com'
        stmp_sever = "smtp.gmail.com"
        with smtp.SMTP(stmp_sever) as conn:
            conn.starttls()
            conn.login(username,password)
            conn.sendmail(username,f'{email}', f'subject: {subject}\n\n{content}')
            print("Sented")
    else:
        print("Email Dismiss!( no email sent)")
    disision = input("Do you want to continue the program? y or n: ")
    if disision == 'y':
     Covid_track = True
    elif disision == 'n':
     Covid_track = False
     print('Thank You For Using Our Application!')