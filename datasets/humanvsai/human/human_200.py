def download():
    ftp = ftplib.FTP(SITE)
    ftp.set_debuglevel(DEBUG)
    ftp.login(USER, PASSWD)
    ftp.cwd(DIR)
    filelist = ftp.nlst()
    filecounter = MANAGER.counter(total=len(filelist), desc='Downloading',
                                  unit='files')
    for filename in filelist:
        with Writer(filename, ftp.size(filename), DEST) as writer:
            ftp.retrbinary('RETR %s' % filename, writer.write)
        print(filename)
        filecounter.update()
    ftp.close()