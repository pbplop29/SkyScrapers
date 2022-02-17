import requests # The requests module allows you to send HTTP requests using Python.


url = "https://unsplash.com/napi/search?query=dog&per_page=20&xp=" # defining the url by getting the GET method

r = requests.get(url) # requesting to get the url

#print(r.status_code) # if it prints 200, then we succesfully connected and we got our response back

data = r.json() # gets all the json from the request

#print(data) # prints the fetched json data

data_photos = data['photos'] # access to the photos section of the data thingy

#print(data_photos)

for item in data_photos['results']:
    name = item['id']
    url = item['urls']
