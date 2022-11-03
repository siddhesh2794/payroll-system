import pymysql



con=None
cur=None
def dbconnect():
    global con,cur
    con = pymysql.connect(host='localhost',
                            database='payroll',
                            user='root',
                            password='')
    cur = con.cursor()
    
def dbdisconnect():
    cur.close()
    con.close()
    
def addEmployee(mempno,mname,mjob,mbasic,mda,mhra,mgross,mtax,mnet):
    try:
        dbconnect()
        sql=f'insert into pay values({mempno},"{mname}","{mjob}",{mbasic},{mda},{mhra},{mgross},{mtax},{mnet})'
        cur.execute(sql)
        con.commit()
        return 'Insert Successful'
    except Exception as e:
        return e
    finally:
        dbdisconnect()
        
def readall():
    dbconnect()
    sql= 'select * from pay'
    cur.execute(sql)
    data= cur.fetchall()
    return data
    dbdisconnect
    
def searchEmployee(id):
    dbconnect()
    sql = f'select * from pay where empno={id}'
    cur.execute(sql)
    data = cur.fetchone()
    dbdisconnect()
    return data

def deleterecord(id):
    try:
        dbconnect()
        sql = f'delete from pay where empno={id}'
        cur.execute(sql)
        con.commit()
        return 'Delete Successful'
    except Exception as e:
        return e
    finally:
        dbdisconnect()
        
def updaterecord(data):
    try:
        dbconnect()
        sql = f'update pay set name="{data[1]}",job="{data[2]}",basicsalary={data[3]},DA={data[4]},HRA={data[5]},GrossSalary={data[6]},Tax={data[7]},NetSalary={data[8]} where empno={data[0]}'
        cur.execute(sql)
        con.commit()
        return 'Update Successful'
    except Exception as e:
        return e
    finally:
        dbdisconnect()
    


