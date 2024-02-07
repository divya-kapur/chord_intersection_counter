# Chord Intersection Counter

This Python script calculates the number of intersections among chords in a circle. Each cord is defined by their start and end points in a circle, represented by their radian measures. The script takes in two parallel lists as input: one containing radianc measures of the start/end points of the chords and another containing identifiers indicating the start ('s') or end ('e') of a chord.  The algorithm consists of a few key steps:
    1. Dictionary creation: Pairs of start and end radian measures are zipped together and stored in a dictionary with chord numbers as keys. Runtime is O(N) where N = number of start/end points in total
    2. Sorting: Dictionary values are sorted based on start radian measures. Runtime is O(N log N)
    3. Intersection checks: Each pair of chords is checked for intersections using geometric criteria. For two chords to intersect, one of the following conditions must be satisified:
        (a) the start point of chord 1 is between the start & end points of chord 2, but the end point of chord 1 is not between the start & end points of chord 2
        (b) the end point of chord 1 is between the start & end points of chord 2, but the start point of chord 1 is not between the start & end points of chord 2. Runtime = O(N^2)
**Overall Big-O Runtime:** O(N^2)

## Dependencies: 
    1. Python 3.x
    2. NumPy

Ensure that you have Python 3.x installed on your system. You can download it from python.org.

NumPy is used for handling arrays efficiently. You can install NumPy using pip:
    pip install numpy

## How to Use:

**Input Format:** The script expects two inputs in list format. The first input is a list of radian measures, and the second is a list of corresponding identifiers.
Example of radian measures: [0.78, 1.47, 1.77, 3.92]
Example of identifiers: ["s1", "s2", "e1", "e2"]

**Running the Script:** Run the script in a terminal or command prompt. When prompted, paste or type your radian measures and identifiers into the respective inputs.
    python chord_intersections.py

**Output:** The script will output the count of intersecting chords based on the provided inputs.

