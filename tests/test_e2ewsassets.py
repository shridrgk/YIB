import time

import pytest
from selenium.webdriver import ActionChains

from TestData.workspacedata import workspacedata
from pageObjects.AssetPage import AssetPage
from pageObjects.WorkSpacePage import WorkSpacePage

from utilities.BaseClass import BaseClass


class Test_WorkspaceAssetSuite(BaseClass):



    def test_workspace_title_check(self,getData):
        log = self.getLogger()
        self.login(getData["UserName"],getData["Password"])
        log.info("Login successfully")
        workSpacePage = WorkSpacePage(self.driver)
        title = workSpacePage.getPageTitle().text
        assert("Workspace" in title )
        log.info("Workspace Title " + workSpacePage.getPageTitle().text)
    def test_workspace_grid_check(self):
        log = self.getLogger()
        workSpacePage = WorkSpacePage(self.driver)
        assert(workSpacePage.GetGridNameColumn().text) == "Name"
        assert(workSpacePage.GetGridDescColumn().text) == "Description"
        assert(workSpacePage.GetGridCreatedOnColumn().text) == "Created_on"
        assert(workSpacePage.GetGridCreatedByColumn().text) == "Created_by"
    # def test_workspace_add_check(self,getData):
    #     log = self.getLogger()
    #     workSpacePage = WorkSpacePage(self.driver)
    #     workSpacePage.GetWorkSpaceAddBtn().click()
    #     log.info("Create workspace should be displayed")
    #     workSpacePage.GetWSpaceName().send_keys(getData["WsName"])
    #     workSpacePage.GetWSpaceDesc().send_keys("Automation Testing of workspace creation")
    #     workSpacePage.GetWspaceCreateBtn().click()
    #     if workSpacePage.GetWspaceDetail().is_displayed():
    #         log.info("Workspace Created Successfully")
    #     else:
    #         log.error("Workspace creation failed with error")
    def test_Workspace_Landing_Page(self,getData):
        log = self.getLogger()
        workSpacePage = WorkSpacePage(self.driver)

        self.WorkspceFilter(getData["FilterWsName"])
        log.info("Workspace Landing page")
        assert (workSpacePage.GetSideNavUspDt().text) == "USP - Digital Twin"
        assert (workSpacePage.GetSideNavDi().text) == "Data Integration"
        assert (workSpacePage.GetSideNavAsset().text) == "Assets"
        assert (workSpacePage.GetSideNavReports().text) == "Reports"

        assert (workSpacePage.GetWsLandingUspList().text) == "Digital Twin - USP"
        assert (workSpacePage.GetWsLandingDIList().text) == "Data Integration"
        assert (workSpacePage.GetWsLandingAssetList().text) == "Assets"
        # assert (workSpacePage.GetWsLandingReportsList().text) == "Reports"
    def test_Asset_Landing_Page(self,getData):
        log = self.getLogger()
        workSpacePage = WorkSpacePage(self.driver)
        assetPage = AssetPage(self.driver)
        self.WorkspceFilter("Data")
        log.info("Workspace Landing page should be displayed")
        workSpacePage.GetWsLandingAssetList().click()
        log.info("Asset Landing page should be displayed")
        assert "Assets" in assetPage.GetAssetLaningTitle().text
        assetPage.GetProductMoleculelist().click()
        assert ("Product Molecules" in assetPage.GetProducMoleculeTitle().text)
    def test_Asset_Product_Molecule_Grid_Check(self,getData):
        log = self.getLogger()
        workSpacePage = WorkSpacePage(self.driver)
        assetPage = AssetPage(self.driver)
        self.WorkspceFilter(getData["FilterWsName"])
        log.info("Workspace Landing page should be displayed")
        workSpacePage.GetWsLandingAssetList().click()
        log.info("Asset Landing page should be displayed")
        assert "Assets" in assetPage.GetAssetLaningTitle().text
        assetPage.GetProductMoleculelist().click()
        time.sleep(2)
        assert  assetPage.GetPmGridComponent().text == "Name"
        assert ("Glycosylation" in assetPage.GetPmGridGlycosylation().text)
        assert ("Charge Variants" in assetPage.GetPmGridChargeVariant().text)
        assert ("Notes" in assetPage.GetPmGridNotes().text)
        assetPage.GetPmGridExpand().click()
        time.sleep(2)
        assetPage.GetCvGridTab().click()
        time.sleep(2)
        assert assetPage.GetCvGridComponent().text == "Component"
        assert ("Low Limit" in assetPage.GetCvGridLlimit().text)
        assert ("High Limit" in assetPage.GetCvGridHLimit().text)
        assert ("Unit" in assetPage.GetCvGridUnit().text)

        assetPage.GetGlycoGridTab().click()
        time.sleep(2)
        assert ("Component" in assetPage.GetGycoGridComponent().text)
        assert ("Low Limit" in assetPage.GetGycoGridLlimit().text)
        assert ("High Limit" in assetPage.GetGycoGridHLimit().text)
        assert ("Unit" in assetPage.GetGycoGridUnit().text)

        assetPage.GetCompGridTab().click()
        time.sleep(2)
        assert ("Component" in assetPage.GetCompGridComponent().text)
        assert ("Values" in assetPage.GetCompGridValues().text)
        assert ("Unit" in assetPage.GetCompGridUnit().text)
    def test_Asset_Cell_Grid_Check(self, getData):
        log = self.getLogger()
        workSpacePage = WorkSpacePage(self.driver)
        assetPage = AssetPage(self.driver)
        self.WorkspceFilter(getData["FilterWsName"])
        log.info("Workspace Landing page should be displayed")
        workSpacePage.GetWsLandingAssetList().click()
        log.info("Asset Landing page should be displayed")
        assert "Assets" in assetPage.GetAssetLaningTitle().text
        assetPage.GetCelllist().click()
        time.sleep(2)
        assert("Name" in assetPage.GetCellGridName().text)
        assert ("Organism" in assetPage.GetCellGridOrganism().text)
        assert ("Host Cell Line" in assetPage.GetCellGridHCL().text)
        assert ("Product Molecule" in assetPage.GetCellGridPM().text)
        assert ("MNM" in assetPage.GetCellGridMNM().text)
        assert ("Notes" in assetPage.GetCellGridNotes().text)

        assetPage.GetPmGridExpand().click()
        time.sleep(2)

        assetPage.GetCellDetailGridMNMtab().click()
        time.sleep(2)
        assert ("Name" in assetPage.GetCellDetailGridMNMName().text)
        assert ("Notes" in assetPage.GetCellDetailGridMNMNotes().text)

        assetPage.GetCellDetailGridPMtab().click()
        time.sleep(2)

        assert ("Name" in assetPage.GetCellDetailGridPMName().text)
        assert ("Glycosylation" in assetPage.GetCellDetailGridPMGlyco().text)
        assert ("Charge Variants" in assetPage.GetCellDetailGridPMCV().text)
        assert ("Notes" in assetPage.GetCellDetailGridPMNotes().text)
    def test_Asset_Medium_Grid_Check(self, getData):
        log = self.getLogger()
        workSpacePage = WorkSpacePage(self.driver)
        assetPage = AssetPage(self.driver)
        self.WorkspceFilter(getData["FilterWsName"])
        log.info("Workspace Landing page should be displayed")
        workSpacePage.GetWsLandingAssetList().click()
        log.info("Asset Landing page should be displayed")
        assert "Assets" in assetPage.GetAssetLaningTitle().text
        assetPage.GetMediumList().click()
        time.sleep(2)
        assert("Name" in assetPage.GetMediumGridName().text)
        assert ("Type" in assetPage.GetMediumGridType().text)
        assert ("Notes" in assetPage.GetMediumGridNotes().text)
        # assert ("Actions" in assetPage.GetMediumGridActions().text)

        assetPage.GetPmGridExpand().click()
        time.sleep(2)

        assert("Components" in assetPage.GetCompComponents().text)
        assert ("Low Limit" in assetPage.GetCompLlimit().text)
        assert ("High Limit" in assetPage.GetCompHlimit().text)
        assert ("Unit" in assetPage.GetCompUnit().text)
        assert ("Error Model" in assetPage.GetCompErr().text)
    def test_Asset_Sparging_Gas_Grid_Check(self, getData):
        log = self.getLogger()
        workSpacePage = WorkSpacePage(self.driver)
        assetPage = AssetPage(self.driver)
        self.WorkspceFilter(getData["FilterWsName"])
        log.info("Workspace Landing page should be displayed")
        workSpacePage.GetWsLandingAssetList().click()
        log.info("Asset Landing page should be displayed")
        assert "Assets" in assetPage.GetAssetLaningTitle().text
        assetPage.GetSpGasList().click()
        time.sleep(2)
        assert("Name" in assetPage.GetSpGasGridName().text)
        assert ("Notes" in assetPage.GetSpGasGridNotes().text)
        # assert ("Actions" in assetPage.GetSpGasGridActions().text)

        assetPage.GetPmGridExpand().click()
        time.sleep(2)

        assert("Components" in assetPage.GetCompGasComponents().text)
        assert ("Low Limit" in assetPage.GetCompGasLlimit().text)
        assert ("High Limit" in assetPage.GetCompGasHlimit().text)
        assert ("Unit" in assetPage.GetCompGasUnit().text)
        assert ("Error Model" in assetPage.GetCompGasErr().text)
    def test_Asset_Sensor_Grid_Check(self, getData):
        log = self.getLogger()
        workSpacePage = WorkSpacePage(self.driver)
        assetPage = AssetPage(self.driver)
        self.WorkspceFilter(getData["FilterWsName"])
        log.info("Workspace Landing page should be displayed")
        workSpacePage.GetWsLandingAssetList().click()
        log.info("Asset Landing page should be displayed")
        assert "Assets" in assetPage.GetAssetLaningTitle().text
        assetPage.GetSensorList().click()
        time.sleep(2)
        assert("Name" in assetPage.GetSensorGridName().text)
        assert ("Notes" in assetPage.GetSensorGridNotes().text)
        # assert ("Actions" in assetPage.GetSensorGridActions().text)
        assert ("Sensed Medium Objects" in assetPage.GetSensorMOGridActions().text)

        assetPage.GetPmGridExpand().click()
        time.sleep(2)
        assetPage.GetSensorSensorCalibrationTab().click()
        time.sleep(2)
        assetPage.GetSensorMOTab().click()
        time.sleep(2)

        assert("Medium Object" in assetPage.GetMOComponents().text)
        assert ("Low Limit" in assetPage.GetMOLlimit().text)
        assert ("High Limit" in assetPage.GetMOHlimit().text)
        assert ("Unit" in assetPage.GetMOUnit().text)
        assert ("Error Model" in assetPage.GetMOErr().text)
    def test_Asset_Controller_Grid_Check(self, getData):
        log = self.getLogger()
        workSpacePage = WorkSpacePage(self.driver)
        assetPage = AssetPage(self.driver)
        self.WorkspceFilter(getData["FilterWsName"])
        log.info("Workspace Landing page should be displayed")
        workSpacePage.GetWsLandingAssetList().click()
        log.info("Asset Landing page should be displayed")
        assert "Assets" in assetPage.GetAssetLaningTitle().text
        assetPage.GetControllersList().click()
        time.sleep(2)
        assert('Name' in assetPage.GetControllerGridName().text)
        assert ('Type' in assetPage.GetControllerGridType().text)
        assert ("Notes" in assetPage.GetControllerGridNotes().text)
        assert ("Error Model" in assetPage.GetControllerGridErr().text)

        assetPage.GetPmGridExpand().click()
        time.sleep(1)
        assetPage.GetControllerTimeParamTab().click()
        time.sleep(2)

        assert ('Parameter Name' in assetPage.GetControllerTimeParamGridName().text)
        assert ('Parameter Notes' in assetPage.GetControllerTimeParamGridNotes().text)
        assert ("Start Time" in assetPage.GetControllerTimeParamGridStart().text)
        # assert ("End Time (hrs)" in assetPage.GetControllerTimeParamGridEnd().text)
        assert ('Low Limit' in assetPage.GetControllerTimeParamGridLlimit().text)
        assert ('High Limit' in assetPage.GetControllerTimeParamGridHlimit().text)
        assert ("Time Unit" in assetPage.GetControllerTimeParamGridUnit().text)
        assert ("Time Unit" in assetPage.GetControllerTimeParamGridUnit().text)

        assetPage.GetControllerParamTab().click()
        time.sleep(2)

        assert ('Parameter Name' in assetPage.GetControllerParamGridName().text)
        assert ('Notes' in assetPage.GetControllerParamGridNotes().text)
        assert ("Value" in assetPage.GetControllerParamGridValue().text)
    def test_Asset_Reactor_Grid_Check(self, getData):
        log = self.getLogger()
        workSpacePage = WorkSpacePage(self.driver)
        assetPage = AssetPage(self.driver)
        self.WorkspceFilter(getData["FilterWsName"])
        log.info("Workspace Landing page should be displayed")
        workSpacePage.GetWsLandingAssetList().click()
        log.info("Asset Landing page should be displayed")
        assert "Assets" in assetPage.GetAssetLaningTitle().text
        assetPage.GetReactorList().click()
        time.sleep(2)
        assert('Name' in assetPage.GetReactorGridName().text)
        assert ("No of Inlets" in assetPage.GetReactorGridInlet().text)
        assert ("No of Outlets" in assetPage.GetReactorGridOutlet().text)
        assert ("Max Working Volume" in assetPage.GetReactorGridMaxWrk().text)
        assert ("Impeller Name" in assetPage.GetReactorGridImplName().text)
        assert ("Notes" in assetPage.GetReactorGridNotes().text)

        assetPage.GetPmGridExpand().click()
        time.sleep(1)
        assetPage.GetReactorOutletGridtab().click()
        time.sleep(2)

        assert ('Name' in assetPage.GetReactoroutletGridName().text)
        assert ('Low Limit' in assetPage.GetReactoroutletGridLlimit().text)
        assert ('High Limit' in assetPage.GetReactoroutletGridHlimit().text)
        assert ("Unit" in assetPage.GetReactoroutletGridUnit().text)
        assert ('Error Model' in assetPage.GetReactoroutletGridErr().text)

        assetPage.GetReactorinletGridtab().click()
        time.sleep(2)

        assert ('Name' in assetPage.GetReactorinletGridName().text)
        assert ('Low Limit' in assetPage.GetReactorinletGridLlimit().text)
        assert ('High Limit' in assetPage.GetReactorinletGridHlimit().text)
        assert ("Unit" in assetPage.GetReactorinletGridUnit().text)
        assert ('Error Model' in assetPage.GetReactorinletGridErr().text)
    def test_Asset_Retention_Grid_Check(self, getData):
        log = self.getLogger()
        workSpacePage = WorkSpacePage(self.driver)
        assetPage = AssetPage(self.driver)
        self.WorkspceFilter(getData["FilterWsName"])
        log.info("Workspace Landing page should be displayed")
        workSpacePage.GetWsLandingAssetList().click()
        log.info("Asset Landing page should be displayed")
        assert "Assets" in assetPage.GetAssetLaningTitle().text
        assetPage.GetRetentionList().click()
        time.sleep(2)
        assert('Name' in assetPage.GetRetentionGridName().text)
        assert ("Notes" in assetPage.GetRetentionGridNotes().text)




        assetPage.GetPmGridExpand().click()
        time.sleep(2)

        assert ('Retained Medium Objects' in assetPage.GetRetentionDetailGridRMO().text)
        assert ('Low Limit' in assetPage.GetRetentionDetailGridLlimit().text)
        assert ('High Limit' in assetPage.GetRetentionDetailGridHlimit().text)
        assert ("Unit" in assetPage.GetRetentionDetailGridUnit().text)
        assert ('Error Model' in assetPage.GetRetentionDetailGridErr().text)





    @pytest.fixture(params=workspacedata.getTestData("test_workspace_title_check"))
    def getData(self, request):
        return request.param

