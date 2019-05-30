import sqlite3

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
        conn = sqlite3.connect('upskilldb.db')
        c = conn.cursor()
        courses = []
        for row in c.execute('SELECT TITLE, SPEAKER, DATETIME, LOCATION, TAG, CTYPE, DETAIL FROM COURSES WHERE UNAME = ?', (uname, )):
            courses.append(row)
        print(courses)
        conn.close()
        return courses
