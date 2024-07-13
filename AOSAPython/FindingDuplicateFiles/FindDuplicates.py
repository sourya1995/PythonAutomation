import sys

def naive_hash(data):
    return sum(data) % 13

def find_groups(filenames):
    groups = {}
    for filename in filenames:
        hash = naive_hash(open(filename, 'rb').read())
        if hash not in groups:
            groups[hash] = set()
        groups[hash].add(filename)
    return groups

def find_duplicates(filenames):
    matches = []
    for i_left in range(len(filenames)):
        left = filenames[i_left]
        for i_right in range(i_left): #files coming BEFORE ileft
            right = filenames[i_right]
            if(same_bytes(left, right)):
                matches.append((left, right))
    return matches

def same_bytes(leftname, rightname):
    left_bytes = open(leftname, 'rb').read()
    right_bytes = open(rightname, 'rb').read()
    return left_bytes == right_bytes
    
    
if __name__ == '__main__':
    duplicates = find_duplicates(sys.argv[1:])
    for (left, right) in duplicates:
        print(f'{left} and {right}')