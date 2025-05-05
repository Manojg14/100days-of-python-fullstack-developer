student_details = { "manoj":22,"deepak":19,"kalis":21,"naveen":18,"kumar":21,"ram":22,"suresh":23 }

student_maths_mark={ "manoj":80,"deepak":75,"kalis":90,"naveen":70,"kumar":50,"ram":30,"suresh":65 }

student_science_mark = { "manoj": 85,"deepak": 77,"kalis": 60,"naveen": 80,"kumar": 40,"ram": 70,"suresh": 55 }

student_english_mark = {"manoj": 70,"deepak": 56,"kalis": 65,"naveen": 87,"kumar": 80,"ram": 44,"suresh": 89}

def students_mark_details(student_name):
    if student_name in (student_details and student_maths_mark and student_science_mark and student_english_mark):
        age = student_details[student_name]
        math_mark =student_maths_mark[student_name]
        science_mark=student_science_mark[student_name]
        english_mark=student_english_mark[student_name]
        return f"\nSTUDENT NAME:{student_name},\nSTUDENT AGE: {age},\nSTUDENT MATHS MARK: {math_mark},\nSTUDENT SCIENCE MARK: {science_mark},\nSTUDENT ENGLISH MARK: {english_mark}"

    else:
        return "enter invalid details"

Student_namelist = list(student_details.keys())
print("STUDENT NAME IN DATABASE:",Student_namelist)

student_name = input("Enter student name: ").lower()



print(students_mark_details(student_name))



