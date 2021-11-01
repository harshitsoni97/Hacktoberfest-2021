T = [[5, 4, 3],  
         [2, 4, 5],  
         [6, 7, 9],  
         [8, 1, 3]]  
 
transResult = [[0, 0, 0, 0],    
                             [0, 0, 0, 0],  
                             [0, 0, 0, 0]]  

for a in range(len(T)):    
   for b in range(len(T[0])):    
          transResult[b][a] = T[a][b]         
print("The transpose of matrix T is:: ")  
for res in transResult:    
   print(res)
