# @lc app=leetcode id=1472 lang=python3
#
# [1472] Design Browser History
#


# @lc tags=Unknown

# @lc imports=start
from imports import *
# @lc imports=end

# @lc idea=start
# 
# 
# 
# @lc idea=end

# @lc group=

# @lc rank=

# @lc code=start


class Doublelinkedlist:
    def __init__(self, url='', prev=None, next=None):
        self.url = url
        self.prev = prev
        self.next = next


class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = Doublelinkedlist(homepage)

    def visit(self, url: str) -> None:
        node = Doublelinkedlist(url)
        curr = self.head
        curr.next = node
        node.prev = curr
        node.next = None
        self.head = node

    def back(self, steps: int) -> str:
        while steps > 0 and self.head.prev:
            self.head = self.head.prev
            steps -= 1
        return self.head.url

    def forward(self, steps: int) -> str:
        while steps > 0 and self.head.next:
            self.head = self.head.next
            steps -= 1
        return self.head.url


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    pass
# @lc main=end
