#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3

import cgi, os
form = cgi.FieldStorage()

pageID = form["pageId"].value
os.remove('data/'+pageID)

#redirectipn
print("Location: index.py") 
print()

