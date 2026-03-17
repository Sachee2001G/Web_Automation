from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto('https://demo.automationtesting.in/FileDownload.html')

    # Step 1: Fill in the PDF text box
    page.fill('#pdfbox', 'Sample content for PDF')

    # Step 2: Click the Generate PDF button (now enabled)
    page.click('#createPdf')

    # Step 3: Wait for the download link and click it
    with page.expect_download() as download_info:
        page.click('//a[@id="pdf-link-to-download"]')
    download = download_info.value
    download.save_as('./files/samplefile.pdf')

    browser.close()
