> **_TIP:_** Use Mozilla Firebox because it has really great dev tools.
> **_CAUTION:_** This is just for educational purposes and personal projects don't try to scrape information if not authorized.

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

# Questions?

    > Why not use the API that the website is using directly by ourselves?
        - There are going to be restrictions.

# Tricks to not get blocked by the site.
