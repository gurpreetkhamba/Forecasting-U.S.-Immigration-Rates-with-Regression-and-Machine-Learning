from playwright.sync_api import sync_playwright
import os

DOWNLOAD_DIR = "downloads"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

SKIP_YEARS = [str(y) for y in range(2015, 2024)]  # 2015 to 2023

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(accept_downloads=True)
    page = context.new_page()

    page.goto("https://ohss.dhs.gov/topics/immigration/lawful-permanent-residents/profiles")
    page.select_option(
        'select[name="table_cob_length"]',
        value='-1'
        )
    
    page.locator("#table_cob tbody tr").first.wait_for()
    
    links = page.locator("a[href]").all()

    for link in links:
        link_text = link.inner_text().strip()
        href = link.get_attribute("href")

        if not href:
            continue

        if not href.lower().endswith((".xlsx", ".xls")):
            continue
        
        if any(year in link_text for year in SKIP_YEARS):
            print("Skipping:", link_text)
            continue
        
        with page.expect_download() as d:
            link.click()

        download = d.value
        ext = download.suggested_filename.split(".")[-1]
        safe_name = link_text.replace(" ", "_").replace("/", "_")
        filename = f"{safe_name}.{ext}"

        download.save_as(os.path.join(DOWNLOAD_DIR, filename))
        print("Downloaded:", filename)
        
    browser.close()
