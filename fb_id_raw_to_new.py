import requests
import json

with open('facebook_id_raw.txt', 'r') as file_1:
    data = file_1.readlines()
    facebook_id_1 = []
    for line in data:
        facebook_id_raw = line.strip()
        url_profile = "http://10.0.8.31:8002/api/person/profile?facebook_id="+facebook_id_raw+"&apikey=PDRkXD7cmyRaHM8R5nGehRo5Z9KXpRnd"    
        url_profile_link = "http://10.0.8.31:8002/api/person/profile?link="+facebook_id_raw+"&apikey=PDRkXD7cmyRaHM8R5nGehRo5Z9KXpRnd"
        profile_res = requests.get(url_profile)
        profile_info = ""
        profile_info = profile_res.json()
        # print(facebook_id_raw)
        
        if("not match" in profile_info['message']):
            profile_res = requests.get(url_profile_link)
            profile_info = ""
            profile_info = profile_res.json()
            
            for each in profile_info['data']:
                if(each == 'fb_id'):
                    facebook_id_1.append(profile_info['data']['fb_id']) 
                    with open("facebook_id_new.txt", 'a', encoding='utf-8') as file_2:
                        file_2.write("%s\n" %(facebook_id_1[-1]))
                    file_2.close()
                elif('fb_id' not in profile_info['data']):
                    facebook_id_1.append(facebook_id_raw) 
                    with open("facebook_id_miss.txt", 'a', encoding='utf-8') as file_3:
                   
                        file_3.write("%s\n" %(facebook_id_raw))
                    file_3.close()
        elif(profile_info['message'] == 'success'):
            with open("facebook_id_new.txt", 'a', encoding='utf-8') as file_2:
             
                file_2.write("%s\n" %(facebook_id_raw))
            file_2.close()
        elif (profile_info['message'] == 'Given person not found'):
            with open("facebook_id_miss.txt", 'a', encoding='utf-8') as file_3:
               
                file_3.write("%s\n" %(facebook_id_raw))
            file_3.close()
            
file_1.close()  
