from flask import make_response
from io import BytesIO

def build_xlsx_response(wb, title="report"):
    """Take a workbook and return a xlsx file response"""
    # Save the workbook to a BytesIO object
    output = BytesIO()
    wb.save(output)
    output.seek(0)

    # Create a response
    response = make_response(output.read())
    response.headers["Content-Disposition"] = "attachment; filename={}.xlsx".format(title)
    response.mimetype = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

    return response