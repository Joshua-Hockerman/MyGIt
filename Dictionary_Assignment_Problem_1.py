def main():

    room_number = {
        'CS101' : 3004,
        'CS102' : 4501,
        'CS103' : 6755,
        'NT110' : 1244,
        'CM241' : 1411
    }

    instructor = {
        'CS101' : 'Haynes',
        'CS102' : 'Alvarado',
        'CS103' : 'Rich',
        'NT110' : 'Burke',
        'CM241' : 'Lee'
    }

    meeting_time = {
        'CS101' : '08:00 a.m.',
        'CS102' : '09:00 a.m.',
        'CS103' : '10:00 a.m.',
        'NT110' : '11:00 a.m.',
        'CM241' : '01:00 p.m.'
    }

    user_input = input("Please enter the Course Number: ")

    print("The course " + user_input + " is held in room " + str(room_number[user_input]) + ", the instructor is Professor " + instructor[user_input] + ", and it is held at " + meeting_time[user_input])

main()
