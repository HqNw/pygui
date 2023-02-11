import requests
import json
import uuid
import time
import timeit

gender = ["male" , "female"]
for i in range (1000):
    index = i%2
    r = requests.get(f"https://randomuser.me/api/?inc=gender,name,email,id&noinfo")

    res = r.json()
    # res = eval(f"{res['results']}")
    print(type(res))
    print(res)

    response = json.dumps(res)
    response = json.loads(response)
    print(type(response))
    
    print(response)
    print(response["results"][0]["gender"])
    print(response["results"][0]["name"]["first"])
    print(response["results"][0]["email"])
    print(response["results"][0]["id"]["name"])
    data ={

        "ID": str(uuid.uuid1()),
        "Name": response["results"][0]["name"]["first"],
        "Age": str(i),
        "Gender": response["results"][0]["gender"],
        "Email": response["results"][0]["email"],
        "Address": response["results"][0]["id"]["name"] 
    }
    
    with open("data.txt", "a") as f:
        f.write(str(data) + "\n")
    # time.sleep(.5)

