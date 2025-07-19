from typing import List

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:

        # 1. Sort
        folder.sort()

        # 2. For each folder that is not a subfolder of the previous, add it to result array
        res = []

        # Add first folder to result, append /
        res.append(folder[0])

        for i in range(1, len(folder)):
            
            # Get curr folder
            curr_folder = folder[i] + "/"

            # Get previous folder
            prev_folder = res[-1] + "/"

            # Check if current folder is a subfolder of last folder added
            if prev_folder != curr_folder[:len(prev_folder)]:

                # If this folder is not subfolder of last folder, then add to res
                res.append(curr_folder[:-1])
                
        return res


print(Solution().removeSubfolders(folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]))
print(Solution().removeSubfolders(folder = ["/a","/a/b/c","/a/b/d"]))
print(Solution().removeSubfolders(folder = ["/a/b/c","/a/b/ca","/a/b/d"]))