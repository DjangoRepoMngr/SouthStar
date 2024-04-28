

def calc_student_dept(student):
    """ calculates the student dept for course """

    # the course which the student is in
    course = student.course

    # the amount the student payed money
    total_pay = student.total_payment

    disc = student.discount

    # the student do not have discount
    if disc is None:
        debt = course.course_fee - total_pay

    else:
        course_fee_with_discount = course.course_fee - ( (course.course_fee*disc.percent) /100)
        debt = course_fee_with_discount - total_pay

    return debt