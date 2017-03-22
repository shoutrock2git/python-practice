#!/usr/bin/env python
import cgi
import cgitb
from janome.tokenizer import Tokenizer
cgitb.enable()

form = cgi.FieldStorage()
textText = form.getvalue("example1")


html_body="""
<html><meta charset="utf-8">
<head>
<script type="text/javascript" src="js/jquery-3.2.0.min.js"></script>
<script type="text/javascript" src="js/sample.js"></script>
</head>

<body>
Python is awesome!</p>
<p id="test"><a href="javascript:;">here</a></p>
<p>
<script>
  $(function(){
    $('p').click(function () {
      $(this).text("yeah!!!!!!");
    });
  });
</script></p>

</body></html>"""

#print("Content-Type:text/html\n\n")
print ("Content-type: text/html; charset=utf-8\n")
listT = []
t = Tokenizer()
for token in t.tokenize(textText):
    listT = token.surface


    print("<center>")
    print(listT)
    print("</p>")



print (html_body)
