#Define a procedure, add_page_to_index,
#that takes three inputs:

#   - index
#   - url (String)
#   - content (String)

#It should update the index to include
#all of the word occurences found in the
#page content by adding the url to the
#word's associated url list.


index = []

#add_page_to_index(index,'fake.text',"This is a test")
#print index => [['This', ['fake.text']], ['is', ['fake.text']], ['a', ['fake.text']], ['test', ['fake.text']]]

def add_to_index(index,keyword,url):
    for entry in index:
        if entry[0] == keyword:
            entry[1].append(url)
            return
    index.append([keyword,[url]])

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


def add_page_to_index(index,url,content):
    words = split_string(content," ,!-")
    for entry in words:
        add_to_index(index,entry,url)
    

add_page_to_index(index,'fake.text',"This is a test")
