#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3

import cgi
import os
form = cgi.FieldStorage()
pageID = form["pageID"].value
title = form["title"].value
description = form['description'].value

opened_file = open('data/'+pageID,'w')
opened_file.write(description) # file 
opened_file.close()

os.rename('data/'+pageID, title)

#redirectipn
print("Location: index.py?id="+title) 
print()