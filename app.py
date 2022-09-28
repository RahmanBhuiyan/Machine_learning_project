# from crypt import method
# from urllib import request
# import sklearn
import os
from http import server
from flask import Flask,render_template,escape,request
import pickle
app = Flask(__name__)
# server=app.server

# model = pickle.load(open('/media/rahman/programming1/Machine_Learning/heart_disease_project/flask/hart_desies_model.pkl', 'rb'))


inpfile = open("/run/media/abdullahar/programming/Machine_Learning/hart_disease_project/flask/model.pkl",'rb')
loaded_model = pickle.load(inpfile)

# @app.route("/")
# def hello_world():
#     return render_template("prediction.html")

@app.route("/")
def heart_disease():
    return render_template("index.html")

@app.route("/predict",methods=["GET","POST"])
def prediction():
    if request.method =="POST":
        BMI=request.form["BMI"]
        PhysicalHealth=request.form["PhysicalHealth"]
        MentalHealth=request.form["MentalHealth"]
        # SleepTime=request.form["SleepTime"]
        AgeCategory=request.form["AgeCategory"]
        Smoking=request.form["Smoking"]
        AlcoholDrinking=request.form["AlcoholDrinking"]
        Stroke=request.form["Stroke"]
        DiffWalking=request.form["DiffWalking"]
        Sex=request.form["Sex"]
        Diabetic=request.form["Diabetic"]
        PhysicalActivity=request.form["PhysicalActivity"]
        Asthma=request.form["Asthma"]
        KidneyDisease=request.form["KidneyDisease"]
        SkinCancer=request.form["SkinCancer"]
        GenHealth=request.form["GenHealth"]

        #Smoking
        if (Smoking == "Yes"):
            Smoking=1
        else:
            Smoking=0

        #AlcoholDrinking
        if (AlcoholDrinking == "Yes"):
            AlcoholDrinking=1
        else:
            AlcoholDrinking=0

        #Stroke
        if (Stroke == "Yes"):
            Stroke=1
        else:
            Stroke=0
        #DiffWalking
        if (DiffWalking == "Yes"):
            DiffWalking=1
        else:
            DiffWalking=0
        #Sex
        if (Sex == "Yes"):
            Sex=1
        else:
            Sex=0
        #Diabetic
        if (Diabetic == "Yes"):
            Diabetic=1
        else:
            Diabetic=0

        #PhysicalActivity
        if (PhysicalActivity == "Yes"):
            PhysicalActivity=1
        else:
            PhysicalActivity=0

        #Asthma
        if (Asthma == "Yes"):
            Asthma=1
        else:
            Asthma=0    

        #KidneyDisease
        if (KidneyDisease == "Yes"):
            KidneyDisease=1
        else:
            KidneyDisease=0 

        #SkinCancer
        if (SkinCancer == "Yes"):
            SkinCancer=1
        else:
            SkinCancer=0    

        GenHealth
        if (GenHealth == "Very good"):
            GenHealth=4
        elif (GenHealth== "Good" ):
            GenHealth=3
        elif (GenHealth== "Excellent" ): 
            GenHealth=2
        elif (GenHealth== "Fair" ): 
            GenHealth=1
        else:
            GenHealth=0

        # predict=loaded_model.predict([[BMI,PhysicalHealth,MentalHealth,SleepTime,AgeCategory,Smoking,AlcoholDrinking,Stroke,DiffWalking,Sex,Diabetic,PhysicalActivity,Asthma,KidneyDisease,SkinCancer]])
        predict=loaded_model.predict([[BMI,PhysicalHealth,MentalHealth,AgeCategory,Smoking,AlcoholDrinking,Stroke,DiffWalking,Sex,Diabetic ,PhysicalActivity,GenHealth,Asthma,KidneyDisease,SkinCancer]])
        if predict==1:
            predict="Yes"
        else:
            predict="Yes"
        
        return render_template("prediction.html",prediction_test="Hart Desies {}".format(predict))
    else:
        return render_template("prediction.html")

if __name__=="__main__":
    app.run(debug=True)
    # port=9090