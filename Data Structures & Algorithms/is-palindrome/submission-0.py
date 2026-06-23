class Solution:
    def isPalindrome(self, s: str) -> bool:
        st=''.join(ch for ch in s if ch.isalnum())
        st=st.lower()
        print(st)
        if st==st[::-1]:
            return True 
        else:
            return False
        