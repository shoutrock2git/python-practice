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

    return template("list_tmpl", item_list = item_list)

run(host='localhost', port=8080, debug=True)
