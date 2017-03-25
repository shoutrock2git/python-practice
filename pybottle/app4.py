import sqlite3
from bottle import route, run, template,request

@route("/add", method=["GET","POST"])
def add_item():
    if request.method == "POST":
        item_name = request.POST.getunicode("item_name")
        conn = sqlite3.connect('items.db')
        c = conn.cursor()

        new_id = c.execute("select max(id) + 1 from items").fetchone()[0]
        c.execute("insert into items values(?,?)",(new_id,item_name))
        conn.commit()
        conn.close()
        return "SUCCESS"
    else:
        return template("add_tmpl")

@route("/list")
def view_list():
    conn = sqlite3.connect('items.db')
    c = conn.cursor()
    c.execute("select id,name from items order by id")
    item_list = []
    for row in c.fetchall():
        item_list.append({
            "id":row[0],
            "name":row[1]
        })
    conn.close()

    return template("list_tmpl", item_list = item_list)

run(host='localhost', port=8080, debug=True)
