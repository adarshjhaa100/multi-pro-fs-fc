BUFFER_SIZE = 1024

# output_file = "outrfc.txt"
# output_file = "outpng1.png"
output_file = "outmkv1.mkv"

fw = open(f"./data/{output_file}", "wb+")


def combine_file_parts(fw, byte_stream):
    fw.write(byte_stream)


with open("./data/randomvijeo.mkv", "rb+") as fr:
    count = 0    
    while True:
        count += 1
        bytes_read = fr.read(BUFFER_SIZE)
        
        combine_file_parts(fw, bytes_read)

        if(bytes_read == b''):
            break
        # print(bytes_read.decode())
    print(count)


fw.close()