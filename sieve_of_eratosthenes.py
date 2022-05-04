def sieve_of_eratosthenes(num):
    """
    The sieve of eratosthenes is an ancient algorithm for finding all prime numbers less than a given value 'num'.
    The function 'sieve_of_eratosthenes takes in an integer as input, and returns a list containing all prime numbers less than it.
    """
    try:
        sieve = [True for i in range(num-2)]
        all_num = [i for i in range(2,num)]

        prime = []

        #Goes through the boolean list and picks the first True as prime number on each loop
        #That is after multiples of the first True 'num' have been changed to False(not prime)
        for index, bool_ in enumerate(sieve):
            if bool_:
                num = all_num[index]
                prime.append(num)
                
                index += num
                while index in range(len(all_num)):
                    sieve[index]=False
                    index += num

        return prime
    
    except:
        return "Invalid input."
