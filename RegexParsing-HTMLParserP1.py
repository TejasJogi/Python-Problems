from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        for key, value in attrs:
            print ("->", key, ">", value)
    def handle_endtag(self, tag):
        print("End   :", tag)
    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        for key, value in attrs:
            print ("->", key, ">", value)
            
n = int(input())
s = ''


for i in range(n):
    s+= input()

res = MyHTMLParser()
res.feed(s)


