
from datetime import datetime

class Transaction:
    """Этот класс используется для обработки транзакций"""

    def commit(self,status): #плдтверждение транзакции
        """This exception is derived from RuntimeError. In user defined base
        classes, abstract methods should raise this exception when they require
         derived classes to override the method.
         """
        raise NotImplementedError()

    def rollBack(self,status): # откат транзакции
        raise NotImplementedError()

    def __init__(self,amount,debitor,creditor,date = None):
        self.status = "INIT"
        self.amount = amount # Сумма транзакции
        self.debitor = debitor # плательщик (просто строка, хранящая ФИО плательщика)
        self.creditor = creditor # получатель
        self._date = datetime.now().strftime("%d.%m.%Y - %H:%M:%S")
    def __str__(self):

        return("Type {0}\nAmount {1}\nDebitor {2}\nCreditor {3}\n {4}\
        ".format(self.status,self.amount,self.debitor,self.creditor,self._date))

class FinancialTransaction(Transaction):
    transaction_type = 'FINANCIAL'

    def __init__(self,amount,debitor,creditor):

        super().__init__(amount,debitor,creditor)

    def commit(self,status):
        self.status = 'COMMITED'

    @staticmethod
    def static_now():
        return time.clock()
    def rollBack(self,status):
        self.status ='ROLLED BACK'
        self.timestamp = self.static_now()
    def display(self):
        print ("Tranzactional type: \n",self.transaction_type)

class OperationalTransaction(Transaction):
    transaction_type = 'OPERATIONAL'
    def __init__(self,amount,debitor,creditor):
        #print("Tranzactional type:\n",self.transaction_type)
        super().__init__(amount,debitor,creditor)
    def commit(self,status):
        self.status = 'COMMITED'
    def display(self):
        print ("Tranzactional type: \n",self.transaction_type)
