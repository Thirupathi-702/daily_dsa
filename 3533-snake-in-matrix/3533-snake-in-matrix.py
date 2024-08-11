class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        c=0
        r=0
        for i in range(len(commands)):
            if commands[i]=='DOWN':
                c+=1
            elif commands[i]=='UP':
                c-=1
            elif commands[i]=='RIGHT':
                r+=1
            else:
                r-=1
        return (c*n)+r