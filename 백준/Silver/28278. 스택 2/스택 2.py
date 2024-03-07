import sys

N = int(sys.stdin.readline())

stack = []  # 스택 초기화
for _ in range(N):
    i = list(map(int, sys.stdin.readline().split()))  # 명령 입력 받기

    # 명령 처리
    command = i[0]
    if command == 1:  # Push
        stack.append(i[1])
    elif command == 2:  # Pop
        if not stack:  # 스택이 비어있는 경우
            print(-1)
        else:
            print(stack.pop())  # 스택에서 값 제거하고 출력
    elif command == 3:  # Size
        print(len(stack))  # 스택의 크기 출력
    elif command == 4:  # Empty
        print(int(not stack))  # 스택이 비어있으면 1 출력, 아니면 0 출력
    elif command == 5:  # Top
        if not stack:  # 스택이 비어있는 경우
            print(-1)
        else:
            print(stack[-1])  # 스택의 맨 위 값 출력
