# springer
Python script to download Springer Books released for free during the 2020 COVID-19 quarantine

# Download excel file from:
https://www.springernature.com/gp/librarians/news-events/all-news-articles/industry-news-initiatives/free-access-to-textbooks-for-institutions-affected-by-coronaviru/17855960

or

```bash
curl https://resource-cms.springernature.com/springer-cms/rest/v1/content/17858272/data/v5 -o books.xlsx
```

You can filter and copy download links saved as `links.txt`
If you saved another name file you should change `links.txt` file name in line 13
The python script and `links.txt` files must be under the same directory

Not: the script requires python3 because of `urllib.request` module
