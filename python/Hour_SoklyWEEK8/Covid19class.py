import requests
from requests.api import get
class covid:
    def get_data_1(country):
        base_url= requests.get(f"https://api.covid19api.com/total/dayone/country/{country}")
        confirm =(base_url.json()[-1]["Confirmed"])
        recover = (base_url.json()[-1]["Recovered"])
        dead = (base_url.json()[-1]["Deaths"])
        active = (base_url.json()[-1]["Active"])
        date = (base_url.json()[-1]["Date"])
        user_info= f'''
        Today data[{date}]

        .......................
        active: {active}
        
        confirmed: {confirm}

        deaths: {dead}

        recovered: {recover} 
        '''
        return user_info
    def get_data_2(country):
        lst =[]
        start_date= input('Enter Starting Date: ')
        end_date = input('Enter Ending Date: ')
        base_url_2 =requests.get(f"https://api.covid19api.com/country/{country}?from={start_date}T00:00:00Z&to={end_date}T00:00:00Z")
        data = base_url_2.json()
        for content in data:
            conf=content["Confirmed"]
            recover = (content["Recovered"])
            dead = (content["Deaths"])
            active = (content["Active"])
            date = (content["Date"])
            user_info_2=f'''
            Data for [{date}] 
            
            ......................
            active: {active}

            confirmed: {conf}

            deaths : {dead}

            recovered: {recover}

            '''
            lst.append(user_info_2)
        return (' '.join(lst))


   