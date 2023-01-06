from flask import Flask

import apps.handlers.sample_handler
from apps.config import config


def create_app(config_key):
    app = Flask(__name__)
    app.config.from_object(config[config_key])

    # DBを連携する
    # FIXME: 以下はDBを設定していないため初期化をしない
    # db.init_app(app)

    # ルーティングを設定する
    app.register_blueprint(apps.handlers.sample_handler.sample, url_prefix='/sample')

    return app
