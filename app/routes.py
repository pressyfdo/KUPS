import os, random, string, subprocess
from subprocess import call
from flask import render_template, flash, redirect, url_for, request, session, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import appHandler, login_manager, db, mail
from .forms import LoginForm, RegistrationForm, ChangePasswordForm
from models import User, Logs, PrintLogs, Printers, Files
from werkzeug import secure_filename, check_password_hash, generate_password_hash
from flask import send_from_directory
from flask_mail import Message

mail.init_app(appHandler)
ALLOWED_EXTENSIONS = set(['txt', 'pdf'])

login_manager.login_view = "login"


def allowed_file(filename):
    return '.' in filename and \
            filename.rsplit('.',1)[1] in ALLOWED_EXTENSIONS

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

@appHandler.before_request
def before_request():
    g.user = current_user

@appHandler.route('/', methods=['GET','POST'])
@appHandler.route('/login', methods=['GET','POST'])
def login():
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('index'))
    form = LoginForm()
    if request.method == 'GET':
        return render_template('login.html',
                                title='Sign In',
                                form=form)
    elif request.method == 'POST':
        if form.validate_on_submit():
            username = request.form['username']
            password = request.form['password']
            remember_me = False
            if 'remember_me' in request.form:
                remember_me = True
            registered_user = User.query.filter_by(username=username).first()
            if registered_user is None:
                log = Logs(username, "LOGIN ERROR", "Login to user " + username + " failed due to wrong credentials")
                db.session.add(log)
                db.session.commit()
                flash('Username or Password is Invalid', 'error')
                return redirect(url_for('login'))
            elif registered_user and check_password_hash(registered_user.password, password):
                login_user(registered_user, remember = remember_me)
                log = Logs(username, "LOGOUT OK", "Login to user " + username + " is successful")
                db.session.add(log)
                db.session.commit()
  
                flash('Logged in successfully')
                if g.user.role == 'user':
                    return redirect(url_for('index'))
                elif g.user.role == 'admin':
                    return redirect(url_for('admin_page'))
       
        log = Logs(username, "LOGIN ERROR", "Login to user " + username + " failed due to wrong credentials")
        db.session.add(log)
        db.session.commit()
 
        flash('Invalid username or password')
        return redirect(url_for('login'))

@appHandler.route('/index')
@login_required
def index():  
    if g.user.role == 'admin': 
        return redirect(url_for('admin_page'))
    if g.user is None or not g.user.is_authenticated():
        return redirect(url_for('login'))
    appHandler.config['UPLOADS_FOLDER'] = 'app/uploads/' + g.user.username
    
    if not os.path.exists(appHandler.config['UPLOADS_FOLDER']):
        os.makedirs(appHandler.config['UPLOADS_FOLDER'])
    lst = os.listdir(appHandler.config['UPLOADS_FOLDER'])
    return render_template('index.html',
                            title='Index Page',
                            user=g.user, lst=lst) 

@appHandler.route('/logout', methods=['GET','POST'])
@login_required
def logout():
    username = g.user.username
    logout_user()
    log = Logs(username, "LOGOUT OK", "User " + username + " logged out successfully")
    db.session.add(log)
    db.session.commit()
    return redirect(url_for('login'))

@appHandler.route('/upload', methods=['POST'])
@login_required
def upload():

   appHandler.config['UPLOADS_FOLDER'] =  'app/uploads/' + g.user.username  

   file = request.files['file'] 
   print file
   if file and allowed_file(file.filename):
        if not os.path.exists(appHandler.config['UPLOADS_FOLDER']):
            os.makedirs(appHandler.config['UPLOADS_FOLDER'])
        filename = secure_filename(file.filename)
        file.save(os.path.join(appHandler.config['UPLOADS_FOLDER'], filename))
        path = appHandler.config['UPLOADS_FOLDER']+"/" + filename
        print path
        size = os.path.getsize(path)
        print size
        files = Files(filename, g.user.username, size, 0, "Active")
        db.session.add(files) 
        db.session.commit()
        return redirect(url_for('index',filename=filename))
   else:
        flash('No file Uploaded')
        return redirect(url_for('index'))

@appHandler.route('/uploads/<filename>')
@login_required
def send_file(filename):
   appHandler.config['UPLOADS_FOLDER'] =  '/uploads/' + g.user.username  
   return send_from_directory(appHandler.config['UPLOADS_FOLDER'],
                                filename)

@appHandler.route('/admin/login', methods=['GET','POST'])
def admin_login():
    form = LoginForm()
    if request.method == 'GET':
        return render_template('login.html',
                                title='Admin Login',
                                form=form)
    pass

@appHandler.route('/admin/index')
@login_required
def admin_page():
    if g.user.role == 'user':
        flash('Not Authorised to view this page')
        return redirect(url_for('index'))
    appHandler.config['UPLOADS_FOLDER'] = 'app/uploads/' + g.user.username
 
    if not os.path.exists(appHandler.config['UPLOADS_FOLDER']):
        os.makedirs(appHandler.config['UPLOADS_FOLDER'])
    lst = os.listdir(appHandler.config['UPLOADS_FOLDER'])

    return render_template('admin_index.html', user = g.user, title = "Admin Index", lst=lst)
    pass

@appHandler.route('/admin/user/register', methods=['GET','POST'])
@login_required
def register_user():
    if g.user.role == 'user':
        flash('Not Authorised to view admin page')
        return redirect(url_for('index'))
    form = RegistrationForm()

    if request.method == 'GET':
        return render_template('register.html',
                                form=form)
    elif request.method == 'POST':
        if form.validate() == False:
            return render_template('register.html',
                                    form=form)
        else:
            password = ''.join(random.choice(string.ascii_letters + string.digits) for x in range(16))
            newuser = User(form.fullname.data, form.username.data, password, form.email.data, form.mobile.data)
            db.session.add(newuser)
            db.session.commit()
            flash('User created successfully')
            msg = Message('Hello', sender=appHandler.config['MAIL_USERNAME'], recipients=[form.email.data])
            msg.body = """
            Password : <%s>
            """ %(password)
            mail.send(msg)
            return render_template('register.html',
                                    form=form)

@appHandler.route('/print', methods=['POST'])
@login_required
def print_page():
    filename = request.form['files']
    pages = request.form['pages']
    copies = request.form['copies']
    layout = request.form['layout']
    size = "media=" + request.form['size']
    printer = request.form['printer']
    side = "sides=" + request.form['side']
    pr_file = 'app/uploads/' + g.user.username + '/' + filename

    if copies < 1:
        copies = 1

    if side == "two-sided":
        if layout == "portrait":
            side = "sides=two-sided-short-edge"
        else:
            side = "sides=two-sided-long-edge"

    if not os.path.isfile(pr_file):
        flash("File does not exists")
        return redirect(url_for('index'))
    
    if pages == "all":
        p = subprocess.Popen(["lp","-d",printer,"-n",copies,"-o",layout,"-o",size,"-o",side,pr_file], stdout=subprocess.PIPE)
        output, error = p.communicate()
    else:
        if request.form['range'] != "":
            ranges = request.form['range'] 
            p = subprocess.Popen(["lp","-d",printer,"-P",ranges,"-n",copies,"-o",layout,"-o",size,"-o",side,pr_file], stdout=subprocess.PIPE)
            output, error = p.communicate()
        else:
            flash('Enter Page range')
            return redirect(url_for('index'))

        
    flash("Printed Successfully")
    return redirect(url_for('index'))
    pass

@appHandler.route('/user/<username>/change_password', methods=['GET','POST']) 
@login_required
def change_password(username):
    form = ChangePasswordForm()

    if request.method == 'GET':
        return render_template('change_password.html', form=form, user=g.user.username)

    elif request.method == 'POST':
        if form.validate() == False:
            return redirect(url_for('change_password', username = g.user.username))
        else:
            old_password = form.old_password.data
            password = form.new_password.data
            password_again = form.password_again.data
            
            if g.user is not None and check_password_hash(g.user.password, old_password) and password == password_again:
                g.user.password = generate_password_hash(password)
                db.session.commit()
                flash('Password Updated Successfully')
                return redirect(url_for('index'))
            else:
                flash('Password didnt match') 
                return redirect(url_for('change_password', username = g.user.username))

@appHandler.route('/printers')
@login_required
def list_printers():
    printers = Printers.query.all()    
    return render_template('printers.html', user = g.user, printers=printers)
    pass

@appHandler.route('/job_queue')
@login_required
def job_queue():
    return render_template('jobs.html', user = g.user) 
    pass

@appHandler.route('/uploads')
@login_required
def uploads():
    files = Files.query.filter_by(username=g.user.username, status='Active')
    return render_template('uploads.html', user = g.user, files=files)

@appHandler.route('/uploads/remove/<filename>')
@login_required
def remove_files(filename):
    appHandler.config['UPLOADS_FOLDER'] =  'app/uploads/' + g.user.username
    name = filename
    path = appHandler.config['UPLOADS_FOLDER'] + '/' + name
    if os.path.exists(path):
        os.remove(path)
    else:
        flash('File not found in the server')
        return redirect(url_for('uploads'))
    files = Files.query.filter_by(username=g.user.username, filename=name, status='Active').first()
    files.status = 'Removed'
    db.session.commit()
    flash('File deleted successfully')
    return redirect(url_for('uploads'))

@appHandler.route('/users')
@login_required
def list_users():
    return render_template('users.html', user = g.user, title='Admin - List Users')
    pass

@appHandler.route('/admin/add_printers', methods=['GET', 'POST'])
@login_required
def add_printers():
    if request.method == 'GET':
        return render_template('add_printers.html', user=g.user, title='Admin - Add Printers')
    elif request.method == 'POST':
        name = request.form['name']
        url = request.form['url']
        model = request.form['model']
        department = request.form['department']
        location = request.form['location']
        description = request.form['description']

        printer = Printers(name, url, model, department, location, description)
        db.session.add(printer)
        db.session.commit()
        flash('Printer added successfully.')
        return redirect(url_for('add_printers'))
    pass
