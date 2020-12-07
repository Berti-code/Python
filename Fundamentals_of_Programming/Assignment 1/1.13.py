def sequence(n):
    sequence_index=1
    if(n==1):
        return 1
    for natural_numbers in range(2,n+1):
        divisor=2
        while natural_numbers!=1:
            if natural_numbers%divisor==0:
                sequence_index+=1
                if sequence_index==n:
                    return (divisor)
            while natural_numbers%divisor == 0:
                natural_numbers/=divisor  
            divisor+=1
        
if __name__ == '__main__':
    n=int(input('N='))
    print("N-th element=",sequence(n))