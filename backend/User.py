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

    def signup(self, fname, lname, birthdate, gender, uname, pw, phone, email, upref, utype):
        conn = sqlite3.connect('upskilldb.sqlite3')
        c = conn.cursor()
        values = (fname, lname, birthdate, uname, phone, email, utype, upref, gender,)
        c.execute('INSERT INTO USER_DETAIL VALUES(?,?,?,?,?,?,?,?,?)', values)
        c.execute('INSERT INTO USERNAME_DETAIL VALUES(?,?)', (uname, pw,))
        conn.commit()
        conn.close()
        return True

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


    def createCourse(self, title, speaker, dateline, loc, tag, ctype, details):
        conn = sqlite3.connect('upskilldb.sqlite3')
        c = conn.cursor()
        values = (title, speaker, dateline, loc, tag, ctype, details, self.uname,)
        print(values)
        c.execute('INSERT INTO COURSES VALUES(?,?,?,?,?,?,?,?)', values)
        conn.commit()
        conn.close()
        return True

    def viewCourse(self):
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("/Users/thossakrai/PycharmProjects/upskill/upskilldb.sqlite3")
        isOpened = db.open()
        print("valid  = ", db.isValid())

        print("database success to connect")
        modal = QSqlQueryModel()
        query = QSqlQuery(db)


        query.prepare("SELECT TITLE, SPEAKER, DATETIME, LOCATION, CTYPE ,  DETAIL FROM COURSES WHERE UNAME = ? ")

        query.addBindValue(self.uname)
        count = 0
        if query.exec_():
            while query.next():
                count += 1
                print(query.value(0))
        print(count)
        modal.setQuery(query)
        db.close()
        return modal


    def deleteCourse(self, title):
        conn = sqlite3.connect('upskilldb.sqlite3')
        c = conn.cursor()
        print("Pass to the function = ", self.uname, title)
        c.execute('DELETE FROM COURSES WHERE UNAME = ? AND TITLE = ?', (self.uname, title, ))
        conn.commit()
        conn.close()
