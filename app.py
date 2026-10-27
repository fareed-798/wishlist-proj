from flask import Flask, request, jsonify

app = Flask(_name_)
wishlist = []

@app.route('/add', methods=['POST'])
def add_item():
    item = request.json.get('item')
    if item: 
        wishlist.append(item)
    return jsonify({"version": "v1", "message": "Item saved"})

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=5000)