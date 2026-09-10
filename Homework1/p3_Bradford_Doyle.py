

def find_dup_str(s,n):
    
    if n <= 0:
        return ""
    if n > len(s):
        return ""

    start = 0
#as long as first part is within length n
    while start <= len(s) -n:
        sub1 = s[start:start+n]
#ooking for a second part later in the string
        start2 = start + 1
        while start2 <= len(s) -n:
            sub2 = s[start2:start2+n]
#checking if the substrings match and do not overlap
            if sub1 == sub2:
                if start2 >= start + n:
                    return sub1

            start2 = start2 + 1
        start = start + 1
    return ""
#user enters string and length of possible duplicate
text = input("enter string: ")
num = int(input("enter length: "))
print(find_dup_str(text,num))

def find_max_dup(s):
    size =len(s) - 1
    while size > 0:
        temp = find_dup_str(s,size)
        if temp != "":
            return temp
        size = size - 1
    return ""

text = input("enter string: ")
print(find_max_dup(text))
