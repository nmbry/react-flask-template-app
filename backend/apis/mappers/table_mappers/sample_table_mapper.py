from apis import db


def select_all():
    """ samplesテーブルから全件取得する """
    query = f"""
        SELECT * FROM samples;
    """

    result = db.session.execute(query)

    return result
