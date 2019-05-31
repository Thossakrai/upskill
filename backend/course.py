import sqlite3
from PySide2.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel


class Course:
    def __init__(self):
        pass

    def createCourse(self, title, speaker, dateline, loc, tag, ctype, details, uname):
        conn = sqlite3.connect('upskilldb.db')
        c = conn.cursor()
        values = (title, speaker, dateline, loc, tag, ctype, details, uname,)
        print(values)
        c.execute('INSERT INTO COURSES VALUES(?,?,?,?,?,?,?, ?)', values)
        conn.commit()
        conn.close()
        return True

    def viewCourse(self, uname):
        # conn = sqlite3.connect('upskilldb.db')
        # c = conn.cursor()
        # courses = []
        # for row in c.execute(
        #         'SELECT TITLE, SPEAKER, DATETIME, LOCATION, TAG, CTYPE, DETAIL FROM COURSES WHERE UNAME = ?', (uname,)):
        #     courses.append(row)
        # print(courses)
        # conn.close()
        # return courses
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName("../upskilldb.db")
        ok = db.open()
        modal = QSqlQueryModel()
        query = QSqlQuery()
        query.prepare('SELECT TITLE, SPEAKER, DATETIME, LOCATION, TAG, CTYPE, DETAIL FROM COURSES WHERE UNAME = ?')
        query.addBindValue(uname)
        query.exec_()
        modal.setQuery(query)
        print(modal)
        return modal

    def deleteCourse(self, uname, title):
        pass

    def browse(self, upref):
        conn = sqlite3.connect('upskilldb.db')
        c = conn.cursor()
        self.courses = []
        for row in c.execute('SELECT TITLE, SPEAKER, DATETIME, LOCATION, CTYPE, DETAIL FROM COURSES WHERE CTYPE = ?',
                             (upref,)):
            self.courses.append(row)
        print(self.courses)
        return self.courses

    def search(self, text):
        conn = sqlite3.connect('upskilldb.db')
        c = conn.cursor()
        self.courses = []
        self.search_text = "%" + text + "%"
        for row in c.execute('SELECT TITLE, SPEAKER, DATETIME, LOCATION, DETAIL FROM COURSES WHERE TITLE LIKE ?',
                             (self.search_text,)):
            self.courses.append(row)
        return self.courses
