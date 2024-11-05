import json


#取得所有檔案的名稱
policy=["LRB","Belady","LRU","GDSF","TinyLFU","LeCaR","AdaptSize"]
cache_size=["05","1","5","10"]
trace=["wiki2018"]
file_names=[p+"_"+c+"_"+t+".txt"  for p in policy for c in cache_size for t in trace]

#讀檔 並計算hit_rate
for f in file_names:
    try:
        with open("result/"+f, 'r') as file:
            data=json.load(file)
            print(f+"- Byte hit ratio: ",round(1-(sum(data["segment_byte_miss"])/sum(data["segment_byte_req"])),2))
            print(f+"- Obj hit ratio: ",round(1-(sum(data["segment_object_miss"])/sum(data["segment_object_req"])),2))
    except FileNotFoundError:
        # 當文件不存在時，輸出沒找到
        print(f+": not found")
        print(f+": not found")

    print("")
