
student_age = input('Please enter your age : ')
student_age = int(student_age)
required_age_at_school =  5

if student_age == required_age_at_school:
    print('You are eligible to go to school')
elif student_age > 14:
    print('You are elgible to go to higher scondary school ')
elif student_age < required_age_at_school:
    print('You should take care of your self and waite for the right time to go to school')
else: 
    print('You can not go to school')
        
