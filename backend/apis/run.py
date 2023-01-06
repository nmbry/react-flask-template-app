import logging

from flask import Flask

import apis.handlers.sample_handler
from apis.config import config


def create_app(config_key):
    app = Flask(
        __name__,
        # 静的ファイルの置き場所を指定する
        static_folder='static',
    )

    # Flaskに適用する環境変数を読み込む
    app.config.from_object(config[config_key])
    # バージョン管理外の情報を読み込む
    app.config.from_pyfile('instance/application.cfg', silent=True)

    # DBを連携する
    # db.init_app(app)

    # ログ関連出力を設定する
    logging.basicConfig(
        level=config[config_key].LOG_LEVEL,
        format='%(asctime)s:%(levelname)s %(filename)s - %(message)s',
    )

    # ルーティングを設定する
    app.register_blueprint(apis.handlers.sample_handler.api, url_prefix='/api/v1/sample')

    return app


if __name__ == '__main__':
    pass
