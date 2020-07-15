def refresh():
    print('It has been Refreshed')


statelist = [
    "Andaman and Nicobar Islands",
    "Andhra Pradesh",
    "Arunachal Pradesh",
    "Assam",
    "Bihar",
    "Chandigarh",
    "Chhattisgarh",
    "Dadra and Nagar Haveli and Daman and Diu",
    "Delhi",
    "Goa",
    "Gujarat",
    "Haryana",
    "Himachal Pradesh",
    "Jammu and Kashmir",
    "Jharkhand",
    "Karnataka",
    "Kerala",
    "Ladakh",
    "Lakshadweep",
    "Madhya Pradesh",
    "Maharashtra",
    "Manipur",
    "Meghalaya",
    "Mizoram",
    "Nagaland",
    "Odisha",
    "Puducherry",
    "Punjab",
    "Rajasthan",
    "Sikkim",
    "Tamil Nadu",
    "Telangana",
    "Tripura",
    "Uttar Pradesh",
    "Uttarakhand",
    "West Bengal",
]

text = ''
optionVal = ''
numberOfSubmit = 0


def getdata():
    global text
    data = requests.get("https://api.covid19india.org/data.json")
    text = data.json()


def printdata():
    global numberOfSubmit
    global optionVal
    state = optionVal
    global text
    print('This is for Debugging')
    print(numberOfSubmit)
    if(numberOfSubmit == 1):
        numberOfSubmit = 0
        label.pack_forget()
    for i in range(0, 38):
        if state.lower() == text['statewise'][i]['state'].lower():
            label = Label(
                text=f"Active Cases           = {text['statewise'][i]['active']}").pack(anchor=W)
            label1 = Label(
                text=f"Confirmed Cases   = {text['statewise'][i]['confirmed']}").pack(anchor=W)
            label2 = Label(
                text=f"Deaths                     = {text['statewise'][i]['deaths']}").pack(anchor=W)
            label3 = Label(
                text=f"Migrated                 = {text['statewise'][i]['migratedother']}").pack(anchor=W)
            label4 = Label(
                text=f"Recovered               = {text['statewise'][i]['recovered']}").pack(anchor=W)
            label5 = Label(
                text=f"Last Updated          = {text['statewise'][i]['lastupdatedtime']}").pack(anchor=W)
            numberOfSubmit = 1


def getstats():
    global numberOfSubmit
    getdata()
    printdata()


def body():
    global optionVal
    label = Label(
        text='Welcome to the COVID 19 Tracker System Made with Love in Python By Aman Ojha')
    label.pack(padx=0, pady=10)
    stateName = Label(text='Enter Your State Name')
    stateName.pack(anchor=NW, pady=5, padx=15)
    option = StringVar(root)
    option.set(statelist[33])
    opt = OptionMenu(root, option, *statelist)
    opt.config(width=15, font=('sanssarif', 8))
    opt.pack()
    button = Button(text='Submit', command=getstats)
    button.pack(anchor=CENTER)
    optionVal = option.get()


def main():
    mymenu = Menu(root)
    file = Menu(mymenu, tearoff=0)
    file.add_command(label='Refresh', command=refresh)
    file.add_command(label='Exit', command=exit)
    mymenu.add_cascade(label='File', menu=file)
    root.config(menu=mymenu)
    body()


if __name__ == '__main__':
    try:
        from tkinter import *
        import os
        import datetime
        import requests
    except Exception as e:
        os.system('pip install requests')
    else:
        root = Tk()
        root.title('COVID update Software')
        root.geometry("655x333")
        root.minsize(655, 333)
        root.maxsize(655, 333)
        main()
        root.mainloop()
