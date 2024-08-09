class BNode:
  def __init__(self,data):
    self.data=data
    self.left=None
    self.right=None
  def lLink(self,node):
    self.left=node
  def rLink(self,node):
    self.right=node


n=int(input())
tNodes=list()
for i in range(n):
  t=BNode(chr(65+i)) #A의 아스키코드가 65
  tNodes.append(t)
#미리 노드들 만듦. 그 값도 1:1 대응시켜 둠.

for i in range(n):
  nodes=input().split()
  rootIdx=ord(nodes[0])-65 #tNodes의 몇번인지 찾기
  if(nodes[1]!="."):
    leftIdx=ord(nodes[1])-65
    tNodes[rootIdx].left=tNodes[leftIdx]
  if(nodes[2]!="."):
    rightIdx=ord(nodes[2])-65
    tNodes[rootIdx].right=tNodes[rightIdx]


preList=list()
def preOrder(node):
  preList.append(node.data)
  if(node.left !=None):
    preOrder(node.left)
  if(node.right != None):
    preOrder(node.right)
preOrder(tNodes[0])
print(''.join(preList))

midList=list()
def midOrder(node):
  if(node.left != None):
    midOrder(node.left)
  midList.append(node.data)
  if(node.right != None):
    midOrder(node.right)
midOrder(tNodes[0])
print(''.join(midList))

posList=list()
def posOrder(node):
  if(node.left != None):
    posOrder(node.left)
  if(node.right != None):
    posOrder(node.right)
  posList.append(node.data)
posOrder(tNodes[0])
print(''.join(posList))

# 총 112ms
