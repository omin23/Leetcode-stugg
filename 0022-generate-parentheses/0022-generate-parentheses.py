class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = "("
        done = []
        numo = n-1
        numc = n
        def back(res,numo,numc):
            if numo < 0 or numc < 0 or numc < numo:
                return
            if numo == 0 and numc == 0:
                # print(res)
                done.append(res)
                return
            
            back(res + "(",numo-1,numc)
            back(res + ")",numo,numc-1)

        back(res,numo,numc)
        return done

    

