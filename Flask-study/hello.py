
from flask import Flask, jsonify

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'emmm...',
        'description': u'wth',
        'done': False
    },
    {
        'id': 2,
        'title': u'wth',
        'description': u'wth',
        'done': False
    }
]

@app.route('/funny/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

if __name__ == '__main__':
    app.run(debug=True)