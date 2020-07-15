state = ''
msg = ''
title = ''


def nottiffyy(title2, msg2):
    notification.notify(
        title=title2,
        message=msg2,
        timeout=5)


def displayy(i):
    global state
    global msg
    global title
    totalCase = text['statewise'][i]['active'] + \
        text['statewise'][i]['confirmed']
    print(
        f"Total Covid state in {text['statewise'][i]['state']} is : {totalCase}(active + confirmed)")
    print(f"    Active Case =       {text['statewise'][i]['active']}")
    print(f"    Confirmed Cases =   {text['statewise'][i]['confirmed']}")
    print(f"    Deaths =            {text['statewise'][i]['deaths']}")
    print(f"    Migrated =          {text['statewise'][i]['migratedother']}")
    print(f"    Recovered =         {text['statewise'][i]['recovered']}")
    print(f"    Last Updated =      {text['statewise'][i]['lastupdatedtime']}")
    title = f'Current Covid - 19 Update in INDIA'
    msg = f"    Active Cases = {text['statewise'][0]['active']}\n    Confirmed Cases = {text['statewise'][0]['confirmed']}\n    Deaths Cases = {text['statewise'][0]['deaths']}"
    nottiffyy(title, msg)


def getinput():
    global state
    state = str(input('Enter The Desired state : '))


def searchh():
    global state
    for i in range(0, 38):
        if state.lower() == text['statewise'][i]['state'].lower():
            displayy(i)


if __name__ == '__main__':
    try:
        import os
        import requests
        import json
        import time
        from plyer import notification
    except Exception as e:
        print('Error Occured Trying to Resolve The Error')
        for i in range(0, 101):
            os.system("cls")
            print('\t\t\t\t\t\tGetting the Update\n\n------------------------------------------------------------------------------------------------------------------------\n\n')
            print(f'\t\t\t\t\tStatus of The Files Setup : {i}%')
            time.sleep(0.01)
        print('\t\t\t\t\tPlease Wait we Found The Error\n\t\t\t\t\tSetting Up the Files According to your Machine')
        os.system('pip install requests')
        os.system('pip install plyer')
        print('\n\nYou Have to Re Run the Application. As On the Next Run this Program will work fine')
    data = requests.get("https://api.covid19india.org/data.json")
    text = data.json()
    getinput()
    searchh()
