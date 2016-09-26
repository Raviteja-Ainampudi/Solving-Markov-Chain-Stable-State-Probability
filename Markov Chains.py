# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 17:14:27 2016

@author: RAVI TEJA
"""
from fractions import Fraction
m = [[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
#m = [[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
#m = [[0, 2, 1, 0, 0, 0], [0, 0, 0, 3, 4, 0], [0, 0, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
#m = [[0, 2, 1, 0, 0], [1, 0, 0, 2, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
#m = [[0, 1, 0, 0, 0, 2], [4, 0, 0, 3, 0, 0], [0, 0, 0, 0, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]

def answer(m):
    i = len(m)
    
    #Pobability Matrix of Non stable sublist elements
    n = m
    for k in range(i):
        total = 0
        for j in range(len(m[k])):
            total = n[k][j] + total
        #print total
        if total > 0:
            for l in range (len(n[k])):
                n[k][l] = Fraction ((n[k][l]), (total))
    print "Converting the nxn matrix into fractions"
    print n
        
    #Possibility to reach a terminal state
    #Terminal states matrix
    ter_mat = []
    for k in range(i):
        total = 0
        for j in range(len(m[k])):
            total = n[k][j] + total
        #print total
        if total == 0:
            ter_mat.append(k)
    #print "Terminal state list Matrix"
    #print ter_mat
   
    prob_mat =[]
    
   #For non loop states in the whole nxn matrix
    for j in range (len(n[0])):    
        for i in range (len(ter_mat)):
       
           #prob = 1
           if (j in ter_mat) and (n[i][j] > 0):
               temp_mat =[]
               u = i+1
               v = j
               while (u < ter_mat[0]):
                   for v in range(j+1):
                       temp_mat.append(n[u][v])
                   u +=1
               #print "Temp_Mat"
               #print temp_mat
               if not any(temp_mat):
                   prob = n[i][j]
                   for k in range(i+1):
                     if k != i:
                       if n[k][i] >0:
                           prob *= n[k][i]
                   prob_mat.append(prob)
               
                               
               elif (j in ter_mat) and (n[i][j] > 0) and (sum(temp_mat) > 0):
                   prob = n[i][j]
                   for k in range(i+1):
                       if n[k][i] >0:
                           prob *= n[k][i]
                   #prob_mat.append(prob)
                   #print "index"        
                   #print ter_mat.index(j)
                   prob_mat.insert(ter_mat.index(j), prob)
                   
               else:
                   pass
                   
                    
              
        
    #Looking for an element with ZERO Probability
    for j in range(len(n[0])):
            if (j in ter_mat):
                 count1 =0   
                 for k in range(len(n)-len(ter_mat)):
                    if n[k][j] == 0:
                        count1 +=1
                 #print "Count1"
                 #print count1
                 if count1 == len(n)-len(ter_mat):
                    prob_mat.insert(ter_mat.index(j), Fraction(0,1))
     
    #display the probability of reaching the terminal state from state-0              
    
    print "Prob mat is"
    print prob_mat
    
    
    # To detect the loop for stable transition and find its probability
    for i in range(len(n)-len(ter_mat)):
        for j in range (len(n[i])):        
              if j not in ter_mat:
                 if n[i][j] >0 and (j>= i):
                    loop_prob = 1
                    if n[j][i] >0:
                        #print i
                        #print j 
                        loop_prob = n[i][j]*n[j][i]
                    loop_den = 1-loop_prob
                    #print loop_den
                    for l in range(len(prob_mat)):
                        #if l == j:
                            if loop_den > 0:
                                prob_mat[l] = Fraction(prob_mat[l], loop_den)
                                #print l
                                #print prob_mat[l]
                    print "prob mat after loop"
                    print prob_mat
    
    #Convert the the resultant matrix into the desired form into numerators and the denominator.
    den_mat = []
    for i in range (len(prob_mat)):
        den_mat.append(prob_mat[i].denominator)
    
    #print den_mat
    #den_max = max(den_mat)
    #LCM of denominators
    mul = 1
    for i in range(len(den_mat)):
        mul *= den_mat[i]
    
    factors = []
    for i in range(2, mul):
      if mul%i == 0:
        factors.append(i)

    y = sorted(factors)
    w = []
    for i in range(len(y)):
        count = 0
        for j in range(len(den_mat)):
            if y[i]%den_mat[j] == 0:
                count +=1
                if count == len(den_mat):
                    w.append(y[i])
                

    tom = sorted(w)
    if len(tom) > 0:
        den_max = tom[0]
    #print den_max
    
    result_lis = []
    if len(prob_mat) > 0:    
        for i in range (len(prob_mat)):
            k = den_max*prob_mat[i]
            result_lis.append(k.numerator)
        result_lis.append(den_max)
    else:
        print "error"
        
    print "Final Result is :"
    print result_lis
                   
            
answer(m)
