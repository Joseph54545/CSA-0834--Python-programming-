# Function to demonstrate all argument types
def student_info(name, age, grade='A', *subjects, **extra_info):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Grade: {grade}")
    
    print("Subjects:", ', '.join(subjects))
    
    for key, value in extra_info.items():
        print(f"{key}: {value}")

# Positional Arguments
student_info('John', 15)

# Keyword Arguments
student_info(name='Alice', age=14, grade='B')

# Default Arguments (Grade defaults to 'A')
student_info('Bob', 13)

# Variable-length Arguments (Using *args)
student_info('Emily', 16, 'A', 'Math', 'Science', 'History')

# Variable-length Keyword Arguments (Using **kwargs)
student_info('Mark', 17, 'A', 'Math', 'Science', address='123 Main St', phone='555-1234')
