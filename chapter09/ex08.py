#без метода zfill() получилось, не поняла, для чего он                      
#Ответ: 198888, 199999

def is_palindrome(s):
    return s == s[::-1]

for n in range(100000, 1000000):
    if is_palindrome(str(n)[2:]):
        if is_palindrome(str(n + 1)[1:]):
            if is_palindrome(str(n + 2)[1:5]):
                if is_palindrome(str(n + 3)):
                    print(n)
