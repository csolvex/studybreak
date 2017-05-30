# inspiration from my 2015-2016 Primary 2 students who loved the Python 3 version of this app
# Christopher Joseph Spiteri December 2016, Flask App - May 29 2017. 
from flask import Flask, render_template
from flask import url_for, redirect
from random import randint



app = Flask(__name__)   
#routes

#Hello World
@app.route('/')
def test():
    return '<h1>TEST</h1>'

@app.route('/exercise')
def exercise():
    # constants and variables   
    count = 5
    exset = []
    selection = []
    choices = (
        "10 Jumping Jacks",
        "Squeeze your R hand firmly with your left hand. ", "Move the Right Side of your Body. ",
        "Rub your entire L arm with your R hand. ","Run in place for 15 seconds.",
        "Touch your L shoulder with your R hand, R shoulder with your L hand - repeat 5X ","Wiggle your whole body for 10 seconds",
        "5 Wall Push Ups", "Spread your legs apart and bend at the waist looking between your knees. Repeat 5X",
        "Touch R hand to bottom of Left foot. Repeat 5X","March in place with high knees for a count of 10.",
        "Move the lower half of your body. ","Bring your R elbow to your L knee 5 X","Move the Upper half of your body",
        "Make 10 small forward circles with your arms","Twist at the waist 10 times with arms out to the side",
        "Squeeze your L hand firmly with your R hand", "Touch hands overhead and try to balance on one foot for 5 seconds",
        "Jump in place 10 times","Spin in a circle 3 times to the right", "10 jumps over a pencil on the floor",
        "Spin in a circle 3 times to the left","Move the left side of your body",
        "Tap your feet on the floor while making small circles your fingers for 10 seconds",
        "Rub your entire R arm with your L hand","Touch L hand to bottom of R foot. Repeat 5X",
        "Give yourself a Big Hug for 10 seconds","Make 10 large circles with your arms",
        "Touch R hand to L foot and then L hand to R foot 5 times", "Take 10 deep breaths"
        )
        
    #exercise selection loop    
    while len (exset) != count:
        x= randint(0,29)        #'choices' currenty set to 30, change values here to reflect total
        if x not in exset:
            exset.append(x)
        else: continue
    for item in exset:
        selection.append(choices[item])
    return render_template('index.html', exercises = selection)

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host ='0.0.0.0', port=8080,debug=False)
    