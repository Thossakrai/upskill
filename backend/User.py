from PySide2.QtSql import QSqlDatabase,QSqlQueryModel,QSqlQuery
import sqlite3

class User:
    def __init__(self, uname = None, password = None):
        self.uname = uname
        self.password = password

    def updateProfile(self):
        pass

    def login(self):
        conn = sqlite3.connect('upskilldb.sqlite3')
        c = conn.cursor()
        c.execute('SELECT USERNAME FROM USERNAME_DETAIL WHERE USERNAME = ? AND PASSWORD = ?',
                  (self.uname, self.password))
        data = c.fetchone()
        if data == None:
            return None
        print(data)
        c.execute('SELECT UTYPE, UPREF FROM USER_DETAIL WHERE USERNAME = ?', (self.uname,))
        utype = c.fetchone()
        conn.close()
        print("utype = ", utype)
        print(type(utype))
        print(utype[0], utype[1])
        return utype

    def signup(self):
        pass

    def getUserInfo(self):
        db = QSqlDatabase("QSQLITE")
        db.setDatabaseName("/Users/thossakrai/PycharmProjects/upskill/upskilldb.sqlite3")
        db.open()
        modal = QSqlQueryModel()
        query = QSqlQuery(db)
        query.prepare("SELECT * FROM USER_DETAIL WHERE USERNAME = ?")
        query.addBindValue(self.uname)
        query.exec_()
        modal.setQuery(query)
        return modal


class Learner(User):
    def __init__(self, uname):
        super().__init__(uname)

    def enroll(self, course_title, speaker):
        db = QSqlDatabase("QSQLITE")
        db.setDatabaseName("/Users/thossakrai/PycharmProjects/upskill/upskilldb.sqlite3")
        db.open()
        modal = QSqlQueryModel()
        query = QSqlQuery(db)

        query.prepare("SELECT UNAME FROM COURSES WHERE TITLE = ? AND SPEAKER = ?")
        query.addBindValue(course_title)
        query.addBindValue(speaker)
        query.exec_()
        modal.setQuery(query)
        c_name = modal.record(0).value("UNAME")
        print("Queried uname = ", c_name)

        query.prepare("INSERT INTO ENROLLMENT VALUES(?,?,?)")
        query.addBindValue(course_title)
        query.addBindValue(c_name)
        query.addBindValue(self.uname)

        complete = query.exec_()
        db.close()
        return complete

    def getEnrolledCourses(self):
        db = QSqlDatabase("QSQLITE")
        db.setDatabaseName("/Users/thossakrai/PycharmProjects/upskill/upskilldb.sqlite3")
        db.open()
        modal = QSqlQueryModel()
        query = QSqlQuery(db)
        query.prepare("SELECT TITLE, DATETIME, LOCATION, CTYPE FROM ENROLLMENT, COURSES WHERE ENROLLMENT.L_UNAME = ? AND ENROLLMENT.C_TITLE = COURSES.TITLE")
        query.addBindValue(self.uname)
        query.exec_()
        modal.setQuery(query)
        return modal

    def cancelEnrollment(self, course_title):
        db = QSqlDatabase("QSQLITE")
        db.setDatabaseName("/Users/thossakrai/PycharmProjects/upskill/upskilldb.sqlite3")
        db.open()
        query = QSqlQuery(db)
        query.prepare("DELETE FROM ENROLLMENT WHERE L_UNAME = ?  AND C_TITLE = ?")
        query.addBindValue(self.uname)
        query.addBindValue(course_title)
        complete = query.exec_()
        db.close()
        return complete

class Organiser(User):
    def __init__(self, uname):
        super().__init__(uname)
