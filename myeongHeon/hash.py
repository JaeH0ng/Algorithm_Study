def h (string:str):
  lenght=len(string)
  hashedIdx=lenght//2-1
  #이러면 0~5
  return hashedIdx
#그냥 해시인데 거기엔 배열 저장 + 거기에 a~z 알파뱃 해시+ 거기서 중복시엔 걍 리스트

def alphaHash(string:str):
  center=string[len(string)//2]
  idx=ord(center)-97
  #a가 0부터 시작함
  return idx


hashedList=[[[] for j in range(26)] for i in range(6)] 
n=int(input())

for _ in range(n):
  string=input()
  if(string==string[::-1]):
    print(len(string),string[len(string)//2])
  hashedIdx= h(string)
  alphaIdx=alphaHash(string)
  targetList=hashedList[hashedIdx][alphaIdx]
  targetList.append(string)
  if(len(targetList)>1):
    reversedString=string[::-1]
    if(reversedString in targetList):
      anserNum=len(reversedString)
      answerStr=reversedString[anserNum//2]
      print(anserNum,answerStr)



