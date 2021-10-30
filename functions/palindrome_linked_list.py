"""
problem statement: Given the head of a singly linked list, return true if it is a palindrome.
"""

def isPalindrome(head):
        """
        :type head: ListNode
        :rtype: bool
        """
        stack = []
        slow = fast = head 
        while fast and fast.next: # Find mid point 
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next
            
        if fast: 
            slow = slow.next # Skip midpoint if odd legnth 
        
        while slow:
            if slow.val != stack.pop(): # Compare right half to left half  
                return False
            slow = slow.next
        return True
      
      
      
      """
Analysis:

Time: O(n)
Space: O(n) for stack
      """
