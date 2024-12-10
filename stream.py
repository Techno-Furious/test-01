from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import random
import string
import streamlit as sm

def get_full_page_content(url):
    # Set up the browser
    options = Options()
    options.headless = True  # Enable headless mode
    options.add_argument("--disable-gpu")  # Improves compatibility
    options.add_argument("--no-sandbox")  # Required for running as root in Docker or servers
    options.add_argument("--disable-dev-shm-usage")  # Overcome shared memory issues
    options.add_argument("--window-size=1920,1080")  # Set a default window size
    options.add_argument("--remote-debugging-port=9222")  # Enable remote debugging if needed

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

def generate_random_string(seed: int) -> str:
    """
    Generate a 16-character random string:
    - Starts with letters.
    - Ends with 3 letters (no digits at the end).
    - Contains a maximum of 3 digits, randomly distributed between letters.
    - Based on a provided seed.

    Args:
        seed (int): The seed value to initialize the random generator.

    Returns:
        str: The generated random string.
    """
    random.seed(seed)

    # Define character pools
    letters = string.ascii_lowercase
    digits = string.digits

    # Ensure string starts with 2 letters
    start_letters = random.choices(letters, k=2)

    # Generate up to 3 random digits
    numbers = random.choices(digits, k=3)

    # Generate 8 more letters (to fill middle part)
    middle_letters = random.choices(letters, k=8)

    # Ensure string ends with 3 letters
    end_letters = random.choices(letters, k=3)

    # Combine the letters and numbers
    middle_combined = middle_letters + numbers

    # Shuffle the middle part to distribute numbers randomly
    random.shuffle(middle_combined)

    # Construct the final string
    final_string = start_letters + middle_combined + end_letters

    # Join into a single string
    return ''.join(final_string)



sm.title("Plum Gift URL Checker")
start=sm.number_input("Start Range", min_value=0, value=0)
end=sm.number_input("End Range", min_value=0, value=10)
start_time = time.time()
if sm.button("Process URLs"):
    sm.spinner("Processing URLs...")
    for i in range(start, end+1):
        url = generate_random_string(i)
        sm.write(url)
        
        df = get_full_page_content(url)
        
        sm.subheader("Results")
        # sm.write(df)
        
        sm.write("The page works")
        sm.write("____________________")
    end_time = time.time()
    sm.write("Time taken: ", end_time - start_time)
