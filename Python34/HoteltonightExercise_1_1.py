# Exercise for Hoteltonight.com 1.1
# Opens a browser and does some verifications (text and links) on hoteltoight.com

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#function to print results of a test
def print_result(test,passed,failed):
    print('\n-Testing Results for '+str(test)+'-')
    print('Tests passed:',passed)
    print('Tests failed:',failed)

#function to compare the actual result(ares) of the test to the expected result(eres) and return a pass or fail
def compair_result(ares,eres):
    if ares != eres:
        print('Test FAILED :(')
        print('Actual result: ',ares,'\n')
        result = "fail"
        
    else:
        print('Test passed! :)\n')
        result = "pass"
        
    return result

#function to return the actual result(ares)  of the test by type of test
def actualresult(test_element, test_type, driver):
    if test_type == "text":
        try:
            elem = driver.find_element_by_xpath(test_element)
            ares = elem.text
        except:
            ares = 'Attemt access xpath failed'
        
    elif test_type == "link":
        try:
            elem = driver.find_element_by_xpath(test_element).click()
            ares = driver.current_url
        except:
            ares = 'Attemt access xpath failed'

    else:
        print('Test type not found.')

    return ares    

#function to iterate tests on data set based on test case number, a test data set, and the type of test being run
def runtests(testcasenum,testdata,testdata_type):
    
    #Open web browser
    driver = webdriver.Firefox()
    driver.set_window_size(1280,800)

    #Loop through each page and verify the text of elements vs. the expected result
    i=0
    passed = 0
    failed = 0

    for item in testdata:
        print ('Running test cases '+str(testcasenum)+'.'+str(i))
        print ('Testing URL: ',testdata[i][0],'\n')

        driver.get(testdata[i][0])

        ii = 0
        for item in testdata[i][1]:
            expresult = testdata[i][2][ii]
            xpath = testdata[i][1][ii]
            testcase = str(testcasenum)+'.'+str(i)+'.'+str(ii)

            print ('Running test case ',testcase)
            print ('Element xpath to be tested: ',xpath)
            print ('Expected result: ',expresult)

            actresult = actualresult(test_element = xpath, test_type = testdata_type, driver = driver)

            test_result = compair_result(ares = actresult,eres = expresult)

            if test_result == "pass":
                passed += 1
            else:
                failed += 1

            ii += 1
        i += 1

    #Print test results summary
    print_result(test = str(testcasenum)+'.0',passed = passed,failed = failed)

    #Close browser
    driver.quit()

    return passed, failed

# Main

totalpassed = 0
totalfailed = 0


##################################
##### TEST CASE 1.0.0 
##### Verify the text is correct
##################################

# Testdata tuple [url to be tested,[xpath to elements to test],[expected results]]
testdata_text = (
            ['https://www.hoteltonight.com/',
            ['//*[@id="value_prop"]/h3',
             '//*[@id="insetcity"]/li[17]'],
            ['Hotels give us their unsold rooms. We show you the day\'s best values. You book them easily and securely on your smartphone.',
             'San Diego']
            ],
            ['https://www.hoteltonight.com/about',
            ['//*[@id="about"]/div/h2',
             '//*[@id="col_l"]/h1',
             '//*[@id="founders"]/hgroup/h2'],
            ['HotelTonight was founded in December 2010 to provide easy mobile booking of same-day unsold hotel inventory.',
             'Sam Shank',
             'FAILURE CASE',
             'Jared Simon']
            ]
            )

testdata_text_passed, testdata_text_failed = runtests(testcasenum = 1, testdata = testdata_text, testdata_type = 'text')

totalpassed += testdata_text_passed
totalfailed += testdata_text_failed

##################################
##### TEST CASE 2.0.0 
##### Verify the links go to the correct URL
##################################

# Testdata tuple [url to be tested,[xpath to elements to test],[expected results]]
testdata_link = (
            ['https://www.hoteltonight.com/press',
            ['/html/body/div[2]/div[1]/div[1]',
             '//*[@id="inse]'],
            ['https://www.hoteltonight.com/',
             'FAILURE CASE']
            ],
            ['https://www.hoteltonight.com/support',
            ['/html/body/div[2]/div[1]/div[3]/p',
             '//*[@id="footer_nav"]/ul/li[1]/a'],
            ['https://www.hoteltonight.com/hotel_partners',
             'https://www.hoteltonight.com/jobs']
            ],
            ['https://www.hoteltonight.com/',
            ['//*[@id="apple_b"]',
             '//*[@id="footer_nav"]/ul/li[5]/a'],
            ['https://itunes.apple.com/us/app/hotel-tonight/id407690035?mt=8',
             'FAILURE CASE']
            ]
            )

# Run test cases 2.0 
testdata_text_passed, testdata_text_failed = runtests(testcasenum = 2, testdata = testdata_link, testdata_type = 'link')

totalpassed += testdata_text_passed
totalfailed += testdata_text_failed

##################################
##### END OF TESTING
##################################

#Summary of all testing
print('-------------------------')
print_result(test = 'Summary Report', passed = totalpassed, failed = totalfailed)

input("\n\nPress the enter key to exit.")
