# app.py

from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL, MySQLdb
import bcrypt

app = Flask(__name__)
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'qwerty1234'
app.config['MYSQL_DB'] = 'sensor'
mysql = MySQL(app)


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password'].encode('utf-8')

        curl = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        curl.execute("SELECT * FROM users WHERE email=%s", (email,))
        user = curl.fetchone()
        curl.close()

        if len(user) > 0:
            if bcrypt.hashpw(password, user["password"].encode('utf-8')) == user["password"].encode('utf-8'):
                session['name'] = user['name']
                session['email'] = user['email']
                return render_template("home.html")
            else:
                return "Error password and email not match"
        else:
            return "Error user not found"
    else:
        return render_template("login.html")


@app.route('/logout', methods=["GET", "POST"])
def logout():
    session.clear()
    return render_template("home.html")


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == 'GET':
        return render_template("register.html")
    else:
        name = request.form['name']
        email = request.form['email']
        password = request.form['password'].encode('utf-8')
        hash_password = bcrypt.hashpw(password, bcrypt.gensalt())
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users (name, email, password) VALUES (%s,%s,%s)",
                    (name, email, hash_password,))
        mysql.connection.commit()
        session['name'] = request.form['name']
        session['email'] = request.form['email']
        return redirect(url_for('home'))

@app.route('/admin')
def admin():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users")
    rv = cur.fetchall()
    cur.close()
    return render_template('admin.html', admins=rv)

# Motor
@app.route('/motor')
def motor():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM motor")
    rv = cur.fetchall()
    cur.close()
    return render_template('motor.html', motors=rv)

@app.route('/simpan-motor', methods=["POST"])
def saveMotor():
    time = request.form['time']
    temp = request.form['temp']
    status = request.form['status']
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO motor (time, temp, status) VALUES (%s, %s, %s)", (time, temp, status))
    mysql.connection.commit()
    return redirect(url_for('motor'))


@app.route('/update-motor', methods=["POST"])
def updateMotor():
    id_data = request.form['id']
    time = request.form['time']
    temp = request.form['temp']
    status = request.form['status']
    cur = mysql.connection.cursor()
    cur.execute("UPDATE motor SET time=%s, temp=%s, status=%s WHERE id=%s", (time,temp,status,id_data,))
    mysql.connection.commit()
    return redirect(url_for('motor'))

@app.route('/hapus-motor/<string:id_data>', methods=["GET"])
def hapusMotor(id_data):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM motor WHERE id=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('motor'))
# end Motor

# Hvac
@app.route('/hvac')
def hvac():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM hvac")
    rv = cur.fetchall()
    cur.close()
    return render_template('hvac.html', hvacs=rv)

@app.route('/simpan-hvac', methods=["POST"])
def saveHvac():
    time = request.form['time']
    temp = request.form['temp']
    status = request.form['status']
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO hvac (time, temp, status) VALUES (%s, %s, %s)", (time, temp, status))
    mysql.connection.commit()
    return redirect(url_for('hvac'))


@app.route('/update-hvac', methods=["POST"])
def updateHvac():
    id_data = request.form['id']
    time = request.form['time']
    temp = request.form['temp']
    status = request.form['status']
    cur = mysql.connection.cursor()
    cur.execute("UPDATE hvac SET time=%s, temp=%s, status=%s WHERE id=%s", (time,temp,status,id_data,))
    mysql.connection.commit()
    return redirect(url_for('hvac'))

@app.route('/hapus-hvac/<string:id_data>', methods=["GET"])
def hapusHvac(id_data):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM hvac WHERE id=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('hvac'))
# end Hvac

# Pompa
@app.route('/pompa')
def pompa():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM pompa")
    rv = cur.fetchall()
    cur.close()
    return render_template('pompa.html', motors=rv)

@app.route('/simpan-pompa', methods=["POST"])
def savePompa():
    time = request.form['time']
    temp = request.form['temp']
    status = request.form['status']
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO pompa (time, temp, status) VALUES (%s, %s, %s)", (time, temp, status))
    mysql.connection.commit()
    return redirect(url_for('pompa'))


@app.route('/update-pompa', methods=["POST"])
def updatePompa():
    id_data = request.form['id']
    time = request.form['time']
    temp = request.form['temp']
    status = request.form['status']
    cur = mysql.connection.cursor()
    cur.execute("UPDATE pompa SET time=%s, temp=%s, status=%s WHERE id=%s", (time,temp,status,id_data,))
    mysql.connection.commit()
    return redirect(url_for('pompa'))

@app.route('/hapus-pompa/<string:id_data>', methods=["GET"])
def hapusPompa(id_data):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM pompa WHERE id=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('pompa'))
# end Pompa

# js dashboard 
@app.route('/jsmotor', methods= ['POST', 'GET'])
def jsmotor():
    curmotor = mysql.connection.cursor()
    curmotor.execute("SELECT * FROM motor")
    rvmotor = curmotor.fetchall()
    return jsonify(rvmotor=rvmotor)

@app.route('/jshvac', methods= ['POST', 'GET'])
def jshvac():
    curhvac = mysql.connection.cursor()
    curhvac.execute("SELECT * FROM hvac")
    rvhvac = curhvac.fetchall()
    return jsonify(rvhvac=rvhvac)

@app.route('/jspompa', methods= ['POST', 'GET'])
def jspompa():
    curpompa = mysql.connection.cursor()
    curpompa.execute("SELECT * FROM pompa")
    rvpompa = curpompa.fetchall()
    return jsonify(rvpompa=rvpompa)

#js clear log
@app.route('/clearlog', methods=["GET"])
def clearlog():
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM motor")
    cur.execute("DELETE FROM hvac")
    cur.execute("DELETE FROM pompa")
    mysql.connection.commit()
    return ('', 204)

#end user
if __name__ == '__main__':
    app.secret_key = "^A%DJAJU^JJ123"
    app.run(host='0.0.0.0', debug=True)
