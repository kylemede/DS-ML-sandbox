import sys
import ast
import cmath
 
def cmd_to_verts():
    """ Convert command line arguments into vertices. 
    This function can accept arguments passed in on the command line in the 
    following formats:
    '  x1,y1   x2,y2   x3,y3'
    ' (x1,y1) (x2,y2) (x3,y3)' 
    ' [x1,y1] [x2,y2] [x3,y3]'
    '((x1,y1),(x2,y2),(x3,y3))' 
    '[[x1,y1],[x2,y2],[x3,y3]]'
    """
    args = sys.argv
    # args[0] is script name
    # args[1:] will be the space separated strings passed in after script name
    s = "Sorry, but this program can only accept command line "+\
        "arguments in the following formats:\n"+"  'x1,y1' 'x2,y2' 'x3,y3\n'"\
        " '(x1,y1)' '(x2,y2)' '(x3,y3)'\n '[x1,y1]' '[x2,y2]' '[x3,y3]'\n"+\
        "'((x1,y1),(x2,y2),(x3,y3))'\n'[[x1,y1],[x2,y2],[x3,y3]]'\n"
        
    ## First need to parse inputs into 3 (x,y) or (y,x) pairs 
    # let's check if there are more than one input 
    if len(args[1:])>1:
        if len(args[1:])==3:
            # inputs were of format '(x1,y1) (x2,y2) (x3,y3)' 
            #                    or '[x1,y1] [x2,y2] [x3,y3]'
            pt1 = ast.literal_eval(args[1])
            pt2 = ast.literal_eval(args[2])
            pt3 = ast.literal_eval(args[3])
        else:
            raise IOError("\n\n"+s)
    elif len(args[1:])==1:
        if ("[[" in args[1]) or ("((" in args[1]):
            # The input is '((x1,y1),(x2,y2),(x3,y3))' 
            #           or '[[x1,y1],[x2,y2],[x3,y3]]'
            [pt1,pt2,pt3] = ast.literal_eval(args[1])  
    else:
        raise IOError("\n\n"+s)
        
    # let user know what we got out of their command line arguments
    print "Argument(s) pass in were:\n"+repr(args[1:])+"\n"
    print "This was converted to:\n"+repr([pt1,pt2,pt3])  
    
    return  (pt1,pt2,pt3)
    
def cmd_to_sides():
    """ Convert command line arguments into side lengths. 
    This function can accept arguments passed in on the command line in the 
    following formats:
    'a,b,c'
    'a' 'b' 'c'
    '(a,b,c)'
    '[a,b,c]'
    """
    args = sys.argv
    # args[0] is script name
    # args[1:] will be the space separated strings passed in after script name
    s = "Sorry, but this program can only accept command line arguments in "+\
        "the following formats:\n"+\
        "'a,b,c'\n'a' 'b' 'c'\n'(a,b,c)'\n'[a,b,c]'\n"
        
    # let's check if there are more than one input 
    if len(args[1:])>1:
        if len(args[1:])==3:
            # inputs were of format 'a' 'b' 'c'
            a = ast.literal_eval(args[1])
            b = ast.literal_eval(args[2])
            c = ast.literal_eval(args[3])
        else:
            raise IOError("\n\n"+s)
    elif len(args[1:])==1:
        if ("[" in args[1]) or ("(" in args[1]):
            # The input is '(a,b,c)' or '[a,b,c]'
            [a,b,c] = ast.literal_eval(args[1])  
    else:
        raise IOError("\n\n"+s)
        
    # let user know what we got out of their command line arguments
    print "Argument(s) pass in were:\n"+repr(args[1:])+"\n"
    print "This was converted to:\n"+repr([a,b,c])  
    
    return (a,b,c)

def triangle_sides_prompt():
    """
    Prompt user to pass in length of triangle sides.
    """
    ## prompt user to input side lengths
    print "#"*40+"\n"+" Please enter the length of each side."
    a = float(input("Length of first side: "))
    b = float(input("Length of second side: "))
    c = float(input("Length of third side: "))
    print "#"*40+"\n"
    
    return (a,b,c)

    
def verts_to_sides(pt1, pt2, pt3):
    """ Convert vertices to side lengths. """
    ## Convert 3 vertices coordinates into side lengths
    a = ((pt1[0]-pt2[0])**2+(pt1[1]-pt2[1])**2)**0.5
    b = ((pt2[0]-pt3[0])**2+(pt2[1]-pt3[1])**2)**0.5
    c = ((pt3[0]-pt1[0])**2+(pt3[1]-pt1[1])**2)**0.5
    
    return (a,b,c)

def triangle_area():
    """
    Calculates the area of a triangle  with Heron's formulat from the length 
    of the 3 sides.
    """
    ###################################
    # Options for how to provide inputs
    ###################################
    ## For command line vertices to side lengths
    (pt1,pt2,pt3) = cmd_to_verts()
    (a,b,c) = verts_to_sides(pt1, pt2, pt3)
    ## For command line side lengths
    #(a,b,c) = cmd_to_sides()
    ## For prompt to provide side lengths
    #(a,b,c) = triangle_sides_prompt()
    
    ## Apply Heron's Formula to get area of triangle
    s = 0.5*(a+b+c)
    area = (s*(s-a)*(s-b)*(s-c))**(1.0/2.0)
    if True:
        if area==0.0:
            s = "\nThe points form a line, thus there is no triangle to "+\
            "calculate the area of.\n"
            print s
        else:
            print ("\nThe triangle's area is: %0.4f" %area +"\n")
    if False:
        return area
    
def quadratic():
    """ Solves the quadratic equation
    ie. ax**2 +bx + c = 0
    """
    
    ## prompt user to input side lengths
    print "#"*62
    print " Please enter value of each coefficient in ax**2 +bx + c = 0"
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))
    print "#"*62+"\n"
    
    ## first calculate 'discriminator'
    d = b**2 - (4.0*a*c)
    
    ## Solve for both solutions
    s1 = (-b-cmath.sqrt(d))/(2*a)
    s2 = (-b+cmath.sqrt(d))/(2*a)
    
    print("The solutions are {0}".format(s1) + " and {0}".format(s2)+"\n")
    
def is_prime():
    """ Determine if the input is a prime number or not."""
    ## prompt user or something to get number
    num=4 ## HACK$$$$$$$$$
    
    ## Check if it is a prime number
    tf = all(num%i for i in xrange(2,num))
    
    tf_txt = ' IS a prime number\n'
    if tf==False:
        tf_txt = ' is NOT a prime number\n'
    
    print("\n"+str(num)+tf_txt)

if __name__ == '__main__':
    triangle_area()
    #quadratic()
    #is_prime()
    
    
    