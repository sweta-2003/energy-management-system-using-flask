from flask import Flask,render_template,jsonify,request
from sqlalchemy import text
from database import engine

app=Flask(__name__)

def load_prod_sec():
    with engine.connect() as conn:
        result=conn.execute(text("select * from prod_sec"))
        prod_sec=[]
        for row in result.all():
            prod_sec.append(dict(row._mapping))
        
        return prod_sec
 

  
    
@app.route("/")
def home():
    return render_template("main.html")

@app.route("/displayproduction")
def display():
    prodsec=load_prod_sec()
    return render_template("display_prod.html",prodsec=prodsec)


@app.route('/deleteproduction/<id>')
def delete(id):
   
    with engine.connect() as conn:
       query=(text("delete from prod_sec where id=:ids"))
       values={'ids':id}
       conn.execute(query,values)
       
    return render_template("main.html")

@app.route('/addform')
def addform():
    return render_template("forms.html")

@app.route('/addproduction',methods=['post'])
def add():
       data=request.form
       with engine.connect()as conn:
           query=text("insert into prod_sec(id,sectionName,noOfMotors,maxPowerUsage,noOfSections,prodCapacity,prodCapacityUnits,status) values(:id,:sectionName,:noOfMotors,:maxPowerUsage,:noOfSections,:prodCapacity,:prodCapacityUnits,:status)")
           values={'id':data['id'],
                   'sectionName':data['section'],
                   'noOfMotors':data['noofmotors'],
                   'maxPowerUsage':data['power'],
                   'noOfSections':data['sectionno'],
                   'prodCapacity':data['pcapacity'],
                   'prodCapacityUnits':data['units'],
                   'status':data['status']
            }
           conn.execute(query,values)
           return render_template("main.html")           
        
@app.route('/api/productionSection')
def jsons():
    prodsec=load_prod_sec()
    return jsonify(prodsec)








def load_motor_sec():
    with engine.connect() as conn:
        result=conn.execute(text("select * from motor"))
        motor_sec=[]
        for row in result.all():
            motor_sec.append(dict(row._mapping))
        
        return motor_sec
 

@app.route("/displaymotor")
def displaymotor():
    motor=load_motor_sec()
    return render_template("displaymotor.html",motor=motor)

@app.route("/displaymotor2")
def displaymotor2():
    motor=load_motor_sec()
    return render_template("displaymotor2.html",motor=motor)

    
@app.route("/addmotorform")
def addmotorform():
    return render_template("motorform.html")

@app.route('/deletemotor/<id>')
def deletemotor(id):
   
    with engine.connect() as conn:
       query=(text("delete from motor where modelno=:ids"))
       values={'ids':id}
       conn.execute(query,values)
       
    return render_template("main.html")



@app.route('/addmotor',methods=['post'])
def addmotor():
       data=request.form
       with engine.connect()as conn:
           query=text("insert into motor(motorname,motorno,motortype,motoruse,power,ratehp,modelno,frequency,ratedrpm,ratedvoltage,ratedcurrent,ambientTemp,ambientHumidity,dom,manufacture,location,lastservicedate,lastservicereason,lastmaintanence,status) values(:motorname,:motorno,:motortype,:motoruse,:power,:ratehp,:modelno,:frequency,:ratedrpm,:ratedvoltage,:ratedcurrent,:ambientTemp,:ambientHumidity,:dom,:manufacture,:location,:lastservicedate,:lastservicereason,:lastmaintanence,:status)")
           values={'motorname':data['mname'],
                   'motorno':data['mno'],
                   'motortype':data['mtype'],
                   'motoruse':data['muse'],
                   'power':data['power'],
                   'ratehp':data['ratehp'],
                   'modelno':data['modelno'],
                   'frequency':data['freq'],
                   'ratedrpm':data['rpm'],
                   'ratedvoltage':data['volt'],
                   'ratedcurrent':data['current'],
                   'ambientTemp':data['temp'],
                   'ambientHumidity':data['humidity'],
                   'dom':data['dom'],
                   'manufacture':data['manufacture'],
                   'location':data['location'],
                   'lastservicedate':data['servicedate'],
                   'lastservicereason':data['reason'],
                   'lastmaintanence':data['maintanence'],
                   'status':data['status']
            
                }

           conn.execute(query,values)
           return render_template("main.html")           
        
@app.route('/api/motorSection')
def jsonmotor():
    motor=load_motor_sec()
    return jsonify(motor)





def load_resource_sec():
    with engine.connect() as conn:
        result=conn.execute(text("select * from resource"))
        resource_sec=[]
        for row in result.all():
            resource_sec.append(dict(row._mapping))
        
        return resource_sec
 

@app.route("/displayresource")
def displayresource():
    resource=load_resource_sec()
    return render_template("displayresource.html",resource=resource)


@app.route("/addresourceform")
def addresourceform():
    return render_template("resourceform.html")

@app.route('/deleteresource/<id>')
def deleteresource(id):
   
    with engine.connect() as conn:
       query=(text("delete from resource  where employee_id=:ids"))
       values={'ids':id}
       conn.execute(query,values)
       
    return render_template("main.html")



@app.route('/addresource',methods=['post'])
def addresource():
       data=request.form
       with engine.connect()as conn:
           query=text("insert into resource(id,name,contact,email,designation,employee_id,experience,dateOfJoining,current_shift) values(:id,:name,:contact,:email,:designation,:employee_id,:experience,:dateOfJoining,:current_shift)")
           values={'id':data['id'],
                   'name':data['name'],
                   'contact':data['contactno'],
                   'email':data['email'],
                   'designation':data['designation'],
                   'employee_id':data['employeeid'],
                   'experience':data['experience'],
                   'dateOfJoining':data['doj'],
                   'current_shift':data['shift']
            }
           conn.execute(query,values)
           return render_template("main.html")           
        
@app.route('/api/resourceSection')
def jsonresource():
    resource=load_resource_sec()
    return jsonify(resource)







def load_pro_sec():
    with engine.connect() as conn:
        result=conn.execute(text("select * from productions"))
        pro_sec=[]
        for row in result.all():
            pro_sec.append(dict(row._mapping))
        
        return pro_sec
 

@app.route("/displaypro")
def displaypro():
    pro=load_pro_sec()
    return render_template("displayprodform.html",pro=pro)


@app.route("/addproform")
def addproform():
    return render_template("addprodform.html")

@app.route('/deletepro/<id>')
def deletepro(id):
   
    with engine.connect() as conn:
       query=(text("delete from productions  where id=:ids"))
       values={'ids':id}
       conn.execute(query,values)
       
    return render_template("main.html")



@app.route('/addpro',methods=['post'])
def addpro():
       data=request.form
       with engine.connect()as conn:
           query=text("insert into productions(id,date,resourcename,section,totalProductions,shift,remark,dateandtime) values(:id,:date,:resourcename,:section,:totalProductions,:shift,:remark,:dateandtime)")
           values={'id':data['id'],
                   'date':data['date'],
                   'resourcename':data['rname'],
                   'section':data['section'],
                   'totalProductions':data['totalProductions'],
                   'shift':data['shift'],
                   'remark':data['remark'],
                   'dateandtime':data['dot'] }
           conn.execute(query,values)
           return render_template("main.html")           
        
@app.route('/api/proSection')
def jsonpro():
    resource=load_resource_sec()
    return jsonify(resource)



if __name__=="__main__":
    app.run(host='0.0.0.0',debug=True)