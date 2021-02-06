def maxScore(self, cardPoints, k):
     n = len(cardPoints)
     sz = n - k


     min_sum = cur_sum = sum(cardPoints[:sz])

     for i in range(sz,n):
         cur_sum = cur_sum + cardPoints[i] - cardPoints[i - sz]
         min_sum = min(min_sum,cur_sum)

     total_sum = sum(cardPoints[:n])
     return  total_sum - min_sum