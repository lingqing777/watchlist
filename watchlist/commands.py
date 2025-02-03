import click

from watchlist import app, db
from watchlist.models import User, Movie

@app.cli.command()
@click.option('--drop', is_flag=True, help='Create after drop.')  # 设置选项
def initdb(drop):
    """Initialize the database."""
    if drop:  # 判断是否输入了选项
        db.drop_all()
    db.create_all()
    click.echo('Initialized database.')  # 输出提示信息

@app.cli.command()  # 注册为命令，可以传入 name 参数来自定义命令
def forge():
    """Generate fake data."""
    db.create_all()

    # 全局的两个变量移动到这个函数内
    name = 'qing'
    movies = [
        {'title': 'spirit-vs-faze-perfect-world-shanghai-major', 'year': '2024'},
        {'title': 'spirit-vs-liquid-perfect-world-shanghai-major', 'year': '2024'},
        {'title': 'spirit-vs-faze-iem-katowice','year': '2024'},
        {'title': 'mouz-vs-spirit-pgl-cs2-major-copenhagen-europe-rmr', 'year': '2024'},
        {'title': 'spirit-vs-wildcard-esl-pro-league-season', 'year': '2024'},
        {'title': 'spirit-vs-heroic-perfect-world-shanghai-major', 'year': '2024'},
        {'title': 'virtuspro-vs-spirit-betboom-dacha', 'year': '2023'},
        {'title': 'spirit-vs-mibr-esports-world-cup', 'year': '2024'},
        {'title': 'g2-vs-spirit-perfect-world-shanghai-major', 'year': '2024'},
        {'title': 'spirit-vs-natus-vincere-blast-premier-spring-final', 'year': '2024'},
    ]
    user = User(name = name)
    db.session.add(user)
    for m in movies:
        movie=Movie(title=m['title'],year=m['year'])
        db.session.add(movie)
        
    db.session.commit()
    click.echo('Done')

@app.cli.command()
@click.option('--username',prompt=True,help='The username used to login')
@click.option('--password',prompt=True,hide_input=True,confirmation_prompt=True,help='The password used to login')
def admin(username,password):
    """Create user."""
    db.create_all()

    user=User.query.first()
    if user is not None:
        click.echo('Updating user...')
        user.username=username
        user.set_password(password)# 设置密码
    else:
        click.echo('Creating user...')
        user=User(username=username,name='Admin')
        user.set_password(password)# 设置密码
        db.session.add(user)

    db.session.commit()
    click.echo('Done.')
