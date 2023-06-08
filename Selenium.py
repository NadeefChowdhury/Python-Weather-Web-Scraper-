
import os
from selenium import webdriver



os.environ['PATH'] += r"H:/selenium" 
driver = webdriver.Chrome()

print('')
print('****   NADEEF WEATHER NETWORK   ****')
print('')
print('Enter the name of your division: ')
print('')

division = input()
print('')
divisions = {'dhaka':'1', 'chattogram':'4','sylhet':'7','mymensingh':'18','rajshahi':'77', 'rangpur':'82', 'khulna':'88', 'barishal':'94'}
search = 'http://live4.bmd.gov.bd/map/' + divisions[division.lower()] + '/'
driver.get(search)


element = driver.find_element('class name', 'big').text
clean_element = element.replace('\n', ' ')

temperature = clean_element[:26].replace(' oC ', ' ')
print('Temperature: ' +temperature)

sun = clean_element[39:].replace('AM ', 'AM | ')
print(sun)

print('')


element1 = driver.find_element('class name', 'small').text
clean_element1 = element1.replace('\n', ' | ')
clean_element1

print(clean_element1)
