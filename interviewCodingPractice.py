import sys
import ast
import numpy as np
import cmath
from _ast import Num

# Lots of interesting geometry based coding puzzles discussed at: http://codegolf.stackexchange.com/questions/tagged/geometry
# Some of the puzzles posed there have functions started at the bottom of this script, but have not been fleshed out yet.
 
def bad_char_finder(ss):
    """Find the character in the string that is not a number or [ ] , ( )"""
    print "\n"+"^"*10+" problem with one of the characters provided "+"^"*10+"\n"
    for s in ss:
        if s not in ['[',']','(',')',',',' ']:
            if s.isdigit()==False:
                print "Character '"+s+"' is not approved for use with this function."
    print "\n"+"^"*65+"\n"

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
            l=[]
            for i in range(1,4):
                try:
                    l.append(ast.literal_eval(args[i]))
                except:
                    bad_char_finder(args[i])
                    raise IOError()
            [pt1,pt2,pt3] = l
        else:
            raise IOError("\n\n"+s)
    elif len(args[1:])==1:
        if ("[[" in args[1]) or ("((" in args[1]):
            # The input is '((x1,y1),(x2,y2),(x3,y3))' 
            #           or '[[x1,y1],[x2,y2],[x3,y3]]'
            try:
                [pt1,pt2,pt3] = ast.literal_eval(args[1])  
            except:
                bad_char_finder(args[1])
                raise IOError()
    else:
        raise IOError("\n\n"+s)

    # let user know what we got out of their command line arguments
    print "\nArgument(s) pass in were:\n"+repr(args[1:])+"\n"
    print "This was converted to:\n"+repr([pt1,pt2,pt3])+"\n"
    
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
            l=[]
            for i in range(1,4):
                try:
                    l.append(ast.literal_eval(args[i]))
                except:
                    bad_char_finder(args[i])
                    raise IOError()
            [a,b,c] = l
        else:
            raise IOError("\n\n"+s)
    elif len(args[1:])==1:
        if ("[" in args[1]) or ("(" in args[1]):
            # The input is '(a,b,c)' or '[a,b,c]'
            try:
                [a,b,c] = ast.literal_eval(args[1])  
            except:
                bad_char_finder(args[1])
                raise IOError()
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
    # Test non character inputs
    
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
    
def is_prime(num=4):
    """ Determine if the input is a prime number or not."""
    ## prompt user or something to get number
    ## REMOVE DEFAULT VALUE IN INPUTS
    # Test non character inputs
    
    ## Check if it is a prime number
    tf = all(num%i for i in xrange(2,num))
    
    tf_txt = ' IS a prime number\n'
    if tf==False:
        tf_txt = ' is NOT a prime number\n'
    
    print("\n"+str(num)+tf_txt)
    
    
def find_factors(num=136):
    """ Find the factors of the input number."""
    ## prompt user or something to get number
    ## REMOVE DEFAULT VALUE IN INPUTS
    # Test non character inputs
    
    ## make a list of all the factors
    factors = [] 
    for i in range(1,num+1):
        if num%i==0:
            factors.append(i)
            
    print "The factors of "+str(num)+" are:\n"+repr(factors)
    
def primes_in_interval(low=4,high=59):
    """ Find all the prime numbers in an interval"""
    ## prompt user or something to get the lower and upper limits of interval
    ## REMOVE DEFAULT VALUE IN INPUTS
    # Test non character inputs
    
    ## find all the primes
    primes = []
    for num in range(low,high+1):
        if num>1:
            if all(num%i for i in xrange(2,num)):
                primes.append(num)
    
    print "\nPrime numbers in the interval "+repr((low,high))+" are:"
    print repr(primes)+"\n"

def armstrong_number(num=-1000):
    """ Determine if number is an 'Armstrong Number'"""
    ## prompt user or something to input number
    ## REMOVE DEFAULT VALUE IN INPUTS
    # Test non character inputs
    
    if num<0:
        print "\nNumber provided is negative; thus, not an Armstrong Number.\n"
    else:
        s = 0
        t = num 
        while t>0:
            d = t%10
            t//=10
            s+=d**3
            
        if s==num:
            print "\n"+str(num)+" IS an Armstrong Number\n"
        else:
            print "\n"+str(num)+" is NOT an Armstrong Number\n"
    
def circles_overlap(r1=10,r2=0,cent_r1=[1,20],cent_r2=[1,3]):
    """ Calculate area of overlapping region between two circles """
    ## prompt user or something to get the inputs
    ## REMOVE DEFAULT VALUE IN INPUTS
    # Test non character inputs
        
    # if one of circles has zero radius, overlap is always zero
    overlap_area = 0
    if (r1*r2<0):
        print "\nOne of the circles has a negative radius; thus, do not overlap.\n"
    elif (r1*r2>0): 
        ## calculate distance between centers
        d = ((cent_r1[0]-cent_r2[0])**2.0+(cent_r1[1]-cent_r2[1])**2.0)**0.5
        
        big_r = r1
        small_r = r2
        if r2>r1:
            big_r = r2
            small_r = r1
        
        if d<=abs(big_r-small_r):
            # smaller circle is inside bigger circle,
            # so overlap is area of smaller circle.
            overlap_area = np.pi*(small_r)**2.0
            print "\nSmaller circle exists completely inside larger circle."
        elif d>=(r1+r2):
            # circles not touching, so no overlap.
            overlap_area = 0
            print "\nTwo circles do not intersect."
        else:
            # calculate opening angles of overlap for each circle
            ang_1 = np.arccos((d**2.0 + r1**2.0 - r2**2.0) / (2.0*d*r1))
            ang_2 = np.arccos((d**2.0 + r2**2.0 - r1**2.0) / (2.0*d*r2))
            # calculate area of cones
            #cone_area_1 = ang_1 * r1**2.0
            #cone_area_2 = ang_2 * r2**2.0
            cone_area_total = (ang_1 * r1**2.0) + (ang_2 * r2**2.0)
            # calculate area of triangles
            triangle_area_1 = 0.5 * r1**2.0 * np.sin(2*ang_1)
            triangle_area_2 = 0.5 * r2**2.0 * np.sin(2*ang_2)
            
            ## Calculate overlap area
            overlap_area = cone_area_total - triangle_area_1 - triangle_area_2
            
        print "\nArea of the overlap region for the two circles was: "+repr(overlap_area)+"\n"
    else:
        print "\nOne of the circles has a radius of zero; thus, do not overlap.\n"
            
def squares_overlap(sl1=1,sl2=3,cent1=[1,1],cent2=[2,2]):
    """ Calculate area of overlap between two squares.  
    Note: This function does not allow for any rotation of the squares."""
    ## prompt user or something to get the lower and upper limits of interval
    ## REMOVE DEFAULT VALUE IN INPUTS
    # Test non character inputs
    
    if sl1*sl2==0:
        print "\nOne of the squares has a side length of 0; thus, no overlap.\n"
    else:
        if sl1*sl2<0:
            msg = "\nOne of the squares has a negative side length.  Will "+\
                  "consider this a typo and use the absolute value instead."
            print msg
            sl1 = abs(sl1)
            sl2 = abs(sl2)
                
        x_diff = abs(cent1[0]-cent2[0])
        y_diff = abs(cent1[1]-cent2[1])
        
        x_overlap = 0
        y_overlap = 0
        if x_diff<(0.5*(sl1+sl2)):
            x_overlap = (0.5*(sl1+sl2))-x_diff
        if y_diff<(0.5*(sl1+sl2)):
            y_overlap = (0.5*(sl1+sl2))-y_diff
            
        if x_overlap*y_overlap==0:
            print "\nSquares do not touch; thus, no overlap.\n"
        else:
            overlap = x_overlap*y_overlap
            print "\nOverlap area for two squares is: "+str(overlap)+"\n"
    
    

def circles_overlap_border(r1,r2,cent_r1,cent_r2):
    """ Calculate the border of two circles that possibly overlap, not 
    counting any area of overlap as part of the border."""
    ## prompt user or something to get the inputs
    ## REMOVE DEFAULT VALUE IN INPUTS
    # Test non character inputs
    ## debug inputs
    ## Test this code, NOT TESTED YET
    temp = 1
    
    
def origin_in_triangle():
    """ Calculate if the origin is contained in a triangle."""
    ## prompt user or something to get the inputs
    ## REMOVE DEFAULT VALUE IN INPUTS
    # Test non character inputs
    ## debug inputs
    ## Test this code, NOT TESTED YET
    temp = 1
    
    
    
    
    
if __name__ == '__main__':
    #triangle_area()
    #quadratic()
    #is_prime()
    #find_factors()
    #primes_in_interval()
    #armstrong_number()
    #circles_overlap()
    squares_overlap()
    
    
    