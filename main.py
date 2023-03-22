from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
  return "<p>Alpianur Ahmad Abdullah Al malik</p><p>Tempat, tanggal lahir : Lebanon, 28 Maret 2003</p><p>Alamat : Terantang, Seranau, Sampit</p><p>Jenis Kelamin : laki laki</p><p>Agama : Islam</p>"
  


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
