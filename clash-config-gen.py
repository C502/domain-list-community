
with open("clash-template.yaml", 'r') as f:
    template = f.read()

head, tail = template.split('##INSERT##')

print(head)

DO_PROXY = '🔰国外流量'
RULE_PREFIX = '  - '


with open("out/dlc_geolocation-!cn.txt", 'r') as f:
    lines = f.readlines()

lines = [line.strip() for line in lines]
# remove comment
lines = [line.strip() for line in lines if len(line) > 0 and line[0] != '#']

'''
domain:google.com @attr1 @attr2
keyword:google
regexp:www\.google\.com$
full:www.google.com
'''
for line in lines:
    if line.startswith("domain:"):
        line = line.removeprefix("domain:")
        print(f'{RULE_PREFIX}DOMAIN-SUFFIX,{line},{DO_PROXY}')
    elif line.startswith("keyword:"):
        line = line.removeprefix("keyword:")
        print(f'{RULE_PREFIX}DOMAIN-KEYWORD,{line},{DO_PROXY}')
        raise RuntimeError(f"why there is keyword ?: {line}")
    elif line.startswith("regexp:"):
        line = line.removeprefix("regexp:")
        # sadly skip regexp
        pass
    elif line.startswith("full:"):
        line = line.removeprefix("full:")
        print(f'{RULE_PREFIX}DOMAIN,{line},{DO_PROXY}')
    else:
        raise RuntimeError(f"unknown rule: {line}")

print(tail)