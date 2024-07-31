import time

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from TestData.workspacedata import workspacedata
from pageObjects.AssetPage import AssetPage
from pageObjects.DiPage import DiPage
from pageObjects.WorkSpacePage import WorkSpacePage

from utilities.BaseClass import BaseClass


class TestWorkspaceAssetSuite(BaseClass):

    def test_DI_Landing_Page_Grid_Validations(self,getData):
        log = self.getLogger()
        workSpacePage = WorkSpacePage(self.driver)
        diPage = DiPage(self.driver)
        self.login(getData["UserName"], getData["Password"])
        log.info("Login successfully")
        self.WorkspceFilter("Data")
        log.info("Workspace Landing page should be displayed")
        workSpacePage.GetWsLandingDIList().click()
        assert ("Data Integration" in diPage.GetDiLandingPageTitle().text)
        assert diPage.GetDiGridName().text == "Name"
        assert diPage.GetDiGridDescription().text == "Description"
        assert diPage.GetDiGridCreated_by().text == "Created_by"
        assert diPage.GetDiGridCreated_on().text == "Created_on"
        assert diPage.GetDiGridStatus().text == "Status"

    def test_DI_Create_DI_Validations(self,getData):
        log = self.getLogger()
        workSpacePage = WorkSpacePage(self.driver)
        diPage = DiPage(self.driver)
        self.WorkspceFilter("Data")
        log.info("Workspace Landing page should be displayed")
        workSpacePage.GetWsLandingDIList().click()
        time.sleep(1)
        diPage.GetAddDiBtn().click()
        diPage.GetCreateDiName().send_keys(getData["DiName"])
        diPage.GetCreateDiDesc().send_keys("Testing of DI creation")
        diPage.GetCreateDiBtn().click()
        assert ("Data Stage" in diPage.GetDiStageTitle().text)

    def test_Data_Stage_Upload_Files(self,getData):
        log = self.getLogger()
        workSpacePage = WorkSpacePage(self.driver)
        diPage = DiPage(self.driver)
        self.WorkspceFilter("Data")
        log.info("Workspace Landing page should be displayed")
        workSpacePage.GetWsLandingDIList().click()
        assert ("Data Integration" in diPage.GetDiLandingPageTitle().text)
        self.DIFilter(getData["DiName"])
        assert ("Data Stage" in diPage.GetDiStageTitle().text)

        diPage.GetDiStageUploadFileBtn().click()
        assert ("Upload Files" in diPage.GetDiStageUploaderTitle().text)
        self.UploadDiStageFile(getData["file_path"], "amino_acid_data.csv")
        self.UploadDiStageFile(getData["file_path"], "biomass_related_data.csv")
        self.UploadDiStageFile(getData["file_path"], "feed_volume_data.csv")
        self.UploadDiStageFile(getData["file_path"], "other_compounds_data.csv")
        self.UploadDiStageFile(getData["file_path"], "media_composition_data.csv")
        self.UploadDiStageFile(getData["file_path"], "sample_volume_data.csv")
        self.UploadDiStageFile(getData["file_path"], "volume_data.csv")
        self.UploadDiStageFile(getData["file_path"],"additional_data.csv")
        diPage.GetDiStageUploadCloseBtn().click()
        diPage.GetDiStageRefreshBtn().click()

    def test_DI_Matching_Template_Grid_Validation(self, getData):
        log = self.getLogger()
        workSpacePage = WorkSpacePage(self.driver)
        diPage = DiPage(self.driver)
        self.WorkspceFilter("Data")
        log.info("Workspace Landing page should be displayed")
        workSpacePage.GetWsLandingDIList().click()
        assert ("Data Integration" in diPage.GetDiLandingPageTitle().text)
        log.info("DI Landing page should be displayed")
        self.DIFilter(getData["DiName"])
        assert ("Data Stage" in diPage.GetDiStageTitle().text)
        diPage.GetDiStageRefreshBtn().click()
        log.info("Data stage landing page should be displayed")
        time.sleep(1)
        diPage.GetDiStageNextBtn().click()
        log.info("ETL Matching Template Page should be displayed")
        assert("ETL Templates" in diPage.GetDiMatchingTempTitle().text)
        assert("Name" in diPage.GetDiMatchingTempName().text)
        assert ("Author" in diPage.GetDiMatchingTempAuthor().text)
        assert ("Published On" in diPage.GetDiMatchingPublish_on().text)
        assert ("Version" in diPage.GetDiMatchingVersion().text)

    def test_DI_Matching_Template_Selection_Apply(self,getData):
        log = self.getLogger()
        workSpacePage = WorkSpacePage(self.driver)
        diPage = DiPage(self.driver)
        self.WorkspceFilter("Data")
        log.info("Workspace Landing page should be displayed")
        workSpacePage.GetWsLandingDIList().click()
        assert ("Data Integration" in diPage.GetDiLandingPageTitle().text)
        log.info("DI Landing page should be displayed")
        self.DIFilter(getData["DiName"])
        assert ("Data Stage" in diPage.GetDiStageTitle().text)
        diPage.GetDiStageRefreshBtn().click()
        log.info("Data stage landing page should be displayed")
        time.sleep(1)
        diPage.GetDiStageNextBtn().click()
        log.info("ETL Matching Template Page should be displayed")
        self.TempFilter("ETL Template for Workshop data V2")

        action = ActionChains(self.driver)
        action.move_to_element(diPage.GetDiMatchingCodeSpaceBtn()).click().perform()
        time.sleep(2)
        assert ["Code Space" in diPage.GetDiCodeSpaceTitle().text]

        action = ActionChains(self.driver)
        action.move_to_element(diPage.GetDiCodeSpaceFileCultivation()).click().perform()
        time.sleep(1)

        action = ActionChains(self.driver)
        action.move_to_element(diPage.GetDiCodeSpaceFilediConfig()).click().perform()
        time.sleep(2)

        action = ActionChains(self.driver)
        action.move_to_element(diPage.GetDiCodeSpaceFilediInflux()).click().perform()
        time.sleep(2)

        action = ActionChains(self.driver)
        action.move_to_element(diPage.GetDiCodeSpaceFilediMain()).click().perform()
        time.sleep(2)

        action = ActionChains(self.driver)
        action.move_to_element(diPage.GetDiCodeSpaceFilediMappings()).click().perform()
        time.sleep(2)

        action = ActionChains(self.driver)
        action.move_to_element(diPage.GetDiCodeSpaceFilediOutflux()).click().perform()
        time.sleep(2)

        action = ActionChains(self.driver)
        action.move_to_element(diPage.GetDiCodeSpaceFilediRelation()).click().perform()
        time.sleep(2)

        action = ActionChains(self.driver)
        action.move_to_element(diPage.GetDiCodeSpaceFilediSesnor()).click().perform()
        time.sleep(2)

        action = ActionChains(self.driver)
        action.move_to_element(diPage.GetDiCodeSpaceFilediTransform()).click().perform()
        time.sleep(2)

        action = ActionChains(self.driver)
        action.move_to_element(diPage.GetDiCodeSpaceFilediValidation()).click().perform()
        time.sleep(2)

        diPage.GetDiCodeSpaceCloseBtn().click()
        time.sleep(2)
        diPage.GetDiMatchingApplyBtn().click()
        time.sleep(4)

    def test_DI_Matching_Template_Detail_Validation(self,getData):
        log = self.getLogger()
        workSpacePage = WorkSpacePage(self.driver)
        diPage = DiPage(self.driver)
        self.WorkspceFilter("Data")
        log.info("Workspace Landing page should be displayed")
        workSpacePage.GetWsLandingDIList().click()
        assert ("Data Integration" in diPage.GetDiLandingPageTitle().text)
        log.info("DI Landing page should be displayed")
        self.DIFilter(getData["DiName"])
        assert ("Data Stage" in diPage.GetDiStageTitle().text)
        diPage.GetDiStageRefreshBtn().click()
        log.info("Data stage landing page should be displayed")
        time.sleep(1)
        diPage.GetDiStageNextBtn().click()
        log.info("ETL Matching Template Detail Page should be displayed")
        assert("ETL Template - " in diPage.GetDiTemplateDetailTitle().text)
        assert  diPage.GetDiTemplateDetailChangeTempBtn().is_enabled()
        assert  diPage.GetDiTemplateDetailRefreshBtn().is_enabled()
        assert diPage.GetDiTemplateDetailExecuteBtn().is_enabled()
        diPage.GetDiTemplateDetailCodeSpace().click()
        time.sleep(1)
        diPage.GetDiTempDetailCodeSpaceFileCultivation().click()
        time.sleep(1)
        diPage.GetDiTempDetailCodeSpaceFilediConfig().click()
        time.sleep(1)
        diPage.GetDiTempDetailCodeSpaceFilediInflux().click()
        time.sleep(1)
        diPage.GetDiTempDetailCodeSpaceFilediMain().click()
        time.sleep(1)
        diPage.GetDiTempDetailCodeSpaceFilediMappings().click()
        time.sleep(1)
        diPage.GetDiTempDetailCodeSpaceFilediOutflux().click()
        time.sleep(1)
        diPage.GetDiTempDetailCodeSpaceFilediRelation().click()
        time.sleep(1)
        diPage.GetDiTempDetailCodeSpaceFilediSesnor().click()
        time.sleep(1)
        diPage.GetDiTempDetailCodeSpaceFilediTransform().click()
        time.sleep(1)
        diPage.GetDiTempDetailCodeSpaceFilediValidation().click()
        time.sleep(1)
        diPage.GetDiTemplateDetailConfig().click()
        diPage.GetDiTemplateDetailTempVarCheckBox().click()
        assert ("Name" in diPage.GetDiTemplateDetailTempVarGridName().text)
        assert ("Description" in diPage.GetDiTemplateDetailTempVarGridDesc().text)
        assert ("Value" in diPage.GetDiTemplateDetailTempVarValue().text)
        diPage.GetDiTemplateDetailAltVarCheckBox().click()

        assert ("Name" in diPage.GetDiTemplateDetailAltVarGridName().text)
        assert ("Alias" in diPage.GetDiTemplateDetailAltVarGridAlias().text)

        assert diPage.GetDiTemplateDetailPrevBtn().is_enabled
        assert diPage.GetDiTempateDetailNextBtn().is_enabled

    def test_DI_Matching_Template_Execution(self,getData):
        log = self.getLogger()
        workSpacePage = WorkSpacePage(self.driver)
        diPage = DiPage(self.driver)
        self.WorkspceFilter("Data")
        log.info("Workspace Landing page should be displayed")
        workSpacePage.GetWsLandingDIList().click()
        assert ("Data Integration" in diPage.GetDiLandingPageTitle().text)
        log.info("DI Landing page should be displayed")
        self.DIFilter(getData["DiName"])
        assert ("Data Stage" in diPage.GetDiStageTitle().text)
        diPage.GetDiStageRefreshBtn().click()
        log.info("Data stage landing page should be displayed")
        time.sleep(1)
        diPage.GetDiStageNextBtn().click()
        log.info("ETL Matching Template Detail Page should be displayed")
        assert("ETL Template - " in diPage.GetDiTemplateDetailTitle().text)
        diPage.GetDiTempolateExecuteBtn().click()
        element = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[role='alertdialog'] span[class*='p-confirm-dialog-message']")))
        assert element.text == "ETL job started, click on refresh button to check for job completion. Once completed Next button will be enabled."
        diPage.GetDiTemplateDialogAcpt().click()
        time.sleep(3)
        diPage.GetDiTemplateExecuteRefreshBtn().click()
        time.sleep(2)
        # diPage.GetDiTemplateExecuteRefreshBtn().click()
        # time.sleep(2)
        # element1 = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[role='alertdialog'] span[class*='p-confirm-dialog-message']")))
        # assert element1.text == "ETL job completed successfully, click on next button to continue to view and load."
        # diPage.GetDiTemplateDialogAcpt().click()
        # time.sleep(3)

        # log.info(file.__getattribute__(self,"aria-label"))
    @pytest.fixture(params=workspacedata.getTestData("test_workspace_title_check"))
    def getData(self, request):
        return request.param