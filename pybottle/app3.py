import sqlite3
from bottle import route, run, template

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
