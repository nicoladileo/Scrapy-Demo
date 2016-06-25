# Scrapy Demo #
This example is to show how to easily parse content from Web Pages using Scrapy Framework
The code is written following example from (https://realpython.com/blog/python/web-scraping-with-scrapy-and-mongodb/)

## Requirements ##
The following are required to run Scrapy
* Python 2.7.6
* Scrapy Framework 1.0.3

## Run ##
To start demo type on terminal:
* cd stack
* scrapy crawl stack -a url_file=start.txt (or scrapy crawl stack -a url_file=start.txt -o users.json -t json to store results in json format)

## Note ##
The file start.txt contains the list of urls from which Scrapy will start crawling data