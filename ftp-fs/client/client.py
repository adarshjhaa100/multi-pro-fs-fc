from ftplib import FTP

FTP_HOST = "127.0.0.1" 

# Specifying server_address during object creation doesnt work for some reason
with FTP(user="user",passwd="12345") as ftp:
    print(ftp)
    # ftp.login("user","12345")
    ftp.connect(host=FTP_HOST, port=2121)
    ftp.login("user","12345")
    print(ftp.getwelcome())

    fr = open("outmkv1.mkv", "rb+")

    # cmd: STOR file name and path at the destination directory
    ftp.storbinary("STOR test_video_over_ftp.mkv",fr)
    
    fr.close()


    
