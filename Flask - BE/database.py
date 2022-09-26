import pymysql
pymysql.install_as_MySQLdb()
import yaml
import MySQLdb

def connection():
    db_config = yaml.safe_load(open('config\database.yml'))
    conn = MySQLdb.connect(host=db_config['mysql_host'],
                           user=db_config['mysql_user'],
                           passwd=db_config['mysql_password'],
                           db=db_config['mysql_db'])


    cursor = conn.cursor(pymysql.cursors.DictCursor)
    return cursor,conn
