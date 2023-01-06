import pytest

from apps.run import create_app


def setup():
    """ 前処理 """
    pass


def cleanup():
    """ 後処理 """
    pass


@pytest.fixture
def sample_fixture():
    app = create_app('testing')
    app.app_context().push()

    setup()

    # テストを実行する
    yield app

    cleanup()
