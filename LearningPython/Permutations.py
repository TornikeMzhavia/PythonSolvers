#Write a function which prints all the permutations of an input text string.
test_input = "abc"

def get_permutations(input_string):
    if(len(input_string) == 1):
        yield input_string
    else:
        for permutation in get_permutations(input_string[1:]):
            for index in range(len(input_string)):
                yield permutation[:index] + input_string[0:1] + permutation[index:]

def all_perms(s):
    if len(s) <= 1: 
        yield s
    else:
        for i in range(len(s)):
            for p in all_perms(s[:i] + s[i+1:]):
                yield s[i] + p        
        
print(list(all_perms(test_input)))
        

