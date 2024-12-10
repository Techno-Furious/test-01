from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time


def get_full_page_content(url):
    # Set up the browser
    options = Options()
    options.headless = True  # Enable headless mode
    options.add_argument("--disable-gpu")  # Optional, for better compatibility
    options.add_argument("--no-sandbox")  # Recommended for Docker environments
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # Open a URL
    driver.get(url)

    # # Execute JavaScript to manipulate or render the page
    # js_script = """
    # document.body.innerHTML = '<h1>This is simulated rendering</h1>';
    # return document.body.innerHTML;
    # """
    # rendered_content = driver.execute_script(js_script)
    # print(rendered_content)
    time.sleep(1)
    driver.implicitly_wait(10)
    # Extract the rendered HTML content
    rendered_page_content = driver.page_source

    # Print or process the content
     
    with open("out.html", "w") as f:
        f.write(rendered_page_content)

    driver.quit()

    return (rendered_page_content)

