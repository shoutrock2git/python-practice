#!/usr/bin/env python
import cgi
import cgitb
from janome.tokenizer import Tokenizer
cgitb.enable()

form = cgi.FieldStorage()
textText = form.getvalue("example1")


#print("Content-Type:text/html\n\n")
print ("Content-type: text/html; charset=utf-8\n")
listT = []
t = Tokenizer()
for token in t.tokenize(textText):
    listT = token.surface


    print("<center>")
    print(listT)
    print("</p>")


#
# print("""<html><meta charset="utf-8">""")
# print("<html>")
#
# print("<head>")
# print("""<script type="text/javascript" src="js/jquery-3.2.0.min.js">""","</script>")
# print("""<script type="text/javascript" src="js/sample.js">""")
# print("</script>")
# print("</head>")
#
# print("<body>")
#
# print("""<p id="test"><a href="javascript:;">here</a></p>""")
# print("<script>")
# print("""
# $(function(){
#     $('p').click(function () {
#         $(this).text("yeah!!!!!!");
#     });
# });
# """)
# print("</script>")
# print("</body></html>")
