# Opening of file that has Student data
with open('StudentList.txt', 'r') as data:

    highest_gwa = 0
    highest_gwa_student = ''
    lowest_gwa = 0
    lowest_gwa_student = ''

    for line in data:
        # Split the name of the students and their GWA
        name, gwa = line.strip().split(',')
        gwa = float(gwa)
        # Initialization
        if highest_gwa == 0:
            highest_gwa = gwa
            lowest_gwa = gwa
            # Check if the current student has a lower GWA than the previous highest
        if gwa > lowest_gwa:
            lowest_gwa = gwa
            lowest_gwa_student = name
        # Check if the current student has a higher GWA than the previous highest
        elif gwa < highest_gwa:
            highest_gwa = gwa
            highest_gwa_student = name

    print(
        f'The student with the highest GWA is {highest_gwa_student} with a GWA of {highest_gwa}.')
    print(
        f'The student with the lowest GWA is {lowest_gwa_student} with a GWA of {lowest_gwa}.')
