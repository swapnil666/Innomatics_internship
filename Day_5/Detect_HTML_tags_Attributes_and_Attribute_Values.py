from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        [print('-> {} > {}'.format(*attr)) for attr in attrs]
html = '\n'.join([input() for i in range(int(input()))])
parser = MyHTMLParser()
parser.feed(html)
parser.close()

# from html.parser import HTMLParser
# class MyHTMLParser(HTMLParser):
#     def handle_starttag(self, tag, attrs):
#         print (tag)
#         for attr, value in attrs:
#             print ("->"), attr, ">", value
#     def handle_startendtag(self, tag, attrs):
#         print (tag)
#         for attr, value in attrs:
#             print ("->"), attr, ">", value
# html = ''
# for _ in range(int(input())):
#     html += input().rstrip() + '\n'
# parser = MyHTMLParser()
# parser.feed(html)
# parser.close()
