import requests
import json
import objectpath
import random
from time import time 
import re
import numpy as np
from datetime import date

random.seed(1)
punctuation_dataset = './punctuation_dataset.txt'
slang_dataset = './slang_dataset.txt'
time_start = time()

# get data from punctuation_dataset
with open(punctuation_dataset, 'r') as punc_dataset:
    punc_data = punc_dataset.readlines()
    punc_text = []
    for line in punc_data:
        punc_text.append(line.strip())
punc_dataset.close()

# get data from slang_dataset
with open(slang_dataset, 'r', encoding='utf-8') as slang_dataset:
    slang_data = slang_dataset.readlines()
    slang_text = []
    for line in slang_data:
        slang_text.append(line.strip())
slang_dataset.close()

def count_letter_for_each_sentences(text):
    count_avg = 0
    count = [] 
    regex = r"(?<!\w\.\w.\:)(?<![A-Z][a-z]\.)(?<=\.|\?)\s"

    # print(len(text))
    subst = "|||| "

    result = re.sub(regex,subst,text,0,re.MULTILINE)
    
  # print(result)
    result = result.split("||||")
    # print(result)
    
    
    for each in result:
        count.append(len(each))

    count_avg = np.mean(count) 
    # print(count)
    # print(count_avg)
    return count_avg
    
with open('./facebook_id_new.txt', 'r') as f1:
    data_line = f1.readlines()
   
    for line in data_line:
        facebook_id = ""
        facebook_id = line.strip()
        facebook_id = str(facebook_id)
        url_status = "http://10.0.8.31:8002/api/list/status?skip=0&limit=500&order_date=desc&owner_type=0&apikey=PDRkXD7cmyRaHM8R5nGehRo5Z9KXpRnd&owner_id=" + facebook_id     
        url_page = "http://10.0.8.31:8002/api/person/pages?facebook_id=" + facebook_id + "&limit=200&apikey=PDRkXD7cmyRaHM8R5nGehRo5Z9KXpRnd"
        url_comment = "http://10.0.8.31:8002/api/person/comments?facebook_id=" + facebook_id + "&limit=500&apikey=PDRkXD7cmyRaHM8R5nGehRo5Z9KXpRnd" 
        url_profile = "http://10.0.8.31:8002/api/person/profile?facebook_id="+ facebook_id +"&apikey=PDRkXD7cmyRaHM8R5nGehRo5Z9KXpRnd" 
        # get info from profile data    

        # gender
        profile_res = requests.get(url_profile)
        profile_info = ""
        profile_info = profile_res.json()
        for each in profile_info['data']:
            if (each == "Giới tính"):
                gender = profile_info['data']['Giới tính']
                break
            elif (each == "Gender"):
                gender = profile_info['data']['Gender']
                break
            gender_random = random.randint(0,1)
            if(gender_random == 0):
                gender = "Nam"
            else:
                gender = "Nữ"
        gender_last = ''
        if(gender=="Nữ" or gender == "Female"):
            gender_last = 'F'
        else:
            gender_last = 'M'
        
        # num_follow
        for each in profile_info['data']:
            if (each == "num_follow"):
                num_follow = profile_info['data']['num_follow']
                break
            num_follow = str(10)

        # teenager or not
        year = 0
        age = 0
        for each in profile_info['data']:
            if (each == "Ngày sinh"):
                year_info = profile_info['data']['Ngày sinh']
                
                if(',' in year_info):
                    year = int(year_info[-4:])
                    current_year = date.today().year
                    age = current_year - year
                break

            elif (each == "Birthday"):
                year_info = profile_info['data']['Birthday']
                if(',' in year_info):
                    year = int(year_info[-4:])
                    current_year = date.today().year
                    age = current_year - year
                break

            elif (each == "Năm sinh"):
                year = int(profile_info['data']['Năm sinh'])
                current_year = date.today().year
                age = current_year - year
                break

            elif (each == "Year of birth"):
                year = int(profile_info['data']['Year of birth'])
                current_year = date.today().year
                age = current_year - year
                break

        if(age != 0):
            if(age < 28):
                teenager = 0
            elif(29<=age and age<=39):
                teenager = 1
            elif(40<=age and age<=54):
                teenager = 2
            elif(age>55):
                teenager = 3
        else:    
            age_random = random.randint(0,100)
            if(age_random < 28):
                teenager = 0
            elif(29<=age_random and age_random<=39):
                teenager = 1
            elif(40<=age_random and age_random<=54):
                teenager = 2
            elif(age_random>55):
                teenager = 3

        # get info from status data
        status_res = requests.get(url_status)
        status_info = ""
        status_info = status_res.json() 
        
        # count letter for each sentences 
        status_detail = []
        count_avg = []
        count_avg_avg = []
        for i in range(0, len(status_info['data'])):
            status_detail.append(status_info['data'][i]['content'])
            count_avg.append(count_letter_for_each_sentences(status_detail[i]))
        if (len(count_avg)!=0):
            count_avg_avg = np.mean(count_avg)  
        else:
            count_avg_avg = random.randint(0,100)
        # print("count_avg_avg: ", count_avg_avg)
        
        #url    
        link_att_count = 0
        status_num = len(status_info['data'])

        for i in range(0, status_num):
            if(status_info['data'][i]['link_attachment'] != ""):
                link_att_count = link_att_count + 1
        
        if(link_att_count > status_num/2):
            link_att = "YES"
        else:
            link_att = "NO"

        #slang
        sst_content = []
        for i in range(status_num):
            sst_content.append(status_info['data'][i]['content'].lower())

        slang_list = []
        for i in range(len(sst_content)):
            for j in range(len(slang_text)):
                if (slang_text[j] in sst_content[i]):
                    slang_list.append('YES')
                    break
            else:
                slang_list.append('NO')

        slang_count = 0
        for i in range(len(slang_list)):
            if (slang_list[i] == 'YES'):
                slang_count = slang_count + 1

        if(slang_count >= 0.2*len(slang_list)):
            slang = 'YES'
        else:
            slang = 'NO'
        # get info from comment
        comment_res = requests.get(url_comment)
        comment_info = ""
        comment_info = comment_res.json()
        comment_detail = [] 
        for i in range(0, len(comment_info['data'])):
            comment_detail.append(comment_info['data'][i]['comment']['content'])

        # punc 20%use: punc: yes
        punc_list = []
        for i in range(len(comment_detail)):
            for j in range(len(punc_text)):
                if (punc_text[j] in comment_detail[i]):
                    punc_list.append('YES')
                    break
            else:
                punc_list.append('NO')

        punc_count = 0
        for i in range(len(punc_list)):
            if (punc_list[i] == 'YES'):
                punc_count = punc_count + 1

        if(punc_count >= 0.2*len(punc_list)):
            punc = 'YES'
        else:
            punc = 'NO'

        # order:slang-punctuation-url-characters numeric-follow num-status num-topic num-gender-teenager
        with open("./data_preprocessed.txt", "a", encoding='utf-8') as f2:
            f2.write("%s,%s,%s,%.3f,%s,%d,%s,%s\n" %(slang, punc, link_att, count_avg_avg, num_follow, status_num, gender_last, teenager))
        f2.close()
    
        # data = response.text
        # parsed = json.loads(data)
        # data_end = json.dumps(parsed, indent=4, ensure_ascii=False)
        
        # with open(f_name, "a", encoding='utf-8') as f:
        #     f.write(data_end)
        #     f.write('\n')
        # f.close()
f1.close()
time_total = time() - time_start
print("time total: %.4fs" %(time_total))

