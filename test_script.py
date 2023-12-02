from seleniumbase import Driver

driver = Driver(undetectable=True)

try:
    driver.get("https:nowsecure.nl/#relax")
    driver.sleep(4)
finally:
    driver.quit()

