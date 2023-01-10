from apis import db


def select_all():
    query = f"""
        SELECT * FROM samples;
    """

    result = db.session.execute(query)

    return result
