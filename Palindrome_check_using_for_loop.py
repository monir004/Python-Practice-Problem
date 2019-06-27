def palindrome_checker(sentence):
    #print("Got the inputted sentence"+sentence)
    sentence_length = len(sentence)
    j=sentence_length-1
    flag=1
    for i in range(sentence_length//2): 
        # / does float division, // does int division
        if sentence[i] == sentence[j]:
            j-=1
            continue
        else:
            flag=0
            break
    return flag
    
        
def main():
    sentence = input("Please enter a number to check palindrome\n")
    flag = palindrome_checker(sentence)
    if flag == 1:
        print(sentence+" is a palindrome")
    else:
        print(sentence+" is not a palindrome")

if __name__ == "__main__":
    main()
