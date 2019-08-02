from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import js2py



browser=webdriver.Chrome(executable_path=r'/home/sekhar/Downloads/chromedriver')

browser.get('http://localhost:3000/login')
time.sleep(1)
browser.find_element_by_name('username').click()
browser.find_element_by_name('username').clear()
browser.find_element_by_name('username').send_keys('admin')
browser.find_element_by_name('password').click()
browser.find_element_by_name('password').clear()
browser.find_element_by_name('password').send_keys('admin@123')
btn_xpath_='//*[@id="login-view"]/form/div[3]/button'
browser.find_element(By.XPATH, btn_xpath_).click()
time.sleep(2)
'''
dash_board_xpath='//*[@id="panel-3"]/div/div/div/plugin-component/panel-plugin-dashlist/grafana-panel/div/div[2]/ng-transclude/div/div[2]/div/div/a'
browser.find_element(By.XPATH, dash_board_xpath).click()

side_xpath='/html/body/grafana-app/sidemenu/div[2]/div[2]/a'
browser.find_element(By.XPATH, side_xpath).click()
manage_xpath='/html/body/grafana-app/sidemenu/div[2]/div[2]/ul/li[4]/a'
browser.find_element(By.XPATH, manage_xpath).click()

dash_xpath='/html/body/grafana-app/div/div/div/div/manage-dashboards/div/div[5]/div[2]/dashboard-search-results/div/div[3]/a/span[2]/div'

browser.find_element(By.XPATH, dash_xpath).click()
'''

ur='http://localhost:3000/d/HB4wyDDWk/koushik?orgId=1'
browser.get(ur)
time.sleep(3)
time_btn_xpath='/html/body/grafana-app/div/div/div/react-container/div/div[1]/div[5]/div[1]/gf-time-picker/button[1]'
browser.find_element(By.XPATH, time_btn_xpath).click()
start_xpath='/html/body/grafana-app/div/div/div/react-container/div/div[1]/div[5]/div[1]/gf-time-picker/div/div[2]/form/div[1]/div[1]/input'
end_xpath='/html/body/grafana-app/div/div/div/react-container/div/div[1]/div[5]/div[1]/gf-time-picker/div/div[2]/form/div[2]/div[1]/input'
time.sleep(1)
browser.find_element(By.XPATH, start_xpath).click()
browser.find_element(By.XPATH, start_xpath).clear()
browser.find_element(By.XPATH, start_xpath).send_keys("now")
time.sleep(2)

browser.find_element(By.XPATH, end_xpath).click()
browser.find_element(By.XPATH, end_xpath).clear()
browser.find_element(By.XPATH, end_xpath).send_keys("now-4M")
time.sleep(1)

btn_xpath='/html/body/grafana-app/div/div/div/react-container/div/div[1]/div[5]/div[1]/gf-time-picker/div/div[2]/form/div[3]/div/button'
browser.find_element(By.XPATH, btn_xpath).click()

time.sleep(4)
browser.find_element(By.XPATH, time_btn_xpath).click()
browser.find_element(By.XPATH, start_xpath).click()
browser.find_element(By.XPATH, start_xpath).clear()
browser.find_element(By.XPATH, start_xpath).send_keys("now-47M")
time.sleep(2)

browser.find_element(By.XPATH, end_xpath).click()
browser.find_element(By.XPATH, end_xpath).clear()
browser.find_element(By.XPATH, end_xpath).send_keys("now-46M")

time.sleep(2)

btn_xpath='/html/body/grafana-app/div/div/div/react-container/div/div[1]/div[5]/div[1]/gf-time-picker/div/div[2]/form/div[3]/div/button'
browser.find_element(By.XPATH, btn_xpath).click()

time.sleep(5)

containers = browser.find_elements_by_xpath('//*[@id="panel-2"]/div/div/div/plugin-component/panel-plugin-graph/grafana-panel/div/div[2]/ng-transclude/div/div[2]/div/div[1]/div')

for items in containers:
    print(items)
    name = items.find_element_by_xpath('.//div[@class="graph-legend-value min"]')
    name1 = items.find_element_by_xpath('.//div[@class="graph-legend-value avg"]')
    name2 = items.find_element_by_xpath('.//div[@class="graph-legend-value total"]')
    print(name.text)
    print(name1.text)
    print(name2.text)
    
containers = browser.find_elements_by_xpath('//*[@id="panel-2"]/div/div/div/plugin-component/panel-plugin-graph/grafana-panel/div/div[2]/ng-transclude/div/div[2]/div/div[1]/div')

for items in containers:
    print(items)
    name = items.find_element_by_xpath('.//div[@class="graph-legend-value min"]')
    name1 = items.find_element_by_xpath('.//div[@class="graph-legend-value avg"]')
    name2 = items.find_element_by_xpath('.//div[@class="graph-legend-value total"]')
    print(name.text)
    print(name1.text)
    print(name2.text)
    
time.sleep(20)
browser.close()
