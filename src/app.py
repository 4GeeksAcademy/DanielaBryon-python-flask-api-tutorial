from flask import Flask, jsonify, request

app = Flask(__name__)

todos = [
    {"label": "My first task", "done": False},
    {"label": "My second task", "done": False}

]

@app.route('/todos', methods=['GET'])  
def get_todos():  
    return jsonify(todos)  



@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    if not request_body or 'label' not in request_body:
        return jsonify({'error': 'Bad Request', 'message': 'Label is required'}), 400
    
    new_todo = {
        "label": request_body['label'],
        "done": request_body.get('done', False)
    }

    todos.append(new_todo)

    return jsonify(todos), 200




@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete:", position)
    if position < 0 or position >= len(todos):
        return jsonify({'error': 'Todo Not Found', 'message': "No todo found in that position"}), 404
    
    todos.pop(position)
    return jsonify(todos)




if __name__ == '__main__':  
    app.run(host='0.0.0.0', port=3245, debug=True)


