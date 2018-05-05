
import tranzaction
import exeptions

class TransactionPool():

    def __init__(self):
        self.empty()
    def empty(self):
        self._data = []
    def add(self,tran):
        self._data.append(tran)
        ###############################################################
    def commit(self):
        for i in self._data: #
            try:
                if i.commit(i.status) == 'COMMITED' or i.commit(i.status) == 'ROLLED BACK':
                    raise exeptions.CommitError()
                    continue
            except exeptions.CommitError() as e:
                print(e)
            finally:
                print("Ok COMMITED")

    def rollBack(self):
        for i in self._data:
            try:
                if i.rollBack(i.status)== 'ROLLED BACK' or i.rollBack(i.status)== 'COMMITED':
                    raise exeptions.RollbackError()
                    continue
            except exeptions.RollbackError() as e:
                print(e)
            finally:
                print("Ok ROLLED BACK")



    ############################################################################
    def _list(self) -> list:#метод для возврата значения
        return self._data
    def __str__(self):

        return ("\n".join("%s" % i for i in self._data))#перегрузка метода/ итеративный проход по списку
