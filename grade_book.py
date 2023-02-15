# students will lilely start from A:
def get_grade(s1, s2, s3):
    m = (s1 + s2 + s3) / 3.0
    if 90 <= m <= 100:
        return 'A'
    elif 80 <= m < 90:
        return 'B'
    elif 70 <= m < 80:
        return 'C'
    elif 60 <= m < 70:
        return 'D'
    return "F"

# or start from F and save yourself some work:
def get_grade(s1, s2, s3):
    avg = (s1 + s2 + s3) / 3.0 
    if avg <= 60:
        return 'F'
    elif avg < 70:
        return 'D'
    elif avg < 80:
        return 'C'
    elif avg < 90:
        return 'B'
    else:
        return 'A'