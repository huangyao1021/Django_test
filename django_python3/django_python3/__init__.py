"""让Django的orm能以mysqldb的方式来调用pymysql"""
from pymysql import install_as_MySQLdb
install_as_MySQLdb()