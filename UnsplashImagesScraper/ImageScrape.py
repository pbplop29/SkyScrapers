import requests # The requests module allows you to send HTTP requests using Python.
import os




# ---------------------------------------------------------------------------- #
#                            BAD APPORACH THAT WORKS                           #
# ---------------------------------------------------------------------------- #

#tag = "plane"
#url = "https://unsplash.com/napi/search?query=" + tag + "&per_page=20&xp=" # defining the url by getting the GET method
# r = requests.get(url) # requesting to get the url
# #print(r.status_code) # if it prints 200, then we succesfully connected and we got our response back
# data = r.json() # gets all the json from the request
# #print(data) # prints the fetched json data
# data_photos = data['photos'] # access to the photos section of the data thingy
# #print(data_photos)
# for item in data_photos['results']:
#     name = item['id']
#     url = item['urls']['thumb']
#     with open(name+".jpg", "wb") as f:
#         f.write(requests.get(url).content) # saves images 


# ---------------------------------------------------------------------------- #
#                                APPROACH TO USE                               #
#           Better approach in terms of scalability and code writing           #
# ---------------------------------------------------------------------------- #

class Unsplash():#class
    def __init__(self, search_term,quality,per_page=20): # constructor - a method automatically called whenver we instantiate an object of a class
        self.search_term = search_term
        self.folder = search_term
        self.per_page = per_page
        self.page = 1
        self.quality = quality
        self.headers={
            "Accept":	"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Encoding":	"gzip, deflate, br",
            "Accept-Language":	"en-US,en;q=0.5",
            "Host":	"unsplash.com",
            "User-Agent":	"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0"
        }

    def set_url(self): # method that sets the url
        # we will make a changeable search query item in the url based on the search_term prop
        # same for per page as well
        return f"https://unsplash.com/napi/search/photos?query={self.search_term}&per_page={self.per_page}&page={self.page}&xp="
        #return f"https://unsplash.com/napi/search?query={self.search_term}&per_page={self.per_page}&xp="

    def make_request(self): # method to make request
        url = self.set_url()
        return requests.request("GET", url, headers = self.headers)

    def get_data(self):
        self.data = self.make_request().json() # added .json() at the end so that the data retrieved is json data

    def save_path(self,name):
        download_dir = self.folder
        project_dir = "UnsplashImagesScraper"
        path = os.path.join(project_dir, download_dir)
        if not os.path.exists(os.path.join(os.getcwd(),path)): # if the path doesnt exist we will create one
           os.mkdir(path)
        return f"{os.path.join(os.path.realpath(os.getcwd()),project_dir, download_dir, name)}.jpg" 
        # getcwd gives us the current working directory and realpath dereferences all the symbolic
        #links on the OS that support them
        #join will then join the working_dir + download_dir + name + extension which is the file path

    def download(self,url,name):
        filepath = self.save_path(name)
        with open(filepath, "wb") as f: # wb = write byte mode
            f.write(requests.request("GET",url).content)

    def scraper(self,pages):
        for page in range(0,pages+1):
            self.make_request()
            self.get_data()
            for item in self.data['results']:
                name = item['id']
                url = item['urls'][self.quality]
                self.download(url, name)
            self.page+=1


if __name__ == "__main__":
    #enter name and quality here 
    
    scraper = Unsplash("fruit","raw")
    scraper.scraper(1)

# Adding headers to our script can help us not get blocked from the servers
# We can also add proxies -> buy good proxies and then use