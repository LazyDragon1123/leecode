import numpy as np


def filtering(email):
    at = email.find('@')
    local = email[:at]
    domain = email[at:]
    local = local.replace('.','')
    if '+' in local:
        local = local[:local.find('+')]
    return local + domain

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        dic = {}
        for email in emails:
            print(filtering(email))
            if dic.get(filtering(email)) is None:
                dic[filtering(email)] = 1
            else:
                continue
        return len(list(dic.keys()))
