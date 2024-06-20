from flask import Flask, render_template, request, jsonify
import pymysql

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/check_mysql_connection', methods=['POST'])
def check_mysql_connection():
    host = str(request.form.get('host'))
    user = str(request.form.get('user'))
    password = str(request.form.get('password'))
    port = int(request.form.get('port'))

    try:
        connection = pymysql.connect(
            host=host,
            user=user,
            password=password,
            port=port
        )
        connection.close()
        return jsonify({'message': 'Connection successful'})
    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run(host='0.0.0.0')
