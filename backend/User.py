from PySide2.QtSql import QSqlDatabase,QSqlQueryModel,QSqlQuery
class User:
    def __init__(self, uname = None):
        self.uname = uname

    def updateProfile(self):
        pass

    def login(self):
        pass

    def signup(self):
        pass

class Learner(User):
    def __init__(self, uname):
        super().__init__(uname)

    def enroll(self, course_title, speaker):
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
        query.addBindValue(self.uname)

        complete = query.exec_()
        db.close()
        return complete
