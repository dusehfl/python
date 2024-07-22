# 사용자가 문자열을 입력한다.
# 입력한 문자열의 처음이 '(', 끝이 ')'인지 검사하고
# 그렇지 않으면 '('와 ')'를 붙여주는 소스 코딩

str = input("문자열 입력 : ")
print("입력된 문자열 -> ", end = " ")

if str.startswith('(') == False:
    print("(", end = "")

print(str, end = "")

if str.endswith(')') == False:
    print(")", end = "")
