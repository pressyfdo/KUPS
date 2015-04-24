import sys
sys.path.append("..")

from flask import redirect, url_for
from flaskext.mysql import MySQL

mysql = MySQL()

appHandler.config['MYSQL_DATABASE_USER'] = 'root'
appHandler.config['MYSQL_DATABASE_PASSWORD'] = 'computer'
appHandler.config['MYSQL_DATABASE_DB'] = 'kups'
appHandler.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(appHandler)

class LoginController:

    def authenticate(self,form):
        
        username = form['username']
        password = form['password']

        cursor = mysql.connect().cursor
        cursor.execute("select * from users where username='" + username + "' and password='" + password + "'")
         data = cursor.fetchone();
         if data is None :
             return "Username or Password is Wrong"
         else :
            return 'Login Successful'

        
