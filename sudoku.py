lookup = [[0, 1, 2, 3, 4, 5, 6, 7, 8], [9, 10, 11, 12, 13, 14, 15, 16, 17], [18, 19, 20, 21, 22, 23, 24, 25, 26], [27, 28, 29, 30, 31, 32, 33, 34, 35], [36, 37, 38, 39, 40, 41, 42, 43, 44], [45, 46, 47, 48, 49, 50, 51, 52, 53], [54, 55, 56, 57, 58, 59, 60, 61, 62], [63, 64, 65, 66, 67, 68, 69, 70, 71], [72, 73, 74, 75, 76, 77, 78, 79, 80], [0, 9, 18, 27, 36, 45, 54, 63, 72], [1, 10, 19, 28, 37, 46, 55, 64, 73], [2, 11, 20, 29, 38, 47, 56, 65, 74], [3, 12, 21, 30, 39, 48, 57, 66, 75], [4, 13, 22, 31, 40, 49, 58, 67, 76], [5, 14, 23, 32, 41, 50, 59, 68, 77], [6, 15, 24, 33, 42, 51, 60, 69, 78], [7, 16, 25, 34, 43, 52, 61, 70, 79], [8, 17, 26, 35, 44, 53, 62, 71, 80], [0, 1, 2, 9, 10, 11, 18, 19, 20], [3, 4, 5, 12, 13, 14, 21, 22, 23], [6, 7, 8, 15, 16, 17, 24, 25, 26], [45,46,47,27,28,29,36,37,38],[48,49,50,39,40,41,30,31,32],[51,52,53,42,43,44,33,34,35],[54,55,56,63,64,65,72,73,74],[57,58,59,66,67,68,75,76,77],[60,61,62,69,70,71,78,79,80]]
listdict = [{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}]
helphelpdict = {}
for x in range(0,9):
    for y in range(1,10):
      listdict[x][y] = set()
      listdict[x+9][y] = set()
      listdict[x+18][y] = set()
lookup = [[0, 1, 2, 3, 4, 5, 6, 7, 8], [9, 10, 11, 12, 13, 14, 15, 16, 17], [18, 19, 20, 21, 22, 23, 24, 25, 26], [27, 28, 29, 30, 31, 32, 33, 34, 35], [36, 37, 38, 39, 40, 41, 42, 43, 44], [45, 46, 47, 48, 49, 50, 51, 52, 53], [54, 55, 56, 57, 58, 59, 60, 61, 62], [63, 64, 65, 66, 67, 68, 69, 70, 71], [72, 73, 74, 75, 76, 77, 78, 79, 80], [0, 9, 18, 27, 36, 45, 54, 63, 72], [1, 10, 19, 28, 37, 46, 55, 64, 73], [2, 11, 20, 29, 38, 47, 56, 65, 74], [3, 12, 21, 30, 39, 48, 57, 66, 75], [4, 13, 22, 31, 40, 49, 58, 67, 76], [5, 14, 23, 32, 41, 50, 59, 68, 77], [6, 15, 24, 33, 42, 51, 60, 69, 78], [7, 16, 25, 34, 43, 52, 61, 70, 79], [8, 17, 26, 35, 44, 53, 62, 71, 80], [0, 1, 2, 9, 10, 11, 18, 19, 20], [3, 4, 5, 12, 13, 14, 21, 22, 23], [6, 7, 8, 15, 16, 17, 24, 25, 26], [27, 28, 29, 36, 37, 38, 45, 46, 47], [30, 31, 32, 39, 40, 41, 48, 49, 50], [33, 34, 35, 42, 43, 44, 51, 52, 53], [54, 55, 56, 63, 64, 65, 72, 73, 74], [57, 58, 59, 66, 67, 68, 75, 76, 77], [60, 61, 62, 69, 70, 71, 78, 79, 80]]
for x in range(0,9):
  for y in range(1,10):
      for z in range(0,9):
        listdict[x][y].add(lookup[x][z])
for x in range(0,9):
  for y in range(1,10):
      for z in range(0,9):
        listdict[x+9][y].add(lookup[x+9][z])
for x in range(0,9):
  for y in range(1,10):
      for z in range(0,9):
        listdict[x+18][y].add(lookup[x+18][z])
helpdict = {}
helpdict2 = {}
helpdict3 = {}
for x in range(0,81):
  helpdict[x] = []
  helpdict2[x] = set()
  helpdict2[x].add(1)
  helpdict2[x].add(2)
  helpdict2[x].add(3)
  helpdict2[x].add(4)
  helpdict2[x].add(5)
  helpdict2[x].add(6)
  helpdict2[x].add(7)
  helpdict2[x].add(8)
  helpdict2[x].add(9)
  for y in range(0,len(lookup)):
      bool = 0
      for z in range(0,len(lookup[y])):
          if lookup[y][z] == x:
              helpdict[x].append(y)
for x in range(0, 81):
      helpdict3[x] = set()
      for item in helpdict[x]:
          for thing in lookup[item]:
              helpdict3[x].add(thing)
def isvalid(puzzle,pos):
    for x in helpdict3[pos]:
        if x != pos:
            if puzzle[pos] == puzzle[x]:
                return 1
    return 0
def pleasecopy(thing):
    thing2 = {}
    for key in thing:
        thing2[key] = set()
        for item in thing[key]:
            thing2[key].add(item)
    return thing2
def keepgoing(puzzle,helpdict,startpos,figure):
    list = []
    for thing in helpdict3[startpos]:
        if puzzle[thing] == 0:
            if helpdict[thing] == set():
                puzzle = []
                return []
            if puzzle[startpos] in helpdict[thing]:
                helpdict[thing].remove(int(puzzle[startpos]))
                if len(helpdict[thing]) == 1:
                    list.append(thing)
    for item in list:
      for instance in helpdict[item]:
        if item == 47 and instance == 8:
            r = "asfd"
        if figure == 1:
          puzzle2 = copy(puzzle)
          puzzle2[item] = instance
          if isvalid(puzzle2,item) == 0:
            puzzle[item] = instance
            keepgoing(puzzle, helpdict, item,1)
        else:
            puzzle[item] = instance
            keepgoing(puzzle, helpdict, item,0)
      else:
          puzzle = []
          return []
def printing(stringer):
    for f in range(0, 9):
      hopestring = ""
      for z in range(0, 9):
        hopestring += str(stringer[f * 9 + z])
      print(hopestring)
    print("")
def checkifallowed(puzzle,counter):
    bool = 0
    if counter == 0:
        return 0
    for x in helpdict[counter-1]:
        s = set()
        c = 0
        for y in range(0, len(lookup[x])):
            if puzzle[lookup[x][y]] != 0:
                c += 1
                s.add(puzzle[lookup[x][y]])
        if len(s) != c:
            bool = 1
            break
    if bool == 1:
        return 1
    else:
        return 0
def copy(puzzle):
    newpuzzle = []
    for y in range(0, len(puzzle)):
        newpuzzle.append(puzzle[y])
    return newpuzzle
def findminnew(listdict):
    min = (100,{1,2,3,4,5,6,7,8,9,10})
    for a in listdict:
        for r in a:
            if 0<len(a[r])<len(min[1]):
                min = (r,a[r])
    return min
def findmin(puzzle,dict,minindex):
    minnum = 10
    count = -1
    for r in range(0, len(puzzle)):
        if r != minindex:
          if puzzle[r] == 0:
            l = len(dict[r])
            if l <= minnum:
                count = r
                if count == 0:
                    adf = "asdf"
                minnum = len(dict[r])
    return count
def doit(puzzle,minindex,helpdictrec2):
    if puzzle == []:
        return []
    else:
        #boo = 0
        #if puzzle[minindex]  != 0:
                #boo = 1
        #if boo == 1:
            #return puzzle
            if minindex<0:
                return puzzle
            for x in helpdictrec2[minindex]:
                adf = minindex
                newpuzzle = puzzle[:]
                helpdictrec22 = {i:{j for j in helpdictrec2[i]}for i in helpdictrec2}
                newpuzzle[minindex] = x
                count = findmin(newpuzzle,helpdictrec22,minindex)
                #count2 = findminnew(listdictrec)
                if count == -1:
                    return newpuzzle
                y = minindex
                #helpdictrec22 = {i:{j for j in range(1,10) if j not in helpdict3[i]}for i in range(81)}
                if newpuzzle[count] == 0:
                        if newpuzzle[y] != 0:
                            for thing in helpdict3[y]:
                                if newpuzzle[thing] == 0:
                                  if newpuzzle[y] in helpdictrec22[thing]:
                                    helpdictrec22[thing].remove(int(newpuzzle[y]))
                                    if len(helpdictrec22[thing]) == 1:
                                      for instance in helpdictrec22[thing]:
                                        newpuzzle[thing] = instance
                                      keepgoing(newpuzzle,helpdictrec22,thing,1)


                #listdictrec2 = [{i: {j for j in listdictrec[r][i]} for i in a} for r, a in enumerate(listdictrec)]
                if count == -1:
                    f = 9
                answer = doit(newpuzzle,count,helpdictrec22)
                if answer != []:
                      return answer
            return []
def solve(list1):
    lookup = [[0, 1, 2, 3, 4, 5, 6, 7, 8], [9, 10, 11, 12, 13, 14, 15, 16, 17], [18, 19, 20, 21, 22, 23, 24, 25, 26],
              [27, 28, 29, 30, 31, 32, 33, 34, 35], [36, 37, 38, 39, 40, 41, 42, 43, 44],
              [45, 46, 47, 48, 49, 50, 51, 52, 53], [54, 55, 56, 57, 58, 59, 60, 61, 62],
              [63, 64, 65, 66, 67, 68, 69, 70, 71], [72, 73, 74, 75, 76, 77, 78, 79, 80],
              [0, 9, 18, 27, 36, 45, 54, 63, 72], [1, 10, 19, 28, 37, 46, 55, 64, 73],
              [2, 11, 20, 29, 38, 47, 56, 65, 74], [3, 12, 21, 30, 39, 48, 57, 66, 75],
              [4, 13, 22, 31, 40, 49, 58, 67, 76], [5, 14, 23, 32, 41, 50, 59, 68, 77],
              [6, 15, 24, 33, 42, 51, 60, 69, 78], [7, 16, 25, 34, 43, 52, 61, 70, 79],
              [8, 17, 26, 35, 44, 53, 62, 71, 80], [0, 1, 2, 9, 10, 11, 18, 19, 20], [3, 4, 5, 12, 13, 14, 21, 22, 23],
              [6, 7, 8, 15, 16, 17, 24, 25, 26], [45, 46, 47, 27, 28, 29, 36, 37, 38],
              [48, 49, 50, 39, 40, 41, 30, 31, 32], [51, 52, 53, 42, 43, 44, 33, 34, 35],
              [54, 55, 56, 63, 64, 65, 72, 73, 74], [57, 58, 59, 66, 67, 68, 75, 76, 77],
              [60, 61, 62, 69, 70, 71, 78, 79, 80]]
    numberwrong = 0
    for x in range(0, len(list1)):
        listdicthelp = [{i: {j for j in listdict[r][i]} for i in a} for r, a in enumerate(listdict)]
        helpdict23 = {0: {1, 2, 3, 4, 5, 6, 7, 8, 9}, 1: {1, 2, 3, 4, 5, 6, 7, 8, 9}, 2: {1, 2, 3, 4, 5, 6, 7, 8, 9},
                      3: {1, 2, 3, 4, 5, 6, 7, 8, 9}, 4: {1, 2, 3, 4, 5, 6, 7, 8, 9}, 5: {1, 2, 3, 4, 5, 6, 7, 8, 9},
                      6: {1, 2, 3, 4, 5, 6, 7, 8, 9}, 7: {1, 2, 3, 4, 5, 6, 7, 8, 9}, 8: {1, 2, 3, 4, 5, 6, 7, 8, 9},
                      9: {1, 2, 3, 4, 5, 6, 7, 8, 9}, 10: {1, 2, 3, 4, 5, 6, 7, 8, 9}, 11: {1, 2, 3, 4, 5, 6, 7, 8, 9},
                      12: {1, 2, 3, 4, 5, 6, 7, 8, 9}, 13: {1, 2, 3, 4, 5, 6, 7, 8, 9}, 14: {1, 2, 3, 4, 5, 6, 7, 8, 9},
                      15: {1, 2, 3, 4, 5, 6, 7, 8, 9}, 16: {1, 2, 3, 4, 5, 6, 7, 8, 9}, 17: {1, 2, 3, 4, 5, 6, 7, 8, 9},
                      18: {1, 2, 3, 4, 5, 6, 7, 8, 9}, 19: {1, 2, 3, 4, 5, 6, 7, 8, 9}, 20: {1, 2, 3, 4, 5, 6, 7, 8, 9},
                      21: {1, 2, 3, 4, 5, 6, 7, 8, 9}, 22: {1, 2, 3, 4, 5, 6, 7, 8, 9}, 23: {1, 2, 3, 4, 5, 6, 7, 8, 9},
                      24: {1, 2, 3, 4, 5, 6, 7, 8, 9}, 25: {1, 2, 3, 4, 5, 6, 7, 8, 9}, 26: {1, 2, 3, 4, 5, 6, 7, 8, 9},
                      27: {1, 2, 3, 4, 5, 6, 7, 8, 9}, 28: {1, 2, 3, 4, 5, 6, 7, 8, 9}, 29: {1, 2, 3, 4, 5, 6, 7, 8, 9},
                      30: {1, 2, 3, 4, 5, 6, 7, 8, 9}, 31: {1, 2, 3, 4, 5, 6, 7, 8, 9}, 32: {1, 2, 3, 4, 5, 6, 7, 8, 9},
                      33: {1, 2, 3, 4, 5, 6, 7, 8, 9}, 34: {1, 2, 3, 4, 5, 6, 7, 8, 9}, 35: {1, 2, 3, 4, 5, 6, 7, 8, 9},
                      36: {1, 2, 3, 4, 5, 6, 7, 8, 9}, 37: {1, 2, 3, 4, 5, 6, 7, 8, 9}, 38: {1, 2, 3, 4, 5, 6, 7, 8, 9},
                      39: {1, 2, 3, 4, 5, 6, 7, 8, 9}, 40: {1, 2, 3, 4, 5, 6, 7, 8, 9}, 41: {1, 2, 3, 4, 5, 6, 7, 8, 9},
                      42: {1, 2, 3, 4, 5, 6, 7, 8, 9}, 43: {1, 2, 3, 4, 5, 6, 7, 8, 9}, 44: {1, 2, 3, 4, 5, 6, 7, 8, 9},
                      45: {1, 2, 3, 4, 5, 6, 7, 8, 9}, 46: {1, 2, 3, 4, 5, 6, 7, 8, 9}, 47: {1, 2, 3, 4, 5, 6, 7, 8, 9},
                      48: {1, 2, 3, 4, 5, 6, 7, 8, 9}, 49: {1, 2, 3, 4, 5, 6, 7, 8, 9}, 50: {1, 2, 3, 4, 5, 6, 7, 8, 9},
                      51: {1, 2, 3, 4, 5, 6, 7, 8, 9}, 52: {1, 2, 3, 4, 5, 6, 7, 8, 9}, 53: {1, 2, 3, 4, 5, 6, 7, 8, 9},
                      54: {1, 2, 3, 4, 5, 6, 7, 8, 9}, 55: {1, 2, 3, 4, 5, 6, 7, 8, 9}, 56: {1, 2, 3, 4, 5, 6, 7, 8, 9},
                      57: {1, 2, 3, 4, 5, 6, 7, 8, 9}, 58: {1, 2, 3, 4, 5, 6, 7, 8, 9}, 59: {1, 2, 3, 4, 5, 6, 7, 8, 9},
                      60: {1, 2, 3, 4, 5, 6, 7, 8, 9}, 61: {1, 2, 3, 4, 5, 6, 7, 8, 9}, 62: {1, 2, 3, 4, 5, 6, 7, 8, 9},
                      63: {1, 2, 3, 4, 5, 6, 7, 8, 9}, 64: {1, 2, 3, 4, 5, 6, 7, 8, 9}, 65: {1, 2, 3, 4, 5, 6, 7, 8, 9},
                      66: {1, 2, 3, 4, 5, 6, 7, 8, 9}, 67: {1, 2, 3, 4, 5, 6, 7, 8, 9}, 68: {1, 2, 3, 4, 5, 6, 7, 8, 9},
                      69: {1, 2, 3, 4, 5, 6, 7, 8, 9}, 70: {1, 2, 3, 4, 5, 6, 7, 8, 9}, 71: {1, 2, 3, 4, 5, 6, 7, 8, 9},
                      72: {1, 2, 3, 4, 5, 6, 7, 8, 9}, 73: {1, 2, 3, 4, 5, 6, 7, 8, 9}, 74: {1, 2, 3, 4, 5, 6, 7, 8, 9},
                      75: {1, 2, 3, 4, 5, 6, 7, 8, 9}, 76: {1, 2, 3, 4, 5, 6, 7, 8, 9}, 77: {1, 2, 3, 4, 5, 6, 7, 8, 9},
                      78: {1, 2, 3, 4, 5, 6, 7, 8, 9}, 79: {1, 2, 3, 4, 5, 6, 7, 8, 9}, 80: {1, 2, 3, 4, 5, 6, 7, 8, 9}}
        t2 = time.time()
        r = list1[x][:len(list1[x]) - 1:]
        # r = list(list1[0])
        startpuz = []
        for y in range(0, len(r)):
            if r[y] == '.':
                startpuz.append(0)
            else:
                startpuz.append(int(r[y]))
        if x == 14:
            aadsf = "asldf"
        # printing(startpuz)
        for y in range(0, len(startpuz)):
            if startpuz[y] != 0:
                for thing in helpdict3[y]:
                    if startpuz[thing] == 0:
                        if startpuz[y] in helpdict23[thing]:
                            helpdict23[thing].remove(int(startpuz[y]))
                            if len(helpdict23[thing]) == 1:
                                for instance in helpdict23[thing]:
                                    startpuz[thing] = instance
                                keepgoing(startpuz, helpdict23, thing, 0)
                for thing in helpdict[y]:
                    listdicthelp[thing][startpuz[y]] = set()
                    for r2 in range(1, 10):
                        if y in listdicthelp[thing][r2]:
                            listdicthelp[thing][r2].remove(y)
                    for secondthing in lookup[thing]:
                        for thirdthing in helpdict[secondthing]:
                            if thirdthing != thing:
                                if secondthing in listdicthelp[thirdthing][startpuz[y]]:
                                    listdicthelp[thirdthing][startpuz[y]].remove(secondthing)
        for t in listdicthelp:
            for a in t:
                if len(t[a]) == 1:
                    me = t[a].pop()
                    if startpuz[me] == 0:
                        startpuz[me] = a
                        for timmy in helpdict3[me]:
                            if a in helpdict23[timmy]:
                                helpdict23[timmy].remove(a)
        isitsolved = 0
        var = 0
        while startpuz[var] != 0:
            var += 1
            if var == len(startpuz):
                isitsolved = 1
                break
        if isitsolved == 0:
            counter = findmin(startpuz, helpdict23, var)
            if counter == -1:
                f = 5
            final = doit(startpuz, counter, helpdict23)
        else:
            final = startpuz
        t3 = time.time()
        print("puzzle" + str(x + 1) + ": " + str(t3 - t2) + " seconds")
        printing(final)
        overallsum = sum(final)
        if overallsum != 405:
            print(overallsum)
            numberwrong += 1
        # printing(final)
file = open("puzzles.txt", "r")
list1 = file.readlines()
# list1 = ['..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..']
import time
t0 = time.time()
solve(list1)
t1 = time.time()
print(str(t1-t0) + " seconds overall")