def generate_value_of_sequence(position):
    #returns the value of the element of the given position 
    # in the sequence of natural numbers by replacing composed
    #  numbers with  their prime divisors
    sequence_index=1
    if(position==1):
        return 1
    for natural_number in range(2,position+1):
        divisor=2
        natural_numbers_to_destroy=natural_number
        while natural_numbers_to_destroy!=1:
            if natural_numbers_to_destroy%divisor==0:
                if divisor==natural_number:
                    sequence_index+=1
                else:
                    sequence_index+=divisor
                if sequence_index>=position:
                    return (divisor)
            while natural_numbers_to_destroy%divisor == 0:
                natural_numbers_to_destroy/=divisor
            divisor+=1

if __name__ == '__main__':
    position=int(input('Position='))
    print("The element of the given position=",generate_value_of_sequence(position))