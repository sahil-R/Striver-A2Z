def recurse(i,j,string):
    if i>j:
        return True
    else:
        if string[i]!=string[j]:
            return False
        else:
            return recurse(i+1,j-1,string)
def isPalindrome(string: str) -> bool:
    return recurse(0,len(string)-1,list(string))