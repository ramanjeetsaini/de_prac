from Stack import *

def is_match(y,x):
    if x=='[' and y==']':
        return True
    if x=='{' and y=='}':
        return True 
    if x=='(' and y==')':
        return True
    else:
        return False       
def is_paren_balanced(paren_string):
    i=0
    s=Stack()
    is_balanced=True

    while i<len(paren_string) and is_balanced:
        if paren_string[i] in "[{(":
            s.push(paren_string[i])
        else:
            if s.is_empty():
                is_balanced = False
                break
            else:
                top=s.pop()
                if not is_match(top,paren_string[i]):
                    is_balanced =False
                    break
        i+=1
    if s.is_empty() and is_balanced:
        return True
    else:
        return False
    
print("String : (((({})))) Balanced or not?")
print(is_paren_balanced("(((({}))))"))