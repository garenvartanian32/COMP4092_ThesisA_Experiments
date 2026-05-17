import os
from ftplib import FTP

def download_ftp_files(server, user, password, ftp_directory, local_directory):
    ftp = FTP(server)
    ftp.login(user=user, passwd=password)
    ftp.cwd(ftp_directory)
    if not os.path.exists(local_directory):
        os.makedirs(local_directory)
    filenames = ftp.nlst()
    for filename in filenames:
        with open(os.path.join(local_directory, filename), "wb") as f:
            ftp.retrbinary("RETR " + filename, f.write)
    ftp.quit()
