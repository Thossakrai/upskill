import sqlite3
from PySide2.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel


class Course:
    def __init__(self):
        pass


    def browse(self, upref):
        db = QSqlDatabase("QSQLITE")
        db.setDatabaseName("/Users/thossakrai/PycharmProjects/upskill/upskilldb.sqlite3")
        db.open()
        modal = QSqlQueryModel()
        query = QSqlQuery(db)
        query.prepare("SELECT TITLE, SPEAKER, DATETIME, LOCATION, CTYPE, DETAIL FROM COURSES WHERE CTYPE = ?")
        query.addBindValue(upref)
        query.exec_()
        modal.setQuery(query)
        db.close()
        return modal


    def search(self, text):
        db = QSqlDatabase("QSQLITE")
        db.setDatabaseName("/Users/thossakrai/PycharmProjects/upskill/upskilldb.sqlite3")
        db.open()
        modal = QSqlQueryModel()
        query = QSqlQuery(db)
        query.prepare("SELECT TITLE, SPEAKER, DATETIME, LOCATION, DETAIL FROM COURSES WHERE TITLE LIKE ?")
        self.search_text = "%" + text + "%"
        query.addBindValue(self.search_text)
        query.exec_()
        modal.setQuery(query)
        db.close()
        return modal


