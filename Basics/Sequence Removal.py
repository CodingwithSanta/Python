def seq_rem(input_string):
    result = [input_string[0]]
    for i  in range (1,len(input_string)):
        if input_string[i] != input_string[i-1]:
            result.append(input_string[i])
    return ''.join(result)

input_string = "aaabbbcddd"
print("After sequence reamoval",seq_rem(input_string)) 