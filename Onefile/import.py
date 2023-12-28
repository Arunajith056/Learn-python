# Consider a module to be the same as a code library.

# A file containing a set of functions you want to include in your application.


import export as imp # also give import export 
from export import multipliy
from OOPS.User import User 


sum = imp.sum  # we have function in export.py file
print(sum(2, 4))

multipliy = multipliy(2,4)
print(multipliy)

user = User("cmd2453", 60060)
user.register()