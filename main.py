import requests
from dotenv import load_dotenv
load_dotenv()
import os
from pprint import pprint

def reduce_url(user_url):
    
        
        data =  {"long_url": user_url}
        response = requests.post('https://api-ssl.bitly.com/v4/shorten', headers=headers, json=data)
        try:
            return response.json()['id']
        except KeyError:
            print("АОАОАОА там написано лалка")


while True:
    bitly_token = os.getenv("TOKEN")

    headers = {
        'Authorization': f'Bearer {bitly_token}',
        'Content-Type': 'application/json',
    }


    print("1-Посмотреть профиль,2-Сокращение ссылки,3-Выход")

    while True:
        try: 
            function_number=int(input("Выберите функцию: "))
            break
        except ValueError:
            print("Низя текст")

        

    
    
    if function_number==3:
        exit()

    if function_number==1:
        
        response = requests.get('https://api-ssl.bitly.com/v4/user', headers=headers)
        print("ВАША ПОЧТА",response.json()['emails'][0]['email'])
        print("ваша логин",response.json()['login'])
        print("ваша имён",response.json()['created'])
    
    
    if function_number==2:
        user_url=input("Твоя ссылка ")  
        reduced_url= reduce_url (user_url=user_url)
        print(reduced_url)

    
    

   


















