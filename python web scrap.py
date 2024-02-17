from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize Chrome WebDriver
driver = webdriver.Chrome()

# Set to keep track of printed comments
printed_comments = set()

try:
    # Iterate over multiple pages
    for page_number in range(1, 12):  # Scraping first 5 pages, adjust as needed
        # Navigate to the webpage
        driver.get(f"https://www.zomato.com/mumbai/ettarra-1-juhu/reviews?page={page_number}")

        # Wait for the review elements to be present
        reviews = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'sc-')]")))
        
        # Loop through each review element
        for review in reviews:
            try:
                # Find <p> elements with class attribute starting with 'sc-1hez2tp-0'
                review_text_elements = review.find_elements(By.XPATH, ".//p[starts-with(@class, 'sc-1hez2tp-0')]")
                
                # Extract text content from each <p> element
                for review_text_element in review_text_elements:
                    review_text = review_text_element.text
                    # Check if the review has more than three words and does not contain 'votes' or 'comments'
                    if len(review_text.split()) > 3 and 'vote' not in review_text.lower() and 'comments' not in review_text.lower():
                        # Check if the comment has not been printed already
                        if review_text not in printed_comments:
                            print(review_text)
                            # Add the comment to the set of printed comments
                            printed_comments.add(review_text)
            except Exception as e:
                print(f"Error while extracting review text: {e}")
except Exception as e:
    print(f"Error while scraping: {e}")

# Close the WebDriver
driver.quit()
