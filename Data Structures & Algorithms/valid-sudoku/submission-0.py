class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # A valid board has 3 constrains
        # 1. row 2. col 3. box
        # 1. iter row
        collist = [[] for _ in range(9)]
        boxlist = [[] for _ in range(9)]
        def utilFunc(iterateList: List[str]) -> bool:
            tempPlace = set()
            for i in iterateList:
                if i is ".":
                    continue
                if i in tempPlace:
                    return False
                tempPlace.add(i)
            return True
 
        for rowIdx, row in enumerate(board):
            if utilFunc(row) == False:
                return False
            for index, item in enumerate(row):
                #populate column list
                collist[index].append(board[rowIdx][index])
                #populate boxlist
                boxlist[rowIdx//3*3 + index//3].append(board[rowIdx][index])

        for item in collist:
            if utilFunc(item) == False:
                return False

        for item in boxlist:
            if utilFunc(item) == False:
                return False

        return True       
