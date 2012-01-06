import re


mail = "('adrian@dealised.com',)"
test = re.sub("([(',)])","",mail)
print test