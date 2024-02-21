from collections import defaultdict
import sys
input=sys.stdin.readline
n,q=map(int,input().split())
words=input().split()
ans=defaultdict(lambda :-1)
for index in range(len(words)):
    for i in range(len(words[index])):
        for j in range(len(words[index])-1,-1,-1):
            ans[(words[index][:i+1],words[index][j:])]=index
for _ in range(q):
    pref,suff=input().split()
    print(ans[(pref,suff)])

