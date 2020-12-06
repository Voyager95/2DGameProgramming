import time


class Key:
    def __init__(self, up, down):
        self.up = up
        self.down = down
        #self.left = left
        #self.right = right


dic_key = {}
dic_key['A'] = Key(('TAB', 'Q', 'W'), ('SHIFT', 'Z', 'X'))
dic_key['B'] = Key(('F', 'G', 'H'), ('SPACE'))
dic_key['C'] = Key(('S', 'D', 'F'), ('SPACE'))
dic_key['D'] = Key(('W', 'E', 'R'), ('X', 'C', 'V'))
dic_key['E'] = Key(('2', '3', '4'), ('S', 'D', 'F'))
dic_key['F'] = Key(('E', 'R', 'T'), ('C', 'V', 'B'))
dic_key['G'] = Key(('R', 'T', 'Y'), ('V', 'B', 'N'))
dic_key['H'] = Key(('T', 'Y', 'U'), ('V', 'B', 'N', 'M'))
dic_key['I'] = Key(('7', '8', '9'), ('j', 'k', 'l'))
dic_key['J'] = Key(('Y', 'U', 'I'), ('N', 'M', ','))
dic_key['K'] = Key(('U', 'I', 'O'), ('M', ',', '.'))
dic_key['L'] = Key(('I', 'O', 'P'), (',', '.', '/'))
dic_key['M'] = Key(('H', 'J', 'K', 'L'), ('SPACE'))
dic_key['N'] = Key(('G', 'H', 'J', 'K'), ('SPACE'))
dic_key['O'] = Key(('8', '9', '0', '-'), ('K', 'L', ';'))
dic_key['P'] = Key(('9', '0', '-', '='), ('L', ';'))
dic_key['Q'] = Key(('`', '1', '2'), ('A', 'S'))
dic_key['R'] = Key(('3', '4', '5'), ('D', 'F', 'G'))
dic_key['S'] = Key(('Q', 'W', 'E'), ('Z', 'X', 'C'))
dic_key['T'] = Key(('4', '5', '6'), ('F', 'G', 'H'))
dic_key['U'] = Key(('6', '7', '8', '9'), ('H', 'J', 'K'))
dic_key['V'] = Key(('D', 'F', 'G'), ('SPACE'))
dic_key['W'] = Key(('1', '2', '3', '4'), ('A', 'S', 'D'))
dic_key['X'] = Key(('A', 'S', 'D'), ('SPACE'))
dic_key['Y'] = Key(('5', '6', '7', '8'), ('G', 'H', 'J'))
dic_key['Z'] = Key(('A', 'S'), ('SPACE'))


class StrokeInputSystem:
    inputProcessingTime = 1

    def __init__(self, upInputCallback, downInputCallback):
        self.inputList = []
        self.upInputCallback = upInputCallback
        self.downInputCallback = downInputCallback

    def updateInput(self):
        toRemove = []
        for k in self.inputList:
            keyTime = k[1]
            if (time.time() - keyTime) > StrokeInputSystem.inputProcessingTime:
                toRemove.append(k)
        for k in toRemove:
            self.inputList.remove(k)

    def inputCheck(self):
        for k in self.inputList:
            if self.upInputCheck(k) == True:
                self.upInputCallback()
            if self.downInputCheck(k) == True:
                self.downInputCallback()

    def upInputCheck(self, firstInput):
        found = False
        firstKeycode = firstInput[0]
        if firstKeycode in dic_key:
            for secondKeycode in dic_key[firstKeycode].up:
                secondInput = self.checkKeyInput(firstInput, secondKeycode)
                if secondInput != None:
                    if secondKeycode in dic_key:
                        for thirdKeycode in dic_key[secondKeycode].up:
                            thirdInput = self.checkKeyInput(
                                secondInput, thirdKeycode)
                            if thirdInput != None:
                                found = True

        if found == True:
            self.inputList.clear()

        return found

    def downInputCheck(self, firstInput):
        found = False
        firstKeycode = firstInput[0]
        if firstKeycode in dic_key:
            for secondKeycode in dic_key[firstKeycode].down:
                secondInput = self.checkKeyInput(firstInput, secondKeycode)
                if secondInput != None:
                    if secondKeycode in dic_key:
                        for thirdKeycode in dic_key[secondKeycode].down:
                            thirdInput = self.checkKeyInput(
                                secondInput, thirdKeycode)
                            if thirdInput != None:
                                found = True

        if found == True:
            self.inputList.clear()

        return found

    def addInput(self, key, time):
        self.inputList.append((key, time))

    def checkKeyInput(self, beforeInput, keyCode):
        for inputKey in self.inputList:
            # 원하는 키가 입력되었는지, 직전 입력보다 이후에 입력되었는지 확인합니다.
            if self.inputList.index(beforeInput) < self.inputList.index(inputKey) and keyCode == inputKey[0]:
                return inputKey
        return None


class DownInputSystem:
    sameInputProcessingTime = 0.05

    def __init__(self, onOneDownInput, onTwoDownInput, onThreeDownInput, onFourDownInput):
        self.inputList = []
        self.onOneDownInputCallback = onOneDownInput
        self.onTwoDownInputCallback = onTwoDownInput
        self.onThreeDownInputCallback = onThreeDownInput
        self.onFourDownInputCallback = onFourDownInput

    def inputCheck(self):
        if len(self.inputList) == 0:
            return
        elif len(self.inputList) == 1:
            if time.time() - self.inputList[0][1] > DownInputSystem.sameInputProcessingTime:
                self.onOneDownInputCallback()
                self.inputList.clear()
                return
        else:
            if time.time() - self.inputList[0][1] < DownInputSystem.sameInputProcessingTime:
                return
            downAtSameTimeCount = 1
            for i in range(1, len(self.inputList)):
                if self.inputList[i][1] - self.inputList[0][1] < DownInputSystem.sameInputProcessingTime:
                    downAtSameTimeCount += 1
            if downAtSameTimeCount == 1:
                self.onOneDownInputCallback()
            elif downAtSameTimeCount == 2:
                self.onTwoDownInputCallback()
            elif downAtSameTimeCount == 3:
                self.onThreeDownInputCallback()
            elif downAtSameTimeCount >= 4:
                self.onFourDownInputCallback()
            self.inputList.clear()

    def addInput(self, key, time):
        self.inputList.append((key, time))
