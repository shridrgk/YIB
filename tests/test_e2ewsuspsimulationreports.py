import time

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from TestData.workspacedata import workspacedata
from pageObjects.AssetPage import AssetPage
from pageObjects.DiPage import DiPage
from pageObjects.UspPage import UspPage
from pageObjects.WorkSpacePage import WorkSpacePage

from utilities.BaseClass import BaseClass


class TestWorkspaceAssetSuite(BaseClass):

    def test_Run_Simulation_Report_Validation(self, getData):
        log = self.getLogger()
        workSpacePage = WorkSpacePage(self.driver)
        uspPage = UspPage(self.driver)
        self.login(getData["UserName"], getData["Password"])
        log.info("Login successfully")
        self.WorkspceFilter("Data")
        log.info("Workspace Landing page is displayed")
        uspPage.GetWsUspLandingPage().click()
        time.sleep(1)
        assert ("Digital Twin - USP" in uspPage.GetUspLandingPageTitle().text)
        log.info("USP landing page is displayed")
        self.UspFilter(getData["UspName"])
        log.info("Use Cases Landing page is displayed")
        assert(getData["UspName"] in uspPage.GetUseCaseListPageTitle().text)
        uspPage.GetUseCaseListNameFilter().click()
        uspPage.GetFilterSearBox().send_keys(getData["UseCaseName"])
        uspPage.GetFilterApplyBtn().click()

        action = ActionChains(self.driver)
        action.move_to_element(uspPage.GetSelectUC()).click().perform()
        time.sleep(1)
        assert (getData["UseCaseName"] in uspPage.GetUseCaseReactorList().text)
        element = WebDriverWait(self.driver, 30).until(
        EC.element_to_be_clickable((uspPage.GetRunSimulationMsgBtn())))
        time.sleep(5)
        element.click()
        assert("Messages" in uspPage.GetMsgBarTitle().text)
        assert ("Run Simulation Started" in uspPage.GetMsgContentP1().text)
        assert ("Run Simulation Completed" in uspPage.GetMsgContentP2().text)
        uspPage.GetMsgBarCloseBtn().click()
        time.sleep(1)
        uspPage.GetRunSimulationReportsBtn().click()
        time.sleep(2)
        assert("Reports" in uspPage.GetReportPageTitle().text)
        assert("Biomass" in uspPage.GetBioMassPlotTitile().text)
        assert("Product", uspPage.GetProductPlotTitile().text)







    @pytest.fixture(params=workspacedata.getTestData("test_workspace_title_check"))
    def getData(self, request):
        return request.param