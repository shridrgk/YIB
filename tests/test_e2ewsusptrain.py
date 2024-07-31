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
    def test_USP_Create(self, getData):
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
        uspPage.GetUspAddBtn().click()
        time.sleep(1)
        log.info("Create USP Page should be displayed")
        assert ("Digital Twin - USP" in uspPage.GetUspAddTitle().text)
        assert ("Create DT for Upstream Process" in uspPage.GetUspAddSubTitle().text)
        uspPage.GetUspAddName().send_keys(getData["UspName"])
        uspPage.GetUspAddDesc().send_keys("Testing Creation of USP")
        uspPage.GetUspCreateBtn().click()
        time.sleep(1)
        assert (uspPage.GetEditUseCaseToast().text == getData["UspName"] + " created successfully")
        assert (getData["UspName"] in uspPage.GetUspReactorSetupPageTitle().text)
        log.info("USP config Reactor Page is displayed")

    def test_Run_Train_RgList_Grid_Validation(self, getData):
        log = self.getLogger()
        workSpacePage = WorkSpacePage(self.driver)
        uspPage = UspPage(self.driver)
        # self.login(getData["UserName"], getData["Password"])
        # log.info("Login successfully")
        self.WorkspceFilter("Data")
        log.info("Workspace Landing page is displayed")
        uspPage.GetWsUspLandingPage().click()
        time.sleep(1)
        assert ("Digital Twin - USP" in uspPage.GetUspLandingPageTitle().text)
        log.info("USP landing page is displayed")
        self.UspEditFilter(getData["UspName"])
        assert("Define" in uspPage.GetUspTrainStepperStage1().text)
        assert(getData["UspName"] in uspPage.GetUspReactorSetupPageTitle().text)
        assert("Group Name" in uspPage.GetUspReactorGridName().text)
        assert ("Reactor Type" in uspPage.GetUspReactorGridType().text)
        assert ("Reactor Vessel Name" in uspPage.GetUspReactorGridVessel().text)
        uspPage.GetUspReactorGridExpand().click()
        time.sleep(1)
        uspPage.GetUspTrainNextBtn().click()

    def test_Run_Train_Reactor_Configure_Grid_Validation(self, getData):
        log = self.getLogger()
        workSpacePage = WorkSpacePage(self.driver)
        uspPage = UspPage(self.driver)
        self.WorkspceFilter("Data")
        log.info("Workspace Landing page is displayed")
        uspPage.GetWsUspLandingPage().click()
        time.sleep(1)
        assert ("Digital Twin - USP" in uspPage.GetUspLandingPageTitle().text)
        log.info("USP landing page is displayed")
        self.UspEditFilter(getData["UspName"])
        uspPage.GetUspTrainNextBtn().click()
        time.sleep(1)
        assert("Configure" in uspPage.GetUspTrainStepperStage2().text)
        assert("USP_group_workshop" in uspPage.GetUspConfigPageTitle().text)
        assert("Reactors" in uspPage.GetUspConfigReactors().text)
        assert(getData["UspName"] in uspPage.GetUspReactorSetupPageTitle().text)
        assert("Name" in uspPage.GetUspConfigCellGridName().text)
        assert("Organism" in uspPage.GetUspConfigCellGridOrganism().text)
        assert("Host Cell Line" in uspPage.GetUspConfigCellGridHostLine().text)
        assert ("Product Molecule" in uspPage.GetUspConfigCellGridPMolecule().text)
        assert ("MNM" in uspPage.GetUspConfigCellGridMNM().text)
        assert ("Notes" in uspPage.GetUspConfigCellGridNotes().text)
        time.sleep(1)
        uspPage.GetUspConfigReactor().click()
        time.sleep(1)
        uspPage.GetUspConfigReactorController().click()
        time.sleep(1)
        assert("USP_config_workshop_cultivation1" in uspPage.GetUspconfigDropDown().text)
        assert("Name" in uspPage.GetUspConfigControllerGridName().text)
        assert ("Notes" in uspPage.GetUspConfigControllerGriddNotes().text)
        assert ("Type" in uspPage.GetUspConfigControllerGriddType().text)
        assert ("Error Model" in uspPage.GetUspConfigControllerGridErr().text)
        assert ("Parameter" in uspPage.GetUspConfigControllerGridparameter().text)
        assert ("Value" in uspPage.GetUspConfigControllerGridValue().text)
        assert ("Notes" in uspPage.GetUspConfigControllerGriddNotes().text)
        uspPage.GetUspConfigReactorImpeller().click()
        time.sleep(1)
        assert("USP_config_workshop_cultivation1" in uspPage.GetUspconfigDropDown().text)
        assert("Name" in uspPage.GetUspConfigimpelllerGridName().text)
        assert ("Notes" in uspPage.GetUspConfigimpelllerGridNotes().text)
        assert ("Diameter" in uspPage.GetUspConfigimpelllerGridDiameter().text)
        assert ("Diameter Unit" in uspPage.GetUspConfigimpelllerGridDiametrUnit().text)
        assert ("Low Limit Speed" in uspPage.GetUspConfigimpelllerGridLSpeed().text)
        assert ("High Limit Speed" in uspPage.GetUspConfigimpelllerGridHSpeed().text)
        assert ("Speed Unit" in uspPage.GetUspConfigimpelllerGridSpeedunit().text)
        uspPage.GetUspConfigReactorSensor().click()
        time.sleep(1)
        assert("Name" in uspPage.GetUspConfigSensorGridName().text)
        assert ("Notes" in uspPage.GetUspConfigSensorGridNotes().text)
        assert ("Medium Object" in uspPage.GetUspConfigSensorGridMediumObject().text)
        assert ("Low Limit" in uspPage.GetUspConfigSensorGridLowLimit().text)
        assert ("High Limit" in uspPage.GetUspConfigSensorGridHighLimit().text)
        assert ("Unit" in uspPage.GetUspConfigSensorGridUnit().text)
        uspPage.GetUspReactorGridExpand().click()
        time.sleep(1)
        uspPage.GetUspTrainNextBtn().click()
        time.sleep(1)

    def test_Run_Train_Setup_Influx_Outflux_Grid_Validation(self, getData):
        log = self.getLogger()
        workSpacePage = WorkSpacePage(self.driver)
        uspPage = UspPage(self.driver)
        self.WorkspceFilter("Data")
        log.info("Workspace Landing page is displayed")
        uspPage.GetWsUspLandingPage().click()
        time.sleep(1)
        assert ("Digital Twin - USP" in uspPage.GetUspLandingPageTitle().text)
        log.info("USP landing page is displayed")
        self.UspEditFilter(getData["UspName"])
        uspPage.GetUspTrainNextBtn().click()
        time.sleep(1)
        uspPage.GetUspConfigInflux().click()
        time.sleep(2)
        assert("Inlet Name" in uspPage.GetUspConfigInfluxGridInletName().text)
        assert ("Influx Type" in uspPage.GetUspConfigInfluxGridType().text)
        assert ("Medium" in uspPage.GetUspConfigInfluxGridMedium().text)
        assert ("Error Model" in uspPage.GetUspConfigInfluxGridErr().text)
        assert ("Controller Name" in uspPage.GetUspConfigInfluxGridControlName().text)

        uspPage.GetUspConfigOutflux().click()
        time.sleep(2)
        assert("Outlet Name" in uspPage.GetUspConfigOutfluxGridInletName().text)
        assert ("Outflux Type" in uspPage.GetUspConfigOutfluxGridType().text)
        assert ("Retention" in uspPage.GetUspConfigOutfluxGridRetention().text)
        assert ("Error Model" in uspPage.GetUspConfigOutfluxGridErr().text)
        assert ("Controller Name" in uspPage.GetUspConfigOutfluxGridControlName().text)

        uspPage.GetUspTrainNextBtn().click()
        time.sleep(1)

    def test_Run_Train_Summary_Grid_Validation(self, getData):
        log = self.getLogger()
        workSpacePage = WorkSpacePage(self.driver)
        uspPage = UspPage(self.driver)
        self.WorkspceFilter("Data")
        log.info("Workspace Landing page is displayed")
        uspPage.GetWsUspLandingPage().click()
        time.sleep(1)
        assert ("Digital Twin - USP" in uspPage.GetUspLandingPageTitle().text)
        log.info("USP landing page is displayed")
        self.UspEditFilter(getData["UspName"])
        uspPage.GetUspTrainNextBtn().click()
        time.sleep(1)
        uspPage.GetUspConfigOutflux().click()
        time.sleep(2)
        uspPage.GetUspTrainNextBtn().click()
        time.sleep(1)
        assert ("Groups" in uspPage.GetUspTrainSummaryGridGroups().text)
        assert ("Impeller Name" in uspPage.GetUspTrainSummaryGridImpellerName().text)
        assert ("No of Inlets" in uspPage.GetUspTrainSummaryGridNoOfInlets().text)
        assert ("No of Outlets" in uspPage.GetUspTrainSummaryGridNoOfOutlets().text)
        assert ("Controllers" in uspPage.GetUspTrainSummaryGridControllers().text)
        assert ("Sensors" in uspPage.GetUspTrainSummaryGridSensors().text)
        uspPage.GetUspTrainNextBtn().click()
        time.sleep(1)

    def test_Run_Train_Grid_Validation(self, getData):
        log = self.getLogger()
        workSpacePage = WorkSpacePage(self.driver)
        uspPage = UspPage(self.driver)
        self.WorkspceFilter("Data")
        log.info("Workspace Landing page is displayed")
        uspPage.GetWsUspLandingPage().click()
        time.sleep(1)
        assert ("Digital Twin - USP" in uspPage.GetUspLandingPageTitle().text)
        log.info("USP landing page is displayed")
        self.UspEditFilter(getData["UspName"])
        uspPage.GetUspTrainNextBtn().click()
        time.sleep(1)
        uspPage.GetUspConfigOutflux().click()
        time.sleep(2)
        uspPage.GetUspTrainNextBtn().click()
        time.sleep(1)
        uspPage.GetUspTrainNextBtn().click()
        time.sleep(2)
        assert ("Cells" in uspPage.GetUspTrainGridCells().text)
        assert ("Cultivations" in uspPage.GetUspTrainGridCultivation().text)
        assert ("Notes" in uspPage.GetUspTrainGridNotes().text)
        assert ("Include" in uspPage.GetUspTrainGridIncude().text)
        # assert("Run Training" in uspPage.GetUspRunTrainBtn().text)
        # uspPage.GetUspRunTrainBtn().click()
        # time.sleep(1)
        # assert ("Started" in uspPage.GetEditUseCaseToast().text)
















    @pytest.fixture(params=workspacedata.getTestData("test_workspace_title_check"))
    def getData(self, request):
        return request.param