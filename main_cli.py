import urllib.request,urllib.parse,urllib.error
import http,json
# API URL
serviceurl = 'https://codeforces.com/api/user.info?'
NOT_EXISTING = 'Not Existing'
while True:
    while True:
        handles = input('Enter the handle name: ')
        names = dict()
        names['handles'] = handles
        url = serviceurl + urllib.parse.urlencode(names)
        try:
            uh = urllib.request.urlopen(url)
        except Exception as e:
            print('Invalid Handle')
            break
        data = uh.read().decode()
        try:
            js = json.loads(data)
        except:
            js = None
        if not js or 'status' not in js or js['status'] != 'OK':
            print('==== Failure To Retrieve ====')
            print(data)
            continue
        presentKeys = js['result'][0]
        if 'firstName' in js['result'][0] and 'lastName' in js['result'][0]:
            Name =  js['result'][0]['firstName'] + ' ' +  js['result'][0]['lastName']
        elif 'lastName' in js['result'][0] == False:
            Name =  js['result'][0]['firstName']
        elif 'firstName' in js['result'][0] == False: 
            Name =  js['result'][0]['lastName']
        else:
            Name = 'Not Existing'
        if 'country' in presentKeys:
            country =  js['result'][0]['country']
        else :
            country = NOT_EXISTING
        if 'city' in presentKeys:
            city = js['result'][0]['city']
        else :
            city = NOT_EXISTING
        if 'organisation' in presentKeys:
            org = js['result'][0]['organization']
        else :
            org = NOT_EXISTING
        if 'organization' in presentKeys:
            org = js['result'][0]['organization']
        else :
            org = NOT_EXISTING
        if 'rank' in presentKeys:
            rank = js['result'][0]['rank']
        else :
            rank = NOT_EXISTING
        if 'rating' in presentKeys:
            currentRating = js['result'][0]['rating'] 
        else :
            currentRating = NOT_EXISTING
        len_name = len(Name) + len('  | Name            :')
        len_country = len(country) + len('  | Country         :')
        len_city = len(city) + len('  | City            :')
        len_org = len(org) + len('  | Organisation    :')
        len_rank = len(rank) + len('  | Rank            :')
        len_rate = len(str(currentRating)) + len('  | Present rating  :')
        lens = [len_name,len_country,len_city,len_org,len_rate]
        maxlen = max(lens)
        #Printing the Output
        print(' ','-'*maxlen)
        print(' | Name            :',Name,' '*(maxlen-len_name),'|')    
        print(' | Country         :',country,' '*(maxlen-len_country),'|')
        print(' | City            :',city,' '*(maxlen-len_city),'|')
        print(' | Organisation    :',org,' '*(maxlen-len_org),'|')
        print(' | Rank            :',rank,' '*(maxlen-len_rank),'|')
        print(' | Present rating  :',currentRating,' '*(maxlen-len_rate),'|')
        print(' ','-'*maxlen)