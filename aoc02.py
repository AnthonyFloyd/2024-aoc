import numpy as np

inputFileLines = open(r"c:\temp\aoc\2024\AOC-02.txt").readlines()
#inputFileLines = open(r"c:\temp\aoc\2024\AOC-02-edges.txt").readlines()
inputData = []
for line in inputFileLines:
    inputData.append([int(_) for _ in line.strip().split()])

# Test data passes, actual data doesn't. :|

nPasses = 0

for line in inputData:
    differences = np.array(line[1:]) - np.array(line[:-1])
    # Run through the tests
    passed = False

    # All increasing but less than 3 gap?
    if np.all(differences>0) and np.all(differences<=3): 
        passed = True
    # All decreasing but less than 3 gap?
    elif np.all(differences < 0) and np.all(differences >= -3):
        passed = True

    if passed:
        nPasses += 1

print(f'Part A: {nPasses}')

# Now, allow for one problem

# Brute force

nPasses = 0
#safeReports = open(r'C:\temp\aoc\2024\AOC-02-safe-amf.txt','w')

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

        newLineR = []
        newLineM = []
        newLineL = []
        wasIncreasing = False
        wasDecreasing = False

        for i, value in enumerate(line[:-1]):
            difference = line[i+1] - line[i]

            if difference == 0:
                # Must be increasing or decreasing
                newLineR = line[:i+1] + line[i+2:]
                newLineM = line[:i] + line[i+1:]
                newLineL = line[:i-1] + line[i:]
                break
            elif difference > 0:
                if wasDecreasing:
                    newLineR = line[:i+1] + line[i+2:]
                    newLineM = line[:i] + line[i+1:]
                    newLineL = line[:i-1] + line[i:]
                    break
                if difference > 3:
                    newLineR = line[:i+1] + line[i+2:]
                    newLineM = line[:i] + line[i+1:]
                    newLineL = line[:i-1] + line[i:]
                    break
                else:
                    wasIncreasing = True # No problem
            else:
                if wasIncreasing:
                    newLineR = line[:i+1] + line[i+2:]
                    newLineM = line[:i] + line[i+1:]
                    newLineL = line[:i-1] + line[i:]
                    break
                if difference < -3:
                    newLineR = line[:i+1] + line[i+2:]
                    newLineM = line[:i] + line[i+1:]
                    newLineL = line[:i-1] + line[i:]
                    break
                else:
                    wasDecreasing = True # No problem

        # Now, check conditions with new list

        newDifferencesR = np.array(newLineR[1:]) - np.array(newLineR[:-1])
        newDifferencesM = np.array(newLineM[1:]) - np.array(newLineM[:-1])
        newDifferencesL = np.array(newLineL[1:]) - np.array(newLineL[:-1])

        # Same test as before

        # All increasing but less than 3 gap?
        if np.all(newDifferencesR > 0) and np.all(newDifferencesR <= 3): 
            passed = True
        # All decreasing but less than 3 gap?
        elif np.all(newDifferencesR < 0) and np.all(newDifferencesR >= -3):
            passed = True
        elif np.all(newDifferencesL > 0) and np.all(newDifferencesL <= 3): 
            passed = True
        # All decreasing but less than 3 gap?
        elif np.all(newDifferencesL < 0) and np.all(newDifferencesL >= -3):
            passed = True
        elif np.all(newDifferencesM > 0) and np.all(newDifferencesM <= 3): 
            passed = True
        # All decreasing but less than 3 gap?
        elif np.all(newDifferencesM < 0) and np.all(newDifferencesM >= -3):
            passed = True
        else:
            print(f'\n{newLineL} didn\'t fix {line} {differences}')
            print(f'{newLineR} didn\'t fix {line} {differences}')
            print(f'{newLineM} didn\'t fix {line} {differences}')
            True == True 

    if passed:
        nPasses += 1
        #safeReports.write(f'{line}\n')

print(f'Part B: {nPasses}')
#safeReports.close()

# Guess 1: 518 too low
# Guess 2: 525 too low
# Guess 3: 525 too low

