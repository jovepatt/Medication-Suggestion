import pickle
import re
import warnings
warnings.filterwarnings("ignore")
import requests
from bs4 import BeautifulSoup
import time

# Fetch Medication list from 'https://www.drugs.com/medical_conditions.html'
small_alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
medication=[]
for c in small_alpha:
    URL = 'https://www.drugs.com/medical_conditions.html/'+c
    time.sleep(1)
    page = requests.get(URL,verify=False)

    soup = BeautifulSoup(page.content, 'html5lib')
    all_medications = soup.find('div', class_='all-medication')

    for element in all_medication.find_all('li'):
        medication.append(element.get_text().strip())

with open('list_medicationNames.pkl', 'rb') as handle:
    medication2 = pickle.load(handle)


# Save the dictionary in PICKLE file
med_symp = tmp_dict
print(len(med_symp))
with open('final_dis_symp.pickle', 'wb') as handle:
   pickle.dump(med_symp, handle, protocol=pickle.HIGHEST_PROTOCOL)
