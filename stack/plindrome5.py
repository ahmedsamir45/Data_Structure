def isPalindrome(A):
#firist index
    i=0
#last index
    j = len(A)-1

    while (i < j and A[i] == A[j]):

        i += 1
        
        j -= 1
    if (i < j ):
        print("Not a Palindrome")
        return 0
    else:
        print("Palindrome")
        return 1
    
name = input('Enter string to check if it plindrome : ')    
isPalindrome(name)
