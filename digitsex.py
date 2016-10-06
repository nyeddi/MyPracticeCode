def solution(digits):
    sp=list(str(digits))
    print sp
    # unbound local error occured because you have nt added condition where
    # no of didgits entererd is less than 5 you should not proceed. if you
    #proceed for loop written by you will not execute and at the end you are
    #returning "high" which is not created
    # Hope you understand my explaination
    if len(sp) < 5:
        print "please enter no with min digits 5"
        return
    sp.sort(reverse=True)
    print sp
    return int("".join(sp[0:5]))
    # No need to write the below code for your problem
    # the answer should straight forward like the sort and get the
    # first five elements of list and convert to int.


    
    """
    for n in range(0,len(sp)-4):
        high=0
        first =(sp[n:n+5])
        krishh= ''.join(map(str, first))
        if krishh>high:
            high = krishh
        else:
            return False
    return high
    """

print solution(555719558836)
