from pandas import DataFrame
from pandas import pandas as pd

f = open("C:\\Users\\aziz\\Desktop\\wits_Rig_Box.txt", "r")
array=f.readlines()
array2json= [500]
record01='01'
First4fromwits=''
Time= {'0101': 'Well Identifier','0101\n': 'Well Identifier', '0102\n': 'Sidetrack/Hole Sect No','0102': 'Sidetrack/Hole Sect No', '0103': 'Record Identifier','0104\n': 'Sequence Identifier',
       '0104': 'Sequence Identifier','0105\n': 'Date', '0105': 'Date','0106\n': 'Time','0106': 'Time','0106\n': 'Time',
       '0107': 'Activity Code', '0108': 'Depth Bit (meas)','0109': 'Depth Bit (vert)',
       '0110': 'Depth Hole (meas)', '0111': 'Depth Hole (vert)', '0112': 'Block Position',
       '0113': 'Rate of Penetration (avg)', '0114': 'Hookload (avg)', '0115': 'Hookload (max)',
       '0116': ' Weight-on-Bit (surf,avg)', '0117': 'Weight-on-Bit (surf,max)', '0118': ' Rotary Torque (surf,avg)',
       '0119': 'Rotary Torque (surf,max)', '0120': 'Rotary Speed (surf,avg) ', '0121': ' Standpipe Pressure (avg)',
       '0122': 'Casing (Choke) Pressure ', '0123': 'Pump Stroke Rate #1 ', '0124': 'Pump Stroke Rate #2',
       '0125': 'Pump Stroke Rate #3', '0126': 'Tank Volume (active)', '0127': 'Tank Volume Change (act)',
       '0128': 'Mud Flow Out %', '0129': 'Mud Flow Out (avg)', '0130': 'Mud Flow In (avg)',
       '0131': 'Mud Density Out (avg) ', '0132': 'Mud Density In (avg)', '0133': 'Mud Temperature Out (avg)',
       '0134': 'Mud Temperature In (avg)', '0135': 'Mud Conductivity Out (avg)', '0136': 'Mud Conductivity In (avg)',
       '0137': 'Pump Stroke Count (cum)', '0138': 'Lag Strokes ', '0139': 'Depth Returns (meas)',
       '0140': 'Gas (avg)', '0141': 'Instantaneous ROP', '0142': 'Upstream choke pressure ',
       '0143': 'Upstream choke temperature', '0144': 'Downstream choke pressure ' ,'0201': 'Well Identifier', '0202': 'Sidetrack/Hole Sect No.', '0203': 'Record Identifier',
       '0204': 'Sequence Identifier', '0205': 'Date', '0206': 'Time',
       '0207': 'Activity Code', '0208': 'Depth Hole (meas)', '0209': 'Depth Hole (vert)',
       '0210': 'Rate of Penetration (avg)', '0211': 'Weight-on-Bit (surf,avg)', '0212': 'Hookload (avg)',
       '0213': 'Standpipe Pressure (avg)', '0214': 'Rotary Torque (surf,avg)', '0215': 'Rotary Speed (surf,avg)',
       '0216': 'Rotary Speed (surf,avg)', '0217': 'Mud Density In (avg) ', '0218': 'ECD at Total Depth',
       '0219': 'Mud Flow In (avg)', '0220': 'Mud Flow Out (avg)', '0221': 'Mud Flow Out %',
       '0222': 'Tank Volume (active)', '0223': 'Cost/Distance (inst)', '0224': 'Cost/Distance (cum)',
       '0225': 'Bit Drilled Time', '0226': 'Bit Drilled Distance ', '0227': 'Corr. Drilling Exponent ',
       '0228': 'Block Position ', '0229': 'Rotary Torque (surf,max)','0405': 'Block Position ','0406': 'Block Position ','0407': 'Block Position ','0408': 'Block Position ','0409': 'Block Position ','0410': 'Block Position ','0411': 'Block Position ','0412': 'Block Position ','0413': 'Block Position ','0414': 'Block Position ','0415': 'Block Position ','0416': 'Block Position ','0417': 'Block Position ','0418': 'Block Position ','0419': 'Block Position ','0420': 'Block Position ','0421': 'Block Position ','0422': 'Block Position ','0423': 'Block Position ','0424': 'Block Position ','0425': 'Block Position ','0426': 'Block Position ','0427': 'Block Position ','0428': 'Block Position ','0429': 'Block Position ','0430': 'Block Position ','0431': 'Block Position ','0432': 'Block Position ','0433': 'Block Position ','0434': 'Block Position '}
Rcords_11={'1101': 'Well Identifier', '1102': 'Sidetrack/Hole Sect No.', '1103': 'Record Identifier',
       '1104': 'Sequence ', '1105': 'Sequence ','1106': 'Sequence ','1107': 'Sequence ',
           '1108': 'Sequence ','1109': 'Sequence ','1110': 'Sequence ','1111': 'Sequence ',
           '1112': 'Sequence ','1113': 'Sequence ','1114': 'Sequence ','1115': 'Sequence ',
           '1116': 'Sequence ','1117': 'Sequence ','1118': 'Sequence ','1119': 'Sequence ',
           '1120': 'Sequence ','1121': 'Sequence ','1122': 'Sequence ','1123': 'Sequence ',
           '1124': 'Sequence ','1125': 'Sequence ','1126': 'Sequence ','1127': 'Sequence ',
           '1128': 'Sequence ','1129': 'Sequence ','1130': 'Sequence ','1131': 'Sequence ',}

Well_Rigbox={'ENTP160': '10.205.61.60', 'GWDC112': '10.205.64.60', 'ENF58': 'Record Identifier',
       'TP161': 'Sequence ', 'TP184': 'Sequence ','TP202': 'Sequence ','TP194': 'Sequence ',
           'TP203': 'Sequence ','ENF59': 'Sequence ','1110': 'Sequence ','1111': 'Sequence ',
           '1112': 'Sequence ','1113': 'Sequence ','1114': 'Sequence ','1115': 'Sequence ',
           '1116': 'Sequence ','1117': 'Sequence ','1118': 'Sequence ','1119': 'Sequence ',
           '1120': 'Sequence ','1121': 'Sequence ','1122': 'Sequence ','1123': 'Sequence ',
           '1124': 'Sequence ','1125': 'Sequence ','1126': 'Sequence ','1127': 'Sequence ',
           '1128': 'Sequence ','1129': 'Sequence ','1130': 'Sequence ','1131': 'Sequence ',}

chanel = []
value = []
Truevalue = []

def chenel_Finder(arra):
      First4fromwits = ''.join([s[:4].upper() for s in arra.split(' ')])
      return First4fromwits

#just affichage of chanel
def afficher_chanel():
      for i in range(1,len(array)) : 
          
          if chenel_Finder(array[i]).startswith('01') or chenel_Finder(array[i]).startswith('02')  or chenel_Finder(array[i]).startswith('03') or chenel_Finder(array[i]).startswith('04') or chenel_Finder(array[i]).startswith('05') :
                chanel.append(chenel_Finder(array[i]))
          else:
                 0
#afficher list of chanel 
def List_chanel():
   for i in range(1,len(chanel)) : 
     #print(chanel[i])
     print(Time[chanel[i]])
    
    
def List_value():
       for i in range(1,len(value)) : 
         if  len(value[i]) != 0:
           #print(value[i].split('\n')[0])
           Truevalue.append(value[i].split('\n')[0])

#this is the True Value           
def truvalue_affiche():           
   for  i in range(0,len(Truevalue)):
      print(Truevalue[i])


def Value_finder(arra):
      After4Fromwits = ''.join([s[4:].upper() for s in arra.split(' ')])
      return After4Fromwits
     #First4 = ''.join([s[:4].upper() for s in arra.split(' ')])
     #if First4.startswith('01') or First4.startswith('02')  or First4.startswith('03') or First4.startswith('04') or First4.startswith('05') or First4.startswith('11') or First4.startswith('12') or First4.startswith('13') or First4.startswith('14') or First4.startswith('10') :
           
          # if After4Fromwits is not None:  
       
          # else :
                 # print('this is None')

#this are values
def in_the_value():
  for i in range(1,len(array)) : 
    
      value.append(Value_finder(array[i]))
      



    #this are channels
def in_the_chanel():
  for i in range(1,len(array)) : 
     
      chanel.append(chenel_Finder(array[i]))


#List of value
in_the_value()
#List of chanel
#in_the_chanel()

#for i in range(4,10):
    # Bug here
 # print(chanel[i])
  #print(Time[chanel[i]])
  #print(value[i])
  
def do_json():
  df = pd.DataFrame(columns=['chanel'])
  for i in range(1,len(chanel)) :
     df = df.append({'chanel': Time[chanel[i]],'value':Truevalue[i]}, ignore_index=True)
     df.to_json(r'C:\Users\aziz\Desktop\wits.json',orient='records') 
     print (df)   


List_value()
afficher_chanel()
truvalue_affiche()
do_json()
#List_chanel()
