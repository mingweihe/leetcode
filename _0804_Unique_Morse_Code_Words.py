class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        # Approach 2
        dic = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
               ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        return len({''.join(dic[ord(i) - ord('a')] for i in w) for w in words})
        # Approach 1
        # dic = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.",
        #        "--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        # dic = {chr(i+97):x for i,x in enumerate(dic)}
        # return len(set([''.join(map(dic.get, x)) for x in words]))
