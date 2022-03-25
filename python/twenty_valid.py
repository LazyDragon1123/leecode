
# class Solution:
#     def isValid(self,s:str) -> bool:
#         check_dic = {'curv':True,
#                      'wave':True,
#                      'sq': True}
#         for char in s:
#             if (char == ')'):
#                 if check_dic['curv'] == False:
#                     check_dic['curv'] = True
#                 else:
#                     return False
#             elif (char == '('):
#                 if check_dic['curv'] == True:
#                     check_dic['curv'] = False
#                 else:
#                     return False
#             elif (char == ']'):
#                 if check_dic['sq'] == False:
#                     check_dic['sq'] = True
#                 else:
#                     return False
#             elif (char == '['):
#                 if check_dic['sq'] == True:
#                     check_dic['sq'] = False
#                 else:
#                     return False
#             elif (char == '}'):
#                 if check_dic['wave'] == False:
#                     check_dic['wave'] = True
#                 else:
#                     return False
#             elif (char == '{'):
#                 if check_dic['wave'] == True:
#                     check_dic['wave'] = False
#                 else:
#                     return False
                
#         return True

def isClose(char):
    if char == ')':
        return True, '('
    elif char == ']':
        return True, '['
    elif char == '}':
        return True, '{'
    else:
        return False, char


class Solution:
    def isValid(self,s:str) -> bool:
        stack = []
        for char in s:
            isclose, pair = isClose(char)
            if isclose:
                if (len(stack) == 0) or (pair != stack[-1]):
                    return False
                else:
                    stack.pop()
            else:
                stack.append(char)
        if len(stack) == 0:
            return True
        else:
            return False
