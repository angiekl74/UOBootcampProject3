import sqlite3
from flask import Flask, render_template, request
from flask import Flask, request, jsonify, render_template
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/enternew')
def new_dog():
   return render_template('dog_intake.html')

@app.route('/delete')
def delete():
   conn = sqlite3.connect("dogtest.db")  
   c = conn.cursor()
   c.execute("DELETE FROM LouisvilleCleanFinal WHERE PrimaryColor='ANGIE'")
   conn.commit()
   rows2 = "Deletions complete where PrimaryColor=ANGIE"
   return render_template("list.html", rows2 = rows2)
   conn.close()

@app.route('/addrec', methods = ['POST'])
def addrec():

    if request.method == 'POST':
        try:
            dog_color2 = request.form['PrimaryColor2']
            dog_category2 = request.form['BreedCategory2']
            dog_behavior2 = request.form['IntakeStatus2']
            dog_age2 = request.form['PetAgeCategory2']
            dog_sex2 = request.form['Sex2']
            dog_breed2 = request.form['PetBreed2']

            with sqlite3.connect("dogtest.db") as conn:
                c = conn.cursor()
                c.execute("INSERT INTO LouisvilleCleanFinal (PrimaryColor, BreedCategory, IntakeStatus, PetAgeCategory, Sex, TopBreed ) VALUES (?,?,?,?,?,?)", (dog_color2, dog_category2, dog_behavior2, dog_age2, dog_sex2, dog_breed2))
                conn.commit()
                msg2 = "Record successfully added"
                return render_template("resultrecord.html", msg = msg2)             
        
        except:            
            conn.rollback()
            msg2 = "Error"
            return render_template("resultrecord.html", msg = msg2)
            conn.close()
        
        # finally:
        #     return render_template("resultrecord.html", msg2 = msg)
        #     conn.close()

@app.route('/list')
def list():
    conn = sqlite3.connect("dogtest.db")
    c = conn.cursor()
    c.execute("SELECT * FROM LouisvilleCleanFinal WHERE PrimaryColor='ANGIE'")
      
    rows = c.fetchmany(10);
    return render_template("list.html", rows = rows)


if __name__ == '__main__':
   app.run(debug = True)