#성적관리 프로그램 작성하기
num = int(input("학생 수: "))

name = input("이름 : ")
num = int(input("번호 : "))
kor = int(input("국어 점수 : "))
eng = int(input("영어 점수 : "))
math = int(input("수학 점수 : "))
phy = int(input("물리 점수 : "))
sum = kor + eng + math + phy 
average = sum / 4
blank = '%-2s' %''

def sungjuk():

    i = 0

    if average >= 90:
        grade = "A"
    elif 90 > average >= 80:
        grade = "B"
    elif 80 > average >= 70:
        grade = "C"
    elif 70 > average >= 60:
        grade = "D"
    else:
        grade = "F"

    
    print("==========================================================")
    print("이름    번호  국어  영어  수학  물리  총점    평균  학점")
    print("==========================================================")
    print(name, blank, num, blank, kor, blank, eng, blank, math, blank, phy, blank, sum, 
    blank, average, blank, grade)


for i in range(num):
    sungjuk()