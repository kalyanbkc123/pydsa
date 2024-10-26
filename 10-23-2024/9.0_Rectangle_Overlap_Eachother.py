
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y


def check_rectangle_overlap(S,P,S_p,P_p):

    if(S.x > P_p.x or P.x > S_p.x):
        return False 
    if(S.y > P_p.y or P.y > S_p.y):
        return False 
    
    return True


# Example

S = Point(1,1)
P = Point(3,3)
S_p = Point(2,2)
P_p = Point(4,4)    

res  = check_rectangle_overlap(S,P,S_p,P_p)

print(res)



