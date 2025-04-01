from typing import List

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:

        # Idea: process each question from the back
        # The value of each question is maximum of
        # 1) the value of the next question (if skip), or
        # 2) the value of this question + the value of the question after skipping the next few questions

        # Loop through questions from the back
        question_values = [questions[-1][0]] # initiate with last question value

        # Go through questions
        for index, question in enumerate(questions[::-1][1:]):
            curr_points = question[0]
            brainpower = question[1]

            # Skip
            skip_value = question_values[-1]

            # Do this question, value = this question + question_values[-brainpower - 1] 
            # only add next question  if not out of bounds
            do_value = curr_points

            if len(question_values) > brainpower:
                do_value += question_values[-brainpower - 1]

            # Add maximum of skip and do values to question_values list
            question_values.append((max(skip_value, do_value)))

        # Return maximum of all question values
        return max(question_values)


print(Solution().mostPoints(questions = [[3,2],[4,3],[4,4],[2,5]]))
print(Solution().mostPoints(questions = [[1,1],[2,2],[3,3],[4,4],[5,5]]))
print(Solution().mostPoints(questions = [[20,4],[78,2],[74,1],[48,1],[38,1],[80,3]]))