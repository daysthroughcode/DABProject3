from flask import request
@app.route('/todo/api/v1.0/tasks', methods=['POST'])
def create_task():
    if not request.json:
        abort(400)
    input = {
        'fieldA': request.json['fieldA'],
        'fieldB': request.json['fieldB']
    }
    result = yourModel.predict(input)
    return jsonify({'result': result}), 200 # return success 