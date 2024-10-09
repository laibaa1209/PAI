import numpy as np

student_dtype = np.dtype([
    ('name', 'U50'), 
    ('height', 'f4'),  
    ('class', 'U10')   
])


students = np.array([
    ('Laiba', 1.65, '10'),
    ('Bilal', 1.75, '8'),
    ('Zafir', 1.68, '6'),
    ('Aira', 1.70, '10'),
    ('Fatima', 1.60, '7')
], dtype=student_dtype)

sorted_students = np.sort(students, order=['class', 'height'])

print(sorted_students)
