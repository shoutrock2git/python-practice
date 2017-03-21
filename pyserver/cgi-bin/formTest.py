#!/usr/bin/env python #おまじない
import cgi#cgiモジュールをインポートする
import cgitb
cgitb.enable()

form = cgi.FieldStorage()
choose_pattern = form["choise_pattern"].value

print ("Content-Type: text/html\n\n")#htmlファイルを表示するためのおまじないをする
print ("<html><body>")#print 以下の文字列""の中身を表示する


if choose_pattern == ("part_a"):
    print ("<p>", u"パターンAが選択されました", "</p>")

elif choose_pattern == ("part_b"):
    print ("<p>", u"パターンBが選択されました", "</p>")

elif choose_pattern == ("part_c"):
    print ("<p>", u"パターンCが選択されました", "</p>")


print ("</body></html>")
