s = "If we took the bones out, it wouldn’t be crunchy, would it?"
s.split()
type(s.split())
s.split("o")
s.split("i")
"0".join(s.split("o"))

def myreplace(old, new, s):
    test(myreplace(",", ";", "this, that, and some other thing") ==
                          "this; that; and some other thing")
    test(myreplace(" ", "**",
                  "Words will now     be   separated by stars.") ==
                  "Words**will**now**be**separated**by**stars.") 
    
myreplace("o","x","What?")


#I have no idea whats going on here