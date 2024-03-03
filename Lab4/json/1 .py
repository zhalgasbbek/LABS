import json 

with open("TSIS 1/Lab4/json/sample-data.json",'r') as file:
  x = json.load(file)

print("Interface Status")
print("="*80)
print("DN                                                 Description           Speed    MTU")
print("-------------------------------------------------- --------------------  ------  -----")

for elementsofx in x['imdata'] :
   DN = elementsofx['l1PhysIf']['attributes']["dn"]
   Description = elementsofx["l1PhysIf"]['attributes']['descr'] 
   Speed = elementsofx["l1PhysIf"]['attributes']['speed']
   MTU = elementsofx["l1PhysIf"]['attributes']['mtu']
   if len(DN) == 1 :
       print(DN , Description ,"                            " , Speed , MTU)
   else:
       print(DN , Description ,"                             ",Speed,MTU)