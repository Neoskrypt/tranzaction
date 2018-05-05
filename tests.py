import pull
import tranzaction as tranz
import db
from log import LOG
TrFin = pull.TransactionPool()
assert TrFin
op = pull.TransactionPool()
assert op
Tr = pull.TransactionPool()
assert Tr
fin = tranz.FinancialTransaction(500,"Taras","Oleg")
assert fin

fin.commit(fin.status)
oper = tranz.OperationalTransaction(1500,"Alex","Bata")
assert oper
oper.commit(oper.status)

fin.display()
i = 0
while i <=20:
    TrFin.add(fin)
    op.add(oper)
    i +=1

print(TrFin)
LOG.debug("Debug message")
print(op)
assert (TrFin != op ),"False" #if + raise

TrFin = str(object=TrFin)
assert type(TrFin) == str
#assert type(TrFin not str),"not str"
op = str(object=op)
assert type(op) == str
#assert isinstanse(TrFin,str), 'Argument of wrong type!'
Db = db.dumpWith(TrFin,op)

Db1 = db.dump2(TrFin,op)
