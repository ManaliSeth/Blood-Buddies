import pymysql


def conn_db():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='root',
        db='project',
        cursorclass=pymysql.cursors.DictCursor,
        use_unicode = True,
        charset = "utf8"
    )
