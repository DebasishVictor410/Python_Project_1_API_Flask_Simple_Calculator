from flask import Flask,request,render_template

app=Flask(__name__,template_folder='htmls',static_folder='css')


@app.route("/")
def home_page():
    return render_template("index.html")


@app.route('/math',methods=['POST'])
def math_ops():
    try:
        if request.method=="POST":
            opt= request.form['operation']
            num1=int(request.form["num_1"])
            num2=int(request.form["num_2"])

            if opt=="add":
                res=num1+num2
                result=f"The result of Addition of {num1} and {num2} is {res}"
            elif opt=="substract":
                res=num1-num2
                result=f"The result of Substraction of {num1} and {num2} is {res}"
            elif opt=="multi":
                res=num1*num2
                result=f"The result of Multiplication of {num1} and {num2} is {res}"
            else:
                res=num1/num2
                result=f"The result of Division of {num1} and {num2} is {res}"

            return render_template("result.html",result=result)
    except Exception as e:
        print(e)


if __name__=="__main__":
    app.run(host="0.0.0.0")