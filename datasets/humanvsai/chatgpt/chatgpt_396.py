import io
from openpyxl import Workbook
from django.http import HttpResponse

def workbook_to_xlsx_response(workbook):
    output = io.BytesIO() # Create a byte stream buffer
    workbook.save(output) # Save the workbook into the buffer
    output.seek(0) # Move the cursor to the beginning of the buffer
    response = HttpResponse(content=output.read(),
                            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=myfile.xlsx' # Set the file name
    return response
