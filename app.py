from flask import Flask, jsonify

# 创建一个Flask实例
app = Flask(__name__)


# 定义一个路由，当访问/hello时返回一个json数据
@app.route(rule='/hello', methods=['GET'])
def handeler():
    data = {'info': 'Hello'}
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)