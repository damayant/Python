import json 

def process_json_stream(input_path,output_path):
    with open(input_path,"r") as f_in, open(output_path,"w") as f_out:
        for line in f_in:
            record = json.loads(line)
            record["dt_entity"]="app_server_01"
            f_out.write(json.dumps(record)+"\n")

def test_process_json_stream(tmp_path):
    input_file,output_file= tmp_path/"in.json",tmp_path/"out.json"
    input_file.write_text(json.dumps({"message":"error"})+"\n")
    process_json_stream(str(input_file),str(output_file))
    result=json.loads(output_file.read_text())
    assert result["dt_entity"] == "app_server_01"