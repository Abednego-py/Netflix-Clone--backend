from flask import request, abort, jsonify, redirect
from flask_cors import CORS
from models import UserEmail, app , db, User
from config import database_path
from flask_migrate import Migrate
from flask_login import LoginManager, login_required, login_user, logout_user
from flask_bcrypt import Bcrypt


app.config["SQLALCHEMY_DATABASE_URI"] = database_path
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
bcrypt =  Bcrypt(app)
migrate = Migrate(app, db)


login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = 'login'

@login_manager.user_loader
def load_user():
    return User.query.get(int(user_id))
CORS(app)
@app.after_request
def after_request(response):
    response.headers.add(
        "Access-Control-Allow-Headers", "Content-Type ,true"
    )
    response.headers.add(
        "Access-Control-Allow-Methods",
        "PUT, POST, PATCH, DELETE, GET, OPTIONS, HEAD",
    )
    response.headers.add("Access-Control-Allow-Credentials", "true")

    # response.headers.add(
    #     "Access-Control-Allow-Origin", "*"
    # )
    return response
@app.route('/', methods=['GET'])
def default():
    return 'Hello from flask'

@app.route('/login')
def login():
    return 'login page'

@app.route('/register', methods=['POST'])
def register():
    error = False
    try:
        email =  request.get_json().get('email')
        useremail = UserEmail(useremail=email)
        db.session.add(useremail)
        db.session.commit()
    except:
        error = True
        db.session.rollback()
    
    finally:
        db.session.close()
        if error == True:
            abort(400)
        else:
            return redirect('http://localhost:3000/signup')

@app.route('/registerUser', methods=['GET', 'POST'])
def registerUser():
    body = request.get_json()
    try:
        email = body.get('email')
        password = body.get('password')
        hashed_password = bcrypt.generate_password_hash(password)
        new_user = User(email=email, password=hashed_password)
        db.session.add(new_user)
        db.commit()
    except:
        db.session.rollback()

    finally:
        db.session.close( )
if __name__ == '__main__':
    app.run(debug=True)