import random


def score_cal(fitness):    
    total_fitness = 0
    
    # For each course that is taught by an instructor who can teach it, other than Staff: +3
    total_fitness += (12 - fitness.count('STAFF'))*3
    
    # For each course taught by Staff: +1
    total_fitness += fitness.count('STAFF')

    # For each course that is the only course scheduled in that room at that time: +5
    x = 0
    indexing = 1
    room_indexing = 2
    holder = fitness.split('.')

    # holder each room that is not twice the enrollment size
    room_counter = []
    
    while x != 12:
        
        # if (holder[room_indexing]+holder[room_indexing+1]) not in room_counter:
        # room_counter.append(holder[room_indexing]+ holder[room_indexing])
            
        # For each course that is in a room large enough to accommodate it: +5
        if int(holder[indexing]) < int(holder[indexing + 4]):
            total_fitness += 5

        if int(holder[indexing]) <= int(holder[indexing + 4])/2:
            total_fitness += 0
            
        x += 1
        indexing += 6
        room_indexing += 5
        
    # Room capacity is no more than twice the expected enrollment: +2
    total_fitness += len(room_counter) * 2
        
    # For each schedule that has the same instructor teaching more than 4 courses: -5 per course over 4
    teachers = ['H.', 'K.', 'B.', 'M.', 'R.', 'S.']
    for teacher in teachers:
        if fitness.count(teacher) > 4:
            total_fitness += (fitness.count(teacher) - 4) * (-5)

    # For each schedule that has Rao or Mitchell (graduate faculty) teaching more courses than Hare or Bingham
    # (same number of courses is OK): -10
    if (fitness.count('R.') or fitness.count('M.')) > (fitness.count('B.') or fitness.count('H.')):
        total_fitness += (-10)
          
    # CS 101 and CS 191 are usually taken the same semester; the same applies to CS 201 and CS 291. Therefore apply
    # these rules to those pairs of courses:
    holder = fitness.split('.')
    time101a = holder[holder.index('CS101A')+3][:-1]
    time101a_location = holder[holder.index('CS101A') + 4]
                      
    time101b = holder[holder.index('CS101B') + 3][:-1]
    time101b_location = holder[holder.index('CS101B') + 4]

    time191a = holder[holder.index('CS191A') + 3][:-1]
    time191a_location = holder[holder.index('CS191A') + 4]

    time191b = holder[holder.index('CS191B') + 3][:-1]
    time191b_location = holder[holder.index('CS191B') + 4]

    time201a = holder[holder.index('CS201A') + 3][:-1]
    time201a_location = holder[holder.index('CS201A') + 4]
                  
    time201b = holder[holder.index('CS201B') + 3][:-1]
    time201b_location = holder[holder.index('CS201B') + 4]
                  
    time291a = holder[holder.index('CS291A') + 3][:-1]
    time291a_location = holder[holder.index('CS291A') + 4]

    time291b = holder[holder.index('CS291B') + 3][:-1]
    time291b_location = holder[holder.index('CS291B') + 4]

    quad = ['Haag', 'Royall', 'Flarsheim']

    times = [time101a, time101b, time191a, time191b, time201a, time201b, time291a, time291b]
    locations = [time101a_location, time101b_location, time191a_location, time191b_location, time201a_location,
                 time201b_location, time291a_location, time291b_location]

# Courses are scheduled for same time: -15
    for time in times:
        for second_time in times:
            
            if times[times.index(time)] != times[times.index(second_time)]:
                if int(time) == int(second_time):
                    total_fitness += (-15)
            # Courses are scheduled for adjacent times: +5
            else:
                total_fitness += 5
                # if these courses are scheduled for adjacent times, and are in the same building: +5 points
                if locations[times.index(time)] == locations[times.index(second_time)]:
                    total_fitness += 5
                # Are both on the quad (Haag, Royall, Flarsheim): no modification
                elif locations[times.index(time)] in quad and time101B_location in quad:
                    total_fitness += 0
                # 1 is in Katz and the other isn’t: -3
                elif (locations[times.index(time)] == 'Katz209' and locations[times.index(second_time)] != 'Katz209') or (locations[times.index(time)] != 'Katz209' and locations[times.index(second_time)] == 'Katz209'):
                    total_fitness += (-3)
                # 1 is in Bloch and the other isn’t: -3
                elif (locations[times.index(time)] == 'Bloch0009' and locations[times.index(second_time)] != 'Bloch0009') or (locations[times.index(time)] != 'Bloch0009' and locations[times.index(second_time)] == 'Bloch0009'):
                    total_fitness += (-3)
                # (Yes, if one’s in Katz and the other’s in Bloch, that’s -6)
                elif (locations[times.index(time)] == 'Bloch0009' and locations[times.index(second_time)] == 'Katz209') or (locations[times.index(time)] == 'Katz209' and locations[times.index(second_time)] == 'Bloch0009'):
                    total_fitness += (-6)
            
    # CS101A and CS101B are scheduled 3 hours apart or more: +5
    if (int(time101a) - int(time101b)) > 0:
        if (int(time101a) - int(time101b)) >= 3:
            total_fitness += 5
    else:
        if (int(time101b) - int(time101a)) >= 3:
            total_fitness += 5

    # CS191A and CS191B are scheduled 3 hours apart or more: +5
    if (int(time191a) - int(time191b)) > 0:
        if (int(time191a) - int(time191b)) >= 3:
            total_fitness += 5
    else:
        if (int(time191b) - int(time191a)) >= 3:
            total_fitness += 5
            
    return total_fitness


# Instructors and what they can teach:
def fitness():
    fitness_string = ''
    classes = ['CS101A.', 'CS101B.', 'CS191A.', 'CS191B.', 'CS201A.', 'CS201B.', 'CS291A.', 'CS291B.', 'CS303.',
               'CS341.', 'CS449.', 'CS461.']
    for x in classes:
        fitness_string += x

        classes_hold ='CS101A.40.CS101B.25.CS191A.60.CS191B.20.CS201A.30.CS201B.30.CS291B.40.CS291A.20.CS303.50.CS341.40.CS449.55.CS461.40.'
        if len(x) == 7:
            fitness_string += classes_hold[classes_hold.find(x) + 7: classes_hold.find(x) + 10]
        else:
            fitness_string += classes_hold[classes_hold.find(x) + 6: classes_hold.find(x) + 9]

        teachers = [
            {'CS101A.': ['H.', 'B.', 'S.']},
            {'CS101B.': ['H.', 'B.', 'S.']},
            {'CS191A.': ['B.', 'M.', 'S.']},
            {'CS191B.': ['B.', 'M.', 'S.']},
            {'CS201A.': ['H.', 'B.', 'S.']},
            {'CS201B.': ['H.', 'B.', 'S.']},
            {'CS291A.': ['H.', 'B.', 'M.', 'R.', 'S.']},
            {'CS291B.': ['H.', 'B.', 'M.', 'R.', 'S.']},
            {'CS303.': ['H.', 'K.', 'M.', 'R.', 'S.']},
            {'CS341.': ['K.', 'M.', 'R.', 'S.']},
            {'CS449.': ['H.', 'B.', 'S.']},
            {'CS461.': ['H.', 'R.', 'S.']}
            ]

        for y in teachers:
            if x in y:
                random_teach = random.randint(0, len(y[x])-1)
                fitness_string += y[x][random_teach]

        time_slots = ['10A.', '11A.', '12P.', '1P.', '2P.', '3P.', '4P.']
        random_time_slot = random.randint(0, len(time_slots)-1)

        fitness_string += time_slots[random_time_slot]

        rooms = ['Hagg301.', 'Hagg206.', 'Royall204.', 'Katz209.', 'Flarsheim310.', 'Flarsheim260.', 'Bloch0009.']
        random_room = random.randint(0, len(rooms)-1)

        fitness_string += rooms[random_room]
         
        class_max = 'Hagg301.70.Hagg206.30.Royall204.70.Katz209.50.Flarsheim310.80.Flarsheim260.25.Bloch0009.30.'

        starting_point = class_max.index(rooms[random_room])

        fitness_string += class_max[starting_point + len(rooms[random_room]):starting_point+len(rooms[random_room])+3]
    
    return fitness_string


def random_switch(fitness):
    classes = ['CS101A.', 'CS101B.', 'CS191A.', 'CS191B.', 'CS201A.', 'CS201B.', 'CS291A.', 'CS291B.', 'CS303.',
               'CS341.', 'CS449.', 'CS461.']
    switch = random.randint(0, len(classes)-1)
    switching = random.randint(1, 3)

    if switching == 1:
        # switching of the classes and students in them
        classes_hold = 'CS101A.40.CS101B.25.CS191A.60.CS191B.20.CS201A.30.CS201B.30.CS291B.40.CS291A.20.CS303.50.CS341.40.CS449.55.CS461.40.'
        class_switch = random.randint(0, len(classes)-1)
        class1 = classes[switch]
        class2 = classes[class_switch]
        class1_students = ''
        class2_students = ''
   
        class1_students += classes_hold[classes_hold.find(class1):classes_hold.find(class1)+len(class1)+3]
        class2_students += classes_hold[classes_hold.find(class2):classes_hold.find(class2)+len(class1)+3]
       
        class_place_holder = '...'
        fitness = fitness.replace(class2 + class2_students, class_place_holder)
        fitness = fitness.replace(class1 + class1_students, class2 + class2_students)
        fitness = fitness.replace(class_place_holder, class1 + class1_students)
        
    elif switching == 2:
        # this switch is for changing a set of rooms
        rooms = ['Hagg301', 'Hagg206', 'Royall204', 'Katz209', 'Flarsheim310', 'Flarsheim260', 'Bloch0009']
        class_max = 'Hagg301.70.Hagg206.30.Royall204.70.Katz209.50.Flarsheim310.80.Flarsheim260.25.Bloch0009.30.'

        # random number for a new room to switch too
        room_change = random.randint(0, len(rooms)-1)
        room_switch = random.randint(0, len(rooms)-1)

        old_classroom = ''
        new_classroom = ''
        room1 = rooms[room_change]
        room2 = rooms[room_switch]

        # this section finds the room that will be switched and the # of students in it
        
        old_classroom += class_max[class_max.find(room1):class_max.find(room1)+len(room1)+4]
       
        # this section finds the new room to replace the old and the # of students in it
        new_classroom += class_max[class_max.find(room2):class_max.find(room2)+len(room2)+4]
  
        # the class hold is to keep duplicate rooms out of the string
        class_place_holder = '...'

        # we then switch the new class to ... so we don't have duplicates, update the old room with the new and replace
        # the ... with the old room thus switching the class and number of students in that class
        fitness = fitness.replace(room2 + new_classroom, class_place_holder)
        fitness = fitness.replace(room1 + old_classroom, room2 + new_classroom)
        fitness = fitness.replace(class_place_holder, room1 + old_classroom)

    elif switching == 3:
        teachers = ['H', 'B', 'M', 'K', 'R', 'S']
        position = [2, 8, 14, 20, 26, 32, 38, 44, 50, 56, 62, 68]
        teacher_switch = random.randint(0, len(position)-1)
        new_teacher = random.randint(0, len(teachers)-1)
        
        combine = '.'
        holder = fitness.split('.')
        holder[position[teacher_switch]] = teachers[new_teacher]
        fitness = combine.join(holder)

    else:
        time_slots = ['10A', '11A', '12P', '1P', '2P', '3P', '4P']
        position = [3, 9, 15, 21, 27, 33, 39, 45, 51, 57, 63, 69]
        time_switch = random.randint(0, len(position)-1)
        new_time = random.randint(0, len(time_slots)-1)
        
        combine = '.'
        holder = fitness.split('.')
        holder[positons[time_switch]] = time_slots[new_time]
        fitness = combine.join(holder)

    return fitness
    

fitness = fitness()
e1 = score_cal(fitness)
attempts = 0
changes = 0
e2 = None
T = 100
temp = 0.5
while attempts <= 4000 or changes <= 400:
    best_score = 0
    new_fitness = random_switch(fitness)
    e2 = score_cal(new_fitness)
    total_energy = e2 - e1
    
    if total_energy > 0:
        e1 = e2
        changes += 1

    elif ((e2-e1)/T) < temp:
        e1 = e2
        changes += 1
        
    if changes == 400:
        input('changes == 400')
        T = T * 0.9
        changes = 0
            
    attempts += 1
    
    if attempts == 4000 and changes == 0:
        input('here')
        break

##    print('current_attempts:', attempts, '  ', 'current_chcanges:', changes)
##    print('current_Temp:', (e2-e1)/T)
##    print('e2=', e2, '', 'e1=', e1)
