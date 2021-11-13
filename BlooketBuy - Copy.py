import requests
import time
import json




def addTokens(addUsername, addToken):

    addData = {'name': addUsername, 'addedTokens': 500, "addedXp": 500}
    addHeaders = {'Authorization': addToken}

    addData = json.dumps(addData)

    addResponse = requests.put('https://api.blooket.com/api/users/add-rewards', data=addData, headers=addHeaders)

    
    print(addResponse.text)







def buy(buyHeaders, buyUsername, box):
    buyData = {"name":buyUsername,"box":box}
    buyData = json.dumps(buyData)

    response = requests.get('https://api.blooket.com/api/users/tokens?name=' + username, headers=buyHeaders)
    print(response.text)
    response = int(''.join(filter(str.isdigit, response.text)))
    text = {'tokens' : response} 
    while text['tokens'] > 24:
    
        response = requests.put('https://api.blooket.com/api/users/unlockblook', data=buyData, headers=buyHeaders)
        print(response.text)
        text = json.loads(response.text)
        if text['isNewBlook'] == True:
            newblooks.append(text['unlockedBlook'])
            print('New Blook!')
    
        print(response.text)
    print(newblooks)
    sell(sellHeaders=buyHeaders, sellUsername=buyUsername, box=box)


def sell(sellHeaders, sellUsername, box):

    print('Selling Dupe Blooks...')
    blooks = requests.get('https://api.blooket.com/api/users/blooks?name=' + sellUsername, headers=sellHeaders)
    blooks = blooks.text
    blooks = json.loads(blooks)
    print(blooks)
    
    for key, value in blooks.items():
        if int(value) > 1:
            
            sellData = {'name': sellUsername, 'blook': key, 'numSold': int(value) - 1}
            sellData = json.dumps(sellData)
            sold = requests.put('https://api.blooket.com/api/users/sellblook', data=sellData, headers=sellHeaders)
            print(sold.text)
            print(key)



    response = requests.get('https://api.blooket.com/api/users/tokens?name=' + username, headers=sellHeaders)
    text = {'tokens' : int(response.text[1:-2])} 


    if text['tokens'] < 25:
        print('Worked')
    else:
        buy(buyUsername=sellUsername, buyHeaders=sellHeaders, box=box)
    





print('Which Box?')
box = input()
newblooks = []

addTokens(addUsername='hahayesboy', addToken='JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2MTg0ODI1NDJkOTU4YTIzZDUzZjUzOTkiLCJuYW1lIjoiaGFoYXllc2JveSIsImVtYWlsIjoicGFya2VyY2hhcmxlc3NtaXRoQGdtYWlsLmNvbSIsImdhbWVzUGxheWVkIjowLCJoYXNQYXNzd29yZCI6ZmFsc2UsInBsYW4iOiJTdGFydGVyIiwicm9sZSI6IlN0dWRlbnQiLCJzdHJpcGUiOiJjdXNfS1hMVW1Dc21QdnFRajkiLCJkYXRlQ3JlYXRlZCI6IjIwMjEtMTEtMDVUMDE6MDE6MDguMjg5WiIsImV4cCI6MTYzNzM3NDMwMn0.XKzSoGYOxK88vT1WAhC3wFkkxGtG5JwDd_1-pkmUmNU')
buy(buyUsername='hahayesboy',box=box, buyHeaders={'Authorization': 'JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2MTg0ODI1NDJkOTU4YTIzZDUzZjUzOTkiLCJuYW1lIjoiaGFoYXllc2JveSIsImVtYWlsIjoicGFya2VyY2hhcmxlc3NtaXRoQGdtYWlsLmNvbSIsImdhbWVzUGxheWVkIjowLCJoYXNQYXNzd29yZCI6ZmFsc2UsInBsYW4iOiJTdGFydGVyIiwicm9sZSI6IlN0dWRlbnQiLCJzdHJpcGUiOiJjdXNfS1hMVW1Dc21QdnFRajkiLCJkYXRlQ3JlYXRlZCI6IjIwMjEtMTEtMDVUMDE6MDE6MDguMjg5WiIsImV4cCI6MTYzNzM3NDMwMn0.XKzSoGYOxK88vT1WAhC3wFkkxGtG5JwDd_1-pkmUmNU'})

