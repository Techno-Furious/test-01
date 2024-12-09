from flask import Flask, render_template, request
import random
import string
from scrap import get_full_page_content
import time

app = Flask(__name__)

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

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        start_range = int(request.form['start_range'])
        end_range = int(request.form['end_range'])
        
        results = []
        t1 = time.time()
        
        for i in range(start_range, end_range + 1):
            seed_value = i
            random_string = generate_random_string(seed_value)
            base = "https://plum.gift/"
            url = base + random_string
            
            if (i == 795):
                url = "https://plum.gift/LH9gA2RznaVOsWMK"
                
            result = get_full_page_content(url)
            works = str(result).find("cancelled") == -1
            
            results.append({
                'url': url,
                'works': works
            })
            
            if works:
                with open('works.txt', 'a') as f:
                    f.write(url + '\n')
        
        t2 = time.time()
        time_taken = t2 - t1
        
        return render_template('results.html', results=results, time_taken=time_taken)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)