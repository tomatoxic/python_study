
#in : 리스트나 문자열 안에 있으면 참 없으면 거짓
list1= [1,2,3,4,5]
string1= "My name is AskPython"
print(5 in list1)      #True
print("is" in string1)    #True

#예제 1) 다음코드의 실행 결과는 ?
a = "Life is too short, you need python"
if "wife" in a: 
    print("wife")
elif "python" in a and "you" not in a: 
    print("python")
elif "shirt" not in a: 
    print("shirt")
elif "need" in a: 
    print("need")
else: 
    print("none")