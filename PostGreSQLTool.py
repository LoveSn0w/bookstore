#!/usr/bin/python
#coding:utf-8
import psycopg2
import config
import time
class DBmanager:
    __cur=''
    __conn=''
    __host=''
    __user=''
    __passwd=''
    __db='' 
    __port='5432'
    __connection_time=0
    __isconnect=0
    __charset=''
    def __init__(self):
        temp=config.Config
        self.__host = temp.host
        self.__user=temp.PostGreusername
        self.__passwd=temp.PostGredatapass
        self.__db=temp.PostGredatabase
        self.__port=temp.PostGredataport
        self.__charset=temp.charset
 
    def connectdb(self):
        try:
            self.__conn=psycopg2.connect(host=self.__host,user=self.__user,password=self.__passwd,database=self.__db,port=self.__port)
            self.__cur=self.__conn.cursor()
            self.__isconnect=1

            print "success connet "
        except Exception,e:
            print "PostGreSQLerror  %s" % e
            if  self.__connection_time<3:
                print 'time out ! and reconnect'
                time.sleep(3)
                self.__connection_time=self.__connection_time+1
                self.connectdb()
            else:
                print  'connect fail'

    def closedb(self):
        if  self.__isconnect==1:
            self.__cur.close()
            self.__conn.close()
            self.__isconnect=0
            print 'database has benn closed'
        else:
            print '''has not connet'''
 
        #searchtableinfo_byparams 输入参数执行对应的查询函数
        #@table 					包含要查询的表，数组
        #@select_params				要显示的列名，数组
        #@request_params     		条件匹配参数，数组
        #@equal_params				每一个与request_params对应相等的数组
    def  searchtableinfo_byparams(self,table,select_params,request_params,equal_params):
        if len(request_params)!=len(equal_params):
            print 'request_params,equals_params长度不相等'
            return
        elif  self.__isconnect==1:
                        
            try:
                sql='select     '
                length=len(select_params)
                if length > 0:

                    for j in range(0,length-1):
                        sql=sql+select_params[j]+','
                    sql=sql+select_params[length-1]
                else:
                    sql=sql+'*'
                sql=sql+' from '
                length=len(table)

                for j in range(0,length-1):
                    sql=sql+table[j]+','
                sql=sql+table[length-1]
                request_params_length=len(request_params)
                if request_params_length>0:

                    sql=sql+' where '
                    for k in range(0,request_params_length-1):
                        sql=sql+request_params[k]+'= '+equal_params[k]+' and '
                    sql=sql+request_params[request_params_length-1]+'= '+equal_params[request_params_length-1]+'  '
                print sql

                self.__cur.execute(sql)
                count= self.__cur.rowcount
                                 
                if count>0:
                    result=self.__cur.fetchall()
                    content=self.__cur.description
                    col= len(content)
                    return result,content,count,col
                                    
                else:
                    print '没有相关信息'
                    return (0,0,0,0)

            except Exception,e:
                print "PostgreSQL Error  %s" % e
        else:
            print '''has not connet'''  


if __name__ == "__main__":
  sqltool=DBmanager()
  sqltool.connectdb()
  sqltool.closedb()
