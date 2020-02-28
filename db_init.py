import pymysql


def create_db():
    conn = pymysql.connect("localhost", "root", "mysql", "ece568project")
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS historical")
    cursor.execute("DROP TABLE IF EXISTS realtime")
    cursor.execute("CREATE TABLE historical ( symbol CHAR(20) NOT NULL, time DATE, open FLOAT, "
                   "high FLOAT, low FLOAT,"
                   "close FLOAT, volume INT )")
    cursor.execute("CREATE TABLE realtime ( symbol CHAR(20) NOT NULL, time DATETIME, price FLOAT,"
                   "volume INT)")
    conn.close()


if __name__ == '__main__':
    create_db()