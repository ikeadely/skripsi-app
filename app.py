from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/user")
def user():
    return render_template('user.html')

@app.route("/mahasiswa")
def mahasiswa():
    return render_template('mahasiswa.html')

@app.route("/bimbingan")
def bimbingan():
    return render_template('bimbingan.html')

@app.route("/laporan")
def laporan():
    return render_template('laporan.html')

@app.route("/pengumuman")
def pengumuman():
    return render_template('pengumuman.html')

@app.route("/rolepermissions")
def rolepermissions():
    return render_template('rolepermissions.html')

@app.route("/roles")
def roles():
    return render_template('roles.html')

if __name__ == "__main__":
    app.run(debug=True)