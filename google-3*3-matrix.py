"""
Given NxN matrix with integer numbers.
Find the greatest number for every 3x3 matrix.

update example

example.1
[[1,2,3],
[4,5,6],
[7,8,9]]

ans:
[9]

example.2
[[1,2,3,6],
[5,2,4,1],
[3,4,2,3],
[8,2,1,4]]

ans:
[[5,6],
[8,4]]

tc-m*n, sc-1
"""
ip=[[1,2,3,6,7],
[5,2,4,1,9],
[3,4,2,3,2],
[8,2,1,4,8],
[5,4,3,2,1]]
def main(ip):
    lim=len(ip)-3
    li=[]
    for i in range(lim+1):
        temp_li=[]
        for j in range(lim+1):
            x=greatest(i,j,ip)
            temp_li.append(x)
        li.append(temp_li)
    return li
        
            
    
    
def greatest(hor,vert,ip):
    m=-inf
    for i in range(hor,hor+3):
        for j in range(vert,vert+3):
            m=max(m,ip[i][j])
    return m
            
            
    
    
print(main(ip))