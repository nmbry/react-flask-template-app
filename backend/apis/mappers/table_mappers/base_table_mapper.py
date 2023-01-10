# from abc import ABCMeta, abstractmethod


# class BaseTableMapper(ABCMeta):

# @abstractmethod
def insert(model: dict) -> int:
    """ モデルの挿入処理を行う

    Args:
        - model (dict): 登録するデータモデル
    Returns:
        - (int): 登録件数
    """
    raise NotImplementedError()


# @abstractmethod
def select_by_primary_key(keys: dict) -> dict:
    """ PKを指定してモデルを取得する

    Args:
        - keys (dict): 主キー
    Returns:
        - (dict): データモデル
    """
    raise NotImplementedError()


# @abstractmethod
def select_all() -> list:
    """ 全てのモデル一覧を取得する

    Returns:
        - (list): データモデルのリスト
    """
    raise NotImplementedError()


# @abstractmethod
def update_by_primary_key(keys: dict) -> int:
    """ モデルの更新処理を行う

    Args:
        - keys (dict): PK
    Returns:
        - (int): 更新件数
    """
    raise NotImplementedError()
