#
#
# def name(page_link):
#
#     match = re.search('^https://subscription\.packtpub\.com/video/[a-z]*/[0-9]*/\w*/video([0-9]*)_([0-9]*)/([\w-]*)$',page_link,re.I)
#
#     if match:
#         sec = match.group(1)
#         no = match.group(2)
#         title = match.group(3).replace('-', ' ')
#
#         name = f"{sec}.{no} {title}"
#
#         print(name)
#         return name
#
#     return None
# try:
#     chrome.get("https://subscription.packtpub.com/login")
#
#     username_ele = chrome.find_element(By.CSS_SELECTOR, locators.LOGIN.USERNAME_LOCATOR)
#     password_ele = chrome.find_element(By.CSS_SELECTOR, locators.LOGIN.PASSWORD_LOCATOR)
#     submit_ele = chrome.find_element(By.CSS_SELECTOR, locators.LOGIN.SIGNIN_LOCATOR)
#
#     username_ele.send_keys(details.LOGIN.USERNAME)
#     password_ele.send_keys(details.LOGIN.PASSWORD)
#     submit_ele.click()
#
#     time.sleep(10)
#     chrome.get("https://subscription.packtpub.com/video/programming/9781839217289/p1/video1_1/welcome-to-this-course")
#     WebDriverWait(chrome, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, locators.SECTION.LOCATOR)))
#     all_sections = chrome.find_elements(By.CSS_SELECTOR, locators.SECTION.LOCATOR)
#     all_sections_with_pages = [sec.find_elements(By.CSS_SELECTOR, locators.WEBPAGE.LOCATOR) for sec in all_sections]
#
#     pages_sec_sections = [[page.get_attribute("href") for page in sec] for sec in all_sections_with_pages]
#
#     for i, sec in enumerate(pages_sec_sections):
#         print(f"Section {i + 1} : ")
#
#         for j, page_link in enumerate(sec):
#             time.sleep(1)
#             print(f"{i + 1}.{j + 1} {page_link}")
#             chrome.maximize_window()
#             chrome.get(page_link)
#
#             WebDriverWait(chrome, 20).until(
#                 EC.element_attribute_to_include((By.CSS_SELECTOR, locators.VIDEO.VIDEO), 'src'))
#             video = chrome.find_element(By.CSS_SELECTOR, locators.VIDEO.VIDEO)
#             video_src = video.get_attribute('src')
#
#             chrome.get(video_src)
#             time.sleep(10)
#             pyautogui.moveTo(1000, 600)
#             # pyautogui.click(button='right')
#             # time.sleep(1)
#             #
#             # pyautogui.press('down')
#             # pyautogui.press('down')
#             # pyautogui.press('down')
#             # pyautogui.press('down')
#             # time.sleep(1)
#             # pyautogui.press('enter')
#             # time.sleep(5)
#             with pyautogui.hold('ctrl'):
#                 pyautogui.press('s')
#
#             time.sleep(3)
#             title = name(page_link)
#             if title:
#                 pyautogui.write(title)
#             time.sleep(1)
#             pyautogui.press('enter')
#             time.sleep(1)
#             pyautogui.press('left')
#             pyautogui.press('enter')
#             break
#
# except Exception as e:
#     print(e)
#     chrome.get("https://subscription.packtpub.com/logout")
#     time.sleep(5)
#     chrome.close()
#
# finally:
#     time.sleep(30)
#     chrome.get("https://subscription.packtpub.com/logout")
#     chrome.close()
#
# # for sec in enumerate(all_sections_with_pages):
# #     print(f"Section {i+1}:")
# #     page_in_section = [page.get_attribute("href") for page in sec]
# #
# #     # for j , page in enumerate(sec):
# # print(page)
# # page_link = page.get_attribute("href")
# # sec.append(page_link)
# # print(f'Page {j+1}. {page_link}')
# # chrome.get(page_link)
# # chrome.maximize_window()
# # print(pyautogui.size())
# # time.sleep(5)
# # pyautogui.moveTo(1000,600)
# # pyautogui.click(button='right')
# # # break
# #
# # # video_ele = chrome.find_element(By.CSS_SELECTOR,locators.VIDEO.LOCATOR)
# # # vid = ActionChains(chrome)
# # # vid.context_click(video_ele).perform()
# # pyautogui.press('down')
# # time.sleep(2)
# # pyautogui.press('down')
# # time.sleep(2)
# # pyautogui.press('down')
# # time.sleep(2)
# # pyautogui.press('down')
# # time.sleep(2)
# # pyautogui.press('enter')
# # time.sleep(2)
# # pyautogui.press('enter')
import time

from Packt import Packt

course_link = 'https://subscription.packtpub.com/video/programming/9781800564084/p1/video1_1/section-overview'

cpp_course = Packt(course_link)
# n = cpp_course.name('https://subscription.packtpub.com/video/programming/9781800564084/p1/video1_3/getting-started-on-macos-or-linux-with-codeblocks-ide')

cpp_course.login()
# cpp_course.download('https://subscription.packtpub.com/video/programming/9781800564084/p1/video1_3/getting-started-on-macos-or-linux-with-codeblocks-ide')
pages_in_section = cpp_course.get_pages_link_section_wise()

for i , section in enumerate(pages_in_section):
    print(f"Section {i+1}")

    for j , page in enumerate(section):

        print(f"{i+1}.{j+1} {page}")
        cpp_course.download(page)


cpp_course.logout()