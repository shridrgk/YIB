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
from pageObjects.UcPage import UcPage
from pageObjects.WorkSpacePage import WorkSpacePage

from utilities.BaseClass import BaseClass


class TestWorkspaceAssetSuite(BaseClass):


    def test_UseCase_Optimization_Report_Page(self, getData):
        log = self.getLogger()
        workSpacePage = WorkSpacePage(self.driver)
        uspPage = UspPage(self.driver)
        ucPage = UcPage(self.driver)
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
        uspPage.GetFilterSearBox().send_keys(getData["OptUseCaseName"])
        uspPage.GetFilterApplyBtn().click()

        action = ActionChains(self.driver)
        action.move_to_element(uspPage.GetSelectUC()).click().perform()
        time.sleep(2)
        ucPage.GetOptUcNextBtn().click()
        time.sleep(2)
        ucPage.GetOptPerformObectiveNextBtn().click()
        time.sleep(1)
        assert ("Objective Function" in ucPage.GetOptUcStepperStage2().text)
        assert ("Aggregation" in ucPage.GetOptAggregation().text)
        ucPage.GetOptAggregateMethodDropdown().click()
        time.sleep(1)
        ucPage.GetOptAggregateMethodSum().click()
        time.sleep(1)
        ucPage.GetOptPONextBtn().click()
        time.sleep(1)
        assert("USP_group_workshop" in ucPage.GetOptDesignSpaceRGroup().text)
        time.sleep(2)
        assert("cultivation1" in ucPage.GetOptDesignSpaceRVessel().text)
        time.sleep(7)
        ucPage.GetOptSummaryNextBtn().click()
        time.sleep(2)
        assert ("Execute" in ucPage.GetOptUcStepperStage4().text)
        time.sleep(1)
        assert ("Bioprocess Specification Name" in ucPage.GetOptSummaryBioProceessName().text)
        assert ("Group" in ucPage.GetOptSummaryGroup().text)
        assert ("Status" in ucPage.GetOptSummaryStatus().text)
        assert ("Optimization Ready" in ucPage.GetOptSummaryGetStatus().text)
        time.sleep(1)
        element = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((ucPage.GetOptReportsBtn())))
        time.sleep(5)
        element.click()
        time.sleep(2)
        assert ("Reports" in ucPage.GetOptReportsTtitle().text)
        assert ("Trajectories" in ucPage.GetOptReportsTrajectories().text)
        assert ("Feed Volume" in ucPage.GetOptReportsFeedVol().text)
        assert ("Media Composition" in ucPage.GetOptReportsMediaComp().text)
        assert ("Optimized Objective" in ucPage.GetOptReportsOptObjective().text)

        ucPage.GetOptReportsTrajectoriesTab().click()
        time.sleep(2)
        ucPage.GetOptReportsFeedVolTab().click()
        time.sleep(2)
        ucPage.GetOptReportsMediaCompTab().click()
        time.sleep(2)
        ucPage.GetOptReportsOptObjectiveTab().click()
        time.sleep(2)


        ucPage.GetOptReportsTrajectoriesTab().click()
        time.sleep(2)

        assert ("USP_group_workshop - cultivation1 - Biomass" in ucPage.GetOptReportsTrajectoriesBioMass().text)
        assert ("USP_group_workshop - cultivation1 - L-Alanine" in ucPage.GetOptReportsTrajectoriesProduct().text)

        ucPage.GetOptReportsTrajectoriesTab().click()
        time.sleep(2)
        ucPage.GetOptReportsFeedVolTab().click()
        time.sleep(2)
        assert ("USP_group_workshop - feed1 - cultivation1" in ucPage.GetOptReportsFeedVolFeed1().text)
        assert ("USP_group_workshop - feed2 - cultivation1" in ucPage.GetOptReportsFeedVolFeed2().text)

        ucPage.GetOptReportsFeedVolTab().click()
        time.sleep(2)
        ucPage.GetOptReportsMediaCompTab().click()
        time.sleep(2)
        assert ("USP_group_workshop - feed1" in ucPage.GetOptReportsMediaCompFeed1().text)
        assert ("USP_group_workshop - feed2" in ucPage.GetOptReportsMediaCompFeed2().text)

        ucPage.GetOptReportsMediaCompTab().click()
        time.sleep(2)
        ucPage.GetOptReportsOptObjectiveTab().click()
        time.sleep(2)
        assert ("USP_group_workshop - cultivation1" in ucPage.GetOptReportsOptObjectiveTitle().text)



    @pytest.fixture(params=workspacedata.getTestData("test_workspace_title_check"))
    def getData(self, request):
        return request.param