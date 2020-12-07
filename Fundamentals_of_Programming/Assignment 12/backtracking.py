#Generate all subsequences of length 2n+1, formed only by 0, -1 or 1, such that 
# 𝑎1= 0, ..., 𝑎2𝑛+1= 0 and |𝑎𝑖+1-𝑎𝑖| = 1 or 2, for any 1 ≤ i ≤ 2n.
#0 -1 1 -1 1

def iterative():
    values=[0,-1,1]
    n=int(input('n='))
    position_for_value=0
    subsequence=[]
    for i in range(2*n):
            if i==0:
                subsequence.append(values[position_for_value])
            elif i==2*n:
                subsequence.append(values[0])
            else:
                while abs(values[position_for_value]-subsequence[i])!=1 or abs(values[position_for_value]-subsequence[i])!=2:
                    if position_for_value==2:
                        position_for_value-=1
                    else:
                        position_for_value+=1
                subsequence.append(values[position_for_value])
    print(subsequence)

def recursive():
    pass

if __name__ == "__main__":
    iterative()