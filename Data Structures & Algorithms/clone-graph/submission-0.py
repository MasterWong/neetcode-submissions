class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node == None:
            return None
        ans = {}
        visited = set()
        def dfs(currNode, visited, ans):
            if currNode.val in visited:
                return
            visited.add(currNode.val)
            ans[currNode.val] = Node(currNode.val)
            for i in currNode.neighbors:
                dfs(i, visited, ans)

        dfs(node, visited, ans)
        
        # Second pass to connect the cloned neighbors
        def dfs_connect(currNode, visited_connect):
            if currNode.val in visited_connect:
                return
            visited_connect.add(currNode.val)
            for neighbor in currNode.neighbors:
                ans[currNode.val].neighbors.append(ans[neighbor.val])
                dfs_connect(neighbor, visited_connect)
        
        dfs_connect(node, set())

        return ans[node.val]