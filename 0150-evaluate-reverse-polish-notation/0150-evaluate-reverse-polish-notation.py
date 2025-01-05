class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        n = []

        for i in tokens:
            if i == "+":
                n1 = n.pop()
                n2 = n.pop()
                n.append(n1 + n2)
            elif i == "-":
                n1 = n.pop()
                n2 = n.pop()
                n.append(n2 - n1)
            elif i == "*":
                n1 = n.pop()
                n2 = n.pop()
                n.append(n1 *n2)
            elif i == "/":
                n1 = n.pop()
                n2 = n.pop()
                n.append(int(n2/n1))
            else:
                n.append(int(i))
        return n[-1]
        

            
        