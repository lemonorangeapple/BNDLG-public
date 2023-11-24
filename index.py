from flask import *
from config import *
import requests
import io

app = Flask(__name__)

url_front = "http://openapi.baidu.com/oauth/2.0/authorize?response_type=token&client_id=" + client_id + "&redirect_uri="
url_end = "&scope=basic,netdisk"

@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    get_url = (request.host_url + 'login_success')
    return redirect(url_front + get_url + url_end)

@app.route("/login_success", methods = ["GET", "POST"])
def login_success():
    if request.method == "POST":
        access_token = request.values.get("access_token")
        return redirect("/main?access_token=" + access_token)
    return render_template('login_success.html')

@app.route("/main")
def main():
    access_token = request.values.get("access_token")
    data = json.loads(requests.get("https://pan.baidu.com/rest/2.0/xpan/multimedia?method=listall&path=%2F&recursion=1&access_token=" + access_token).text)
    return render_template("main.html", lst = data['list'], access_token = access_token)

@app.route("/download")
def download():
    fsid = request.values.get("fs_id")
    access_token = request.values.get("access_token")
    dlink = json.loads(requests.get("https://pan.baidu.com/rest/2.0/xpan/multimedia?method=filemetas&dlink=1&fsids=[" + fsid + "]&access_token=" + access_token).text)["list"][0]["dlink"]
    dlink = dlink.replace("pan.baidu.com", api_link)
    return redirect(dlink + '&access_token=' + access_token)