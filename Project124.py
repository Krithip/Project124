from flask import Flask, jsonify, request
app = Flask(__name__)
list = [
    {"id": 1, "name": u"Krithi", "contact": u"1234567890", "done": False},
    {"id": 2, "name": u"Rachel", "contact": u"0987654321", "done": False},
    {"id": 3, "name": u"Sahita", "contact": u"1234512345", "done": False}
]
@app.route("/")
def helloWorld():
    return "Hello World"
@app.route("/add-contact", methods = ["POST"])
def addList():
    if not request.json:
        return jsonify({
            "status": "error", "message": "please provide data"
        }, 400)
    addContact = {'id': list[-1]["id"]+1, "name": request.json["name"], "contact": request.json.get("contact", ""), "done": False}
    list.append(addContact)
    return jsonify({"status": "success", "message": "conatct added successfully"})
@app.route("/get-contact")
def getList(): 
    return jsonify({
        "data": list
    })
if (__name__ == "__main__"):
    app.run(debug = True) 