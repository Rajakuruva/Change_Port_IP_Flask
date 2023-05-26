from flask import Flask

FAI=Flask(__name__)

@FAI.route('/Wish/<name>')
def Wish(name):
    return f"Hai Hello Everyone {name}"

if __name__=='__main__':
    FAI.run(debug=True,host='192.168.1.111')