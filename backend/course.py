import sqlite3
from PySide2.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel


class Course:
    def __init__(self):
        pass

    def createCourse(self, title, speaker, dateline, loc, tag, ctype, details, uname):
        conn = sqlite3.connect('upskilldb.sqlite3')
        c = conn.cursor()
        values = (title, speaker, dateline, loc, tag, ctype, details, uname,)
        print(values)
        c.execute('INSERT INTO COURSES VALUES(?,?,?,?,?,?,?,?)', values)
        conn.commit()
        conn.close()
        return True

    def viewCourse(self, uname):
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("/Users/thossakrai/PycharmProjects/upskill/upskilldb.sqlite3")
        isOpened = db.open()
        print("valid  = ", db.isValid())

        print("database success to connect")
        modal = QSqlQueryModel()
        query = QSqlQuery(db)

        # uname = "\'" + uname + "\'"
        query.prepare("SELECT TITLE, SPEAKER, DATETIME, LOCATION, CTYPE ,  DETAIL FROM COURSES WHERE UNAME = ? ")

        query.addBindValue(uname)
        count = 0
        # query = QSqlQuery("SELECT * FROM COURSE")
        if query.exec_():
            while query.next():
                count += 1
                print(query.value(0))
        print(count)
        modal.setQuery(query)
        db.close()
        return modal

    def deleteCourse(self, uname, title):
        conn = sqlite3.connect('upskilldb.sqlite3')
        c = conn.cursor()
        print("Pass to the function = ", uname, title)
        c.execute('DELETE FROM COURSES WHERE UNAME = ? AND TITLE = ?', (uname, title, ))
        conn.commit()
        conn.close()


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

        # conn = sqlite3.connect('upskilldb.sqlite3')
        # c = conn.cursor()
        # self.courses = []
        # for row in c.execute('SELECT TITLE, SPEAKER, DATETIME, LOCATION, CTYPE, DETAIL FROM COURSES WHERE CTYPE = ?',
        #                      (upref,)):
        #     self.courses.append(row)
        # print(self.courses)
        # return self.courses

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

        # conn = sqlite3.connect('upskilldb.sqlite3')
        # c = conn.cursor()
        # self.courses = []
        # self.search_text = "%" + text + "%"
        # for row in c.execute('SELECT TITLE, SPEAKER, DATETIME, LOCATION, DETAIL FROM COURSES WHERE TITLE LIKE ?',
        #                      (self.search_text,)):
        #     self.courses.append(row)
        # return self.courses

    def enroll(self, course_title, speaker,  uname):
        db = QSqlDatabase("QSQLITE")
        db.setDatabaseName("/Users/thossakrai/PycharmProjects/upskill/upskilldb.sqlite3")
        db.open()
        modal = QSqlQueryModel()
        query = QSqlQuery(db)

        query.prepare("SELECT UNAME FROM COURSES WHERE TITLe = ? AND SPEAKER = ?")
        query.addBindValue(course_title)
        query.addBindValue(speaker)
        query.exec_()
        modal.setQuery(query)
        c_name = modal.record(0).value("UNAME")
        print("Queried uname = ", c_name)


        query.prepare("INSERT INTO ENROLLMENT VALUES(?,?,?)")
        query.addBindValue(course_title)
        query.addBindValue(c_name)
        query.addBindValue(uname)

        complete = query.exec_()
        db.close()
        return complete