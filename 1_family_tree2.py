from collections import defaultdict
class Solution:

   def __init__(self, head_name):
      self.family = defaultdict(list)
      self.head = head_name
      self.dead = set()

   def birth(self, p_name, c_name):
      self.family[p_name].append(c_name)

   def death(self, name):
      self.dead.add(name)

   def inheritance(self):
      self.ans = []
      self.depth_search(self.head)
      return self.ans

   def depth_search(self, current):
      if current not in self.dead:
         self.ans.append(current)
      for child in self.family[current]:
         self.depth_search(child)

print("Enter head name")
headname = input()
ob = Solution(headname)
print("Enter\n1)Birth\n2)Death\n3)Inheritance(Family members)\n4)Exit\n")
t = int(input())
while(t>=1 and t<4):
    if t==1:
        print("Enter headname and child")
        headname = input()
        child = input()
        ob.birth(headname,child)
    elif t==2:
        print("Enter name")
        name = input()
        ob.death(name)
    else:
        print(ob.inheritance())
    print("Enter t")
    t = int(input())
