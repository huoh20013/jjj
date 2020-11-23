import sys

#sys.argv 是一个列表 在控制台输入命令的时候 一次将参数存入argv中 外部输入参数
input_file='supplier_data.csv'
output_file='1output.csv'

with open(input_file,'r',newline='') as filereader:
    with open(output_file,'w',newline='') as filewriter:
        #readline 读取一行 返回字符串
        header=filereader.readline()
        #strip 消除前后的空格
        header=header.strip()
        #split 将字符串按照,分离 返回一个列表 列表中是分离好的字符串 
        header_list=header.split(',')
        print(header_list)
        #writer函数将数据写入  map函数中运用str函数为了保证列表中每个都是字符串 join函数是在列表中每个值之间加入',' 并将整个列表转化为一个字符串 
        filewriter.write(','.join(map(str,header_list))+'\n')
        #采用for循环对输入文件的剩余行进行相同处理 
        for row in filereader:
            row=row.strip()
            row_list=row.split(',')
            print(row_list)
            filewriter.write(','.join(map(str,row_list))+'\n')
