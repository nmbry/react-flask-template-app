import pytest

from run import create_app


def setup():
    """
    前処理を行う。
    特にDB操作のINSERTを行う場合などに利用する。
    """
    pass


def cleanup():
    """
    後処理を行う。
    特にDB操作のDELETEを行う場合などに利用する。
    """
    pass


@pytest.fixture
def sample_fixture():
    app = create_app('testing')
    app.app_context().push()

    setup()

    # テストを実行する
    yield app

    cleanup()
