	def inserdata(cls):
		if  cls.__isconnect==1:
      
   		         cls.__cur.execute('insert into webdata(address,content,meettime) values(%s,%s,%s)',['这个稳重','123123','1992-12-12 12:12:12'])
   		         cls.__conn.commit()
                else:
                        print '''has not connet'''
       def showtableinfo(cls,table,params):
                if  cls.__isconnect==1:
                        request=len(params)
                        request_item=''
                        for j in range(0,request-1):
                                  request_item=request_item+params[j]+','
                        request_item=request_item+params[request-1]
                        print request_item
                        try:
                                count=cls.__cur.execute('select  '+request_item+' from '+table)
                                result=cls.__cur.fetchall()

                                for temp in result:
                                        for i in range(0,len(temp)):
                                                print temp[i],
                                        print ''
                        except MySQLdb.Error,e:
                                print "Mysql Error %d: %s" % (e.args[0], e.args[1])
                else:
                          print '''has not connet'''
        def searchtableinfo(cls,table,params,value):
                paramsValue=(value)
                if  cls.__isconnect==1:
                        try:
                                count=cls.__cur.execute('select  * from  '+table+'  where  '+params+' = %s',paramsValue)
                                if count>0:
                                        result=cls.__cur.fetchall()
                                        print '相关信息如下：'
                                        for temp in result:
                                               for i in range(0,len(temp)):
                                                        print temp[i],
                                               print ''
                                else:
                                       print '没有相关信息'

                        except MySQLdb.Error,e:
                                print "Mysql Error %d: %s" % (e.args[0], e.args[1])
                else:
                          print '''has not connet'''

        def  searchtableinfo_byitem(cls,table,select_params,params,value):
                paramsValue=(value)
                if  cls.__isconnect==1:
                        try:
                                sql='select     '
                                request=len(select_params)

                                for j in range(0,request-1):
                                        sql=sql+select_params[j]+','
                                sql=sql+select_params[request-1]
                                sql=sql+' from '
                                request=len(table)

                                for j in range(0,request-1):
                                       sql=sql+table[j]+','
                                sql=sql+table[request-1]
                                sql=sql+' where '
                                sql=sql+table[0]+'.'+params[0]+'='+table[1]+'.'+params[1]

                                print sql
                                count=cls.__cur.execute(sql+' and '+params[1]+'=%s',paramsValue)
                                if count>0:
                                        result=cls.__cur.fetchall()
                                        print '相关信息如下：'
                                        for temp in result:
                                               for i in range(0,len(temp)):
                                                        print temp[i],
                                               print ''
                                else:
                                       print '没有相关信息'

                        except MySQLdb.Error,e:
                                print "Mysql Error %d: %s" % (e.args[0], e.args[1])
                else:
                          print '''has not connet'''      
                          #@select_params 为要显示的属性
                          #@table为要查看的信息在哪几个表
                          #
        def  searchtableinfo_byitemmore(cls,table,select_params,params,value):
                paramsValue=(value)
                if  cls.__isconnect==1:
                        try:
                                sql='select     '
                                request=len(select_params)

                                for j in range(0,request-1):
                                        sql=sql+select_params[j]+','
                                sql=sql+select_params[request-1]
                                sql=sql+' from '
                                request=len(table)

                                for j in range(0,request-1):
                                       sql=sql+table[j]+','
                                sql=sql+table[request-1]
                                sql=sql+' where '
                            #    sql=sql+table[0]+'.'+params[0]+'='+table[1]+'.'+params[1]+' and '
                               # sql=sql+table[0]+'.'+params[0]+'='+table[1]+'.'+second_params[1]+' and '
                                sql=sql+'orderbook.orderid=orders.oid and orderbook.bookid=book.bid and orders.user=users.uid  '
                                print sql
                                count=cls.__cur.execute(sql+' and '+params[1]+'=%s',paramsValue)
                                if count>0:
                                        result=cls.__cur.fetchall()
                                        print '相关信息如下：'
                                        for temp in result:
                                               for i in range(0,len(temp)):
                                                        print temp[i],
                                               print ''
                                else:
                                       print '没有相关信息'

                        except MySQLdb.Error,e:
                                print "Mysql Error %d: %s" % (e.args[0], e.args[1])
                else:
                        print '''has not connet'''      
 
        def  searchtableinfo_bystate(cls,table,select_params,params,value):
                paramsValue=value
                if  cls.__isconnect==1:
                        try:
                                sql='select     '
                                request=len(select_params)

                                for j in range(0,request-1):
                                        sql=sql+select_params[j]+','
                                sql=sql+select_params[request-1]
                                sql=sql+' from '
                                request=len(table)

                                for j in range(0,request-1):
                                       sql=sql+table[j]+','
                                sql=sql+table[request-1]
                                sql=sql+' where '
                                #sql=sql+table[0]+'.'+params[0]+'='+table[1]+'.'+params[1]+' and '
                                #sql=sql+table[0]+'.'+params[0]+'='+table[1]+'.'+second_params[1]+' and '
                                sql=sql+'orderbook.orderid=orders.oid and orderbook.bookid=book.bid   and orders.user=users.uid '
                                print sql
                                if len(params)>1 :
                                        count=cls.__cur.execute(sql+' and '+params[1]+'=%s and orders.state = %s ',paramsValue)
                                else:
                                        count=cls.__cur.execute(sql+'  and orders.state = %s ',paramsValue)
                                if count>0:
                                        result=cls.__cur.fetchall()
                                        print '相关信息如下：'
                                        for temp in result:
                                               for i in range(0,len(temp)):
                                                        print temp[i],
                                               print ''
                                else:
                                       print '没有相关信息'

                        except MySQLdb.Error,e:
                                print "Mysql Error %d: %s" % (e.args[0], e.args[1])
                else:
                        print '''has not connet''' 