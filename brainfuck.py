import sys
import argparse

def compile(code):
    input = sys.stdin.readline
    var = [0]
    loop = []
    var_ix = 0
    loop_ix = 0

    ix = 0
    while ix < len(code):
        s = code[ix]
        if s == '>':
            var_ix += 1
            if len(var) == var_ix:
                var.append(0)
        elif s == '<':
            var_ix -= 1
            if var_ix < 0:
                raise RuntimeError
        elif s == '+':
            var[var_ix] += 1
        elif s == '-':
            var[var_ix] -= 1
        elif s == '.':
            print(chr(var[var_ix]),end="")
        elif s == ',':
            inp = input()
            var[var_ix] = ord(inp[0])
        elif s == '[':
            if len(loop) == loop_ix:
                loop.append(0)
            loop[loop_ix] = ix
            loop_ix+=1
            if var[var_ix] == 0:
                while True:
                    if code[ix] == ']':
                        if len(loop) == loop_ix:
                            loop_ix-=1
                            loop.pop()
                            break
                        else:
                            loop.pop()
                    elif code[ix] == '[':
                        if len(loop) == loop_ix:
                            loop.append(0)
                        loop[loop_ix] = ix
                        loop_ix += 1
                    ix+=1
        elif s == ']':
            if var[var_ix]:
                ix = loop[loop_ix-1]
            else:
                if loop_ix == 0:
                    raise RuntimeError
                loop.pop()
                loop_ix-=1
        ix += 1
    if loop_ix:
        raise RuntimeError

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', type=str, required=True)
    args = parser.parse_args()
    with open(args.file, 'r') as f:
        lines = f.readlines()
        code = ''
        for line in lines:
            for i in line:
                if i in '><+-.,[]':
                    code += i
    try:
        compile(code)
    except RuntimeError:
        print("Compile error!!")
