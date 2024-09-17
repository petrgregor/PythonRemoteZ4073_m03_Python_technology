import modul_a as m_a
#import modul_a1
#from modul_a1 import test as test_a1, name
from modul_a1 import *

print(m_a.test)
#print(modul_a1.test)
#print(test_a1)
print(test)
print(name)

courses = ["Tělocvik", "Historie", "Matematika"]
index = m_a.find_index(courses, "Tělocvik")
print(index)

name = "Martin"
name = "David"
print(name)
