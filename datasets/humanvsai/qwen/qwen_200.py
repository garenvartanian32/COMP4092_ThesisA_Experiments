def download():
    import ftplib
    import os
    FTP_HOST = 'ftp.example.com'
    FTP_USER = 'username'
    FTP_PASS = 'password'
    LOCAL_DIR = '/path/to/local/directory'
    ftp = ftplib.FTP(FTP_HOST, FTP_USER, FTP_PASS)
    ftp.cwd('/path/to/remote/directory')
    files = ftp.nlst()
    for file in files:
        local_file_path = os.path.join(LOCAL_DIR, file)
        with open(local_file_path, 'wb') as local_file:
            ftp.retrbinary(f'RETR {file}', local_file.write)
    ftp.quit()