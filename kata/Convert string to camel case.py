def to_camel_case(text):
    if len(text) == 0:
        return ''
    if '-' in text:
        return text.replace('-', '')
    for a in text:
        if a.isupper():
            return 'a'


print(to_camel_case("the_stealth_warrior"))