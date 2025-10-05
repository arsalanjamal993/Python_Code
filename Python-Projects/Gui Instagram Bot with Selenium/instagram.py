from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import os
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Instagram credentials (use environment variables for security)
USERNAME = os.getenv('INSTAGRAM_USERNAME', 'slaavey90')
PASSWORD = os.getenv('INSTAGRAM_PASSWORD', 'w1o2r3k4')

# List of profiles to message
profile_urls = [
 
"https://www.instagram.com/jeremiasgabriel",
"https://www.instagram.com/stephanylimaoficial",
"https://www.instagram.com/llucassatiro",
"https://www.instagram.com/cilane_dantas",
"https://www.instagram.com/layla.goncallves",
"https://www.instagram.com/todamaeprecisadeoracao",
"https://www.instagram.com/manddantas",
"https://www.instagram.com/barbaratrosal",
"https://www.instagram.com/yagdasales",
"https://www.instagram.com/lyviahenrique",
"https://www.instagram.com/morena_bjs17",
"https://www.instagram.com/malta_nivea",
"https://www.instagram.com/gisele_giiu",
"https://www.instagram.com/suellenmarquess",
"https://www.instagram.com/_ynndycosta99",
"https://www.instagram.com/kamillyoficialll",
"https://www.instagram.com/_anaseabra",
"https://www.instagram.com/anaaperall",
"https://www.instagram.com/adrianobellinazzo",
"https://www.instagram.com/jeanettecastillo01",
"https://www.instagram.com/lucaveros.1",
"https://www.instagram.com/jullyavitoriia_",
"https://www.instagram.com/luanitahh",
"https://www.instagram.com/euugilvaniasantos",
"https://www.instagram.com/sllots_slots",
"https://www.instagram.com/edlacalumby",
"https://www.instagram.com/panteranavoz",
"https://www.instagram.com/xavier_realiza01",
"https://www.instagram.com/wellisonw1",
"https://www.instagram.com/mayaramatias2",
"https://www.instagram.com/eududuslz",
"https://www.instagram.com/xshorr",
"https://www.instagram.com/gabrimartinho",
"https://www.instagram.com/jako.sr",
"https://www.instagram.com/papinhabebeofiicial",
"https://www.instagram.com/teteu77.fv",
"https://www.instagram.com/djravennaa",
"https://www.instagram.com/manusilva.oficiall",
"https://www.instagram.com/thatgirlover500",
"https://www.instagram.com/bregalizaa_",
"https://www.instagram.com/eukauanhenriquee",
"https://www.instagram.com/daaianemeelo",
"https://www.instagram.com/layzasousa__",
"https://www.instagram.com/jaroldstone",
"https://www.instagram.com/bianca_gomes010",
"https://www.instagram.com/rodionlorax"




]

# Message to send (remove non-BMP characters like emojis)
MESSAGE = "Olá a todos, sou Maya, gerente sênior de negócios da plataforma de jogos enoisjogo. Procure blogueiros pagos para trabalhar e que tenham recursos promocionais. Se você estiver interessado, entre em contato comigo para discutir o preço da cooperação em detalhes. Número de contato: +5511958203911"

# Rate limiting settings
MAX_MESSAGES_PER_SESSION = 25  # Number of messages to send before taking a break
DELAY_BETWEEN_MESSAGES = random.uniform(5, 10)  # Reduced delay between messages (in seconds)
BREAK_TIME = 60  # 1-minute break after sending MAX_MESSAGES_PER_SESSION (in seconds)

def create_driver():
    """Create a Chrome WebDriver with some basic anti-detection options."""
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    return webdriver.Chrome(options=options)

def login(driver):
    """Log in to Instagram and handle popups."""
    driver.get("https://www.instagram.com/")
    time.sleep(random.uniform(1, 2))  # Reduced delay
    try:
        username_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "username"))
        )
        password_input = driver.find_element(By.NAME, "password")
        username_input.send_keys(USERNAME)
        password_input.send_keys(PASSWORD)
        
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        
        # Handle possible "Not Now" popups
        for _ in range(2):
            try:
                not_now_btn = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))
                )
                not_now_btn.click()
            except:
                pass
        
        logging.info("✅ Login successful!")
    except Exception as e:
        logging.error(f"❌ Login failed: {e}")
        driver.quit()
        exit()

def close_popups(driver):
    """Closes popups like 'Turn on Notifications' if they appear."""
    try:
        not_now_btn = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))
        )
        not_now_btn.click()
        logging.info("✅ Closed 'Turn on Notifications' popup.")
        time.sleep(random.uniform(0.5, 1))  # Reduced delay
    except:
        logging.info("⚠️ No 'Turn on Notifications' popup detected.")

def check_profile_exists(driver, url):
    """Check if the Instagram profile exists."""
    driver.get(url)
    time.sleep(random.uniform(2, 3))  # Reduced delay
    
    try:
        # Check for the "Sorry, this page isn't available" message
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//h2[contains(text(), 'Sorry, this page isn't available')]"))
        )
        logging.error(f"❌ Profile does not exist: {url}")
        return False
    except:
        logging.info(f"✅ Profile exists: {url}")
        return True

def send_message(driver, message):
    """
    Tries two approaches:
    1. Paste text & press Enter in the message box
    2. Click the 'Send' button if pressing Enter doesn't work
    """
    success = False

    # 1) Find the DM box and press Enter
    try:
        dm_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, 'div[role="textbox"][aria-label="Message"][contenteditable="true"]')
            )
        )
        dm_box.click()
        time.sleep(0.3)  # Reduced delay
        dm_box.send_keys(message)
        time.sleep(0.3)  # Reduced delay
        dm_box.send_keys(Keys.ENTER)
        logging.info("Method 1: Sent by pressing Enter.")
        success = True
    except Exception as e:
        logging.error(f"Method 1 failed: {e}")

    # 2) If Method 1 didn’t work, try clicking the 'Send' button
    if not success:
        try:
            dm_box = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, 'div[role="textbox"][aria-label="Message"][contenteditable="true"]')
                )
            )
            dm_box.click()
            time.sleep(0.3)  # Reduced delay
            
            # Paste text via JS (optional if Method 1 typed nothing)
            driver.execute_script("arguments[0].innerText = arguments[1];", dm_box, message)
            driver.execute_script("arguments[0].dispatchEvent(new Event('input', { bubbles: true }));", dm_box)
            time.sleep(0.5)  # Reduced delay
            
            # Now click the 'Send' button
            send_btn = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@role='button' and text()='Send']"))
            )
            send_btn.click()
            logging.info("Method 2: Sent by clicking the 'Send' button.")
            success = True
        except Exception as e:
            logging.error(f"Method 2 failed: {e}")

    return success

def send_dm_to_profile(driver, url, message):
    """Navigates to the profile, opens DM, closes popups, and sends a message."""
    if not check_profile_exists(driver, url):
        time.sleep(5)  # Wait for 5 seconds before skipping
        logging.info(f"⏭️ Skipping non-existent or private profile: {url}")
        return  # Skip non-existent or private profiles

    try:
        msg_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@role='button' and contains(text(), 'Message')]"))
        )
        msg_btn.click()
        time.sleep(random.uniform(1, 2))  # Reduced delay
        
        # Close the popup if it appears
        close_popups(driver)
        
        # Now send the message
        if send_message(driver, message):
            logging.info(f"✅ Message successfully sent to {url}")
        else:
            logging.error(f"❌ Failed to send message to {url}.")
    
    except Exception as e:
        logging.error(f"❌ Could not open DM for {url}: {e}")
        time.sleep(5)  # Wait for 5 seconds before skipping
        logging.info(f"⏭️ Skipping profile due to error: {url}")

def main():
    driver = create_driver()
    login(driver)

    total_messages_sent = 0

    for profile in profile_urls:
        if total_messages_sent >= 50:  # Stop after sending 50 messages
            break

        send_dm_to_profile(driver, profile, MESSAGE)
        total_messages_sent += 1
        logging.info(f"Total messages sent: {total_messages_sent}")

        # Rate limiting
        if total_messages_sent % MAX_MESSAGES_PER_SESSION == 0:
            logging.info(f"Taking a break for {BREAK_TIME // 60} minute(s)...")
            time.sleep(BREAK_TIME)
        else:
            time.sleep(DELAY_BETWEEN_MESSAGES)
    
    driver.quit()
    logging.info("✅ All done!")

if __name__ == "__main__":
    main()
