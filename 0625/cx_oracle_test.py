import cx_Oracle
import cv2


class Test:

    def __init__(self, num=None, name=None, price=None, desc=None):
        self.num = num

        self.name = name

        self.price = price

        self.desc = desc

    def print(self):
        print('num:', self.num, '/ name:', self.name, '/ price:', self.price, '/ descript:', self.desc)


class Dao_test:
    #전체검색
    def select_all(self):
        #커넥션 수립. ID,PW, ip:리스너/sid(작업관리자 -> 서비스 -> oracleservice뒤에있는거 )
        conn = cx_Oracle.connect("hr", "hr", "localhost:1521/xe", encoding='utf-8')

        cursor = conn.cursor()#spl문 실행하고 select인 경우 검색결과 반환

        sql = 'select * from test'

        cursor.execute(sql)

        datas = []

        for row in cursor:
            datas.append(Test(row[0], row[1], row[2], row[3]))

        conn.close()#커넥션 끊는다

        return datas

    def select(self, num):

        conn = cx_Oracle.connect("hr", "hr", "localhost:1521/xe", encoding='utf-8')

        cursor = conn.cursor()

        sql = 'select * from test where num=:1'

        d = (num,)#튜플로 sql 바인딩할 값 지정

        cursor.execute(sql, d)#sql실행. 바인딩 튜플을 2번째 값으로

        row = cursor.fetchone()

        conn.close()#연결끊기

        if row is not None:
            return Test(row[0], row[1], row[2], row[3])

    def insert(self, t):

        conn = cx_Oracle.connect("hr", "hr", "localhost:1521/xe", encoding='utf-8')

        cursor = conn.cursor()

        sql = 'insert into test values(seq_test.nextval, :1, :2, :3)'

        d = (t.name, t.price, t.desc)

        cursor.execute(sql, d)

        conn.commit()#자바와 달리 자동 커밋이 안되므로 쓰기동작 후 커밋 필수

        conn.close()

    def update(self, t):

        conn = cx_Oracle.connect("hr", "hr", "localhost:1521/xe", encoding='utf-8')

        cursor = conn.cursor()

        sql = 'update test set price=:1, disc=:2 where num=:3'

        d = (t.price, t.desc, t.num)

        cursor.execute(sql, d)

        conn.commit()

        conn.close()


def main():
    dao = Dao_test()

    #dao.insert(Test(0, 'aaa', 1400, 'info1'))

    dao.update(Test(2, '', 2500, '가나다'))

    datas = dao.select_all()

    for t in datas:
        t.print()


main()