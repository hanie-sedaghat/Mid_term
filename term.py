import json
import sqlite3
cnt=sqlite3.connect('e:\python\passed.db')
action=input("what do you want to do? ")
scores={}
if action=='input' :
    while True:
        user=input("Enter your username: ")
        score=int(input("Enter your score: "))
        if(0 > score > 20):
            print("wrong score!!")
        if(user=="exit"):
            break
        else:
            scores[user]=score
    with open ('e:\python\scores.json','w') as s:
         json.dump(scores,s)
    
elif action=='export' :
    with open ('e:\python\scores.json') as s:
         finale_score=json.load(s)
    for item in finale_score :
        if 0 <(finale_score[item])<10 :
            sql='''CREATE TABLE passed
                  (id INTEGER PRIMARY KEY,
                   username CHAR(20) NOT NULL,
                   score INTEGER(1) NOT NULL);'''
            cnt.execute(sql)
            cnt.close()
            sql='''INSERT INTO passed(username,score)
                   VALUES(?,?)'''
            cnt.execute(sql,(item,finale_score[item]))
            cnt.commit()
            cnt.close()
            sql='''SELECT username,score'''
            result=cnt.execute(sql)

        else:
            with open ('e:\python\failed.json') as f:
                json.dump(item,finale_score[item],f)
                
         
            
            

            
            
            
            
            
            
            
            