from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scraper(url, page):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-logging')
    options.add_argument('--log-level=3')
    options.add_argument('--silent')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    
    driver = webdriver.Edge(options=options)
    results = []
    try:
        driver.get(f"{url}/{page}")
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "content__inner")))
        lotto_boxes = driver.find_elements(By.CLASS_NAME, "archive--lotto")
        
        for lotto_box in lotto_boxes:
            lotto_body = lotto_box.find_element(By.CLASS_NAME, "archive--lotto__body")
            
            date_element = lotto_body.find_element(By.CLASS_NAME, "archive--lotto__date")
            date_str = date_element.get_attribute('datetime')
            
            title = lotto_body.find_element(By.CLASS_NAME, "archive--lotto__head-lot").text.strip()
            
            result_list = lotto_body.find_elements(By.CLASS_NAME, "archive--lotto__result-list")[0]
            result_items = result_list.find_elements(By.TAG_NAME, "li")
            
            lottery_data = {
                "date": date_str,
                "title": title,
                "first_prize": None,
                "front_three": [],
                "back_three": [],
                "back_two": None
            }
            
            for item in result_items:
                result_type = item.find_element(By.CLASS_NAME, "archive--lotto__result-txt").text.strip()
                numbers = item.find_element(By.CLASS_NAME, "archive--lotto__result-number")
                
                if "รางวัลที่ 1" in result_type:
                    lottery_data["first_prize"] = numbers.text.strip()
                elif "เลขหน้า 3 ตัว" in result_type:
                    spans = numbers.find_elements(By.TAG_NAME, "span")
                    lottery_data["front_three"] = [span.text.strip() for span in spans]
                elif "เลขท้าย 3 ตัว" in result_type:
                    spans = numbers.find_elements(By.TAG_NAME, "span")
                    lottery_data["back_three"] = [span.text.strip() for span in spans]
                elif "เลขท้าย 2 ตัว" in result_type:
                    lottery_data["back_two"] = numbers.text.strip()
            
            results.append(lottery_data)
    except Exception as e:
        print(f"Error occurred: {e}")
    
    driver.quit()
    return results

    

