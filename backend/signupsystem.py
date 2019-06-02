import sqlite3

class SignUpSystem :
    def __init__(self, fname, lname, birthdate, gender, uname, pw, phone, email, upref, utype):
        self.fname = fname
        self.lname = lname
        self.birthdate = birthdate
        self.gender = gender
        self.uname = uname
        self.password = pw
        self.phone = phone
        self.email = email
        self.upref = upref
        self.utype = utype

    def signup(self):
        conn = sqlite3.connect('upskilldb.sqlite3')
        c = conn.cursor()
        values = (self.fname, self.lname, self.birthdate, self.uname, self.phone, self.email, self.utype, self.upref, )
        # values = ("x", "x", "x", "xxxxxxaaaa", "x", "x", "x", "x", )
        c.execute('INSERT INTO USER_DETAIL VALUES(?,?,?,?,?,?,?,?)', values)
        c.execute('INSERT INTO USERNAME_DETAIL VALUES(?,?)', (self.uname, self.password, ))
        conn.commit()
        conn.close()
        return True

