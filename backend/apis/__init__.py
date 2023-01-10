from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# DBの初期化
db = SQLAlchemy()


def create_app(config_key):
    # ##############################################################
    # Flask App
    # ##############################################################
    app = Flask(
        __name__,
        # 静的ファイルの置き場所を指定する
        static_folder='static',
    )

    # ##############################################################
    # 環境変数
    # ##############################################################
    from apis.config import config
    app.config.from_object(config[config_key])
    app.config.from_pyfile('instance/application.cfg', silent=True)

    # ##############################################################
    # データベース
    # ##############################################################
    # DBを連携する
    db.init_app(app)

    # ##############################################################
    # ログ
    # ##############################################################
    import logging
    logging.basicConfig(
        level=app.config['LOG_LEVEL'],
        format='[%(asctime)s] [%(levelname)s] [%(filename)s] %(message)s',
    )

    # ##################################################
    # ルーティング
    # ##################################################
    api_v1 = '/api/v1'

    import apis.handlers.sample_handler
    app.register_blueprint(apis.handlers.sample_handler.api, url_prefix=f"{api_v1}/sample")

    return app
