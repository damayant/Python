import pandas as pd


def process_csv_batch(input_path,output_path,batch_size=100):
    #chunksize returns iterator of df
    reader = pd.read_csv(input_path,chunksize=batch_size)
    for i , chunk in enumerate(reader):
        chunk["timestamp"]=pd.Timestamp.now()
        chunk.to_csv(output_path,mode="a",index=False,header=(i==0))

def test_csv_process(tmp_path):
    csv_in,csv_out= tmp_path/"data.csv",tmp_path/"warehouse.csv"
    pd.DataFrame({"id":[1,2]}).to_csv(csv_in,index=False)
    process_csv_batch(str(csv_in),str(csv_out),batch_size=1)
    result_df=pd.read_csv(csv_out)
    assert "timestamp" in result_df.columns
    assert len(result_df) == 2