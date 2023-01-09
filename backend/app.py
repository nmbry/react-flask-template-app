import logging
import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import apis.handlers.sample_handler
from apis.config import config

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
config_key = os.environ.get('FLASK_ENV', 'development')

app.config.from_object(config[config_key])
app.config.from_pyfile('instance/application.cfg', silent=True)

# ##############################################################
# データベース
# ##############################################################
db = SQLAlchemy()
# DBを連携する
# db.init_app(app)

# ##############################################################
# ログ
# ##############################################################
logging.basicConfig(
    level=config[config_key].LOG_LEVEL,
    format='%(asctime)s:%(levelname)s %(filename)s - %(message)s',
)

# ##################################################
# ルーティング
# ##################################################
api_v1 = '/api/v1'
app.register_blueprint(apis.handlers.sample_handler.api, url_prefix=f"{api_v1}/sample")
