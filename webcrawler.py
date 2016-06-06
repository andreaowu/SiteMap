#!/usr/local/bin/python

import os
import urllib

#
# Function to get links from given url
# Inputs:
#   - orig: original URL given by the user
#   - url: URL from which data is getting grabbed
#   - already_visited: a set of URLs already visited
#   - need_to_visit: a list of URLs that still need to get visited
#
# Outputs:
#   - list of links found on given URL's page that have not been traversed yet
#
def get_links(orig, url, already_visited, need_to_visit):
    # Save the links that need to be traversed from current URL data page
    links = []

    try:
        # Get data from given url
        response = urllib.urlopen(url)
    
        # Only check HTML page responses
        if "text/html" in response.headers["content-type"]:
    
            # Read the response
            data = response.read().decode("utf-8")
    
            # Links in HTML start with "href"
            href_str = "href=\""
            href_str_len = len(href_str)
            href_ind = data.find(href_str)
    
            # Find all the links in the data
            while len(data) > 0 and href_ind > -1:
    
                # Locate where the link is in the data
                data = data[href_ind:]
                quote_ind = data.find("\"", href_str_len)
                link = data[href_str_len:quote_ind]
    
                # Format the link correctly 
                if len(link) > 0 and link[0] == "/":
                    origLen = len(orig) - 1
                    if orig[origLen] == "/":
                        orig = orig[:origLen]
                    link = orig + link
                link = link.encode('utf-8').strip()
    
                # Check for links with "\" at the end, don't want to reexamine
                same_link = False
                if link[:-1] == url or link == url or \
                        link[:-1] == orig or link == orig:
                    same_link = True

                # Only need to traverse new links not seen before
                if orig in link and not same_link and \
                        link not in already_visited and link not in need_to_visit:
                    links.insert(0, link)
    
                # Truncate the data already inspected
                data = data[quote_ind:]
                href_ind = data.find(href_str)
    
    except IOError:
        if orig == url:
            raise IOError("ERROR: Bad URL given, output file not created")
        else:
            return links
        pass

    return links

#
# Function that deletes output file if necessary
#
# Input:
#   - output_file: file that needs to get deleted
#
# Output:
#   None, but deletes output_file if it exists
#

def del_output(output_file):
    if os.path.isfile(output_file):
        os.remove(output_file)

#
# Function performs webcrawling to produce a site map
# 
# Input:
#   None
#
# Output:
#   None, but creates an output file with site map
#
def web_crawl():
    # URL for which to create a site map
    url = ""
    # Location of output file for site map
    output = ""
    try:
        # Get the url 
        url = raw_input("Please provide a URL for which you want a site map: ")
        # Get the location
        output = raw_input("Provide output site map file location: ")

        # List of links that still need to be examined
        visit_pages = [url]
        # Set of links already visited
        already_visited = set()

        f = open(output, 'w')

        # Visit and get all links
        while len(visit_pages) > 0:
            visiting = visit_pages.pop()

            # Visit link
            if visiting not in already_visited:
                f.write(visiting + "\n")
                f.flush()
                already_visited.add(visiting)

                # Get links from visiting link
                try:
                    visit_pages = visit_pages + get_links(url, visiting, already_visited, visit_pages)
                except IOError as err:
                    del_output(output)
                    print str(err)
        f.close()
    except KeyboardInterrupt:
        del_output(output)
        print str("\nERROR: KeyboardInterrupt, output file not created")
    except IOError as err:
        del_output(output)
        print str(err),
        print ", output file not created"
    except Exception:
        del_output(output)
        print "ERROR occurred, output file not created"

web_crawl()
