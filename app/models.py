from app import db 
from datetime import datetime
from werkzeug import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column('id', db.Integer, nullable=False, primary_key=True)
    fullname = db.Column('fullname', db.String(100), nullable=False)
    username = db.Column('username', db.String(30), nullable=False, unique=True, index=True)
    password = db.Column('password', db.String(100), nullable=False, index=True)
    email = db.Column('email', db.String(100), nullable=False, unique=True)
    mobile = db.Column('mobile', db.Integer)
    role = db.Column('role', db.String(20), nullable=False)
    created_at = db.Column('created_at', db.DateTime, nullable=False, default=datetime.now())
    updated_at = db.Column('updated_at', db.DateTime, nullable=False, default=datetime.now())

    def __init__(self, fullname, username, password, email, mobile, role):
        self.fullname = fullname
        self.username = username
        self.set_password(password)
        self.email = email.lower()
        self.mobile = mobile
        self.role = role

    def set_password(self,password):
        self.password = generate_password_hash(password)

    def check_password(password):
        return check_password_hash(self.password, password)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False
        
    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '<User %r>' %(self.username)

class Logs(db.Model):
    __tablename__ = 'logs'
    id = db.Column('id', db.Integer, nullable=False, primary_key=True)
    username = db.Column('username', db.String(30), nullable=False)
    log_type = db.Column('log_type', db.String(30), nullable=False)
    message = db.Column('message', db.String(2000), nullable=False)
    created_at = db.Column('created_at', db.DateTime, nullable=False, default=datetime.now())

    def __init__(self, username, log_type, message):
        self.username = username
        self.log_type = log_type
        self.message = message

class PrintLogs(db.Model):
    __tablename__ = 'printlogs'
    id = db.Column('id', db.Integer, nullable=False, primary_key=True)
    username = db.Column('username', db.String(30), nullable=False)
    filename = db.Column('filename', db.String(30), nullable=False)
    pages = db.Column('pages', db.Integer, nullable=False)
    copies = db.Column('copies', db.Integer, nullable=False)
    cost = db.Column('cost', db.Float(10,2), nullable=False)
    created_at = db.Column('created_at', db.DateTime, nullable=False, default=datetime.now())

    def __init__(self, username, filename, pages, copies, cost):
        self.username = username
        self.filename = filename
        self.pages = pages
        self.copies = copies
        self.cost = cost

class Printers(db.Model):
    __tablename__ = 'printers'
    id = db.Column('id', db.Integer, nullable=False, primary_key=True)
    name = db.Column('name', db.String(30), nullable=False, unique=True)
    url = db.Column('url', db.String(500), nullable=False)
    model = db.Column('make_and_model', db.String(500), nullable=False)
    department = db.Column('Department', db.String(100), nullable=False)
    location = db.Column('location', db.String(100), nullable=False)
    description = db.Column('description', db.String(500), nullable=False)
    created_at = db.Column('created_at', db.DateTime, nullable=False, default=datetime.now())
   
    def __init__(self, name, url, model, department, location, description):
        self.name = name
        self.url = url
        self.model = model
        self.department = department
        self.location = location
        self.description = description

class Files(db.Model):
    __tablename__ = 'files'
    id = db.Column('id', db.Integer, nullable=False, primary_key=True)
    filename = db.Column('filename', db.String(500), nullable=False)
    username = db.Column('username', db.String(100), nullable=False)
    size = db.Column('size', db.Integer, nullable=False)
    pages = db.Column('pages', db.Integer, nullable=False)
    status = db.Column('status', db.String(30), nullable=False)
    created_at = db.Column('created_at', db.DateTime, nullable=False, default=datetime.now())

    def __init__(self, filename, username, size, pages, status):
        self.filename = filename
        self.username = username
        self.size = size
        self.pages = pages
        self.status = status
