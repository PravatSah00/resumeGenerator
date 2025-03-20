import pdfkit
import fitz

inter_pdf = 'interResume.pdf'
final_pdf = 'resume.pdf'

# Convert local HTML file to PDF
pdfkit.from_file("web/index.html", inter_pdf, options={
    'enable-local-file-access': True,  # Required for local CSS
    'page-size': 'A4',
    'print-media-type': '',
})

print( f"Intermediate pdf generated: ${inter_pdf}" )


# Define bookmarks with approximate Y-coordinates
bookmarks = [
    ("Education", 80),
    ("Experience", 200),
    ("Projects", 450),
    ("Skills", 550),
]

doc = fitz.open(inter_pdf)
page = doc[0]  # Single-page PDF

# Add bookmarks to the sidebar
toc = []
for i, (title, y_position) in enumerate(bookmarks, start=1):
    toc.append([1, title, 1, y_position])  # Format: [Level, Title, Page, Y-Position]

doc.set_toc(toc)  # Apply bookmarks

# Save the updated PDF
doc.save(final_pdf)
doc.close()

print(f"PDF with bookmarks created: {final_pdf}")
