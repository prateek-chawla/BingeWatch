from flask import Flask , render_template as render , url_for , request , redirect
from helper import createResponse , getImageLinks

app=Flask(__name__) 

@app.route('/',methods=['POST','GET'])
def index():
    if request.method=='POST':
        result=createResponse(request.form['search'])
        if result:
            return render('content.html', result=result)
        else:
            return render('404.html')
    else:
        images=getImageLinks()
        return render('index.html',images=images)

@app.route('/about')
def about():
    return render('about.html')

if __name__=="__main__":
    app.run(host='0.0.0.0' , use_reloader=True, port=5000)

 
