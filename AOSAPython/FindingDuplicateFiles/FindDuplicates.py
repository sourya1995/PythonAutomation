import sys


def find_duplicates(filenames):
    matches = []
    for left in filenames:
        for right in filenames:
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