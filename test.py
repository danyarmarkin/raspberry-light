import requests
a = 0
session = requests.Session()
while True:
    # get response from firebase of compass data
    r = session.get('https://camera-scan-e5684-default-rtdb.europe-west1.firebasedatabase.app/compassData.json?print=pretty')
    print(r.text)
    print(a)
    a += 1