def isValid(s):
    while s != "":
        if "[]" in s:
            s = s.replace("[]", "")
        elif "{}" in s:
            s = s.replace("{}", "")
        elif "()" in s:
            s = s.replace("()", "")
        else:
            print('1')
            return False
    print('2')
    return True
isValid("[[]][][]")
isValid("[([]])")
isValid("()")
isValid("{[]}")
isValid("{}[]()")
isValid("{}]()")
isValid("(){}}{")
isValid("()[{}]")
isValid("(]")
isValid("([)]")
isValid("(([]){})")
