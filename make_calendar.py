from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
import calendar

# Define the page size and margins
PAGE_SIZE = letter
LEFT_MARGIN = 20
RIGHT_MARGIN = 20
TOP_MARGIN = 50
BOTTOM_MARGIN = 50

# Define the data for the calendar
year = 2023
month = 3
data = calendar.monthcalendar(year, month)

# Define the table style
table_style = TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.gray),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 14),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ('GRID', (0, 0), (-1, -1), 1, colors.black)
])

# Define the table data
table_data = [['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']]
for week in data:
    week_row = []
    for day in week:
        if day == 0:
            week_row.append('')
        else:
            # Add sample events to the calendar
            events = ['Event 1', 'Event 2', 'Event 3']
            event_text = ''
            for event in events:
                event_text += event + '\n'
            week_row.append(f'{day}\n{event_text}')
    table_data.append(week_row)

# Calculate the width of each table cell based on the page size and margins
page_width = PAGE_SIZE[0] - LEFT_MARGIN - RIGHT_MARGIN
cell_width = page_width / 7

# Create the PDF document
pdf_doc = SimpleDocTemplate('calendar4.pdf', pagesize=PAGE_SIZE,
                            leftMargin=LEFT_MARGIN, rightMargin=RIGHT_MARGIN,
                            topMargin=TOP_MARGIN, bottomMargin=BOTTOM_MARGIN)

# Create the table and apply the table style
pdf_table = Table(table_data, colWidths=[cell_width]*7)
pdf_table.setStyle(table_style)

# Add the table to the PDF document and generate the PDF
pdf_doc.build([pdf_table])
