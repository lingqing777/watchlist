from glob import escape

from flask import Flask, url_for

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home')
@app.route('/index')

def index():
    return render_template('index.html', name=name, movies=movies)
def hello():
    return '<h1>Hello qing!</h1><img src="https://img-cdn.hltv.org/gallerypicture/K-G8CCzpFD4-IxV7rMHg-w.jpg?auto=compress&ixlib=java-2.1.0&m=%2Fm.png&mw=713&mx=132&my=3167&q=75&w=5352&s=42a36be0d798c5089f63cb2ae3d759e7"width="350" height="200">'
    
@app.route('/user/<name>')
def user_page(name):
    return f'User:{escape(name)}'

@app.route('/test')
def test_url_for():
    # 下面是一些调用示例（请访问 http://localhost:5000/test 后在命令行窗口查看输出的 URL）：
    print(url_for('hello'))  # 生成 hello 视图函数对应的 URL，将会输出：/
    # 注意下面两个调用是如何生成包含 URL 变量的 URL 的
    print(url_for('user_page', name='qing'))  # 输出：/user/greyli
    print(url_for('user_page', name='peter'))  # 输出：/user/peter
    print(url_for('test_url_for'))  # 输出：/test
    # 下面这个调用传入了多余的关键字参数，它们会被作为查询字符串附加到 URL 后面。
    print(url_for('test_url_for', num=2))  # 输出：/test?num=2
    return 'Test page'
name = 'qing'
movies = [
    {'title': 'My Neighbor Totoro', 'year': '1988'},
    {'title': 'Dead Poets Society', 'year': '1989'},
    {'title': 'A Perfect World', 'year': '1993'},
    {'title': 'Leon', 'year': '1994'},
    {'title': 'Mahjong', 'year': '1996'},
    {'title': 'Swallowtail Butterfly', 'year': '1996'},
    {'title': 'King of Comedy', 'year': '1999'},
    {'title': 'Devils on the Doorstep', 'year': '1999'},
    {'title': 'WALL-E', 'year': '2008'},
    {'title': 'The Pork of Music', 'year': '2012'},
]
