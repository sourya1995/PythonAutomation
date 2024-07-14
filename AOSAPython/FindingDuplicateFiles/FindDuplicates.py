import sys
from hashlib import sha256

def naive_hash(data):
    return sum(data) % 13

def find_groups(filenames):
    groups = {}
    for filename in filenames:
        file_hash = sha256(open(filename, 'rb').read()).hexdigest()
        if file_hash not in groups:
            groups[file_hash] = set()
        groups[file_hash].add(filename)
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
    groups = find_groups(sys.argv[1:])
    for filenames in groups.values:
        duplicates = find_duplicates(list(filenames))
        for (left, right) in duplicates:
            print(f'{left} and {right}')