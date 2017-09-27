import pymysql

def connection():
    conn = pymysql.connect(host="localhost",
	                       port=3306,
                           user = "root",
                           passwd = "A1rtel$2016",
                           db = "pythonprogramming")
    c = conn.cursor()

    return c, conn		