# 모듈 모음
import os
import time
from datetime import datetime
from git import Repo

#########################################################################
# 변수 모음

# dateset 이라는 변수안에 오늘 날짜에 대한 정보를 담는다.
dateset = datetime.today()

# filename에다가 filename으로 사용될 형식의 오늘 날짜의 값을 넣는다.
filename = (dateset.strftime("%Y.%m.%d"))

# tmcheck라는 변수에 오늘의 월을 기록한다.
tmcheck = (dateset.strftime("%m"))

# tycheck라는 변수에 오늘의 년도를 기록한다.
tycheck = (dateset.strftime("%Y"))

#########################################################################
# 함수 모음

# 시작하기전 input값을 입력받는 함수
def setup():
    os.system("cls")
    print("\n---------------------")
    print("|  Record your day. | ")
    print("---------------------")
    print("\nNumber to be recorded:\n")
    recnum = int(input("        "))
    print("\n---------------------")
    print("Loding...")
    time.sleep(2)
    os.system("cls")
    return recnum
# diary 브런치에 업로드할 TIL파일을 만드는 함수
def crtfie():
    os.chdir('<GIT_DIR>/')
    os.system("git checkout diary") 
    os.system("cls") 
    f = open(f"<GIT_DIR>/{tycheck}/{tmcheck}/{filename}.md",'w')
    f.write("# Today I Learned\n")
    COMMIT_MESSAGE = filename

    if (recnum > 0):
        for i in range(recnum):
            rrecnum = i + 1
            print("Record ", rrecnum)
            recording = input ("")
            f.write(f"\n- {recording}")

    f.close()
# diary 브런치로 git push를 진행하는 함수
def git_push():
    try:
        os.system("cls")
        os.chdir('<GIT_DIR>/')
        os.system("git add -A")
        os.system(f"git commit -m {filename}")
        os.system("git push origin diary")
        os.system("cls")
    except:
        print('Some error occured while pushing the code')    
# main 브런치에 업로드할 체크리스트 파일을 만드는 함수
def crtcheck():
    os.chdir('<GIT_DIR>/')
    os.system("git checkout main") 
    os.system("cls") 
    f = open(f"<GIT_DIR>/push_check/{filename}.md",'w')
    f.write("# Today I Learned Check List\n")
    f.write(f"\n- {filename} push check")

    f.close()
# main 브런치에 업로드하는 함수
def git_check():
    try:
        os.chdir('<GIT_DIR>/')       
        os.system("git add -A")
        os.system(f"git commit -m {filename}_check")
        os.system("git push origin main")
        os.system("cls")
    except:
        print('Failed push to main branch')    
#########################################################################
# 함수들 사용

recnum = setup()
crtcheck()
git_check()
crtfie()
git_push()

print("Good Night")