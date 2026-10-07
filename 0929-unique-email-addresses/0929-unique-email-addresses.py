class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        hashe = set()
        for i in emails: 
            local,domain = i.split('@')
            print(local)
            local = local.split("+")[0]
            local = local.replace(".",'')
            cleaned_email = local + "@" + domain
            hashe.add(cleaned_email)
        print(hashe)
        return len(hashe)
