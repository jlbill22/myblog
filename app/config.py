import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://root:123@localhost:3306/myblog'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    POSTS_PER_PAGE = 5

    # mail相关
    MAIL_SERVER = 'smtp.163.com'
    MAIL_PORT = 25
    MAIL_USE_TLS = False
    MAIL_USERNAME = 'jlbill@163.com'
    MAIL_PASSWORD = 'ji161797'
    ADMINS = ['1520129400@qq.com']

    LANGUAGES = ['en', 'zh-cn']