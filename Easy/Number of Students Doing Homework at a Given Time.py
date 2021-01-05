class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        combined = []
        count = 0
        for i in range(len(startTime)):
            combined.append([startTime[i],endTime[i]])
        
        for times in combined:
            if times[0] <= queryTime <= times[1]:
                count += 1
        return count
