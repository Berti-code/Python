def break_into_digits(number,frequency_list):
    while number!=0:
        index=int(number%10)
        frequency_list[index]+=1
        number=int(number/10)

def compose_smallest_number_from_digits(frequency_list):
    number=0
    for i in range(0,10):
        while(frequency_list[i]!=0):
            number+=i
            number*=10
            frequency_list[i]-=1
    return int(number/10)

if __name__ == '__main__':
    frequency_list=[0,0,0,0,0,0,0,0,0,0]
    number=int(input('Number='))

    break_into_digits(number,frequency_list)
    print('Minimal natural number with the same digits:',compose_smallest_number_from_digits(frequency_list))
