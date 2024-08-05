class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        countTF = {}

        left = 0

        max_length = 0

        for right in range(len(answerKey)):

            if(answerKey[right] not in countTF):
                countTF[answerKey[right]] = 1

            else:
                countTF[answerKey[right]] += 1

            max_count = 0
            for char, value in countTF.items():
                max_count = max(max_count, value)

            if((right - left + 1) - max_count <= k):
                max_length = max(max_length, right - left + 1)

            else:
                countTF[answerKey[left]] -= 1
                left += 1


        return max_length