class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students = collections.deque(students)
        sandwiches = collections.deque(sandwiches)
        count = 0

        while len(students) > count:
            if students[0] == sandwiches[0]:
                sandwiches.popleft()
                count = 0
            else:
                students.append(students[0])
                count += 1
            students.popleft()
        return len(students)