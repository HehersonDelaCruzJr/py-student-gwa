# Opening of file that has Student data
with open('StudentList.txt', 'r') as f:

    highest_gwa = 0
    highest_gwa_student = ''

    for line in f:
        # Split the name of the students and their GWA
        name, gwa = line.strip().split(',')
        gwa = float(gwa)

    print(
        f'The student with the highest GWA is {highest_gwa_student} with a GWA of {highest_gwa}.')
