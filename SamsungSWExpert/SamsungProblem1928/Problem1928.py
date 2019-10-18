"""
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PR4DKAG0DFAUq&categoryId=AV5PR4DKAG0DFAUq&categoryType=CODE
1928. Base64 Decoder
"""
import base64


def main():
    test_cases = int(input())
    for t in range(test_cases):
        encoded = input()
        print('#%d %s' % (t+1, base64.b64decode(encoded).decode('utf-8')))


if __name__ == '__main__':
    main()
