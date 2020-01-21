from flask import Flask, request, render_template,jsonify
import json
from telnetlib import Telnet
import time
from datetime import datetime, timezone,timedelta
from split4letre import do_json
app = Flask(__name__,static_folder='templates')

def do_something(text1,text2):
   text1 = text1.upper()
   text2 = text2.upper()
   combine = text1 + text2
   print(combine)
   return combine

   #Return the Data from path
@app.route('/json', methods=['GET','POST'])
def Troublshoot_Rigbox(): 
   data=read_JSON()
   return json.dumps(data, indent=4)

   
   
#Use telnet to get the Data
@app.route('/json_telnet', methods=['GET','POST'])
def Troublshoot_Telnet(): 
   text1 = request.form['text1']
   print(text1)
   telnet(text1)
   data=read_JSON()
   return json.dumps(data, indent=4)
   


#Telnet methode
def telnet(adresip):
 now =datetime.now()
 dt = datetime.now()
 dt.microsecond
 date_time_str = now.strftime(" %H%M%S")
 date_time_as_bytes = str.encode(date_time_str)
 with Telnet(adresip, 9101) as tn:
        OUTPUT=tn.read_until(b'0106'+date_time_as_bytes,40)
        FILE=open('C:\\Users\\aziz\\Desktop\\wits_Rig_Box.txt', "w")
        FILE.write(OUTPUT.decode("utf-8"))
        FILE.close()
 return FILE


data=[
    {
        'name':'Audrin',
        'place': 'kaka',
        'mob': '7736'
    },
    {
        'name': 'Stuvard',
        'place': 'Goa',
        'mob' : '546464'
    }
]


#Not this one
@app.route('/Rig', methods=['GET','POST'])
def Data_Rig():
    text1 = request.form['text1']
    word = request.args.get('text1')
    text2 = request.form['text1']
    combine = do_something(text1,text2)
    result = {
        "output": combine
    }
    print('Rig')
    people = [{'name': 'Alice', 'birth-year': 1986},
          {'name': 'Bob', 'birth-year': 1985}]
    return jsonify(people) 
    #result = {str(key): value for key, value in result.items()}
    #return jsonify(result=result)
    

# Not This one
@app.route('/')
def home():
    user_details = {
      'name': 'TP161',
        'email': 'GASA'
    }
    return render_template('home.html', user=user_details)


#From json to DATA
def read_JSON():
      with open('C:\\Users\\aziz\\Desktop\\wits.json') as json_file:
         data = json.load(json_file)
      #for p in data:
       # print('value: ' + p['value'])
       # print('chanel: ' + p['chanel'])
      return data


    
    #result = {str(key): value for key, value in result.items()}
    #return jsonify(result=result)

if __name__ == '__main__':
     app.run(debug=True)
     app.run(host='10.171.59.7', port=1234)
