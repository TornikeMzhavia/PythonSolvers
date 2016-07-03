import collections

def extract_dif(A_dict, B_dict):
    for number, count in B_dict.items():
        if(number not in A_dict or count > A_dict[number]):
            yield int(number)

n=int(input())
A_dict=collections.Counter(input().split(' '))

m=int(input())
B_dict=collections.Counter(input().split(' '))

print(' '.join((str(el) for el in sorted(extract_dif(A_dict, B_dict)))))