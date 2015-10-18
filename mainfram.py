# -*- coding: utf-8 -*-

"""
Module implementing mainframcontrol.
"""
import sys
from PyQt4.QtCore import pyqtSignature
from PyQt4.QtGui import QMainWindow
from PyQt4 import QtGui
from Ui_mainfram import Ui_mainfram
import SQLtool
import sys 
reload(sys)
sys.setdefaultencoding('utf-8')

class mainframcontrol(QMainWindow, Ui_mainfram):
    """
    Class documentation goes here.
    """

    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget (QWidget)
        """
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.itemcommo.addItems([u'按作者',u'按书名',u'按出版社',u'按书号'])
        self.ordercommobox.addItems([u'按用户',u'按用户名',u'按书目',u'按书号'])
        self.buycommobox.addItems([u'按书名',u'按书号'])
 #       self.inittable()
        self.initsearch()
        self.initordersearch()
        self.initbuysearch()
    def drawtable(self,result,description,count,col,datacontent):


        datacontent.setRowCount(count) #行
        datacontent.setColumnCount(col) #列
        if (col==0 or count==0):
            return 
        contentarray=[]
        for temp  in description:
               contentarray.append(unicode(temp[0]))
        datacontent.setHorizontalHeaderLabels(contentarray)  
        for i in range(0,len(result)):
                for j in range(0,len(result[i])):
                        newItem = QtGui.QTableWidgetItem(unicode(result[i][j]) )
                        datacontent.setItem(i, j, newItem)  
#                        
    def initsearch(self):
        bookSQL=SQLtool.DBmanager()
        bookSQL.connectdb()
        (result,description,count,col)=bookSQL.searchtableinfo_byparams(['book'],[],[],[])
        self .drawtable(result,description,count,col,self.datacontent)
        bookSQL.closedb()
    def initordersearch(self):
        orderSQL=SQLtool.DBmanager()
        orderSQL.connectdb()
        (result,description,count,col)=orderSQL.searchtableinfo_byparams(['orders','users'],['oid','user','orders.state','payment','ordertime','name'],['user'],['uid'])
        self .drawtable(result,description,count,col,self.orderdatacontent)
        orderSQL.closedb()
    def initbuysearch(self):
        buySQL=SQLtool.DBmanager()
        buySQL.connectdb()
        (result,description,count,col)=buySQL.searchtableinfo_byparams(['orders','orderbook','book','users'],['bookid','title','count(bookid) as buy_time'],['bookid','orderid','user','orders.state>'],['book.bid','oid','uid','3 group by bookid'])
        self .drawtable(result,description,count,col,self.buydatacontent)
        buySQL.closedb()

    @pyqtSignature("")
    def on_search_clicked(self):
        """
        Slot documentation goes here.
        """
        choice= self.itemcommo.currentIndex()
        searchcontent=unicode(self.searchcontent.text())
        bookSQL=SQLtool.DBmanager()
        bookSQL.connectdb()
        searchcontent_temp='\''+searchcontent+'\''
        print searchcontent_temp
        if choice==0:
                (result,description,count,col)=bookSQL.searchtableinfo_byparams(['book'],[],['author'],[searchcontent_temp])
                self .drawtable(result,description,count,col,self.datacontent)
        elif choice==1:
                (result,description,count,col)=bookSQL.searchtableinfo_byparams(['book'],[],['title'],[searchcontent_temp])
                self .drawtable(result,description,count,col,self.datacontent)
        elif choice==2:
                (result,description,count,col)=bookSQL.searchtableinfo_byparams(['book'],[],['press'],[searchcontent_temp])
                self .drawtable(result,description,count,col,self.datacontent)
        else:
                (result,description,count,col)=bookSQL.searchtableinfo_byparams(['book'],[],['bid'],[searchcontent_temp])
                self .drawtable(result,description,count,col,self.datacontent)
        bookSQL.closedb()

        # TODO: not implemented yet

    @pyqtSignature("")
    def on_showallbook_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.initsearch()
        
        

    
    @pyqtSignature("")
    def on_ordersearch_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        
        choice= self.ordercommobox.currentIndex()
        searchcontent=unicode(self.searchordercontent.text())
        orderSQL=SQLtool.DBmanager()
        orderSQL.connectdb()
        searchcontent_temp='\''+searchcontent+'\''
        print searchcontent_temp
        if choice==0:
                (result,description,count,col)=orderSQL.searchtableinfo_byparams(['orders','users'],['oid','user','orders.state','payment','ordertime','name'],['user','name'],['uid',searchcontent_temp])
                self .drawtable(result,description,count,col,self.orderdatacontent)
        elif choice==1:
                (result,description,count,col)=orderSQL.searchtableinfo_byparams(['orders','users'],['oid','user','orders.state','payment','ordertime','name'],['user','user'],['uid',searchcontent_temp])

                self .drawtable(result,description,count,col,self.orderdatacontent)
        elif choice==2:
                (result,description,count,col)=orderSQL.searchtableinfo_byparams(['orders','orderbook','book','users'],['oid','user','orders.state','payment','ordertime','title','users.name' ,'bookid'],['bookid','orderid','user','title'],['book.bid','oid','uid',searchcontent_temp])

                self .drawtable(result,description,count,col,self.orderdatacontent)
        else:
                (result,description,count,col)=orderSQL.searchtableinfo_byparams(['orders','orderbook','book','users'],['oid','user','orders.state','payment','ordertime','title','users.name' ,'bookid'],['bookid','orderid','user','bookid'],['book.bid','oid','uid',searchcontent_temp])

                self .drawtable(result,description,count,col,self.orderdatacontent)
        orderSQL.closedb()
    
    @pyqtSignature("")
    def on_showallorder_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.initordersearch()

    
    
    @pyqtSignature("")
    def on_buy_time_search_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        choice= self.ordercommobox.currentIndex()
        searchcontent=unicode(self.searchordercontent.text())
        buySQL=SQLtool.DBmanager()
        buySQL.connectdb()
        searchcontent_temp='\''+searchcontent+'\''
        print searchcontent_temp
        if choice==0:
                (result,description,count,col)=buySQL.searchtableinfo_byparams(['orders','orderbook','book','users'],['bookid','title','count(bookid) as buy_time'],['bookid','orderid','user','title','orders.state>'],['book.bid','oid','uid',searchcontent_temp,'3 group by bookid'])
                self .drawtable(result,description,count,col,self.buydatacontent)
        else :
                (result,description,count,col)=buySQL.searchtableinfo_byparams(['orders','orderbook','book','users'],['bookid','title','count(bookid) as buy_time'],['bookid','orderid','user','bookid','orders.state>'],['book.bid','oid','uid',searchcontent_temp,'3 group by bookid'])

                self .drawtable(result,description,count,col,self.buydatacontent)
        buySQL.closedb()
    
    @pyqtSignature("")
    def on_showallbuy_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.initbuysearch()
if __name__ == "__main__":

    app = QtGui.QApplication(sys.argv)
    ui = mainframcontrol()

    ui.show()
    sys.exit(app.exec_())
