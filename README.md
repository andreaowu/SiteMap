# Web Crawler
Web crawler that produces a site map, for user-given site and user-given output file location.

## Usage
### Inputs and Outputs
The program will prompt you to provide two inputs:
    - website for which you would like a site map 
    - output location of the file with the site map

### Start the web crawler
Option 1: Download the webcrawler.py file, and in a command-line prompt, type 'python webcrawler.py' to start the web crawler.

Option 2: Download the executable file, and ouble click on it to run.

## Code Design
All the code is in one file: webcrawler.py, which has three functions.

### web_crawl()
This is where the functionality begins. It asks for the input website and output file location, and then it starts grabbing links from the URL given. It tracks all links still need to be inspected, and it does this one by one.

### get_links()
This function grabs the data from the given URL and finds all the links in the returned HTML page. 
