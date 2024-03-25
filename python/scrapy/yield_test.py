


def run(a):
    
    yield 1
    
    if a == 1:
        yield 2
    if a==1:
        yield 3
        
if __name__ == "__main__":
    foo = run(1)
    for i in foo:
        print(i)