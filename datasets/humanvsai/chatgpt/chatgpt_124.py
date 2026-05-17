import win32com.client


def get_stores():
    stores = {}
    oStore = win32com.client.Dispatch("ADODB.Connection")
    oStore.Open("Provider=Microsoft.ACE.OLEDB.12.0;Data Source='\\\\localhost\\c$\\ProgramData\\Microsoft\\Crypto\\RSA\\MachineKeys\\';Extended Properties=Text;")
    rs = win32com.client.Dispatch("ADODB.Recordset")
    rs.Open("SELECT * FROM machinekeys", oStore, 1, 1)
    while not rs.EOF:
        stores[rs.Fields.Item("StoreName").Value] = rs.Fields.Item("StoreLocation").Value
        rs.MoveNext()
    rs.Close()
    return stores
