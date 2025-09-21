import datetime




transactions = []


def add_transaction(transaction):
    current_bal=get_balance()
    last_transaction=None
    if len(transaction)>0:
        last_transaction= transaction[::-1]
    if transaction:
        if datetime(transaction.date)< datetime(last_transaction.date):
            raise Exception 
        if (current_bal+transaction.amount)<0:
            raise Exception
        else:
            transactions.append(transaction)

def get_transactions():
    return transactions

def clear_transactions():
    for i in range(len(transactions)):
        del transactions[i]

def get_balance():
    total_balance=0
    for i in range(len(transactions)):
        item=transactions[i]
        total_balance+=item.amount
    return total_balance


transaction={"amount":10,"date":datetime.date}

def test_transaction_types(transaction):
    assert isinstance(transaction["amount"],int)


def test_add_transaction(transaction):
    add_transaction(transaction)
    assert len(transactions)==1

# def test_get_transaction():
#     t1={"amount":10,"datetime":datetime.time}
#     add_transaction()
#     assert len(get_transactions())>1

test_transaction_types(transaction)





