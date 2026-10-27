from flask import Flask, request, jsonify

app = Flask(_name_)
wishlist = []

@app.route('/add', methods=['POST'])
def add_item():
    item = request.json.get('item')
    if item: 
        wishlist.append(item)
    return jsonify({"version": "v1", "message": "Item saved"})

@app.route('/remove/<item>', methods=['DELETE'])
def remove_item(item):
    global wishlist
    wishlist = [i for i in wishlist if i != item]
    return jsonify({"version": "v2", "message": "Item deleted"})

@app.route('/view', methods=['GET'])
def view_wishlist():
    return jsonify({"version": "v3", "wishlist": wishlist})

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=5000)