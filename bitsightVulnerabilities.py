import requests
import time

api_key = "USER_APIKEY"
url = "https://api.bitsighttech.com/ratings/v1/companies/XXXXXX/findings?limit=10000000&grade=WARN&grade=BAD&affects_rating=true" 


response = requests.get(url, auth=(api_key, ""))

json = response.json()
#print(json['results'])

for result in json['results']:
    #time.sleep(2)
    print("------------------------------------\n\n")
    try:
        print(result['evidence_key'] + ' -->\n')
        print(result['risk_vector_label'] + ' :')
    except KeyError:
        pass
        
    try:
        print(result['details']['diligence_annotations']['message'])
        print(result['details']['diligence_annotations']['risks'])
        print(result['remediations']['message'])
    except KeyError:
        pass