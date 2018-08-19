import sys
from pymongo import MongoClient

def get_rank(user_id):
    client = MongoClient()
    db = client.shiyanlou
    contests = db.contests

    d = {}
    for userdata in contests.find():
        id = userdata['user_id']
        user_score = userdata['score']
        stime = userdata['submit_time']
        if d.get(id):
            #print(user_id,end=':')
            #print(d[user_id][0])
            d[id][0] += user_score
           # print(d[user_id][0])
           # print(user_id,end=':')
           # print(d[user_id][1])
            d[id][1] += stime
           # print(d[user_id][1])
        else:
            d[id] = [user_score,stime]
           # print(user_id,end=':')
           # print('not get ')

    l = sorted(d.values(),key=lambda x:(-x[0],x[1]))
    for i,j in enumerate(l):
        d[[k for k,v in d.items() if v==j][0]].insert(0,i+1)

    #print(tuple(d[user_id]))
    #print(d[user_id])
    #print(user_id)
    # return tuple(d[user_id])
    #    return rank,score,submit_time
  
    i = d[user_id]
    rank = d[user_id][0]
    score = i[1]
    submit_time = i[2]
    #rank = d[user_id].get(0)
    #score = tuple(d[user_id])[1]
    #submit_time = tuple(d[user_id])[2]
 
    return rank,score,submit_time
    
    #return tuple(d[user_id])

if __name__ == '__main__':
    try:
        user_id = int(sys.argv[1])
    except ValueError:
        print('Parameter Error')
        exit()
        
    userdata = get_rank(user_id)
    #print('userdate',end='-')
    print(userdata)
