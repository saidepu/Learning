#!/usr/bin/python3

def max_nested_braces(expr):
    max_count = count = 0
    for char in expr:
        if char == '{':
            count += 1
            if count > max_count:
                max_count = count
        elif char == '}':
            if count == 0:
                return -1
            count -= 1

    if count != 0:
        return -1
    return max_count

assert max_nested_braces('a*b') == 0
assert max_nested_braces('a*b{') == -1
assert max_nested_braces('a*{b+c}') == 1
assert max_nested_braces('{a+2}*{b+c}') == 1
assert max_nested_braces('a*{b+c*{e*3.14}}') == 2
assert max_nested_braces('a*{b+c*{e*3.14}}}') == -1
assert max_nested_braces('a*{b+c}}') == -1
assert max_nested_braces('a*b+{}') == 1
assert max_nested_braces('}a+b{') == -1
assert max_nested_braces('{{a+2}*{b+c}+e}') == 2
assert max_nested_braces('{{a+2}*{b+{c*d}}+e}') == 3
assert max_nested_braces('{{a+2}*{{b+{c*d}}+e*d}}') == 4
assert max_nested_braces('{{a+2}*{{b}+{c*d}}+e*d}}') == -1

print('all tests passed')


#### alternate using regular expressions

#import re
#
#def max_nested_braces(expr):
#    count = 0
#    while True:
#        expr, no_of_subs = re.subn(r'\{[^{}]*\}', '', expr)
#        if no_of_subs == 0:
#            break
#        count += 1
#
#    if re.search(r'[{}]', expr):
#        return -1
#    return count

# for bonus, use + instead of *
#assert max_nested_braces('a*b+{}') == -1
#assert max_nested_braces('a*{b+{}+c*{e*3.14}}') == -1
