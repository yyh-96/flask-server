from flask import Flask
from api import apis
from common.db_extension import db
# 从flask_migrate导入迁移工具、迁移命令
from flask_migrate import Migrate
from core import load_backends

def init_application():
    load_backends()
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:111213@localhost:3306/test'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_ECHO'] = True
    # 注册api
    for api in apis:
        for api_bp in api.APIs:
            api_bp.register_to_app(app)
    
    # 初始化db
    db.init_app(app)
    migrate = Migrate(app, db)

    return app
#app = init_application()
if __name__ == '__main__':
    app = init_application()
    print(app.url_map)
    app.run(host='0.0.0.0')