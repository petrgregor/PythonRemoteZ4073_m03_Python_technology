import school
from school import student
from school import student, teacher
from school import *
from school import classroom as room
from school.student import get_grades

from school.teacher import *
#from school.student import *

from school.classrooms import *
from school.classrooms.classroom1 import *

print(get_grades())

number = float(int(input('Zadej číslo')))
