> :bulb: **_TIP:_** Use Mozilla Firebox because it has really great dev tools.

> :no*entry: \*\*\_CAUTION:*\*\* This is just for educational purposes and personal projects don't try to scrape information if not authorized.

# How to proceed?

- Go to the unsplash webpage. https://unsplash.com/
- Inspect Element
- Network Tab
- XHR Tab
- Here you will be able to see all the requests that are made by the page.
- Our goal is to extract the request to the API that provides the images.

```
* We are interested in json requests that are structured like:
  - search?query=dog&per_page=20&xp=
  - This has a search query and looks like its being sent to an API.
```

- We don't even need bs4 and just request library to extract these images.

# Script writing and analysis of the URLs and Webpage

- If we look at the URL **search?query=dog&per_page=20&xp=** we can see that the query parameter has the keyword **dog**, if we change it by **cat** we will indeed get the request to images of cats.
- Also the request is using a **GET** method to call for these images.
- The **per_page=20** parameter is the one that defines how many images we are calling for in the given page.The maximum the API can allow can be restricted.

> ## Explaining the class and methods called in script
>
> 1. **_class Unsplash()_** - the class we will be operating under
> 2. **_def \_\_init\_\_(<props>)_** - the constructor that we will be using to create object of above class
>
> 3) **_def set_url()_** - sets the url using the props passed in constructor
> 4) **_def make_request()_** - makes get request to the url from above
> 5) **_def get_data()_** - gets data from above request in json format
> 6) **_def save_path()_** - checks and creates the necessary folder paths if needed
> 7) **_def download()_** - saves the images after scraping
> 8) **_def scrapper()_** - actual scraping of the website

> ## Now create a new object of Unsplash class inside main and then call the scraper function to it
>
> 1. item = Unsplash("fruit","raw") when creating th object of the given class pass in (search_item, quality)
>    - raw - best
>    - full
>    - regular
>    - small
>    - thumb - worst
> 2. When calling item.scraper(1) function pass in (no_of_pages)

# Questions?

> Why not use the API that the website is using directly by ourselves?
>
> - There are going to be restrictions.

# Tricks to not get blocked by the site.

> 1. **_Make use of headers_**
>
> - Go to the header section in the dev tools
> - Copy the essential and bring to the code
> - Pass headers when making requests

> 2. **_Make use of proxies_**
>
> - Buy a good proxy and use it to not get blocked <3
