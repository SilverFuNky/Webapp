from flask import Flask , redirect , url_for , render_template , request
import math

def calc(a,b,c):
    if a or b or c != int:
        a = int(a)
        b = int(b)
        c = int(c)
    if a or b or c == int:
        try:
            #step 1 is multiplying a and c just like in the quadratic equation 
            step1 = (a * c)
            #step 2 is multiplying b to the power of 2
            step2 = (b * b)
            #step 3 is putting it step 1 and step 2 together so it can square root it
            step3 = step2 -4 * step1
            #the if statement is checking if step 3 isnt 0 or a negative number
            if step3 < 0:
                print('Error, the equation is unsolveable due to negetive number or = 0')
            
            else:
                #step 4 is square rooting step 3
                step4 = math.sqrt(step3)
                #divide is calculating how much it should divide
                divide = a * 2 

                #X1 is calculating x,1
                X1= -b + step4
                #X1_2 is dividing to get the final result
                X1_2 = X1 / divide


                #X2 is the same as X1 its calculating x,2
                X2 = -b - step4
                #X2_2 is the same as X1_2 its dividing to get the final result
                X2_2 = X2 / divide

                answer = f'{X1_2} , {X2_2}'
                return answer
                
        except ValueError: 
            ValueError = True

    else:  
        return



app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def home():
    if request.method == 'POST':
        a = request.form['a']
        b = request.form['b']
        c = request.form['c']
        
        answer = calc(a,b,c)
        if answer == None:
            return f'<p class="font-monospace" style= "font-size:50;">Error you must input digits only!</p>'
            '<p class="font-monospace"><input class="btn btn-primary" type="submit" value="Submit">Back home</p>'
        return redirect(url_for("answer" , cal = answer))
    else:
        return render_template('home.html')

@app.route("/answer/<cal>")
def answer(cal):
    return f'<p class="font-monospace" style= "font-size:200;">{cal}</p>'




if __name__ == '__main__':
    app.run(debug = True)