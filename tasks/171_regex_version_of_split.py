import re
texxt = '   will it work k    '

def stripFunction(text, strip=' kor'):
    stripList = list(strip)
    textRegexStart = re.compile('^(%s*)'%stripList)
    textRegexEnd = re.compile('(%s*)$'%stripList)
    textStripStart = textRegexStart.sub('', text)
    textStripEnd = textRegexEnd.sub('', textStripStart)
    print(textStripEnd)
stripFunction(texxt)