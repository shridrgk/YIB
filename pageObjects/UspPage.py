from selenium.webdriver.common.by import By
import pytest
class UspPage:

    def __init__(self, driver):
        self.driver = driver

    WsUspLandingPage = (By.CSS_SELECTOR,"app-workspace-detail-item a[href*='usp-dt']")
    UspLandingPageTitle = (By.CSS_SELECTOR,"app-usp-usp-list h1")
    UspListGridName=(By.XPATH,"//app-usp-usp-list//div[@class='ag-header-cell-label']//span[contains(text(),'Name')]")
    UspListGridDesc=(By.XPATH,"//app-usp-usp-list//div[@class='ag-header-cell-label']//span[contains(text(),'Description')]")
    UspListGridNumReactor=(By.XPATH,"//app-usp-usp-list//div[@class='ag-header-cell-label']//span[contains(text(),'No of Reactors')]")
    UspListGridStatus = (By.XPATH, "//app-usp-usp-list//div[@class='ag-header-cell-label']//span[contains(text(),'Status')]")
    UspListGridAction = (By.XPATH, "//app-usp-usp-list//div[@class='ag-header-cell-label']//span[contains(text(),'Actions')]")
    UspAddBtn=(By.CSS_SELECTOR,"p-button[ptooltip='Add USP'] button")
    UspAddName = (By.CSS_SELECTOR,"app-usp-create-usp input[formcontrolname='upstream_process_name']")
    UspAddDesc = (By.CSS_SELECTOR,"app-usp-create-usp textarea[formcontrolname='upstream_process_notes']")
    UspCreateBtn =(By.CSS_SELECTOR,"app-usp-create-usp button[type='submit']")
    UspAddTitle = (By.CSS_SELECTOR,"app-usp-create-usp h1")
    UspAddSubTitle = (By.CSS_SELECTOR, "app-usp-create-usp h3")
    UspListGridNameFilter = (By.XPATH,"//app-usp-usp-list//div[@class='ag-header-cell-label']//span[contains(text(),'Name')]/parent::div/parent::div/span")
    FilterSearBox = (By.CSS_SELECTOR, "input[aria-label='Search filter values']")
    FilterApplyBtn = (By.CSS_SELECTOR, "button[type='submit']")
    SelectUSP=(By.XPATH,"//div[contains(@class,'ag-row-first')]//div[@col-id='upstream_process_name']/parent::div")
    SelectUC = (By.XPATH, "//div[contains(@class,'ag-row-first')]//div[@col-id='usp_use_case_name']/parent::div")




    UseCaseListPageTitle = (By.CSS_SELECTOR,"app-usp-usecase-list h1")
    UseCaseGridName = (By.XPATH,"//app-usp-usecase-list//div[@class='ag-header-cell-label']//span[contains(text(),'Name')]")
    UseCaseGridDesc = (By.XPATH,"//app-usp-usecase-list//div[@class='ag-header-cell-label']//span[contains(text(),'Description')]")
    UseCaseGridPrediction = (By.XPATH,"//app-usp-usecase-list//div[@class='ag-header-cell-label']//span[contains(text(),'Prediction Usecase')]")
    UseCaseGridType = (By.XPATH,"//app-usp-usecase-list//div[@class='ag-header-cell-label']//span[contains(text(),'Set-up')]")
    UseCaseGridStatus = (By.XPATH,"//app-usp-usecase-list//div[@class='ag-header-cell-label']//span[contains(text(),'Status')]")
    UseCaseAddBtn=(By.CSS_SELECTOR,"p-button[ptooltip='Add Usecase'] button")
    UseCaseAddName=(By.CSS_SELECTOR,"app-usp-create-usecase input[id='name']")
    UseCaseAddDesc = (By.CSS_SELECTOR, "app-usp-create-usecase textarea[formcontrolname='description']")
    UseCaseGridPredictionType = (By.CSS_SELECTOR,"app-usp-create-usecase p-dropdown")
    UseCaseGridPredictionTypeSimulation = (By.CSS_SELECTOR,"app-usp-create-usecase li[aria-label='simulation']")
    UseCaseGridPredictionTypeOptimization = (By.CSS_SELECTOR, "app-usp-create-usecase li[aria-label='optimization']")
    UseCaseSetpDropDown = (By.CSS_SELECTOR,"app-usp-create-usecase p-dropdown[formcontrolname='usecaseSetups']")
    UseCaseSetupReactor = (By.CSS_SELECTOR,"li[aria-label='reactor']")

    UseCaseCreateBtn=(By.CSS_SELECTOR,"app-usp-create-usecase div button[type='submit']")

    UseCaseReactorList=(By.CSS_SELECTOR,"app-simulation-reactor-list h1")
    UseCaseReactorName = (By.XPATH,"//app-simulation-reactor-list//div[@class='ag-header-cell-label']//span[contains(text(),'Group Name')]")
    UseCaseReactorType = (By.XPATH,"//app-simulation-reactor-list//div[@class='ag-header-cell-label']//span[contains(text(),'Reactor Type')]")
    UseCaseReactorCells = (By.XPATH,"//app-simulation-reactor-list//div[@class='ag-header-cell-label']//span[contains(text(),'Cells')]")
    UseCaseReactorReactor = (By.XPATH,"//app-simulation-reactor-list//div[@class='ag-header-cell-label']//span[contains(text(),'Reactors')]")
    UseCaseReactorStatus = (By.XPATH,"//app-simulation-reactor-list//div[@class='ag-header-cell-label']//span[contains(text(),'Status')]")

    UseCaseEditBtn=(By.CSS_SELECTOR,"app-usp-edit-cell-renderer button")
    EditUseCaseTitle=(By.CSS_SELECTOR,"p-sidebar div[role='complementary'] h3")
    EditUseCaseControlVar=(By.CSS_SELECTOR," app-usp-reactor-setup p-accordiontab[header='Control Variable'] a")
    EditUseCaseMediaVar=(By.CSS_SELECTOR," app-usp-reactor-setup p-accordiontab[header='Medium'] a")
    EditControlVarGridName=(By.XPATH,"//app-usp-reactor-setup//p-accordiontab[@header='Control Variable']//div[@class='ag-header-cell-label']//span[text()='Name']")
    EditControlVarGridParamName=(By.XPATH,"//app-usp-reactor-setup//p-accordiontab[@header='Control Variable']//div[@class='ag-header-cell-label']//span[text()='Parameter Name']")
    EditControlVarGridDesc=(By.XPATH,"//app-usp-reactor-setup//p-accordiontab[@header='Control Variable']//div[@class='ag-header-cell-label']//span[text()='Description']")
    EditControlVarGridParamType=(By.XPATH,"//app-usp-reactor-setup//p-accordiontab[@header='Control Variable']//div[@class='ag-header-cell-label']//span[text()='Parameter Type']")
    EditControlVarGridValue=(By.XPATH,"//app-usp-reactor-setup//p-accordiontab[@header='Control Variable']//div[@class='ag-header-cell-label']//span[text()='Value']")
    EditControlVarGridCultivation=(By.XPATH,"//app-usp-reactor-setup//p-accordiontab[@header='Control Variable']//div[@class='ag-header-cell-label']//span[text()='Cultivation Start Time(Hrs)']")
    EditControlVarGridUnit=(By.XPATH,"//app-usp-reactor-setup//p-accordiontab[@header='Control Variable']//div[@class='ag-header-cell-label']//span[text()='Unit']")

    EditVriables=(By.CSS_SELECTOR,"div[row-index='0'] app-usp-input-cell-renderer input[inputmode='decimal']")


    EditMediumGridName=(By.XPATH,"//app-usp-reactor-setup//p-accordiontab[@header='Control Variable']//div[@class='ag-header-cell-label']//span[text()='Medium Name']")
    EditMediumGridDesc=(By.XPATH,"//app-usp-reactor-setup//p-accordiontab[@header='Control Variable']//div[@class='ag-header-cell-label']//span[text()='Description']")
    EditMediumGridLLimit=(By.XPATH,"//app-usp-reactor-setup//p-accordiontab[@header='Control Variable']//div[@class='ag-header-cell-label']//span[text()='Lower Limit']")
    EditMediumGridULimit=(By.XPATH,"//app-usp-reactor-setup//p-accordiontab[@header='Control Variable']//div[@class='ag-header-cell-label']//span[text()='Upper Limit']")
    EditMediumGridUnit=(By.XPATH,"//app-usp-reactor-setup//p-accordiontab[@header='Control Variable']//div[@class='ag-header-cell-label']//span[text()='Units']")
    EditUseCaseCloseBtn=(By.CSS_SELECTOR,"button[data-pc-section='closebutton']")
    EditUseCaseSaveBtn=(By.CSS_SELECTOR,"p-button[label='Save'] button")
    EditUseCaseToast = (By.CSS_SELECTOR, "p-toastitem div[class*='p-toast-message']")

    RunSimulationBtn=(By.CSS_SELECTOR,"p-button[label='Run Simulation'] button")
    RunSimulationMsgBtn=(By.CSS_SELECTOR,"p-button[ptooltip='Messages'] button")
    RunSimulationReportsBtn=(By.CSS_SELECTOR,"p-button[ptooltip='Reports'] button")
    MsgBarTitle=(By.CSS_SELECTOR,"p-sidebar[class*='messagesSidebar '] div h3")
    MsgContentP1=(By.XPATH,"//p-sidebar[contains(@class,'messagesSidebar ')]//div/p[1]")
    MsgContentP2=(By.XPATH,"//p-sidebar[contains(@class,'messagesSidebar ')]//div/p[2]")
    MsgBarCloseBtn=(By.XPATH,"//p-sidebar[contains(@class,'messagesSidebar ')]//button[@data-pc-section='closebutton']")

    ReportPageTitle=(By.CSS_SELECTOR,"app-reports-usp-landing h1")
    BioMassPlotTitile=(By.CSS_SELECTOR,"app-reports-usp-landing text[data-unformatted='Biomass']")
    ProductPlotTitile = (By.CSS_SELECTOR, "app-reports-usp-landing text[data-unformatted='Product']")

    UseCaseStatus=(By.CSS_SELECTOR,"app-usp-icon-cell-renderer span")
    UseCaseListNameFilter = (By.XPATH,"//app-usp-usecase-list//div[@class='ag-header-cell-label']//span[contains(text(),'Name')]/parent::div/parent::div/span")
    SelectedUspLandingPageTitle=(By.CSS_SELECTOR,"app-usp-selected-usplanding h1")
    SelectUspLandingUseCases = (By.CSS_SELECTOR,"//app-usp-selected-usplanding//a[1]")
    SelectUspLandingUsp = (By.CSS_SELECTOR, "//app-usp-selected-usplanding//a[2]")

    UspListGridEditBtn=(By.CSS_SELECTOR,"app-usp-action-cell-renderer button")
    UspReactorSetupPageTitle = (By.CSS_SELECTOR,"app-usp-reactor-group-shell h1")
    UspTrainStepperStage1 = (By.CSS_SELECTOR,"app-usp-reactor-group-shell p-steps a[href*='/reactor-group/rg-list']")
    UspReactorGridName = (By.XPATH,"//app-usp-reactor-group-define//div[@class='ag-header-cell-label']//span[contains(text(),'Group Name')]")
    UspReactorGridType = (By.XPATH,"//app-usp-reactor-group-define//div[@class='ag-header-cell-label']//span[contains(text(),'Reactor Type')]")
    UspReactorGridVessel = (By.XPATH,"//app-usp-reactor-group-define//div[@class='ag-header-cell-label']//span[contains(text(),'Reactor Vessel Name')]")
    UspReactorGridExpand = (By.XPATH,"//span[@ref='eContracted']")
    ReactorAddBtn=(By.CSS_SELECTOR,"p-button[label='Create New Reactor Group'] button")
    UspTrainNextBtn=(By.CSS_SELECTOR,"p-button[label='Next'] button")

    UspTrainStepperStage2 = (By.CSS_SELECTOR, "app-usp-reactor-group-shell p-steps a[href*='/reactor-group/configure']")
    UspTrainStepperStage3 = (By.CSS_SELECTOR, "app-usp-reactor-group-shell p-steps a[href*='/reactor-group/summary']")
    UspTrainStepperStage4 = (By.CSS_SELECTOR, "app-usp-reactor-group-shell p-steps a[href*='/reactor-group/train']")
    UspConfigPageTitle=(By.CSS_SELECTOR,"app-usp-reactor-group-configure h3")
    UspConfigReactors=(By.CSS_SELECTOR,"app-usp-reactor-group-configure p")
    UspconfigDropDown=(By.CSS_SELECTOR,"app-usp-reactor-group-configure p-dropdown span")

    UspConfigCellGridName = (By.XPATH,"//app-usp-cells//div[@class='ag-header-cell-label']//span[contains(text(),'Name')]")
    UspConfigCellGridOrganism = (By.XPATH,"//app-usp-cells//div[@class='ag-header-cell-label']//span[contains(text(),'Organism')]")
    UspConfigCellGridHostLine = (By.XPATH,"//app-usp-cells//div[@class='ag-header-cell-label']//span[contains(text(),'Host Cell Line')]")
    UspConfigCellGridPMolecule = (By.XPATH,"//app-usp-cells//div[@class='ag-header-cell-label']//span[contains(text(),'Product Molecule')]")
    UspConfigCellGridMNM = (By.XPATH,"//app-usp-cells//div[@class='ag-header-cell-label']//span[contains(text(),'MNM')]")
    UspConfigCellGridNotes = (By.XPATH,"//app-usp-cells//div[@class='ag-header-cell-label']//span[contains(text(),'Notes')]")

    UspConfigReactor=(By.CSS_SELECTOR,"a[aria-label='Reactor Configuration']")
    UspConfigInflux=(By.CSS_SELECTOR,"a[aria-label='Setup Influxes']")
    UspConfigOutflux = (By.CSS_SELECTOR, "a[aria-label='Setup Outfluxes']")
    UspConfigReactorController = (By.XPATH,"//div[@class='reactor-configuration-shell']//p-accordiontab[2]")
    UspConfigReactorImpeller = (By.XPATH, "//div[@class='reactor-configuration-shell']//p-accordiontab[1]")
    UspConfigReactorSensor = (By.XPATH, "//div[@class='reactor-configuration-shell']//p-accordiontab[3]")

    UspConfigControllerGridName = (By.XPATH,"//div[@class='reactor-configuration-shell']//p-accordiontab[2]//div[@class='ag-header-cell-label']//span[contains(text(),'Name')]")
    UspConfigControllerGriddNotes = (By.XPATH,"//div[@class='reactor-configuration-shell']//p-accordiontab[2]//div[@class='ag-header-cell-label']//span[contains(text(),'Notes')]")
    UspConfigControllerGriddType = (By.XPATH,"//div[@class='reactor-configuration-shell']//p-accordiontab[2]//div[@class='ag-header-cell-label']//span[contains(text(),'Type')]")
    UspConfigControllerGridErr = (By.XPATH,"//div[@class='reactor-configuration-shell']//p-accordiontab[2]//div[@class='ag-header-cell-label']//span[contains(text(),'Error Model')]")
    UspConfigControllerGridparameter = (By.XPATH,"//div[@class='reactor-configuration-shell']//p-accordiontab[2]//div[@class='ag-header-cell-label']//span[contains(text(),'Parameter')]")
    UspConfigControllerGridValue = (By.XPATH,"//div[@class='reactor-configuration-shell']//p-accordiontab[2]//div[@class='ag-header-cell-label']//span[contains(text(),'Value')]")

    UspConfigimpelllerGridName = (By.XPATH,"//div[@class='reactor-configuration-shell']//p-accordiontab[1]//div[@class='ag-header-cell-label']//span[contains(text(),'Name')]")
    UspConfigimpelllerGridNotes = (By.XPATH,"//div[@class='reactor-configuration-shell']//p-accordiontab[1]//div[@class='ag-header-cell-label']//span[contains(text(),'Notes')]")
    UspConfigimpelllerGridDiameter = (By.XPATH,"//div[@class='reactor-configuration-shell']//p-accordiontab[1]//div[@class='ag-header-cell-label']//span[contains(text(),'Diameter')]")
    UspConfigimpelllerGridDiametrUnit = (By.XPATH,"//div[@class='reactor-configuration-shell']//p-accordiontab[1]//div[@class='ag-header-cell-label']//span[contains(text(),'Diameter Unit')]")
    UspConfigimpelllerGridLSpeed = (By.XPATH,"//div[@class='reactor-configuration-shell']//p-accordiontab[1]//div[@class='ag-header-cell-label']//span[contains(text(),'Low Limit Speed')]")
    UspConfigimpelllerGridHSpeed = (By.XPATH,"//div[@class='reactor-configuration-shell']//p-accordiontab[1]//div[@class='ag-header-cell-label']//span[contains(text(),'High Limit Speed')]")
    UspConfigimpelllerGridSpeedunit = (By.XPATH,"//div[@class='reactor-configuration-shell']//p-accordiontab[1]//div[@class='ag-header-cell-label']//span[contains(text(),'Speed Unit')]")


    UspConfigSensorGridName = (By.XPATH,"//div[@class='reactor-configuration-shell']//p-accordiontab[3]//div[@class='ag-header-cell-label']//span[contains(text(),'Name')]")
    UspConfigSensorGridNotes = (By.XPATH,"//div[@class='reactor-configuration-shell']//p-accordiontab[3]//div[@class='ag-header-cell-label']//span[contains(text(),'Notes')]")
    UspConfigSensorGridMediumObject = (By.XPATH,"//div[@class='reactor-configuration-shell']//p-accordiontab[3]//div[@class='ag-header-cell-label']//span[contains(text(),'Medium Object')]")
    UspConfigSensorGridLowLimit = (By.XPATH,"//div[@class='reactor-configuration-shell']//p-accordiontab[3]//div[@class='ag-header-cell-label']//span[contains(text(),'Low Limit')]")
    UspConfigSensorGridHighLimit = (By.XPATH,"//div[@class='reactor-configuration-shell']//p-accordiontab[3]//div[@class='ag-header-cell-label']//span[contains(text(),'High Limit')]")
    UspConfigSensorGridUnit = (By.XPATH,"//div[@class='reactor-configuration-shell']//p-accordiontab[3]//div[@class='ag-header-cell-label']//span[contains(text(),'Unit')]")

    UspConfigInfluxGridInletName = (By.XPATH,"//app-usp-setup-influxes-shell//div[@class='ag-header-cell-label']//span[contains(text(),'Inlet Name')]")
    UspConfigInfluxGridType = (By.XPATH,"//app-usp-setup-influxes-shell//div[@class='ag-header-cell-label']//span[contains(text(),'Influx Type')]")
    UspConfigInfluxGridMedium = (By.XPATH,"//app-usp-setup-influxes-shell//div[@class='ag-header-cell-label']//span[contains(text(),'Medium')]")
    UspConfigInfluxGridErr = (By.XPATH,"//app-usp-setup-influxes-shell//div[@class='ag-header-cell-label']//span[contains(text(),'Error Model')]")
    UspConfigInfluxGridControlName = (By.XPATH,"//app-usp-setup-influxes-shell//div[@class='ag-header-cell-label']//span[contains(text(),'Controller Name')]")

    UspConfigOutfluxGridInletName = (By.XPATH,"//app-usp-setup-outfluxes-shell//div[@class='ag-header-cell-label']//span[contains(text(),'Outlet Name')]")
    UspConfigOutfluxGridType = (By.XPATH,"//app-usp-setup-outfluxes-shell//div[@class='ag-header-cell-label']//span[contains(text(),'Outflux Type')]")
    UspConfigOutfluxGridRetention = (By.XPATH,"//app-usp-setup-outfluxes-shell//div[@class='ag-header-cell-label']//span[contains(text(),'Retention')]")
    UspConfigOutfluxGridErr = (By.XPATH,"//app-usp-setup-outfluxes-shell//div[@class='ag-header-cell-label']//span[contains(text(),'Error Model')]")
    UspConfigOutfluxGridControlName = (By.XPATH,"//app-usp-setup-outfluxes-shell//div[@class='ag-header-cell-label']//span[contains(text(),'Controller Name')]")


    UspTrainSummaryGridGroups = (By.XPATH,"//app-usp-reactor-group-summary//div[@class='ag-header-cell-label']//span[contains(text(),'Groups')]")
    UspTrainSummaryGridImpellerName = (By.XPATH,"//app-usp-reactor-group-summary//div[@class='ag-header-cell-label']//span[contains(text(),'Impeller Name')]")
    UspTrainSummaryGridNoOfInlets = (By.XPATH,"//app-usp-reactor-group-summary//div[@class='ag-header-cell-label']//span[contains(text(),'No of Inlets')]")
    UspTrainSummaryGridNoOfOutlets = (By.XPATH,"//app-usp-reactor-group-summary//div[@class='ag-header-cell-label']//span[contains(text(),'No of Outlets')]")
    UspTrainSummaryGridControllers = (By.XPATH,"//app-usp-reactor-group-summary//div[@class='ag-header-cell-label']//span[contains(text(),'Controllers')]")
    UspTrainSummaryGridSensors = (By.XPATH,"//app-usp-reactor-group-summary//div[@class='ag-header-cell-label']//span[contains(text(),'Sensors')]")

    UspTrainGridCultivation = (By.XPATH,"//app-usp-reactor-group-train//div[@class='ag-header-cell-label']//span[contains(text(),'Cultivations')]")
    UspTrainGridCells = (By.XPATH,"//app-usp-reactor-group-train//div[@class='ag-header-cell-label']//span[contains(text(),'Cells')]")
    UspTrainGridNotes = (By.XPATH,"//app-usp-reactor-group-train//div[@class='ag-header-cell-label']//span[contains(text(),'Notes')]")
    UspTrainGridIncude = (By.XPATH,"//app-usp-reactor-group-train//div[@class='ag-header-cell-label']//span[contains(text(),'Include')]")

    UspRunTrainBtn=(By.CSS_SELECTOR,"app-usp-reactor-group-train p-button[ptooltip='Run Training'] button")
    UspTrainMsgBtn = (By.CSS_SELECTOR, "p-button[ptooltip='Messages'] button")
    UspTrainReportBtn = (By.CSS_SELECTOR, "p-button[ptooltip='Reports'] button")
    UspTrainReportMetricsTitle = (By.XPATH,"//app-reports-usp-simulation-landing//div[1]//h1")
    UspTrainReportPlotTitle = (By.XPATH, "//app-reports-usp-simulation-landing//div[2]//h1")
    UspMetricsReportGridStateName=(By.XPATH,"//app-reports-usp-simulation-landing//div[1]//div[@class='ag-header-cell-label']//span[contains(text(),'State Name')]")
    UspMetricsReportGridTrainData=(By.XPATH,"//app-reports-usp-simulation-landing//div[1]//div[@class='ag-header-cell-label']//span[contains(text(),'Train Data')]")
    UspMetricsReportGridTestData=(By.XPATH,"//app-reports-usp-simulation-landing//div[1]//div[@class='ag-header-cell-label']//span[contains(text(),'Test Data')]")
    UspTrainStatus=(By.CSS_SELECTOR,"app-usp-usp-list app-usp-status-cell-renderer")


    def GetWsUspLandingPage(self):
        return self.driver.find_element(*UspPage.WsUspLandingPage)

    def GetUspLandingPageTitle(self):
        return self.driver.find_element(*UspPage.UspLandingPageTitle)
    def GetUspListGridName(self):
        return self.driver.find_element(*UspPage.UspListGridName)
    def GetUspListGridDesc(self):
        return self.driver.find_element(*UspPage.UspListGridDesc)
    def GetUspListGridNumReactor(self):
        return self.driver.find_element(*UspPage.UspListGridNumReactor)
    def GetUspListGridStatus(self):
        return self.driver.find_element(*UspPage.UspListGridStatus)
    def GetUspListGridAction(self):
        return self.driver.find_element(*UspPage.UspListGridAction)
    def GetUspAddBtn(self):
        return self.driver.find_element(*UspPage.UspAddBtn)
    def GetUspAddName(self):
        return self.driver.find_element(*UspPage.UspAddName)
    def GetUspAddDesc(self):
        return self.driver.find_element(*UspPage.UspAddDesc)
    def GetUspCreateBtn(self):
        return self.driver.find_element(*UspPage.UspCreateBtn)
    def GetUspAddTitle(self):
        return self.driver.find_element(*UspPage.UspAddTitle)
    def GetUspAddSubTitle(self):
        return self.driver.find_element(*UspPage.UspAddSubTitle)
    def GetUspListGridNameFilter(self):
        return self.driver.find_element(*UspPage.UspListGridNameFilter)
    def GetFilterSearBox(self):
        return self.driver.find_element(*UspPage.FilterSearBox)
    def GetFilterApplyBtn(self):
        return self.driver.find_element(*UspPage.FilterApplyBtn)
    def GetSelectUSP(self):
        return self.driver.find_element(*UspPage.SelectUSP)
    def GetUseCaseListPageTitle(self):
        return self.driver.find_element(*UspPage.UseCaseListPageTitle)
    def GetUseCaseGridName(self):
        return self.driver.find_element(*UspPage.UseCaseGridName)
    def GetUseCaseGridDesc(self):
        return self.driver.find_element(*UspPage.UseCaseGridDesc)
    def GetUseCaseGridPrediction(self):
        return self.driver.find_element(*UspPage.UseCaseGridPrediction)
    def GetUseCaseGridType(self):
        return self.driver.find_element(*UspPage.UseCaseGridType)
    def GetUseCaseGridStatus(self):
        return self.driver.find_element(*UspPage.UseCaseGridStatus)
    def GetUseCaseAddBtn(self):
        return self.driver.find_element(*UspPage.UseCaseAddBtn)
    def GetUseCaseAddName(self):
        return self.driver.find_element(*UspPage.UseCaseAddName)
    def GetUseCaseCreateBtn(self):
        return self.driver.find_element(*UspPage.UseCaseCreateBtn)
    def GetUseCaseReactorList(self):
        return self.driver.find_element(*UspPage.UseCaseReactorList)
    def GetUseCaseReactorName(self):
        return self.driver.find_element(*UspPage.UseCaseReactorName)
    def GetUseCaseReactorType(self):
        return self.driver.find_element(*UspPage.UseCaseReactorType)
    def GetUseCaseReactorCells(self):
        return self.driver.find_element(*UspPage.UseCaseReactorCells)
    def GetUseCaseReactorReactor(self):
        return self.driver.find_element(*UspPage.UseCaseReactorReactor)
    def GetUseCaseReactorStatus(self):
        return self.driver.find_element(*UspPage.UseCaseReactorStatus)
    def GetUseCaseEditBtn(self):
        return self.driver.find_element(*UspPage.UseCaseEditBtn)
    def GetEditUseCaseTitle(self):
        return self.driver.find_element(*UspPage.EditUseCaseTitle)
    def GetEditUseCaseControlVar(self):
        return self.driver.find_element(*UspPage.EditUseCaseControlVar)
    def GetEditUseCaseMediaVar(self):
        return self.driver.find_element(*UspPage.EditUseCaseMediaVar)
    def GetEditControlVarGridName(self):
        return self.driver.find_element(*UspPage.EditControlVarGridName)
    def GetEditControlVarGridParamName(self):
        return self.driver.find_element(*UspPage.EditControlVarGridParamName)
    def GetEditControlVarGridDesc(self):
        return self.driver.find_element(*UspPage.EditControlVarGridDesc)
    def GetEditControlVarGridParamType(self):
        return self.driver.find_element(*UspPage.EditControlVarGridParamType)
    def GetEditControlVarGridValue(self):
        return self.driver.find_element(*UspPage.EditControlVarGridValue)
    def GetEditControlVarGridCultivation(self):
        return self.driver.find_element(*UspPage.EditControlVarGridCultivation)
    def GetEditControlVarGridUnit(self):
        return self.driver.find_element(*UspPage.EditControlVarGridUnit)
    def GetEditVriables(self):
        return self.driver.find_element(*UspPage.EditVriables)
    def GetEditMediumGridName(self):
        return self.driver.find_element(*UspPage.EditMediumGridName)
    def GetEditMediumGridDesc(self):
        return self.driver.find_element(*UspPage.EditMediumGridDesc)
    def GetEditMediumGridLLimit(self):
        return self.driver.find_element(*UspPage.EditMediumGridLLimit)
    def GetEditMediumGridULimit(self):
        return self.driver.find_element(*UspPage.EditMediumGridULimit)
    def GetEditMediumGridUnit(self):
        return self.driver.find_element(*UspPage.EditMediumGridUnit)
    def GetEditUseCaseCloseBtn(self):
        return self.driver.find_element(*UspPage.EditUseCaseCloseBtn)
    def GetEditUseCaseSaveBtn(self):
        return self.driver.find_element(*UspPage.EditUseCaseSaveBtn)
    def GetEditUseCaseToast(self):
        return self.driver.find_element(*UspPage.EditUseCaseToast)
    def GetRunSimulationBtn(self):
        return self.driver.find_element(*UspPage.RunSimulationBtn)
    def GetRunSimulationMsgBtn(self):
        return self.driver.find_element(*UspPage.RunSimulationMsgBtn)
    def GetRunSimulationReportsBtn(self):
        return self.driver.find_element(*UspPage.RunSimulationReportsBtn)
    def GetMsgBarTitle(self):
        return self.driver.find_element(*UspPage.MsgBarTitle)
    def GetMsgContentP1(self):
        return self.driver.find_element(*UspPage.MsgContentP1)
    def GetMsgContentP2(self):
        return self.driver.find_element(*UspPage.MsgContentP2)
    def GetMsgBarCloseBtn(self):
        return self.driver.find_element(*UspPage.MsgBarCloseBtn)
    def GetReportPageTitle(self):
        return self.driver.find_element(*UspPage.ReportPageTitle)
    def GetBioMassPlotTitile(self):
        return self.driver.find_element(*UspPage.BioMassPlotTitile)
    def GetProductPlotTitile(self):
        return self.driver.find_element(*UspPage.ProductPlotTitile)
    def GetUseCaseStatus(self):
        return self.driver.find_element(*UspPage.UseCaseStatus)
    def GetUseCaseListNameFilter(self):
        return self.driver.find_element(*UspPage.UseCaseListNameFilter)
    def GetSelectedUspLandingPageTitle(self):
        return self.driver.find_element(*UspPage.SelectedUspLandingPageTitle)
    def GetSelectUspLandingUseCases(self):
        return self.driver.find_element(*UspPage.SelectUspLandingUseCases)
    def GetSelectUspLandingUsp(self):
        return self.driver.find_element(*UspPage.SelectUspLandingUsp)
    def GetUspListGridEditBtn(self):
        return self.driver.find_element(*UspPage.UspListGridEditBtn)
    def GetUspReactorSetupPageTitle(self):
        return self.driver.find_element(*UspPage.UspReactorSetupPageTitle)
    def GetUspTrainStepperStage1(self):
        return self.driver.find_element(*UspPage.UspTrainStepperStage1)
    def GetUspReactorGridName(self):
        return self.driver.find_element(*UspPage.UspReactorGridName)
    def GetUspReactorGridType(self):
        return self.driver.find_element(*UspPage.UspReactorGridType)
    def GetUspReactorGridVessel(self):
        return self.driver.find_element(*UspPage.UspReactorGridVessel)
    def GetUspReactorGridExpand(self):
        return self.driver.find_element(*UspPage.UspReactorGridExpand)
    def GetReactorAddBtn(self):
        return self.driver.find_element(*UspPage.ReactorAddBtn)
    def GetUspTrainNextBtn(self):
        return self.driver.find_element(*UspPage.UspTrainNextBtn)
    def GetUspTrainStepperStage2(self):
        return self.driver.find_element(*UspPage.UspTrainStepperStage2)
    def GetUspConfigPageTitle(self):
        return self.driver.find_element(*UspPage.UspConfigPageTitle)
    def GetUspConfigReactors(self):
        return self.driver.find_element(*UspPage.UspConfigReactors)
    def GetUspconfigDropDown(self):
        return self.driver.find_element(*UspPage.UspconfigDropDown)
    def GetUspConfigCellGridName(self):
        return self.driver.find_element(*UspPage.UspConfigCellGridName)
    def GetUspConfigCellGridOrganism(self):
        return self.driver.find_element(*UspPage.UspConfigCellGridOrganism)
    def GetUspConfigCellGridHostLine(self):
        return self.driver.find_element(*UspPage.UspConfigCellGridHostLine)
    def GetUspConfigCellGridPMolecule(self):
        return self.driver.find_element(*UspPage.UspConfigCellGridPMolecule)
    def GetUspConfigCellGridMNM(self):
        return self.driver.find_element(*UspPage.UspConfigCellGridMNM)
    def GetUspConfigCellGridNotes(self):
        return self.driver.find_element(*UspPage.UspConfigCellGridNotes)
    def GetUspConfigReactor(self):
        return self.driver.find_element(*UspPage.UspConfigReactor)
    def GetUspConfigInflux(self):
        return self.driver.find_element(*UspPage.UspConfigInflux)
    def GetUspConfigOutflux(self):
        return self.driver.find_element(*UspPage.UspConfigOutflux)
    def GetUspConfigReactorController(self):
        return self.driver.find_element(*UspPage.UspConfigReactorController)
    def GetUspConfigControllerGridName(self):
        return self.driver.find_element(*UspPage.UspConfigControllerGridName)
    def GetUspConfigControllerGriddNotes(self):
        return self.driver.find_element(*UspPage.UspConfigControllerGriddNotes)
    def GetUspConfigControllerGriddType(self):
        return self.driver.find_element(*UspPage.UspConfigControllerGriddType)
    def GetUspConfigControllerGridErr(self):
        return self.driver.find_element(*UspPage.UspConfigControllerGridErr)
    def GetUspConfigControllerGridparameter(self):
        return self.driver.find_element(*UspPage.UspConfigControllerGridparameter)
    def GetUspConfigControllerGridValue(self):
        return self.driver.find_element(*UspPage.UspConfigControllerGridValue)
    def GetUspConfigimpelllerGridName(self):
        return self.driver.find_element(*UspPage.UspConfigimpelllerGridName)
    def GetUspConfigimpelllerGridNotes(self):
        return self.driver.find_element(*UspPage.UspConfigimpelllerGridNotes)
    def GetUspConfigimpelllerGridDiameter(self):
        return self.driver.find_element(*UspPage.UspConfigimpelllerGridDiameter)
    def GetUspConfigimpelllerGridDiametrUnit(self):
        return self.driver.find_element(*UspPage.UspConfigimpelllerGridDiametrUnit)
    def GetUspConfigimpelllerGridLSpeed(self):
        return self.driver.find_element(*UspPage.UspConfigimpelllerGridLSpeed)
    def GetUspConfigimpelllerGridHSpeed(self):
        return self.driver.find_element(*UspPage.UspConfigimpelllerGridHSpeed)
    def GetUspConfigimpelllerGridSpeedunit(self):
        return self.driver.find_element(*UspPage.UspConfigimpelllerGridSpeedunit)
    def GetUspConfigSensorGridName(self):
        return self.driver.find_element(*UspPage.UspConfigSensorGridName)
    def GetUspConfigSensorGridNotes(self):
        return self.driver.find_element(*UspPage.UspConfigSensorGridNotes)
    def GetUspConfigSensorGridMediumObject(self):
        return self.driver.find_element(*UspPage.UspConfigSensorGridMediumObject)
    def GetUspConfigSensorGridLowLimit(self):
        return self.driver.find_element(*UspPage.UspConfigSensorGridLowLimit)
    def GetUspConfigSensorGridHighLimit(self):
        return self.driver.find_element(*UspPage.UspConfigSensorGridHighLimit)
    def GetUspConfigSensorGridUnit(self):
        return self.driver.find_element(*UspPage.UspConfigSensorGridUnit)
    def GetUspConfigInfluxGridInletName(self):
        return self.driver.find_element(*UspPage.UspConfigInfluxGridInletName)
    def GetUspConfigInfluxGridType(self):
        return self.driver.find_element(*UspPage.UspConfigInfluxGridType)
    def GetUspConfigInfluxGridMedium(self):
        return self.driver.find_element(*UspPage.UspConfigInfluxGridMedium)
    def GetUspConfigInfluxGridErr(self):
        return self.driver.find_element(*UspPage.UspConfigInfluxGridErr)
    def GetUspConfigInfluxGridControlName(self):
        return self.driver.find_element(*UspPage.UspConfigInfluxGridControlName)
    def GetUspConfigOutfluxGridInletName(self):
        return self.driver.find_element(*UspPage.UspConfigOutfluxGridInletName)
    def GetUspConfigOutfluxGridType(self):
        return self.driver.find_element(*UspPage.UspConfigOutfluxGridType)
    def GetUspConfigOutfluxGridRetention(self):
        return self.driver.find_element(*UspPage.UspConfigOutfluxGridRetention)
    def GetUspConfigOutfluxGridErr(self):
        return self.driver.find_element(*UspPage.UspConfigOutfluxGridErr)
    def GetUspConfigOutfluxGridControlName(self):
        return self.driver.find_element(*UspPage.UspConfigOutfluxGridControlName)
    def GetUspTrainSummaryGridGroups(self):
        return self.driver.find_element(*UspPage.UspTrainSummaryGridGroups)
    def GetUspTrainSummaryGridImpellerName(self):
        return self.driver.find_element(*UspPage.UspTrainSummaryGridImpellerName)
    def GetUspTrainSummaryGridNoOfInlets(self):
        return self.driver.find_element(*UspPage.UspTrainSummaryGridNoOfInlets)
    def GetUspTrainSummaryGridNoOfOutlets(self):
        return self.driver.find_element(*UspPage.UspTrainSummaryGridNoOfOutlets)
    def GetUspTrainSummaryGridControllers(self):
        return self.driver.find_element(*UspPage.UspTrainSummaryGridControllers)
    def GetUspTrainSummaryGridSensors(self):
        return self.driver.find_element(*UspPage.UspTrainSummaryGridSensors)
    def GetUspTrainGridCultivation(self):
        return self.driver.find_element(*UspPage.UspTrainGridCultivation)
    def GetUspTrainGridCells(self):
        return self.driver.find_element(*UspPage.UspTrainGridCells)
    def GetUspTrainGridNotes(self):
        return self.driver.find_element(*UspPage.UspTrainGridNotes)
    def GetUspTrainGridIncude(self):
        return self.driver.find_element(*UspPage.UspTrainGridIncude)
    def GetUspRunTrainBtn(self):
        return self.driver.find_element(*UspPage.UspRunTrainBtn)
    def GetUspTrainMsgBtn(self):
        return self.driver.find_element(*UspPage.UspTrainMsgBtn)
    def GetUspTrainReportBtn(self):
        return self.driver.find_element(*UspPage.UspTrainReportBtn)
    def GetUspTrainReportMetricsTitle(self):
        return self.driver.find_element(*UspPage.UspTrainReportMetricsTitle)
    def GetUspTrainReportPlotTitle(self):
        return self.driver.find_element(*UspPage.UspTrainReportPlotTitle)
    def GetUspMetricsReportGridStateName(self):
        return self.driver.find_element(*UspPage.UspMetricsReportGridStateName)
    def GetUspMetricsReportGridTrainData(self):
        return self.driver.find_element(*UspPage.UspMetricsReportGridTrainData)
    def GetUspMetricsReportGridTestData(self):
        return self.driver.find_element(*UspPage.UspMetricsReportGridTestData)
    def GetUspTrainStatus(self):
        return self.driver.find_element(*UspPage.UspTrainStatus)
    def GetUspConfigReactorImpeller(self):
        return self.driver.find_element(*UspPage.UspConfigReactorImpeller)

    def GetUspConfigReactorSensor(self):
        return self.driver.find_element(*UspPage.UspConfigReactorSensor)
    def GetUspTrainStepperStage3(self):
        return self.driver.find_element(*UspPage.UspTrainStepperStage3)
    def GetUspTrainStepperStage4(self):
        return self.driver.find_element(*UspPage.UspTrainStepperStage4)
    def GetUseCaseGridPredictionType(self):
        return self.driver.find_element(*UspPage.UseCaseGridPredictionType)
    def GetUseCaseGridPredictionTypeSimulation(self):
        return self.driver.find_element(*UspPage.UseCaseGridPredictionTypeSimulation)

    def GetUseCaseSetpDropDown(self):
        return self.driver.find_element(*UspPage.UseCaseSetpDropDown)

    def GetUseCaseSetupReactor(self):
        return self.driver.find_element(*UspPage.UseCaseSetupReactor)
    def GetUseCaseAddDesc(self):
        return self.driver.find_element(*UspPage.UseCaseAddDesc)
    def GetSelectUC(self):
        return self.driver.find_element(*UspPage.SelectUC)
    def GetUseCaseGridPredictionTypeOptimization(self):
        return self.driver.find_element(*UspPage.UseCaseGridPredictionTypeOptimization)