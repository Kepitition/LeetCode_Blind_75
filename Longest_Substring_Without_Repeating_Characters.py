class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Initialize a dictionary to store the last index of each character
        char_index = {}
        # Initialize pointers for the start and end of the substring
        start = 0
        max_length = 0

        for end in range(len(s)):
            # If the character is already in the substring, update the start pointer
            if s[end] in char_index and char_index[s[end]] >= start:
                start = char_index[s[end]] + 1

            # Update the index of the current character in the dictionary
            char_index[s[end]] = end

            # Update the maximum length of the substring
            max_length = max(max_length, end - start + 1)

        return max_length