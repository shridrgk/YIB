import inspect
import logging
import time
import pytest
import requests
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

from pageObjects.DiPage import DiPage
from pageObjects.UspPage import UspPage
from pageObjects.WorkSpacePage import WorkSpacePage


@pytest.mark.usefixtures("setup")
class BaseClass:
    def login(self,username,password):
        workSpacePage = WorkSpacePage(self.driver)
        element = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,"input[id='gigya-loginID-77152811960799260']")))
        element.send_keys(username)

        workSpacePage.getLogin().click()

        element1 = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[data-gigya-placeholder="Password"]')))
        element1.send_keys(password)

        workSpacePage.getLogin().click()

        Token = self.getToken()
        EnterToken = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[class="gig-tfa-code-textbox"]')))
        EnterToken.send_keys(Token)

        workSpacePage.GetSubmitBtn().click()
        time.sleep(15)
    def getToken(self):
        # host = "http://api.testdataservices.com.au/v0001F_GetGoogleAuthCode"
        # headers = {
        #     "content-type": "application/json",
        #     'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICI0R1RJWWRrb01LbXRWODRRWlRFNTJBQlg5cHpiYWRxX1RrNDBDM05naFpvIn0.eyJleHAiOjE3MDI0MTQyMjIsImlhdCI6MTcwMjQxMjQyMiwiYXV0aF90aW1lIjoxNzAyNDA4ODczLCJqdGkiOiI2Mzc5NzMxMy1mZDJiLTQ1NGUtODViMy01YTI1YTg3Njg1OGIiLCJpc3MiOiJodHRwczovL2FwaS5tc2EyLmFwcHMueW9rb2dhd2EuYnVpbGQvaWRwdC1hdXRoei9hdXRoL3JlYWxtcy9ZSUJQT0MiLCJhdWQiOlsieWlic3VpdGUtdWktcWEiLCJhY2NvdW50Il0sInN1YiI6ImQ2NjNmYjg5LTk3NmItNDQ3Ni05YjUwLTA5OGJjZDZjOWI5NSIsInR5cCI6IkJlYXJlciIsImF6cCI6InlpYnN1aXRlLXVpLXFhIiwibm9uY2UiOiJiWGxOVlVacFkyUktRamRWVEZOTlpHTnFVMWwwYWxSMVlVNDVUWFl1UkUxMmFUVnlUamhtZDE5a2JtUXoiLCJzZXNzaW9uX3N0YXRlIjoiYmVjYzdjMGItM2VkZS00ZmM5LWEzZjEtZjI5NWNlOGY2MGExIiwiYWNyIjoiMSIsImFsbG93ZWQtb3JpZ2lucyI6WyJodHRwczovL2Nsb3VkLm1zYTIuYXBwcy55b2tvZ2F3YS5idWlsZCIsImh0dHBzOi8vY2xvdWQubXNhMi5hcHBzLnlva29nYXdhLmJ1aWxkL2FwcC15aWItaG9zdC95aWJwb2MvKiIsImh0dHA6Ly9sb2NhbGhvc3Q6NDIwMCIsImh0dHBzOi8vY2xvdWQubXNhMi5hcHBzLnlva29nYXdhLmJ1aWxkL2FwcC15aWItaG9zdC1xYS95aWJwb2MvKiJdLCJyZWFsbV9hY2Nlc3MiOnsicm9sZXMiOlsiU2NpZW50aWZpYyBNYW5hZ2VyIiwiRGF0YSBTY2llbnRpc3QiLCJvZmZsaW5lX2FjY2VzcyIsIlN1cGVyIEFkbWluIiwidW1hX2F1dGhvcml6YXRpb24iLCJkZWZhdWx0LXJvbGVzLXlpYnBvYyIsIlNjaWVudGlzdCBQRCJdfSwicmVzb3VyY2VfYWNjZXNzIjp7ImFjY291bnQiOnsicm9sZXMiOlsibWFuYWdlLWFjY291bnQiLCJtYW5hZ2UtYWNjb3VudC1saW5rcyIsInZpZXctcHJvZmlsZSJdfX0sInNjb3BlIjoib3BlbmlkIGVtYWlsIGF1ZC15aWJzdWl0ZS11aS1xYSBwcm9maWxlIiwic2lkIjoiYmVjYzdjMGItM2VkZS00ZmM5LWEzZjEtZjI5NWNlOGY2MGExIiwiZW1haWxfdmVyaWZpZWQiOmZhbHNlLCJuYW1lIjoic2hyaWRoYXJhIHJhbWFzd2FteSIsInByZWZlcnJlZF91c2VybmFtZSI6ImNiMjIyYzYxOTJjZjQ4MTQ4ZjA2ZThlNjZhNzJkNjc0IiwiZ2l2ZW5fbmFtZSI6InNocmlkaGFyYSIsImZhbWlseV9uYW1lIjoicmFtYXN3YW15IiwiZW1haWwiOiJzaHJpZGhhcmEucmFtYXN3YW15QHlva29nYXdhLmNvbSJ9.a02lvspi2tV9RwiZ5ooYp98M6VS50_fowYhSVld2yk12jQO_Gz4ywpfXDjNqF2BOBjA3ZBmtokq43wT_bKMgDms9FCsSpYAGjY9PSQ-dkDS4LuKcoSqFsHfYx6zR8HSiGigBwMliIgXRu3wDpD5YSKE_W8Qg3JhGiq4ceirnCcCvkU-uwR3YJGit0qiMCglRNsIyy_kgak1S5QcyCqVzQLvfJd_sqF-6-xuVm7KhwN2L_10elxb9jC8vFhq08fTuOYHgIMPSB4D5dkjLMhwR0p05jcOuWvONKNQ_EVBHUD77CPryBFQrEkDaeC7x24KKu2KcASNCTk5kPzHrIR_WHg'
        # }
        # response = requests.get(host, {'Email': 'shridhara.ramaswamy@yokogawa.com','SecretKey':'QEHCNXXUA7Y76BDPEZ4PBESBE5FQ3CEO','SubscriptionKey':'bksLG5nuZEeyrQr9AttIw474WbyNrsRP'},headers=headers,verify=False)
        # data = response.json()
        # assert response.status_code == 200
        # if data['SecondsRemaining'] < 5:
        #     return data['ThisToken']
        # else:
        #     return data['NextToken']
        import json

        import pyotp
        import time

        # Replace with your own secret key
        secret = 'RBZ7ZCXKDTD3BPP5ETCBVOEKZL5YWWJP'

        # Create a TOTP object
        totp = pyotp.TOTP(secret)
        # Print the current OTP
        print("Current OTP:", totp.now())

        return totp.now()
        # Optionally, you can loop to print OTPs every 30 seconds
        # while True:
        #     print("Current OTP:", totp.now())
        #     time.sleep(30)

    def WorkspceFilter(self,WsName):
        workSpacePage = WorkSpacePage(self.driver)
        self.driver.refresh()
        time.sleep(5)
        workSpacePage.GetSideNavWSpace().click()
        workSpacePage.GetWspaceNameFltr().click()
        workSpacePage.GetFilterSearBox().send_keys(WsName)
        workSpacePage.GetFilterApplyBtn().click()
        time.sleep(2)
        action = ActionChains(self.driver)
        action.move_to_element(workSpacePage.GetSelectWspace()).click().perform()
        time.sleep(2)

    def DIFilter(self,DiName):
        diPage = DiPage(self.driver)
        workSpacePage = WorkSpacePage(self.driver)

        diPage.GetDiGridNameFilter().click()
        diPage.GetFilterSearBox().send_keys(DiName)
        diPage.GetFilterApplyBtn().click()
        time.sleep(2)
        action = ActionChains(self.driver)
        action.move_to_element(diPage.GetSelectDI()).click().perform()
        time.sleep(2)

    def UspFilter(self, UspName):
        uspPage = UspPage(self.driver)
        workSpacePage = WorkSpacePage(self.driver)

        uspPage.GetUspListGridNameFilter().click()
        uspPage.GetFilterSearBox().send_keys(UspName)
        uspPage.GetFilterApplyBtn().click()
        time.sleep(2)
        action = ActionChains(self.driver)
        action.move_to_element(uspPage.GetSelectUSP()).click().perform()
        time.sleep(2)

    def UspEditFilter(self, UspName):
        uspPage = UspPage(self.driver)
        workSpacePage = WorkSpacePage(self.driver)

        uspPage.GetUspListGridNameFilter().click()
        uspPage.GetFilterSearBox().send_keys(UspName)
        uspPage.GetFilterApplyBtn().click()
        time.sleep(2)
        action = ActionChains(self.driver)
        action.move_to_element(uspPage.GetUspListGridEditBtn()).click().perform()
        time.sleep(2)
    def TempFilter(self,TempName):
        diPage = DiPage(self.driver)
        workSpacePage = WorkSpacePage(self.driver)

        diPage.GetDiMatchingTempNameFilter().click()
        time.sleep(1)
        diPage.GetFilterSearBox().send_keys(TempName)
        diPage.GetFilterApplyBtn().click()
        time.sleep(2)
        diPage.GetSelectTemplate().click()
        time.sleep(2)
    def UploadDiStageFile(self,FilePath,FileName):

        diPage = DiPage(self.driver)
        diPage.GetDiStageUploaderFile().send_keys(FilePath + "\\" + FileName)
        time.sleep(1)
        diPage.GetDiStageUploaderBtn().click()
        time.sleep(1)
        assert ("Successfully uploaded " in diPage.GetDistageuploadToast().text)
        time.sleep(1)

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('Logs/logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger


    #
    # def verifyLinkPresence(self, text):
    #     element = WebDriverWait(self.driver, 10).until(
    #     EC.presence_of_element_located((By.LINK_TEXT, text)))
    #
    # def selectOptionByText(self,locator,text):
    #     sel = Select(locator)
    #     sel.select_by_visible_text(text)

