import heapq
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap=[]
        for i,node in enumerate(lists):
            if node:
                heapq.heappush(heap,(node.val,i,node))
        dummy=ListNode(-1)
        temp=dummy
        while heap:
          value,index,node=heapq.heappop(heap)
          temp.next=node
          if node.next: 
            heapq.heappush(heap,(node.next.val,index,node.next))
          temp=temp.next
        return dummy.next
