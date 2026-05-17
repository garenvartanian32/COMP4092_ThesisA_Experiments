import ftplib

def download():
    # Create an FTP object
    ftp = ftplib.FTP('ftp.example.com')

    # Login to the FTP server
    ftp.login('username', 'password')

    # Change to the directory where the files are located
    ftp.cwd('path/to/files')

    # Get a list of all files in the directory
    files = ftp.nlst()

    # Loop through the files
    for file in files:
        # Open the file in write binary mode
        with open(file, 'wb') as f:
            # Retrieve the file from the FTP server
            ftp.retrbinary('RETR ' + file, f.write)

    # Close the FTP connection
    ftp.quit()