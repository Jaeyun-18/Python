id=20190612
password=20030310

class python:
    def passcheck(self):
        self.password=int(input())
        if self.password==password:
            print("로그인 성공")
        else:
            print("비밀번호가 틀렸습니다.")
    def idcheck(self):
        self.id=int(input())
        if self.id==id:
            self.passcheck()
        else:
            print("아이디가 틀렸습니다.")

id1=python() 
id1.idcheck()
