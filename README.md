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
This is where the functionality begins. It asks for the input website and output file location, and then it starts grabbing links from the URL given by calling get_links() with the URL needing to be inspect. It tracks all links still need to be inspected, and it does this one by one.

In this function, I decided to use a set to track all the already-visited links; the purpose of this is to not examine the same link twice. A set is a good data structure to use for this, because checking whether an element is in the set usually is O(1), worst case O(n). Adding to a set is also O(1). Adding and checking whether an element exists are the only ways the set is used, and since both are on average constant time, this is a good data structure to use.

I use a list to track the links that still need to be inspected. A list keeps some sort of ordering, which isn't entirely necessary but the site map output makes a bit more sense because of the ordering. The list operates like a stack - links that get put in first get inspected last. The program starts from the top layer of links, and inspects many layers of links until it hits a layer without any links that have not been inspected before returning to the top layer of links to further inspect those. I decided to do this because the links are grouped together somewhat in this manner.

### get_links()
This function grabs the data from the given URL and finds all the links in the returned HTML page. 

To find all the links in the data, I find all the "href" parts of the response text and parse those to get the links. Then, the ones that belong to the original URL's domain and have not been inspected yet get added to the list of urls that need to be inspected, and this list gets returned to web_crawl().

## Tests Ran
Here is a list of tests I ran: 
- empty URL with empty output file
- existent URL with empty output file
- empty URL with output file name
- existent base URL (ie "https://github.com") with output file name
- existent URL with output file name but kill process while it's running
- existent URL that already is a sub-page of the site (ie "https://github.com/andreaowu/SiteMap"), with output file name
