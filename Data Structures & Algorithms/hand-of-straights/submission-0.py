class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        stack1 = []
        stack2 = []

        hand = sorted(hand)

        for i in hand:
            if not stack1: 
                stack1.append(i)

            else:
                if i == stack1[-1] + 1 and len(stack1) < groupSize:
                    stack1.append(i)
                else:
                    if not stack2: 
                        stack2.append(i)
                    elif i == stack2[-1] + 1 and len(stack2) < groupSize:
                        stack2.append(i)
                    else:
                        return False
        return True
