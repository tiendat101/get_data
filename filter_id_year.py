import requests
import json
from datetime import date

with open('facebook_id_new.txt', 'r') as f1:
    data_line = f1.readlines()

    for line in data_line:
        facebook_id = ""
        facebook_id = line.strip()
        facebook_id = str(facebook_id)
        
        url_profile = "http://10.0.8.31:8002/api/person/profile?facebook_id="+facebook_id+"&apikey=PDRkXD7cmyRaHM8R5nGehRo5Z9KXpRnd" 
    
        profile_res = requests.get(url_profile)
        profile_info = ""
        profile_info = profile_res.json()
        year = 0
        age = 0
         
        for each in profile_info['data']:
            
            if (each == "Ngày sinh"):
                year_info = profile_info['data']['Ngày sinh']
                
                if(',' in year_info):
                    year = int(year_info[-4:])
                    current_year = date.today().year
                    age = current_year -year
                    # print(age)
                    with open('id_has_year_of_birth.txt', 'a', encoding='utf-8') as id_has_year_of_birth:
                        id_has_year_of_birth.write("%s\n" % (facebook_id))
                    id_has_year_of_birth.close()
                    break
            elif (each == "Birthday"):
                year_info = profile_info['data']['Birthday']
                if(',' in year_info):
                    year = int(year_info[-4:])
                    current_year = date.today().year
                    age = current_year -year
                    # print(age)
                    with open('id_has_year_of_birth.txt', 'a', encoding='utf-8') as id_has_year_of_birth:
                        id_has_year_of_birth.write("%s\n" % (facebook_id))
                    id_has_year_of_birth.close()
                    break
                    
            elif (each == "Năm sinh"):
                year = int(profile_info['data']['Năm sinh'])
                current_year = date.today().year
                age = current_year -year
                # print(age)
                with open('id_has_year_of_birth.txt', 'a', encoding='utf-8') as id_has_year_of_birth:
                    id_has_year_of_birth.write("%s\n" % (facebook_id))
                id_has_year_of_birth.close()
                break
                
            elif (each == "Year of birth"):
                year = int(profile_info['data']['Year of birth'])
                current_year = date.today().year
                age = current_year -year
                # print(age)
                with open('id_has_year_of_birth.txt', 'a', encoding='utf-8') as id_has_year_of_birth:
                    id_has_year_of_birth.write("%s\n" % (facebook_id))
                id_has_year_of_birth.close() 
                break
               
        else:
            with open('id_doesnot_has_year_of_birth.txt', 'a', encoding='utf-8') as id_doesnot_has_year_of_birth:
                id_doesnot_has_year_of_birth.write("%s\n" % (facebook_id))
            id_doesnot_has_year_of_birth.close()  
        
                     
f1.close()