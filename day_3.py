import requests

def url(address):
    arr = []
    address = address.replace(" ", "")
    address_2 = address.split(',')
    for i in address_2:
        i.lower()
        if "http" in i :
            arr.append(i)
        else:
            i = "http://" + i
            arr.append(i)
    return arr

def check(real_address):
    for i in real_address:
        r = requests.get(i)
        if(r.status_code == requests.codes.ok):
            return True
        else:
            return False



real_address=[]
print("Welcome to IsItDown.py!")
address=input('Please write a URL or URL_s you want to check.(seperated by comma)')
real_address=url(address)
check_address=check(real_address)
if(check_address == True):
    print ("Do you want to start over?")
    n = input ('y/n')
else:
    print ("Not invalid url")