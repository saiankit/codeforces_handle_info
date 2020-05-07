from tkinter import *
import urllib.request,urllib.parse,urllib.error
import http,json
class CodeForcesInfo:
    def __init__(self):
        window = Tk() 
        window.geometry("800x400")                   #Create a GUI Window
        window.config(background = "white")
        window.title("CodeForces Info")  #Set title of GUI Window
        Label(window, text = "Enter the Handle").grid(row = 1, column = 1,sticky = W)
        Label(window, text = "Name").grid(row = 2, column = 1,sticky = W)
        Label(window, text = "Rating").grid(row = 3, column = 1,sticky = W)
        Label(window, text = "Rank").grid(row = 4, column = 1,sticky = W)
        Label(window, text = "Country").grid(row = 5, column = 1,sticky = W)
        Label(window, text = "City").grid(row = 6, column = 1,sticky = W)
        Label(window, text = "Organisation").grid(row = 7, column = 1,sticky = W)
        #Declaring the variables
        self.handleID = StringVar()
        self.name = StringVar()
        self.rating = StringVar()
        self.rank = StringVar()
        self.country = StringVar()
        self.city = StringVar()
        self.organisation = StringVar()
        self.existence = StringVar()
        #Entry box for taking handle inputs
        Entry(window, textvariable = self.handleID, justify = LEFT).grid(row = 1,column = 2)
        #Instantiating the variables
        handleName = Label(window, textvariable = self.name).grid(row = 2 , column = 2 , sticky = E)
        handleRating = Label(window, textvariable = self.rating).grid(row = 3 , column = 2 , sticky = E)
        handleRank = Label(window, textvariable = self.rank).grid(row = 4 , column = 2 , sticky = E) 
        handleCountry = Label(window, textvariable = self.country).grid(row = 5 , column = 2 , sticky = E) 
        handleCity = Label(window, textvariable = self.city).grid(row = 6 , column = 2 , sticky = E) 
        handleOrganisation = Label(window, textvariable = self.organisation).grid(row = 7 , column = 2 , sticky = E)
        handleExistence = Label(window, textvariable = self.existence).grid(row = 8,column = 1,sticky = E)
        #Button Creation
        btSubmit = Button(window, text = "Submit", command = self.showInfo).grid(row = 8 , column = 2, sticky = E)
        window.mainloop()#TheEventLoop
    def showInfo(self):
        serviceurl = 'https://codeforces.com/api/user.info?'
        NOT_EXISTING = 'Not Existing'
        handles = self.handleID.get()
        names = dict()
        names['handles'] = handles
        url = serviceurl + urllib.parse.urlencode(names)
        try:
            uh = urllib.request.urlopen(url)
        except Exception as e:
            self.existence.set("Invalid Handle")
            self.clearScreen()
        data = uh.read().decode()
        try:
            js = json.loads(data)
        except:
            js = None
        if not js or 'status' not in js or js['status'] != 'OK':
            print('==== Failure To Retrieve ====')
            print(data)
        presentKeys = js['result'][0]
        if 'firstName' in js['result'][0] and 'lastName' in js['result'][0]:
            self.name.set(js['result'][0]['firstName'] + ' ' +  js['result'][0]['lastName'])
        elif 'lastName' in js['result'][0] == False:
           self.name.set(js['result'][0]['firstName'])
        elif 'firstName' in js['result'][0] == False: 
            self.name.set(js['result'][0]['lastName'])
        else:
            self.name.set(NOT_EXISTING)
        if 'rating' in presentKeys:
            self.rating.set(js['result'][0]['rating'])
        else :
            self.rating.set(NOT_EXISTING)
        if 'rank' in presentKeys:
            self.rank.set(js['result'][0]['rank'])
        else :
            self.rank.set(NOT_EXISTING)
        if 'country' in presentKeys:
            self.country.set(js['result'][0]['country'])
        else :
            self.country.set(NOT_EXISTING)
        if 'city' in presentKeys:
            self.city.set(js['result'][0]['city'])
        else :
            self.city.set(NOT_EXISTING)
        if 'organisation' in presentKeys:
            self.organisation.set(js['result'][0]['organization'])
        else :
            self.organisation.set(NOT_EXISTING)
        if 'organization' in presentKeys:
            self.organisation.set(js['result'][0]['organization'])
        else :
            self.organisation.set(NOT_EXISTING)
    def clearScreen(self):
        self.rating.set(" ")
        self.rank.set(" ")
        self.country.set(" ")
        self.city.set(" ")
        self.organisation.set(" ")
CodeForcesInfo()             