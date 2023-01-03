if __name__ == '__main__':

 def nestedlist():
    records=[]
    unique_scores=set()
    for x in range(int(input())):
        name = input()
        score = float(input())
        records.append([name,score])
        unique_scores.add(score)
    
    segundo=(sorted(unique_scores))[1]
    nombres_segundo=[]
    for y in range(len(records)):
        if segundo==records[y][1]:
            nombres_segundo.append(records[y][0])
    
    nombres_segundo.sort() 
    for z in range(len(nombres_segundo)):
       print(nombres_segundo[z])
   

  

nestedlist()