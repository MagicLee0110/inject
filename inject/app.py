from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def input_page():
    return render_template('input.html')

@app.route('/receive')
def receive_page():
    return render_template('receive.html')

@socketio.on('input_data')
def handle_input_data(input_data):
    # 当接收到前台输入的数据时，将数据发送给接收页面
    emit('update_data', input_data, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
