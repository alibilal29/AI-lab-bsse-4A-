from collections import deque
graph={"A":["B","C"],"B":["D","E"],"C":["F"],"D":[],"E":["G"],"F":[],"G":[]}
def bfs(start, goal):
    q=deque([(start,[start])]); seen={start}
    while q:
        node,path=q.popleft()
        if node==goal: return path
        for n in graph[node]:
            if n not in seen:
                seen.add(n); q.append((n,path+[n]))
def dfs(start, goal):
    stack=[(start,[start])]; seen=set()
    while stack:
        node,path=stack.pop()
        if node==goal: return path
        if node in seen: continue
        seen.add(node)
        for n in reversed(graph[node]):
            stack.append((n,path+[n]))
def dls(node,goal,limit,path):
    if node==goal: return "FOUND",path
    if limit==0: return "CUTOFF",None
    cutoff=False
    for n in graph[node]:
        if n not in path:
            status,result=dls(n,goal,limit-1,path+[n])
            if status=="FOUND": return status,result
            if status=="CUTOFF": cutoff=True
    return ("CUTOFF" if cutoff else "FAILURE"),None
def iddfs(start,goal,max_depth):
    for limit in range(1,max_depth+1):
        status,path=dls(start,goal,limit,[start])
        if status=="FOUND": return status,path,list(range(1,limit+1))
    return status,None,list(range(1,max_depth+1))
print("BFS:",bfs("A","G"))
print("DFS:",dfs("A","G"))
for limit in range(1,5):
    print("DLS Limit:",limit,dls("A","G",limit,["A"]))
for depth in range(1,5):
    print("IDDFS Max Depth:",depth,iddfs("A","G",depth))
