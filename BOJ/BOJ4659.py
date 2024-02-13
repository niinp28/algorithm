# 비밀번호 발음하기
vowels = set(['a','e','i','o','u'])

while True:
    word = input()
    if word == 'end':
        break
    else:
        is_vowel = False
        is_v_three = 0
        is_c_three = 0
        err = False
        for i in range(len(word)):
            if word[i] in vowels:
                is_vowel = True
                is_c_three = 0
                is_v_three += 1
            else:
                is_v_three = 0
                is_c_three += 1
            
            if is_v_three == 3 or is_c_three == 3:
                err = True
                break
            if i < len(word)-1:
                if word[i] == word[i+1]:
                    if word[i] == 'e' or word[i] == 'o':
                        continue
                    else:
                        err = True
                        break
        
        if err == False and is_vowel == True:
            print(f'<{word}> is acceptable.')
        else:
            print(f'<{word}> is not acceptable.')