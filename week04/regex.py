import re


def find_date(line):
    pattern = (r'[A-Z][a-z]*)[\s-]([A-Z][a-z]*)
    result = re.findall(pattern,line)

    pattern=(r'^(Mr\.|Mrs\.|Ms\.) ([a-z]+)( [a-z]+)*( [a-z]+)*$')')
    result = result + re.findall(pattern,line)
    return result





f = open("name.txt")
for line in f.readlines():
    #print(line)
    result = find_name(line)
    if (len(result)>0):
        print(result)
