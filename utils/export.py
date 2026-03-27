import xlsxwriter
from datetime import datetime

def create_tracker():
    workbook = xlsxwriter.Workbook('Job_Application_Tracker.xlsx')
    
    sheet = workbook.add_worksheet('Job Application Data')

    headers = [
        "Application ID","Date Applied","Company","Position","Status","Notes"
    ]

    for col, h in enumerate(headers):
        sheet.write(0, col, h)

    today = datetime.now()

    sample = [
        ["APP-001", today.strftime("%Y-%m-%d"), "TechCorp", "GIS Analyst", "Applied", "First apply"]
    ]

    for r, row in enumerate(sample, start=1):
        for c, val in enumerate(row):
            sheet.write(r, c, val)

    workbook.close()
