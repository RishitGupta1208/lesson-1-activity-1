student_data={'id1':
        {'name':['Sara'],
        'class':['V'],
        'subject_interoggation':['physics,bio,chemistry']
        },
        'id2':
        {'name':['David'],
        'class':['IV'],
        'subject_interoggation':['physics,bio,chemistry']
        },
        'id3':
        {'name':['Sparsh'],
        'class':['IX'],
        'subject_interoggation':['physics,bio,chemistry']
        },
}
result={}
for key,value in student_data.items():
    if value not in result.values():
        result[key]=value
print(result)