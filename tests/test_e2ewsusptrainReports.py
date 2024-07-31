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

    def test_Run_Train_Report_Validation(self, getData):
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
        uspPage.GetUspListGridNameFilter().click()
        uspPage.GetFilterSearBox().send_keys(getData["UspName"])
        uspPage.GetFilterApplyBtn().click()
        time.sleep(2)
        assert ("COMPLETED" in uspPage.GetUspTrainStatus().text)
        action = ActionChains(self.driver)
        action.move_to_element(uspPage.GetUspListGridEditBtn()).click().perform()
        time.sleep(2)

        uspPage.GetUspTrainNextBtn().click()
        time.sleep(1)
        uspPage.GetUspConfigOutflux().click()
        time.sleep(2)
        uspPage.GetUspTrainNextBtn().click()
        time.sleep(1)
        uspPage.GetUspTrainNextBtn().click()
        time.sleep(2)
        self.driver.refresh()
        time.sleep(3)
        assert ("Cells" in uspPage.GetUspTrainGridCells().text)
        assert ("Cultivations" in uspPage.GetUspTrainGridCultivation().text)
        assert ("Notes" in uspPage.GetUspTrainGridNotes().text)
        assert ("Include" in uspPage.GetUspTrainGridIncude().text)
        assert("Run Training" in uspPage.GetUspRunTrainBtn().text)


        time.sleep(1)
        uspPage.GetUspTrainReportBtn().click()
        time.sleep(2)
        assert("Metrics" in uspPage.GetUspTrainReportMetricsTitle().text)
        assert ("Reports" in uspPage.GetUspTrainReportPlotTitle().text)
        assert ("Train Data" in uspPage.GetUspMetricsReportGridTrainData().text)
        assert ("Test Data" in uspPage.GetUspMetricsReportGridTestData().text)

















    @pytest.fixture(params=workspacedata.getTestData("test_workspace_title_check"))
    def getData(self, request):
        return request.param