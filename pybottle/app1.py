from bottle import route, run, template

# @route("/")
# def index():
#     return "<h1>Hello World!</h1>"

@route("/list")
def view_list():
    item_list = [
        {"id":1,"name":"りんご"},
        {"id":2,"name":"ばなな"},
        {"id":3,"name":"すいか"},
    ]

    display_html =  "<table border='1'>"
    for item in item_list:
        display_html += "<tr>"
        display_html += "<td>{}</td>".format(item["id"])
        display_html += "<td>{}</td>".format(item["name"])
        display_html += "</tr>"
    display_html += "</table>"


    return display_html

run(host='localhost', port=8080, debug=True)
