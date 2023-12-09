import pandas as pd

def largest_orders(orders:pd.DataFrame):
    #if order empty return an empty DataFrame
    if orders.empty:
        return pd.DataFrame({'customer_number':[]})
    
    orders = orders.groupby('customer_number').size().reset_index(name='count')
    orders.sort(by='count',ascending = False, inplace= True)

    return orders[['customer_number'][:1]]
