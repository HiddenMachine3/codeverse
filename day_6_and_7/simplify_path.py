class Solution:
    def simplifyPath(self, path: str) -> str:
        if len(path) == 1:
            return path
        path_stack = []
        for name in path.split("/"):
            if len(name) > 0:
                if name==".":
                    continue
                elif name=="..":
                    if path_stack:
                        path_stack.pop()

                else:
                    path_stack.append(name)  
        return ("/"+"/".join(path_stack)) if path_stack else "/"