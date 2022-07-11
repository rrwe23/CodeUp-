# cabinet = {3:"유재석",100:"김태호"}      /// 캐비넷에 집어넣고 꺼내기
# print(cabinet[3])

# print(3 in cabinet)
# print(10 in cabinet)

# print(cabinet.values())
# print(cabinet.keys())


# menu = ("돈가스","치즈가스")        ## 속도가 빠르기 때문에 변하지 않는 값 쓸때 사용

# print(menu[0])
# print(menu[1])


# name = "김종국"
# age = 20
# hobby = "코딩"
# print(name,age,hobby)

# name,age,hobby = "김종국",20,"코딩"

# print(name,age,hobby)



                                                        ##집합  중복안됨,순서없음

# my_set = {1,2,3,3,3}

# java = {"유재석", "김태호","박명수"}
# python = set(["유재석","박명수"])

# print(java&python)   ## 교집합
# print(java.intersection(python))  ## 교집합

# print(java or python)    ## 합집합
# print(java | python) 
# print(java.union(python))

# print(java - python)            # 차집합
# print(java.difference(python))

# python.add("김태호")    # 추가
# print(python)

# python.remove("김태호")
# print(python)


menu = {"커피","우유","주스"}

print(menu,type(menu))

menu = list(menu)
print(menu,type(menu))
menu = tuple(menu)
print(menu,type(menu))












