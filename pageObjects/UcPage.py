from selenium.webdriver.common.by import By
import pytest
class UcPage:

    def __init__(self, driver):
        self.driver = driver

    OptimizationPageTitle = (By.CSS_SELECTOR,"app-usp-usecase-optimization h1")
    OptUcReactorName = (By.XPATH, "//app-usp-usecase-optimization//div[@class='ag-header-cell-label']//span[contains(text(),'Group Name')]")
    OptUcReactorType = (By.XPATH, "//app-usp-usecase-optimization//div[@class='ag-header-cell-label']//span[contains(text(),'Reactor Type')]")
    OptUcReactors = (By.XPATH, "//app-usp-usecase-optimization//div[@class='ag-header-cell-label']//span[contains(text(),'Reactor Vessel Name')]")
    OptUcStepperStage1 = (By.XPATH,"//app-usp-usecase-optimization//li[1]//span[contains(@class,'step-name')]")
    OptUcStepperStage2 = (By.XPATH,"//app-usp-usecase-optimization//li[2]//span[contains(@class,'step-name')]")
    OptUcStepperStage3 = (By.XPATH, "//app-usp-usecase-optimization//li[3]//span[contains(@class,'step-name')]")
    OptUcStepperStage4 = (By.XPATH, "//app-usp-usecase-optimization//li[4]//span[contains(@class,'step-name')]")
    OptUcNextBtn = (By.XPATH,"//app-usp-usecase-optimization//span[contains(text(),'Next')]/parent::button")
    OptPONextBtn = (By.XPATH,"(//app-usp-usecase-optimization//span[contains(text(),'Next')]/parent::button)[2]")
    OptDesignSpaceNextBtn = (By.XPATH,"(//app-usp-usecase-optimization//span[contains(text(),'Next')]/parent::button)[4]")
    OptSummaryNextBtn = (By.XPATH, "(//app-usp-usecase-optimization//span[contains(text(),'Next')]/parent::button)[5]")
    OptSaveConfigBtn = (By.CSS_SELECTOR,"app-usp-usecase-configuration p-button[label='Save Configurations'] button")
    EditUseCaseToast1 = (By.XPATH, "//p-toastitem//div[contains(@class,'p-toast-message-success')]")


    OptPeformObective = (By.XPATH,"//app-usp-objective-function//div[contains(@class,'p-stepper-panel')][1]/div/p-stepperheader/button")
    OptPerformObectiveNextBtn = (By.XPATH,"//app-usp-objective-function//div[contains(@class,'p-stepper-panel')][1]//p-button[@label='Next']/button")
    OptPOveGridObjective = (By.XPATH,"//app-usp-objective-function//div[contains(@class,'p-stepper-panel')][1]//div[@class='ag-header-cell-label']//span[contains(text(),'Objective')]")
    OptPOveGridComponent = (By.XPATH,"//app-usp-objective-function//div[contains(@class,'p-stepper-panel')][1]//div[@class='ag-header-cell-label']//span[contains(text(),'Component')]")
    OptPOveGridWeight = (By.XPATH,"//app-usp-objective-function//div[contains(@class,'p-stepper-panel')][1]//div[@class='ag-header-cell-label']//span[contains(text(),'Weight')]")
    OptPOveGridAttribute = (By.XPATH,"//app-usp-objective-function//div[contains(@class,'p-stepper-panel')][1]//div[@class='ag-header-cell-label']//span[contains(text(),'Attribute')]")
    OptPOveGridVariable = (By.XPATH,"//app-usp-objective-function//div[contains(@class,'p-stepper-panel')][1]//div[@class='ag-header-cell-label']//span[contains(text(),'Variable')]")
    OptPOveGridalltime = (By.XPATH,"//app-usp-objective-function//div[contains(@class,'p-stepper-panel')][1]//div[@class='ag-header-cell-label']//span[contains(text(),'All / Time')]")
    OptPOveGridValue = (By.XPATH,"//app-usp-objective-function//div[contains(@class,'p-stepper-panel')][1]//div[@class='ag-header-cell-label']//span[contains(text(),'Value')]")
    OptDesignSpaceRGroup = (By.XPATH,"//app-usp-usecase-configuration//p-dropdown[@formcontrolname='reactorGroup']")
    OptDesignSpaceRVessel = (By.XPATH, "//app-usp-usecase-configuration//p-dropdown[@formcontrolname='reactorVessel']")
    OptDesignSpaceReactorVariable = (By.XPATH, "//app-usp-usecase-configuration//li[contains(@class,'p-tabmenuitem')][1]")
    OptDesignSpaceReactorConstraints = (By.XPATH, "//app-usp-usecase-configuration//li[contains(@class,'p-tabmenuitem')][2]")

    OptDesignSpaceRVAgitation = (By.XPATH, "//app-usp-usecase-reactor-control-variable//div[contains(@class,'p-stepper-panel')][1]/div/p-stepperheader/button")
    OptRvGridAgitationImpeller = (By.XPATH, "//app-usp-usecase-reactor-control-variable//div[contains(@class,'p-stepper-panel')][1]//div[@class='ag-header-cell-label']//span[contains(text(),'Impeller')]")
    OptRvGridAgitationController = (By.XPATH, "//app-usp-usecase-reactor-control-variable//div[contains(@class,'p-stepper-panel')][1]//div[@class='ag-header-cell-label']//span[contains(text(),'Controller')]")
    OptRvGridAgitationModify = (By.XPATH, "//app-usp-usecase-reactor-control-variable//div[contains(@class,'p-stepper-panel')][1]//div[@class='ag-header-cell-label']//span[contains(text(),'Modify')]")
    OptRvGridAgitationControlerOpt = (By.XPATH, "//app-usp-usecase-reactor-control-variable//div[contains(@class,'p-stepper-panel')][1]//div[@class='ag-header-cell-label']//span[contains(text(),'Controller(Optimization)')]")
    optRVAgitationNextBtn = (By.XPATH,"//app-usp-usecase-reactor-control-variable//div[contains(@class,'p-stepper-panel')][1]//p-button[@label='Next']")


    OptDesignSpaceRVInflux = (By.XPATH, "//app-usp-usecase-reactor-control-variable//div[contains(@class,'p-stepper-panel')][2]/div/p-stepperheader/button")
    OptRvGridInfluxInletName = (By.XPATH, "//app-usp-usecase-reactor-control-variable//div[contains(@class,'p-stepper-panel')][2]//div[@class='ag-header-cell-label']//span[contains(text(),'Inlet Name')]")
    OptRvGridInfluxtype = (By.XPATH, "//app-usp-usecase-reactor-control-variable//div[contains(@class,'p-stepper-panel')][2]//div[@class='ag-header-cell-label']//span[contains(text(),'Influx Type')]")
    OptRvGridInfluxNotes = (By.XPATH, "//app-usp-usecase-reactor-control-variable//div[contains(@class,'p-stepper-panel')][2]//div[@class='ag-header-cell-label']//span[contains(text(),'Notes')]")
    optRVInfluxNextBtn = (By.XPATH,"//app-usp-usecase-reactor-control-variable//div[contains(@class,'p-stepper-panel')][2]//p-button[@label='Next']")
    optRVInfluxPrevBtn = (By.XPATH,"//app-usp-usecase-reactor-control-variable//div[contains(@class,'p-stepper-panel')][2]//p-button[@label='Previous']")

    OptDesignSpaceRVOutflux = (By.XPATH, "//app-usp-usecase-reactor-control-variable//div[contains(@class,'p-stepper-panel')][3]/div/p-stepperheader/button")
    OptRvGridOutfluxOutletName = (By.XPATH, "//app-usp-usecase-reactor-control-variable//div[contains(@class,'p-stepper-panel')][3]//div[@class='ag-header-cell-label']//span[contains(text(),'Outlet Name')]")
    OptRvGridOutfluxtype = (By.XPATH, "//app-usp-usecase-reactor-control-variable//div[contains(@class,'p-stepper-panel')][3]//div[@class='ag-header-cell-label']//span[contains(text(),'Outflux Type')]")
    OptRvGridOutfluxNotes = (By.XPATH, "//app-usp-usecase-reactor-control-variable//div[contains(@class,'p-stepper-panel')][3]//div[@class='ag-header-cell-label']//span[contains(text(),'Notes')]")
    optRVOutfluxNextBtn = (By.XPATH,"//app-usp-usecase-reactor-control-variable//div[contains(@class,'p-stepper-panel')][3]//p-button[@label='Next']")
    optRVOutfluxPrevBtn = (By.XPATH,"//app-usp-usecase-reactor-control-variable//div[contains(@class,'p-stepper-panel')][3]//p-button[@label='Previous']")


    OptDesignSpaceGenController = (By.XPATH, "//app-usp-usecase-reactor-control-variable//div[contains(@class,'p-stepper-panel')][4]/div/p-stepperheader/button")
    OptRvGridGenController = (By.XPATH, "//app-usp-usecase-reactor-control-variable//div[contains(@class,'p-stepper-panel')][4]//div[@class='ag-header-cell-label']//span[contains(text(),'Controller')]")
    OptRvGridGenControllerModify = (By.XPATH, "//app-usp-usecase-reactor-control-variable//div[contains(@class,'p-stepper-panel')][4]//div[@class='ag-header-cell-label']//span[contains(text(),'Modify')]")
    OptRvGridGenControllerOpt = (By.XPATH, "//app-usp-usecase-reactor-control-variable//div[contains(@class,'p-stepper-panel')][4]//div[@class='ag-header-cell-label']//span[contains(text(),'Controller(Optimization)')]")
    optRVGenControllerNextBtn = (By.XPATH,"//app-usp-usecase-reactor-control-variable//div[contains(@class,'p-stepper-panel')][4]//p-button[@label='Next']")
    optRVGenControllerPrevBtn = (By.XPATH,"//app-usp-usecase-reactor-control-variable//div[contains(@class,'p-stepper-panel')][4]//p-button[@label='Previous']")


    OptConstraintsReactorVolume = (By.XPATH, "//app-usp-usecase-config-constraint//div[contains(@class,'p-stepper-panel')][1]/div/p-stepperheader/button")
    OptReactorVolumeGridLLimit = (By.XPATH, "//app-usp-usecase-config-constraint//div[contains(@class,'p-stepper-panel')][1]//div[@class='ag-header-cell-label']//span[contains(text(),'Lower Limit')]")
    OptReactorVolumeGridHLimit = (By.XPATH, "//app-usp-usecase-config-constraint//div[contains(@class,'p-stepper-panel')][1]//div[@class='ag-header-cell-label']//span[contains(text(),'Upper Limit')]")
    optReactorVolumeNextBtn = (By.XPATH,"//app-usp-usecase-config-constraint//div[contains(@class,'p-stepper-panel')][1]//p-button[@label='Next']")
    optReactorVolumePrevBtn = (By.XPATH,"//app-usp-usecase-config-constraint//div[contains(@class,'p-stepper-panel')][1]//p-button[@label='Previous']")

    OptConstraintsOsmolality = (By.XPATH, "//app-usp-usecase-config-constraint//div[contains(@class,'p-stepper-panel')][2]/div/p-stepperheader/button")
    OptOsmolalityGridLLimit = (By.XPATH, "//app-usp-usecase-config-constraint//div[contains(@class,'p-stepper-panel')][2]//div[@class='ag-header-cell-label']//span[contains(text(),'Lower Limit')]")
    OptOsmolalityGridHLimit = (By.XPATH, "//app-usp-usecase-config-constraint//div[contains(@class,'p-stepper-panel')][2]//div[@class='ag-header-cell-label']//span[contains(text(),'Upper Limit')]")
    optOsmolalityNextBtn = (By.XPATH,"//app-usp-usecase-config-constraint//div[contains(@class,'p-stepper-panel')][2]//p-button[@label='Next']")
    optOsmolalityPrevBtn = (By.XPATH,"//app-usp-usecase-config-constraint//div[contains(@class,'p-stepper-panel')][2]//p-button[@label='Previous']")

    OptConstraintsPQA = (By.XPATH,"//app-usp-usecase-config-constraint//div[contains(@class,'p-stepper-panel')][3]/div/p-stepperheader/button")
    OptPQAGridAttributeName = (By.XPATH,"//app-usp-usecase-config-constraint//div[contains(@class,'p-stepper-panel')][3]//div[@class='ag-header-cell-label']//span[contains(text(),'Attribute Name')]")
    OptPQAGridLlimitRef = (By.XPATH,"//app-usp-usecase-config-constraint//div[contains(@class,'p-stepper-panel')][3]//div[@class='ag-header-cell-label']//span[contains(text(),'Lower limit ref')]")
    OptPQAGridLlimitOpt = (By.XPATH,"//app-usp-usecase-config-constraint//div[contains(@class,'p-stepper-panel')][3]//div[@class='ag-header-cell-label']//span[contains(text(),'Lower limit for Optimization')]")
    OptPQAGridHlimitRef = (By.XPATH,"//app-usp-usecase-config-constraint//div[contains(@class,'p-stepper-panel')][3]//div[@class='ag-header-cell-label']//span[contains(text(),'Upper limit ref')]")
    OptPQAGridHlimitOpt = (By.XPATH,"//app-usp-usecase-config-constraint//div[contains(@class,'p-stepper-panel')][3]//div[@class='ag-header-cell-label']//span[contains(text(),'Upper limit for Optimization')]")
    optPQANextBtn = (By.XPATH,"//app-usp-usecase-config-constraint//div[contains(@class,'p-stepper-panel')][3]//p-button[@label='Next']")
    optPQAPrevBtn = (By.XPATH,"//app-usp-usecase-config-constraint//div[contains(@class,'p-stepper-panel')][3]//p-button[@label='Previous']")


    OptConstraintsConMetabolite = (By.XPATH,"//app-usp-usecase-config-constraint//div[contains(@class,'p-stepper-panel')][4]/div/p-stepperheader/button")
    OptConMetaboliteGridMetaboliteName = (By.XPATH,"//app-usp-usecase-config-constraint//div[contains(@class,'p-stepper-panel')][4]//div[@class='ag-header-cell-label']//span[contains(text(),'Extracellular metabolite name')]")
    OptConMetaboliteGridLlimit = (By.XPATH,"//app-usp-usecase-config-constraint//div[contains(@class,'p-stepper-panel')][4]//div[@class='ag-header-cell-label']//span[contains(text(),'Lower limit')]")
    OptConMetaboliteGridHlimit = (By.XPATH,"//app-usp-usecase-config-constraint//div[contains(@class,'p-stepper-panel')][4]//div[@class='ag-header-cell-label']//span[contains(text(),'Upper limit')]")
    optConMetaboliteNextBtn = (By.XPATH,"//app-usp-usecase-config-constraint//div[contains(@class,'p-stepper-panel')][4]//p-button[@label='Next']")
    optConMetabolitePrevBtn = (By.XPATH,"//app-usp-usecase-config-constraint//div[contains(@class,'p-stepper-panel')][4]//p-button[@label='Previous']")

    OptSummaryBioProceessName = (By.XPATH,"//app-usp-usecase-summary//div[@class='ag-header-cell-label']//span[contains(text(),'Bioprocess Specification Name')]")
    OptSummaryGroup = (By.XPATH,"//app-usp-usecase-summary//div[@class='ag-header-cell-label']//span[contains(text(),'Group')]")
    OptSummaryStatus = (By.XPATH,"//app-usp-usecase-summary//div[@class='ag-header-cell-label']//span[contains(text(),'Status')]")
    OptSummaryGetStatus = (By.XPATH,"//app-usp-usecase-summary//div[@col-id='statuses'][@role='gridcell']//span//span[2]")
    RunOptBtn = (By.XPATH,"//span[contains(text(),'Run Optimization')]/parent::button")
    OptReportsBtn = (By.CSS_SELECTOR,"p-button[ptooltip*='Reports'] button")
    OptReportsTrajectories = (By.CSS_SELECTOR,"app-reports-usp-optimization-landing p-accordiontab[header*='Trajectories'] span")
    OptReportsFeedVol = (By.CSS_SELECTOR,"app-reports-usp-optimization-landing p-accordiontab[header*='Feed Volume'] span")
    OptReportsMediaComp = (By.CSS_SELECTOR,"app-reports-usp-optimization-landing p-accordiontab[header='Media Composition'] span")
    OptReportsOptObjective = (By.CSS_SELECTOR,"app-reports-usp-optimization-landing p-accordiontab[header='Optimized Objective'] span")
    OptReportsTtitle = (By.CSS_SELECTOR,"app-reports-usp-optimization-landing h1")
    OptReportsTrajectoriesTab = (By.CSS_SELECTOR, "app-reports-usp-optimization-landing p-accordiontab[header*='Trajectories'] a")
    OptReportsFeedVolTab = (By.CSS_SELECTOR, "app-reports-usp-optimization-landing p-accordiontab[header*='Feed Volume'] a")
    OptReportsMediaCompTab = (By.CSS_SELECTOR, "app-reports-usp-optimization-landing p-accordiontab[header='Media Composition'] a")
    OptReportsOptObjectiveTab = (By.CSS_SELECTOR, "app-reports-usp-optimization-landing p-accordiontab[header='Optimized Objective'] a")

    OptReportsTrajectoriesBioMass = (By.XPATH, "//app-reports-trajectories//div//div[1]//h3")
    OptReportsTrajectoriesProduct = (By.XPATH, "//app-reports-trajectories//div//div[2]//h3")
    OptReportsFeedVolFeed1 = (By.XPATH, "//app-reports-fed-volume//div//div[1]//h3")
    OptReportsFeedVolFeed2 = (By.XPATH, "//app-reports-fed-volume//div//div[2]//h3")
    OptReportsMediaCompFeed1 = (By.XPATH, "//app-reports-media-compositions//div//div[1]//h3")
    OptReportsMediaCompFeed2 = (By.XPATH, "//app-reports-media-compositions//div//div[2]//h3")
    OptReportsOptObjectiveTitle = (By.XPATH, "//app-reports-optimized-objective//div//div[1]//h3")

    BreadCrumUspLanding = (By.XPATH,"(//nav[@data-pc-name='breadcrumb']//a[contains(@href,'/app-bdx-host-qa/yibpoc/workspace')])[3]")

    OptAggregation = (By.XPATH, "//app-usp-objective-function//div[contains(@class,'p-stepper-panel')][2]/div/p-stepperheader/button")
    OptAggregationPrevBtn = (By.XPATH,"//app-usp-objective-function//div[contains(@class,'p-stepper-panel')][2]//p-button[@label='Previous']")
    OptAggregateMethodDropdown = (By.XPATH,"//app-usp-objective-function//div[contains(@class,'p-stepper-panel')][2]//p-dropdown[@formcontrolname='aggregationMethod']")
    OptAggregateMethodSum = (By.XPATH,"//li[@aria-label='Sum']")


    def GetOptimizationPageTitle(self):
        return self.driver.find_element(*UcPage.OptimizationPageTitle)



    def GetOptUcReactorName(self):
        return self.driver.find_element(*UcPage.OptUcReactorName)

    def GetOptUcReactorType(self):
        return self.driver.find_element(*UcPage.OptUcReactorType)

    def GetOptUcReactors(self):
        return self.driver.find_element(*UcPage.OptUcReactors)

    def GetOptUcStepperStage1(self):
        return self.driver.find_element(*UcPage.OptUcStepperStage1)

    def GetOptUcStepperStage2(self):
        return self.driver.find_element(*UcPage.OptUcStepperStage2)

    def GetOptUcStepperStage3(self):
        return self.driver.find_element(*UcPage.OptUcStepperStage3)

    def GetOptUcStepperStage4(self):
        return self.driver.find_element(*UcPage.OptUcStepperStage4)

    def GetOptUcNextBtn(self):
        return self.driver.find_element(*UcPage.OptUcNextBtn)
    def GetOptPONextBtn(self):
        return self.driver.find_element(*UcPage.OptPONextBtn)

    def GetOptPeformObective(self):
        return self.driver.find_element(*UcPage.OptPeformObective)

    def GetOptPerformObectiveNextBtn(self):
        return self.driver.find_element(*UcPage.OptPerformObectiveNextBtn)

    def GetOptPOveGridObjective(self):
        return self.driver.find_element(*UcPage.OptPOveGridObjective)

    def GetOptPOveGridComponent(self):
        return self.driver.find_element(*UcPage.OptPOveGridComponent)

    def GetOptPOveGridWeight(self):
        return self.driver.find_element(*UcPage.OptPOveGridWeight)

    def GetOptPOveGridAttribute(self):
        return self.driver.find_element(*UcPage.OptPOveGridAttribute)

    def GetOptPOveGridVariable(self):
        return self.driver.find_element(*UcPage.OptPOveGridVariable)

    def GetOptPOveGridalltime(self):
        return self.driver.find_element(*UcPage.OptPOveGridalltime)

    def GetOptPOveGridValue(self):
        return self.driver.find_element(*UcPage.OptPOveGridValue)

    def GetOptDesignSpaceRGroup(self):
        return self.driver.find_element(*UcPage.OptDesignSpaceRGroup)

    def GetOptDesignSpaceRVessel(self):
        return self.driver.find_element(*UcPage.OptDesignSpaceRVessel)

    def GetOptDesignSpaceReactorVariable(self):
        return self.driver.find_element(*UcPage.OptDesignSpaceReactorVariable)

    def GetOptDesignSpaceReactorConstraints(self):
        return self.driver.find_element(*UcPage.OptDesignSpaceReactorConstraints)

    def GetOptDesignSpaceRVAgitation(self):
        return self.driver.find_element(*UcPage.OptDesignSpaceRVAgitation)

    def GetOptRvGridAgitationImpeller(self):
        return self.driver.find_element(*UcPage.OptRvGridAgitationImpeller)

    def GetOptRvGridAgitationController(self):
        return self.driver.find_element(*UcPage.OptRvGridAgitationController)

    def GetOptRvGridAgitationModify(self):
        return self.driver.find_element(*UcPage.OptRvGridAgitationModify)

    def GetOptRvGridAgitationControlerOpt(self):
        return self.driver.find_element(*UcPage.OptRvGridAgitationControlerOpt)

    def GetoptRVAgitationNextBtn(self):
        return self.driver.find_element(*UcPage.optRVAgitationNextBtn)

    def GetOptDesignSpaceRVInflux(self):
        return self.driver.find_element(*UcPage.OptDesignSpaceRVInflux)

    def GetOptRvGridInfluxInletName(self):
        return self.driver.find_element(*UcPage.OptRvGridInfluxInletName)

    def GetOptRvGridInfluxtype(self):
        return self.driver.find_element(*UcPage.OptRvGridInfluxtype)

    def GetOptRvGridInfluxNotes(self):
        return self.driver.find_element(*UcPage.OptRvGridInfluxNotes)

    def GetoptRVInfluxNextBtn(self):
        return self.driver.find_element(*UcPage.optRVInfluxNextBtn)

    def GetoptRVInfluxPrevBtn(self):
        return self.driver.find_element(*UcPage.optRVInfluxPrevBtn)

    def GetOptDesignSpaceRVOutflux(self):
        return self.driver.find_element(*UcPage.OptDesignSpaceRVOutflux)

    def GetOptRvGridOutfluxOutletName(self):
        return self.driver.find_element(*UcPage.OptRvGridOutfluxOutletName)

    def GetOptRvGridOutfluxtype(self):
        return self.driver.find_element(*UcPage.OptRvGridOutfluxtype)

    def GetOptRvGridOutfluxNotes(self):
        return self.driver.find_element(*UcPage.OptRvGridOutfluxNotes)

    def GetoptRVOutfluxNextBtn(self):
        return self.driver.find_element(*UcPage.optRVOutfluxNextBtn)

    def GetoptRVOutfluxPrevBtn(self):
        return self.driver.find_element(*UcPage.optRVOutfluxPrevBtn)

    def GetOptDesignSpaceGenController(self):
        return self.driver.find_element(*UcPage.OptDesignSpaceGenController)

    def GetOptRvGridGenController(self):
        return self.driver.find_element(*UcPage.OptRvGridGenController)

    def GetOptRvGridGenControllerModify(self):
        return self.driver.find_element(*UcPage.OptRvGridGenControllerModify)

    def GetOptRvGridGenControllerOpt(self):
        return self.driver.find_element(*UcPage.OptRvGridGenControllerOpt)

    def GetoptRVGenControllerNextBtn(self):
        return self.driver.find_element(*UcPage.optRVGenControllerNextBtn)

    def GetoptRVGenControllerPrevBtn(self):
        return self.driver.find_element(*UcPage.optRVGenControllerPrevBtn)

    def GetOptConstraintsReactorVolume(self):
        return self.driver.find_element(*UcPage.OptConstraintsReactorVolume)

    def GetOptReactorVolumeGridLLimit(self):
        return self.driver.find_element(*UcPage.OptReactorVolumeGridLLimit)

    def GetOptReactorVolumeGridHLimit(self):
        return self.driver.find_element(*UcPage.OptReactorVolumeGridHLimit)

    def GetoptReactorVolumeNextBtn(self):
        return self.driver.find_element(*UcPage.optReactorVolumeNextBtn)

    def GetoptReactorVolumePrevBtn(self):
        return self.driver.find_element(*UcPage.optReactorVolumePrevBtn)

    def GetOptConstraintsOsmolality(self):
        return self.driver.find_element(*UcPage.OptConstraintsOsmolality)

    def GetOptOsmolalityGridLLimit(self):
        return self.driver.find_element(*UcPage.OptOsmolalityGridLLimit)

    def GetOptOsmolalityGridHLimit(self):
        return self.driver.find_element(*UcPage.OptOsmolalityGridHLimit)

    def GetoptOsmolalityNextBtn(self):
        return self.driver.find_element(*UcPage.optOsmolalityNextBtn)

    def GetoptOsmolalityPrevBtn(self):
        return self.driver.find_element(*UcPage.optOsmolalityPrevBtn)

    def GetOptConstraintsPQA(self):
        return self.driver.find_element(*UcPage.OptConstraintsPQA)

    def GetOptPQAGridAttributeName(self):
        return self.driver.find_element(*UcPage.OptPQAGridAttributeName)

    def GetOptPQAGridLlimitRef(self):
        return self.driver.find_element(*UcPage.OptPQAGridLlimitRef)

    def GetOptPQAGridLlimitOpt(self):
        return self.driver.find_element(*UcPage.OptPQAGridLlimitOpt)

    def GetOptPQAGridHlimitRef(self):
        return self.driver.find_element(*UcPage.OptPQAGridHlimitRef)

    def GetOptPQAGridHlimitOpt(self):
        return self.driver.find_element(*UcPage.OptPQAGridHlimitOpt)

    def GetoptPQANextBtn(self):
        return self.driver.find_element(*UcPage.optPQANextBtn)

    def GetoptPQAPrevBtn(self):
        return self.driver.find_element(*UcPage.optPQAPrevBtn)

    def GetOptConstraintsConMetabolite(self):
        return self.driver.find_element(*UcPage.OptConstraintsConMetabolite)

    def GetOptConMetaboliteGridMetaboliteName(self):
        return self.driver.find_element(*UcPage.OptConMetaboliteGridMetaboliteName)

    def GetOptConMetaboliteGridLlimit(self):
        return self.driver.find_element(*UcPage.OptConMetaboliteGridLlimit)

    def GetOptConMetaboliteGridHlimit(self):
        return self.driver.find_element(*UcPage.OptConMetaboliteGridHlimit)

    def GetoptConMetaboliteNextBtn(self):
        return self.driver.find_element(*UcPage.optConMetaboliteNextBtn)

    def GetoptConMetabolitePrevBtn(self):
        return self.driver.find_element(*UcPage.optConMetabolitePrevBtn)

    def GetOptSummaryBioProceessName(self):
        return self.driver.find_element(*UcPage.OptSummaryBioProceessName)

    def GetOptSummaryGroup(self):
        return self.driver.find_element(*UcPage.OptSummaryGroup)

    def GetOptSummaryStatus(self):
        return self.driver.find_element(*UcPage.OptSummaryStatus)

    def GetOptSummaryGetStatus(self):
        return self.driver.find_element(*UcPage.OptSummaryGetStatus)

    def GetRunOptBtn(self):
        return self.driver.find_element(*UcPage.RunOptBtn)

    def GetOptReportsBtn(self):
        return self.driver.find_element(*UcPage.OptReportsBtn)

    def GetOptReportsTrajectories(self):
        return self.driver.find_element(*UcPage.OptReportsTrajectories)

    def GetOptReportsFeedVol(self):
        return self.driver.find_element(*UcPage.OptReportsFeedVol)

    def GetOptReportsMediaComp(self):
        return self.driver.find_element(*UcPage.OptReportsMediaComp)

    def GetOptReportsOptObjective(self):
        return self.driver.find_element(*UcPage.OptReportsOptObjective)

    def GetOptReportsTtitle(self):
        return self.driver.find_element(*UcPage.OptReportsTtitle)

    def GetOptReportsTrajectoriesTab(self):
        return self.driver.find_element(*UcPage.OptReportsTrajectoriesTab)

    def GetOptReportsFeedVolTab(self):
        return self.driver.find_element(*UcPage.OptReportsFeedVolTab)

    def GetOptReportsMediaCompTab(self):
        return self.driver.find_element(*UcPage.OptReportsMediaCompTab)

    def GetOptReportsOptObjectiveTab(self):
        return self.driver.find_element(*UcPage.OptReportsOptObjectiveTab)

    def GetOptReportsTrajectoriesBioMass(self):
        return self.driver.find_element(*UcPage.OptReportsTrajectoriesBioMass)

    def GetOptReportsTrajectoriesProduct(self):
        return self.driver.find_element(*UcPage.OptReportsTrajectoriesProduct)

    def GetOptReportsFeedVolFeed1(self):
        return self.driver.find_element(*UcPage.OptReportsFeedVolFeed1)

    def GetOptReportsFeedVolFeed2(self):
        return self.driver.find_element(*UcPage.OptReportsFeedVolFeed2)

    def GetOptReportsMediaCompFeed1(self):
        return self.driver.find_element(*UcPage.OptReportsMediaCompFeed1)

    def GetOptReportsMediaCompFeed2(self):
        return self.driver.find_element(*UcPage.OptReportsMediaCompFeed2)

    def GetBreadCrumUspLanding(self):
        return self.driver.find_element(*UcPage.BreadCrumUspLanding)

    def GetOptAggregation(self):
        return self.driver.find_element(*UcPage.OptAggregation)

    def GetOptAggregationPrevBtn(self):
        return self.driver.find_element(*UcPage.OptAggregationPrevBtn)

    def GetOptAggregateMethodDropdown(self):
        return self.driver.find_element(*UcPage.OptAggregateMethodDropdown)

    def GetOptAggregateMethodSum(self):
        return self.driver.find_element(*UcPage.OptAggregateMethodSum)
    def GetOptDesignSpaceNextBtn(self):
        return self.driver.find_element(*UcPage.OptDesignSpaceNextBtn)
    def GetOptSaveConfigBtn(self):
        return self.driver.find_element(*UcPage.OptSaveConfigBtn)
    def GetEditUseCaseToast1(self):
        return self.driver.find_element(*UcPage.EditUseCaseToast1)
    def GetOptSummaryNextBtn(self):
        return  self.driver.find_element(*UcPage.OptSummaryNextBtn)
    def GetOptReportsOptObjectiveTitle(self):
        return self.driver.find_element(*UcPage.OptReportsOptObjectiveTitle)