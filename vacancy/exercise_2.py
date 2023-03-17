def bigger_Is_greater():
    # T
    while True:
        T = int(input("enter the number of test cases: "))
        1 <= T <= 10**5
        break

    final_result = []
    
    #Python magic
    for case_number in range(T):
        # w
        while True:
            w = input("enter the word: ").strip()    
            #checks the range[a...z]
            if not w.isalpha():
                print("enter only letters in the range ascii[a...z]")
                continue
            #checks length
            1 <= len(w) <= 100
            break

        #swap letters
        w_list = []
        for letter in w:
            w_list.append(letter)
        n = len(w) - 1
        answer = False
        while n > 0:
            if w_list[n] > w_list[n-1]:
                extra = w_list[n]
                w_list[n] = w_list[n-1]
                w_list[n-1] = extra
                answer = True
                break
            else:
                n -= 1

        #put result in final output
        if answer:
            final_result.append("".join(w_list))
        else:
            final_result.append("no answer")
    
    #results
    return " ".join(final_result)

print(bigger_Is_greater())