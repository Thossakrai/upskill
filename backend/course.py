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