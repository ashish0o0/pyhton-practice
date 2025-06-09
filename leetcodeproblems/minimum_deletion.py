def minDeletion(s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        freq = {}
        deleted_chars = 0

        for char in s:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
        
        items = []
        for key in freq:
            items.append([key, freq[key]])

        unique_count = len(freq)
        
        if unique_count <= k:
            return 0
        
        n = len(items)
        for i in range(n):
            for j in range(0, n - i - 1):
                if items[j][1] < items[j + 1][1]:
                    temp = items[j]
                    items[j] = items[j + 1]
                    items[j + 1] = temp

        deleted_chars = 0
        for i in range(k, len(items)):
            deleted_chars += items[i][1]

        return deleted_chars             

s = input("Type s: ")
k = int(input("Type k: "))
call = minDeletion(s, k)
print(call)
