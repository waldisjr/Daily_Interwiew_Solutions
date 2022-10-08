class Solution:
    def reverse_words(self, target: str) -> str:
        return ' '.join([word[::-1] for word in target.split(' ')])


print(Solution().reverse_words("The cat in the hat"))
