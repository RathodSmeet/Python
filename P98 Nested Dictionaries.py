# Nested Dictionaries
stud1 = {
    'rno':1,
    'stud_name':"Raxit",
    'class':'BCA',
    'sem':6
}
stud2 = {
    'rno':2,
    'stud_name':"Smeet",
    'class':'BCA',
    'sem':6
}
stud3 = {
    'rno':3,
    'stud_name':"Harsh",
    'class':'BCA',
    'sem':6
}
students = {
    'stud1' : stud1,
    'stud2' : stud2,
    'stud3' : stud3
}
print(students['stud1']['stud_name'])