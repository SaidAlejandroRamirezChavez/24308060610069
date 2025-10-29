from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def formula():
    return render_template("formulario.html")

@app.route("/calcular", methods=['POST'])
def calcular():
    peso = float(request.form['peso'])
    altura = float(request.form['altura'])
    edad = int(request.form['edad'])
    genero = request.form['genero']
    actividad = request.form['actividad']


    if genero == '1':
        tmb = 88.36 + (13.4 * peso) + (4.8 * altura) - (5.7 * edad)
        if actividad == '1': 
            get = tmb * 1.2
        elif actividad == '2': 
            get = tmb * 1.375   
        elif actividad == '3': 
            get = tmb * 1.55   
        elif actividad == '4': 
            get = tmb * 1.725


    else:  # femenino
        tmb = 447.6 + (9.2 * peso) + (3.1 * altura) - (4.3 * edad)
        if actividad == '1':  
            get = tmb * 1.2
        elif actividad == '2': 
            get = tmb * 1.375   
        elif actividad == '3':
            get = tmb * 1.55   
        elif actividad == '4': 
            get = tmb * 1.725



    tmb = round(tmb, 2)
    get = round(get, 2)
    
    return render_template("resultado.html", 
                         tmb=tmb,
                         get=get)



@app.route("/formulario")
def tkinter_app():
    return render_template("formulario.html")



@app.route("/resultado")
def resultado():
    return render_template("resultado.html")




if __name__ == "__main__":
    app.run(debug = True)