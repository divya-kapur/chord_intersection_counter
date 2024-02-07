
import json
import numpy as np

def count_intersections(rad_measures, ids):
    input_list = list(zip(rad_measures, ids))

    
    chords_dict = {}
    for rad_measure, id in input_list:
        chord_num = int(id[1:])
        point_type = 's' if id[0] == 's' else 'e'
        if chord_num not in chords_dict:
            chords_dict[chord_num] = [None, None]
        if point_type == 's':
            chords_dict[chord_num][0] = rad_measure
        else:
            chords_dict[chord_num][1] = rad_measure

    # Starting from 0 -> 2 pi, sort chords based on starting points
    chords_dict = dict(sorted(chords_dict.items(), key=lambda item: item[1][0]))

    chord_measures = np.array(list(chords_dict.values()))

    intersections_count = 0
    for chord_i in range(0, len(chord_measures)):
        for chord_j in range(chord_i+1, len(chord_measures)):
            s1 = chord_measures[chord_i][0]
            e1 = chord_measures[chord_i][1]
            s2 = chord_measures[chord_j][0]
            e2 = chord_measures[chord_j][1]
            # For two chords to intersect, one of the following conditions must be satisfied:
            # 1. s1 is b/w s2 & e2, and e1 is not b/w s2 & e2
            if (s2 < s1 < e2) and (e1 > e2):
                intersections_count += 1
            # 2. e1 is b/w s2 & e2, and s1 is not b/w s2 & e2
            elif (s2 < e1 < e2) and (s1 < s2):
                intersections_count += 1

    return intersections_count

rad_measures = input("Enter list of radian measures:")
ids = input("Enter list of corresponding identifiers")
try:
    rad_measures = json.loads(rad_measures)
    ids = json.loads(ids)
except json.JSONDecodeError:
    print("Error: please ensure your input lists are in correct JSON list format.")

count_intersections(rad_measures, ids)


