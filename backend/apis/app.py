import os

from apis import create_app

config_key = os.environ.get('FLASK_CONFIG_MODE', 'development')

app = create_app(config_key)
