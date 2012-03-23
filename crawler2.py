#Custom StringSplitter -- This is a simple and basic splitter,Will improve this soon.
def split_string(source,splitlist):
    output=[]
    atsplit = True
    for char in source:
        if char in splitlist:
            atsplit = True
        else:
            if atsplit:
                output.append(char)
                atsplit = False
            else:
                output[-1] = output[-1] + char
    return output

def get_page(url):
	try:
		import urllib
		return urllib.urlopen(url).read()    
	except:
        	return ""
    
def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1: 
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote


def get_all_links(page):
    links = []
    while True:
        url,endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links

def add_to_index(index,keyword,url):
    for entry in index:
        if entry[0] == keyword:
            entry[1].append(url)
            return
    index.append([keyword,[url]])
    
def add_page_to_index(index,url,content):
    #words = split_string(content," ,!-")
    words = content.split()
    for entry in words:
        add_to_index(index,entry,url)

def lookup(index,keyword):
    for entry in index:
         if entry[0] == keyword:   
            return entry[1]
    return

    
def union(a,b):
    for e in b:
        if e in a:
            continue;
        else:
            a.append(e)
    return a

def crawl_web(seed):
    tocrawl = [seed]
    crawled = []
    index = []
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
            content = get_page(page)
            add_page_to_index(index,page,content)
            union(tocrawl,get_all_links(content))
            crawled.append(page)
    return index
    
index = crawl_web("http://xkcd.com/353")
print index
print lookup(index,'happened')

