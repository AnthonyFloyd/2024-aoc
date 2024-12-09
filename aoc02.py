# Advent of Code 2024
# Day 2

# Thought I'd be clever and use numpy. A good call but unnecessary.
import numpy as np

inputFileLines = open(r"c:\temp\aoc\2024\AOC-02.txt").readlines()

# Ugh. Had to grab edge cases from github because I'd clearly missed something
#inputFileLines = open(r"c:\temp\aoc\2024\AOC-02-edges.txt").readlines()

# Read the data in.
inputData = []
for line in inputFileLines:
    inputData.append([int(_) for _ in line.strip().split()])

nPasses = 0 # The number of cases that pass

# Step through each line in the input.
# The input is a list of integers.
# Calculate the differences between adjacent integers
# Then see if the progression is "valid".
#
# Part A:
# Valid progression is that the numbers are only increasing or decreasing
# and that the step can be no larger than 3

for line in inputData:
    # Calculate the step between adjacent numbers
    differences = np.array(line[1:]) - np.array(line[:-1])

    passed = False
    # All increasing but less than 3 gap?
    if np.all(differences>0) and np.all(differences<=3): 
        passed = True
    # All decreasing but less than 3 gap?
    elif np.all(differences < 0) and np.all(differences >= -3):
        passed = True

    # Count 'em up!    
    if passed:
        nPasses += 1

print(f'Part A: {nPasses}')

# Now, allow for one "problem" in each row
# Do this by allowing any one item in the list to be removed
# then testing the resulting list.
#
# VERY IMPORTANT: _Any_ item in the list.
#

# Reset the counter.
nPasses = 0

# Debugging
reportAllSafe = False

if reportAllSafe:
    safeReports = open(r'C:\temp\aoc\2024\AOC-02-safe-amf.txt','w')

# Step through all the input data again
for line in inputData:
    differences = np.array(line[1:]) - np.array(line[:-1])

    passed = False

    # Same test as before

    # All increasing but less than 3 gap?
    if np.all(differences>0) and np.all(differences<=3): 
        passed = True
    # All decreasing but less than 3 gap?
    elif np.all(differences < 0) and np.all(differences >= -3):
        passed = True

    # Now, if we didn't pass look closer

    if not passed:
        # Locate the problem, pop out the value, create new list, test again
        # But only allow one problem
        # But which one is the problem one? Always the right most? No, try both.
        # And try the middle
        #
        # In retrospect, this was the worse approach, but I'd committed to it.

        # Some lists to hold the copies of the data line with either the current item removed
        # the one before the current (left) or the one after the current (right)
        newLineR = []
        newLineM = []
        newLineL = []

        # We need to track if we've been increasing or decreasing as we march along
        wasIncreasing = False
        wasDecreasing = False

        # Check, number by number, to see if the step to the next number is valid or not
        for i, value in enumerate(line[:-1]):
            difference = line[i+1] - line[i]

            if difference == 0:
                # Must be increasing or decreasing, this is a failure
                newLineR = line[:i+1] + line[i+2:]
                newLineM = line[:i] + line[i+1:]
                newLineL = line[:i-1] + line[i:]
                break
            elif difference > 0:
                # We're increasing. This could be okay.
                if wasDecreasing: # But not if we were decreasing before
                    newLineR = line[:i+1] + line[i+2:]
                    newLineM = line[:i] + line[i+1:]
                    newLineL = line[:i-1] + line[i:]
                    break
                if difference > 3: # Also not if the step is greater than 3
                    newLineR = line[:i+1] + line[i+2:]
                    newLineM = line[:i] + line[i+1:]
                    newLineL = line[:i-1] + line[i:]
                    break
                else:
                    wasIncreasing = True # No problem
            else:
                # We're decreasing. This could be okay.
                if wasIncreasing: # But not if we were increasing before
                    newLineR = line[:i+1] + line[i+2:]
                    newLineM = line[:i] + line[i+1:]
                    newLineL = line[:i-1] + line[i:]
                    break
                if difference < -3: # Also not if the step is greater than 3
                    newLineR = line[:i+1] + line[i+2:]
                    newLineM = line[:i] + line[i+1:]
                    newLineL = line[:i-1] + line[i:]
                    break
                else:
                    wasDecreasing = True # No problem

        # Now, check conditions with new list
        # These end up being empty if there was no problem
        # But also we don't get here if there was no problem

        newDifferencesR = np.array(newLineR[1:]) - np.array(newLineR[:-1])
        newDifferencesM = np.array(newLineM[1:]) - np.array(newLineM[:-1])
        newDifferencesL = np.array(newLineL[1:]) - np.array(newLineL[:-1])

        # Same testing as before but we need to check each of the 3 lists

        # All increasing but less than 3 gap?
        if np.all(newDifferencesR > 0) and np.all(newDifferencesR <= 3): 
            passed = True
        # All decreasing but less than 3 gap?
        elif np.all(newDifferencesR < 0) and np.all(newDifferencesR >= -3):
            passed = True
        # All increasing but less than 3 gap?
        elif np.all(newDifferencesL > 0) and np.all(newDifferencesL <= 3): 
            passed = True
        # All decreasing but less than 3 gap?
        elif np.all(newDifferencesL < 0) and np.all(newDifferencesL >= -3):
            passed = True
        # All increasing but less than 3 gap?            
        elif np.all(newDifferencesM > 0) and np.all(newDifferencesM <= 3): 
            passed = True
        # All decreasing but less than 3 gap?
        elif np.all(newDifferencesM < 0) and np.all(newDifferencesM >= -3):
            passed = True
        # else:
        #     print(f'\n{newLineL} didn\'t fix {line} {differences}')
        #     print(f'{newLineR} didn\'t fix {line} {differences}')
        #     print(f'{newLineM} didn\'t fix {line} {differences}')
        #     True == True 

    if passed:
        nPasses += 1
        if reportAllSafe:
            safeReports.write(f'{line}\n')

print(f'Part B: {nPasses}')

if reportAllSafe: safeReports.close()

