student_data = {'id1':
                 {'Name': 'Sara',
                 'Class': 'V',
                 'Subject Integration' : ['English, Math , Science']},
                 'id2': 
                 {'Name': 'David',
                  'Class': 'V',
                  'Subject integration': ['Math , Science , Social studies']},
                 'id3': 
                 {'Name': 'Surya',
                  'Class': 'V',
                  'Subject integration': ['Math , Science , English']},
                 'id4': 
                 {'Name': 'Saina',
                  'Class': 'V',
                  'Subject integration': ['Math , Science , English']}
                }
result = {}

for key, value in student_data.items():
    if value not in result.values():
        result[key] = value

print(result)
