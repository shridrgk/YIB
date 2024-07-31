from selenium.webdriver.common.by import By
import pytest


class AssetPage:

    def __init__(self, driver):
        self.driver = driver

    AssetLaningTitle = (By.CSS_SELECTOR, "app-assets-assets-landing-page h1")
    ProductMoleculelist = (By.CSS_SELECTOR, "app-assets-assets-landing-page a[href*='product-molecule']")
    Celllist = (By.CSS_SELECTOR, "app-assets-assets-landing-page a[href*='cells']")
    ProducMoleculeTitle = (By.CSS_SELECTOR, "app-assets-product-molecules h1")

    PmGridComponent = (
    By.XPATH, "//app-assets-product-molecules//div[@class='ag-header-cell-label']//span[contains(text(),'Name')]")
    PmGridGlycosylation = (By.XPATH,
                           "//app-assets-product-molecules//div[@class='ag-header-cell-label']//span[contains(text(),'Glycosylation')]")
    PmGridChargeVariant = (By.XPATH,
                           "//app-assets-product-molecules//div[@class='ag-header-cell-label']//span[contains(text(),'Charge Variants')]")
    PmGridNotes = (
    By.XPATH, "//app-assets-product-molecules//div[@class='ag-header-cell-label']//span[contains(text(),'Notes')]")

    PmGridExpand = (By.XPATH, "//span[@ref='eContracted']")
    GlycoGridTab = (By.CSS_SELECTOR, "app-assets-product-molecule-detail-shell li a[data-pc-index='0']")
    CvGridTab = (By.CSS_SELECTOR, "app-assets-product-molecule-detail-shell li a[data-pc-index='1']")
    CompGridTab = (By.CSS_SELECTOR, "app-assets-product-molecule-detail-shell li a[data-pc-index='2']")

    GycoGridComponent = (
    By.XPATH, "//app-assets-pm-glycosylation//div[@class='ag-header-cell-label']//span[contains(text(),'Component')]")
    GycoGridLlimit = (
    By.XPATH, "//app-assets-pm-glycosylation//div[@class='ag-header-cell-label']//span[contains(text(),'Low Limit')]")
    GycoGridHLimit = (
    By.XPATH, "//app-assets-pm-glycosylation//div[@class='ag-header-cell-label']//span[contains(text(),'High Limit')]")
    GycoGridUnit = (
    By.XPATH, "//app-assets-pm-glycosylation//div[@class='ag-header-cell-label']//span[contains(text(),'Unit')]")

    CvGridComponent = (
    By.XPATH, "//app-assets-pm-charge-variant//div[@class='ag-header-cell-label']//span[contains(text(),'Component')]")
    CvGridLlimit = (
    By.XPATH, "//app-assets-pm-charge-variant//div[@class='ag-header-cell-label']//span[contains(text(),'Low Limit')]")
    CvGridHLimit = (
    By.XPATH, "//app-assets-pm-charge-variant//div[@class='ag-header-cell-label']//span[contains(text(),'High Limit')]")
    CvGridUnit = (
    By.XPATH, "//app-assets-pm-charge-variant//div[@class='ag-header-cell-label']//span[contains(text(),'Unit')]")

    CompGridComponent = (
    By.XPATH, "//app-assets-pm-composition//div[@class='ag-header-cell-label']//span[contains(text(),'Component')]")
    CompGridValues = (
    By.XPATH, "//app-assets-pm-composition//div[@class='ag-header-cell-label']//span[contains(text(),'Values')]")
    CompGridUnit = (
    By.XPATH, "//app-assets-pm-composition//div[@class='ag-header-cell-label']//span[contains(text(),'Unit')]")

    CellGridName = (By.XPATH, "//app-assets-cells//div[@class='ag-header-cell-label']//span[contains(text(),'Name')]")
    CellGridOrganism = (
    By.XPATH, "//app-assets-cells//div[@class='ag-header-cell-label']//span[contains(text(),'Organism')]")
    CellGridHCL = (
    By.XPATH, "//app-assets-cells//div[@class='ag-header-cell-label']//span[contains(text(),'Host Cell Line')]")
    CellGridPM = (
    By.XPATH, "//app-assets-cells//div[@class='ag-header-cell-label']//span[contains(text(),'Product Molecule')]")
    CellGridMNM = (By.XPATH, "//app-assets-cells//div[@class='ag-header-cell-label']//span[contains(text(),'MNM')]")
    CellGridNotes = (By.XPATH, "//app-assets-cells//div[@class='ag-header-cell-label']//span[contains(text(),'Notes')]")

    MediumList = (By.CSS_SELECTOR, "app-assets-assets-landing-page a[href*='medium']")
    MediumGridName = (
    By.XPATH, "//app-assets-medium//div[@class='ag-header-cell-label']//span[contains(text(),'Name')]")
    MediumGridType = (
    By.XPATH, "//app-assets-medium//div[@class='ag-header-cell-label']//span[contains(text(),'Type')]")
    MediumGridNotes = (
    By.XPATH, "//app-assets-medium//div[@class='ag-header-cell-label']//span[contains(text(),'Notes')]")
    MediumGridActions = (
    By.XPATH, "//app-assets-medium//div[@class='ag-header-cell-label']//span[contains(text(),'Actions')]")
    CompComponents = (By.XPATH,
                      "//app-assets-compositions-detail-cell-renderer//div[@class='ag-header-cell-label']//span[contains(text(),'Components')]")
    CompLlimit = (By.XPATH,
                  "//app-assets-compositions-detail-cell-renderer//div[@class='ag-header-cell-label']//span[contains(text(),'Low Limit')]")
    CompHlimit = (By.XPATH,
                  "//app-assets-compositions-detail-cell-renderer//div[@class='ag-header-cell-label']//span[contains(text(),'High Limit')]")
    CompUnit = (By.XPATH,
                "//app-assets-compositions-detail-cell-renderer//div[@class='ag-header-cell-label']//span[contains(text(),'Unit')]")
    CompErr = (By.XPATH,
               "//app-assets-compositions-detail-cell-renderer//div[@class='ag-header-cell-label']//span[contains(text(),'Error Model')]")

    SpGasList = (By.CSS_SELECTOR, "app-assets-assets-landing-page a[href*='sparging-gases']")
    SpGasGridName = (
    By.XPATH, "//app-assets-sparging-gases//div[@class='ag-header-cell-label']//span[contains(text(),'Name')]")
    SpGasGridNotes = (
    By.XPATH, "//app-assets-sparging-gases//div[@class='ag-header-cell-label']//span[contains(text(),'Notes')]")
    SpGasGridActions = (
    By.XPATH, "//app-assets-sparging-gases//div[@class='ag-header-cell-label']//span[contains(text(),'Actions')]")
    CompGasComponents = (By.XPATH,
                         "//app-assets-sg-compositions-detail//div[@class='ag-header-cell-label']//span[contains(text(),'Components')]")
    CompGasLlimit = (By.XPATH,
                     "//app-assets-sg-compositions-detail//div[@class='ag-header-cell-label']//span[contains(text(),'Low Limit')]")
    CompGasHlimit = (By.XPATH,
                     "//app-assets-sg-compositions-detail//div[@class='ag-header-cell-label']//span[contains(text(),'High Limit')]")
    CompGasUnit = (
    By.XPATH, "//app-assets-sg-compositions-detail//div[@class='ag-header-cell-label']//span[contains(text(),'Unit')]")
    CompGasErr = (By.XPATH,
                  "//app-assets-sg-compositions-detail//div[@class='ag-header-cell-label']//span[contains(text(),'Error Model')]")

    SensorList = (By.CSS_SELECTOR, "app-assets-assets-landing-page a[href*='sensors']")
    SensorGridName = (
    By.XPATH, "//app-assets-sensors//div[@class='ag-header-cell-label']//span[contains(text(),'Name')]")
    SensorGridNotes = (
    By.XPATH, "//app-assets-sensors//div[@class='ag-header-cell-label']//span[contains(text(),'Notes')]")
    SensorGridActions = (
    By.XPATH, "//app-assets-sensors//div[@class='ag-header-cell-label']//span[contains(text(),'Actions')]")
    SensorMOGridActions = (By.XPATH,
                           "//app-assets-sensors//div[@class='ag-header-cell-label']//span[contains(text(),'Sensed Medium Objects')]")
    SensorSensorCalibrationTab = (By.CSS_SELECTOR, "app-assets-sensor-shell li a[data-pc-index='1']")
    SensorMOTab = (By.CSS_SELECTOR, "app-assets-sensor-shell li a[data-pc-index='0']")
    MOComponents = (
    By.XPATH, "//app-sensor-medium-object//div[@class='ag-header-cell-label']//span[contains(text(),'Medium Object')]")
    MOLlimit = (
    By.XPATH, "//app-sensor-medium-object//div[@class='ag-header-cell-label']//span[contains(text(),'Low Limit')]")
    MOHlimit = (
    By.XPATH, "//app-sensor-medium-object//div[@class='ag-header-cell-label']//span[contains(text(),'High Limit')]")
    MOUnit = (By.XPATH, "//app-sensor-medium-object//div[@class='ag-header-cell-label']//span[contains(text(),'Unit')]")
    MOErr = (
    By.XPATH, "//app-sensor-medium-object//div[@class='ag-header-cell-label']//span[contains(text(),'Error Model')]")

    ControllersList = (By.CSS_SELECTOR, "app-assets-assets-landing-page a[href*='controllers']")
    ControllerGridName = (
    By.XPATH, "//app-assets-controllers//div[@class='ag-header-cell-label']//span[contains(text(),'Name')]")
    ControllerGridType = (
    By.XPATH, "//app-assets-controllers//div[@class='ag-header-cell-label']//span[contains(text(),'Type')]")
    ControllerGridNotes = (
    By.XPATH, "//app-assets-controllers//div[@class='ag-header-cell-label']//span[contains(text(),'Notes')]")
    ControllerGridErr = (
    By.XPATH, "//app-assets-controllers//div[@class='ag-header-cell-label']//span[contains(text(),'Error Model')]")
    ControllerTimeParamTab = (By.CSS_SELECTOR, "app-assets-controller-shell li a[data-pc-index='1']")
    ControllerParamTab = (By.CSS_SELECTOR, "app-assets-controller-shell li a[data-pc-index='0']")
    ControllerTimeParamGridName = (By.XPATH,
                                   "//app-assets-time-profile-parameter//div[@class='ag-header-cell-label']//span[contains(text(),'Parameter Name')]")
    ControllerTimeParamGridNotes = (By.XPATH,
                                    "//app-assets-time-profile-parameter//div[@class='ag-header-cell-label']//span[contains(text(),'Parameter Notes')]")
    ControllerTimeParamGridStart = (By.XPATH,
                                    "//app-assets-time-profile-parameter//div[@class='ag-header-cell-label']//span[contains(text(),'Start Time')]")
    ControllerTimeParamGridEnd = (
    By.XPATH, "//app-assets-time-profile-parameter//div[@class='ag-header-cell-label']//span[contains(text(),'End Time (hrs)')]")
    ControllerTimeParamGridLlimit = (
    By.XPATH, "//app-assets-time-profile-parameter//div[@class='ag-header-cell-label']//span[contains(text(),'Low Limit')]")
    ControllerTimeParamGridHlimit = (
    By.XPATH, "//app-assets-time-profile-parameter//div[@class='ag-header-cell-label']//span[contains(text(),'High Limit')]")
    ControllerTimeParamGridUnit = (By.XPATH,
                                   "//app-assets-time-profile-parameter//div[@class='ag-header-cell-label']//span[contains(text(),'Time Unit')]")
    ControllerTimeParamGridLimitUnit = (By.XPATH,
                                   "//app-assets-time-profile-parameter//div[@class='ag-header-cell-label']//span[contains(text(),'Limit Unit')]")
    ControllerParamGridName = (By.XPATH,
                               "//app-assets-controller-parameter//div[@class='ag-header-cell-label']//span[contains(text(),'Parameter Name')]")
    ControllerParamGridNotes = (By.XPATH,
                                "//app-assets-controller-parameter//div[@class='ag-header-cell-label']//span[contains(text(),'Notes')]")
    ControllerParamGridValue = (
    By.XPATH, "//app-assets-controller-parameter//div[@class='ag-header-cell-label']//span[contains(text(),'Value')]")

    RetentionList = (By.CSS_SELECTOR, "app-assets-assets-landing-page a[href*='retention-system']")
    RetentionGridName = (
    By.XPATH, "//app-assets-retention-system//div[@class='ag-header-cell-label']//span[contains(text(),'Name')]")
    RetentionGridNotes = (
    By.XPATH, "//app-assets-retention-system//div[@class='ag-header-cell-label']//span[contains(text(),'Notes')]")
    RetentionDetailGridRMO = (By.XPATH,
                              "//app-assets-retention-system-detail-cell-renderer//div[@class='ag-header-cell-label']//span[contains(text(),'Retained Medium Objects')]")
    RetentionDetailGridLlimit = (By.XPATH,
                                 "//app-assets-retention-system-detail-cell-renderer//div[@class='ag-header-cell-label']//span[contains(text(),'Low Limit')]")
    RetentionDetailGridHlimit = (By.XPATH,
                                 "//app-assets-retention-system-detail-cell-renderer//div[@class='ag-header-cell-label']//span[contains(text(),'High Limit')]")
    RetentionDetailGridUnit = (By.XPATH,
                               "//app-assets-retention-system-detail-cell-renderer//div[@class='ag-header-cell-label']//span[contains(text(),'Unit')]")
    RetentionDetailGridErr = (By.XPATH,
                              "//app-assets-retention-system-detail-cell-renderer//div[@class='ag-header-cell-label']//span[contains(text(),'Error Model')]")
    ReactorList = (By.CSS_SELECTOR, "app-assets-assets-landing-page a[href*='reactors']")
    ReactorGridName = (
    By.XPATH, "//app-assets-reactors//div[@class='ag-header-cell-label']//span[contains(text(),'Name')]")
    ReactorGridInlet = (
    By.XPATH, "//app-assets-reactors//div[@class='ag-header-cell-label']//span[contains(text(),'No of Inlets')]")
    ReactorGridOutlet = (
    By.XPATH, "//app-assets-reactors//div[@class='ag-header-cell-label']//span[contains(text(),'No of Outlets')]")
    ReactorGridMaxWrk = (
    By.XPATH, "//app-assets-reactors//div[@class='ag-header-cell-label']//span[contains(text(),'Max Working Volume')]")
    ReactorGridImplName = (
    By.XPATH, "//app-assets-reactors//div[@class='ag-header-cell-label']//span[contains(text(),'Impeller Name')]")
    ReactorGridNotes = (
    By.XPATH, "//app-assets-reactors//div[@class='ag-header-cell-label']//span[contains(text(),'Notes')]")
    ReactorinletGridName = (
    By.XPATH, "//app-assets-reactors-inlets//div[@class='ag-header-cell-label']//span[contains(text(),'Name')]")
    ReactorinletGridLlimit = (
    By.XPATH, "//app-assets-reactors-inlets//div[@class='ag-header-cell-label']//span[contains(text(),'Low Limit')]")
    ReactorinletGridHlimit = (
    By.XPATH, "//app-assets-reactors-inlets//div[@class='ag-header-cell-label']//span[contains(text(),'High Limit')]")
    ReactorinletGridUnit = (
    By.XPATH, "//app-assets-reactors-inlets//div[@class='ag-header-cell-label']//span[contains(text(),'Unit')]")
    ReactorinletGridErr = (
    By.XPATH, "//app-assets-reactors-inlets//div[@class='ag-header-cell-label']//span[contains(text(),'Error Model')]")
    ReactorOutletGridtab = (By.CSS_SELECTOR, "app-assets-reactors-shell li a[data-pc-index='1']")
    ReactorinletGridtab = (By.CSS_SELECTOR, "app-assets-reactors-shell li a[data-pc-index='0']")
    ReactoroutletGridName = (
    By.XPATH, "//app-assets-reactors-outlets//div[@class='ag-header-cell-label']//span[contains(text(),'Name')]")
    ReactoroutletGridLlimit = (
    By.XPATH, "//app-assets-reactors-outlets//div[@class='ag-header-cell-label']//span[contains(text(),'Low Limit')]")
    ReactoroutletGridHlimit = (
    By.XPATH, "//app-assets-reactors-outlets//div[@class='ag-header-cell-label']//span[contains(text(),'High Limit')]")
    ReactoroutletGridUnit = (
    By.XPATH, "//app-assets-reactors-outlets//div[@class='ag-header-cell-label']//span[contains(text(),'Unit')]")
    ReactoroutletGridErr = (
    By.XPATH, "//app-assets-reactors-outlets//div[@class='ag-header-cell-label']//span[contains(text(),'Error Model')]")

    CellDetailGridMNMtab = (By.CSS_SELECTOR, "app-assets-cell-shell li a[data-pc-index='1']")
    CellDetailGridPMtab = (By.CSS_SELECTOR, "app-assets-cell-shell li a[data-pc-index='0']")
    CellDetailGridMNMName = (By.XPATH,"//app-assets-cell-shell//app-assets-cell-mnm-model//div[@class='ag-header-cell-label']//span[contains(text(),'Name')]")
    CellDetailGridMNMNotes = (By.XPATH,
                              "//app-assets-cell-shell//app-assets-cell-mnm-model//div[@class='ag-header-cell-label']//span[contains(text(),'Notes')]")
    CellDetailGridPMName = (By.XPATH,
                            "//app-assets-cell-shell//app-assets-cell-product-molecule//div[@class='ag-header-cell-label']//span[contains(text(),'Name')]")
    CellDetailGridPMGlyco = (By.XPATH,
                             "//app-assets-cell-shell//app-assets-cell-product-molecule//div[@class='ag-header-cell-label']//span[contains(text(),'Glycosylation')]")
    CellDetailGridPMCV = (By.XPATH,
                          "//app-assets-cell-shell//app-assets-cell-product-molecule//div[@class='ag-header-cell-label']//span[contains(text(),'Charge Variants')]")
    CellDetailGridPMNotes = (By.XPATH,
                             "//app-assets-cell-shell//app-assets-cell-product-molecule//div[@class='ag-header-cell-label']//span[contains(text(),'Notes')]")

    def GetAssetLaningTitle(self):
        return self.driver.find_element(*AssetPage.AssetLaningTitle)

    def GetProductMoleculelist(self):
        return self.driver.find_element(*AssetPage.ProductMoleculelist)

    def GetProducMoleculeTitle(self):
        return self.driver.find_element(*AssetPage.ProducMoleculeTitle)

    def GetPmGridComponent(self):
        return self.driver.find_element(*AssetPage.PmGridComponent)

    def GetPmGridGlycosylation(self):
        return self.driver.find_element(*AssetPage.PmGridGlycosylation)

    def GetPmGridChargeVariant(self):
        return self.driver.find_element(*AssetPage.PmGridChargeVariant)

    def GetPmGridNotes(self):
        return self.driver.find_element(*AssetPage.PmGridNotes)

    def GetPmGridExpand(self):
        return self.driver.find_element(*AssetPage.PmGridExpand)

    def GetGlycoGridTab(self):
        return self.driver.find_element(*AssetPage.GlycoGridTab)

    def GetCvGridTab(self):
        return self.driver.find_element(*AssetPage.CvGridTab)

    def GetCompGridTab(self):
        return self.driver.find_element(*AssetPage.CompGridTab)

    def GetGycoGridComponent(self):
        return self.driver.find_element(*AssetPage.GycoGridComponent)

    def GetGycoGridLlimit(self):
        return self.driver.find_element(*AssetPage.GycoGridLlimit)

    def GetGycoGridHLimit(self):
        return self.driver.find_element(*AssetPage.GycoGridHLimit)

    def GetGycoGridUnit(self):
        return self.driver.find_element(*AssetPage.GycoGridUnit)

    def GetCvGridComponent(self):
        return self.driver.find_element(*AssetPage.CvGridComponent)

    def GetCvGridLlimit(self):
        return self.driver.find_element(*AssetPage.CvGridLlimit)

    def GetCvGridHLimit(self):
        return self.driver.find_element(*AssetPage.CvGridHLimit)

    def GetCvGridUnit(self):
        return self.driver.find_element(*AssetPage.CvGridUnit)

    def GetCompGridComponent(self):
        return self.driver.find_element(*AssetPage.CompGridComponent)

    def GetCompGridValues(self):
        return self.driver.find_element(*AssetPage.CompGridValues)

    def GetCompGridUnit(self):
        return self.driver.find_element(*AssetPage.CompGridUnit)

    def GetCelllist(self):
        return self.driver.find_element(*AssetPage.Celllist)

    def GetCellGridName(self):
        return self.driver.find_element(*AssetPage.CellGridName)

    def GetCellGridOrganism(self):
        return self.driver.find_element(*AssetPage.CellGridOrganism)

    def GetCellGridHCL(self):
        return self.driver.find_element(*AssetPage.CellGridHCL)

    def GetCellGridPM(self):
        return self.driver.find_element(*AssetPage.CellGridPM)

    def GetCellGridMNM(self):
        return self.driver.find_element(*AssetPage.CellGridMNM)

    def GetCellGridNotes(self):
        return self.driver.find_element(*AssetPage.CellGridNotes)

    def GetMediumList(self):
        return self.driver.find_element(*AssetPage.MediumList)

    def GetMediumGridName(self):
        return self.driver.find_element(*AssetPage.MediumGridName)

    def GetMediumGridType(self):
        return self.driver.find_element(*AssetPage.MediumGridType)

    def GetMediumGridNotes(self):
        return self.driver.find_element(*AssetPage.MediumGridNotes)

    def GetMediumGridActions(self):
        return self.driver.find_element(*AssetPage.MediumGridActions)

    def GetCompComponents(self):
        return self.driver.find_element(*AssetPage.CompComponents)

    def GetCompLlimit(self):
        return self.driver.find_element(*AssetPage.CompLlimit)

    def GetCompHlimit(self):
        return self.driver.find_element(*AssetPage.CompHlimit)

    def GetCompUnit(self):
        return self.driver.find_element(*AssetPage.CompUnit)

    def GetCompErr(self):
        return self.driver.find_element(*AssetPage.CompErr)

    def GetSpGasList(self):
        return self.driver.find_element(*AssetPage.SpGasList)

    def GetSpGasGridName(self):
        return self.driver.find_element(*AssetPage.SpGasGridName)

    def GetSpGasGridNotes(self):
        return self.driver.find_element(*AssetPage.SpGasGridNotes)

    def GetSpGasGridActions(self):
        return self.driver.find_element(*AssetPage.SpGasGridActions)

    def GetCompGasComponents(self):
        return self.driver.find_element(*AssetPage.CompGasComponents)

    def GetCompGasLlimit(self):
        return self.driver.find_element(*AssetPage.CompGasLlimit)

    def GetCompGasHlimit(self):
        return self.driver.find_element(*AssetPage.CompGasHlimit)

    def GetCompGasUnit(self):
        return self.driver.find_element(*AssetPage.CompGasUnit)

    def GetCompGasErr(self):
        return self.driver.find_element(*AssetPage.CompGasErr)

    def GetSensorList(self):
        return self.driver.find_element(*AssetPage.SensorList)

    def GetSensorGridName(self):
        return self.driver.find_element(*AssetPage.SensorGridName)

    def GetSensorGridNotes(self):
        return self.driver.find_element(*AssetPage.SensorGridNotes)

    def GetSensorGridActions(self):
        return self.driver.find_element(*AssetPage.SensorGridActions)

    def GetSensorMOGridActions(self):
        return self.driver.find_element(*AssetPage.SensorMOGridActions)

    def GetSensorSensorCalibrationTab(self):
        return self.driver.find_element(*AssetPage.SensorSensorCalibrationTab)

    def GetSensorMOTab(self):
        return self.driver.find_element(*AssetPage.SensorMOTab)

    def GetMOComponents(self):
        return self.driver.find_element(*AssetPage.MOComponents)

    def GetMOLlimit(self):
        return self.driver.find_element(*AssetPage.MOLlimit)

    def GetMOHlimit(self):
        return self.driver.find_element(*AssetPage.MOHlimit)

    def GetMOUnit(self):
        return self.driver.find_element(*AssetPage.MOUnit)

    def GetMOErr(self):
        return self.driver.find_element(*AssetPage.MOErr)

    def GetControllersList(self):
        return self.driver.find_element(*AssetPage.ControllersList)

    def GetControllerGridName(self):
        return self.driver.find_element(*AssetPage.ControllerGridName)

    def GetControllerGridType(self):
        return self.driver.find_element(*AssetPage.ControllerGridType)

    def GetControllerGridNotes(self):
        return self.driver.find_element(*AssetPage.ControllerGridNotes)

    def GetControllerGridErr(self):
        return self.driver.find_element(*AssetPage.ControllerGridErr)

    def GetControllerTimeParamTab(self):
        return self.driver.find_element(*AssetPage.ControllerTimeParamTab)

    def GetControllerParamTab(self):
        return self.driver.find_element(*AssetPage.ControllerParamTab)

    def GetControllerTimeParamGridName(self):
        return self.driver.find_element(*AssetPage.ControllerTimeParamGridName)

    def GetControllerTimeParamGridNotes(self):
        return self.driver.find_element(*AssetPage.ControllerTimeParamGridNotes)

    def GetControllerTimeParamGridStart(self):
        return self.driver.find_element(*AssetPage.ControllerTimeParamGridStart)

    def GetControllerTimeParamGridEnd(self):
        return self.driver.find_element(*AssetPage.ControllerTimeParamGridEnd)

    def GetControllerTimeParamGridLlimit(self):
        return self.driver.find_element(*AssetPage.ControllerTimeParamGridLlimit)

    def GetControllerTimeParamGridHlimit(self):
        return self.driver.find_element(*AssetPage.ControllerTimeParamGridHlimit)

    def GetControllerTimeParamGridUnit(self):
        return self.driver.find_element(*AssetPage.ControllerTimeParamGridUnit)
    def GetControllerTimeParamGridlimitUnit(self):
        return self.driver.find_element(*AssetPage.ControllerTimeParamGridLimitUnit)
    def GetControllerParamGridName(self):
        return self.driver.find_element(*AssetPage.ControllerParamGridName)

    def GetControllerParamGridNotes(self):
        return self.driver.find_element(*AssetPage.ControllerParamGridNotes)

    def GetControllerParamGridValue(self):
        return self.driver.find_element(*AssetPage.ControllerParamGridValue)

    def GetRetentionList(self):
        return self.driver.find_element(*AssetPage.RetentionList)

    def GetRetentionGridName(self):
        return self.driver.find_element(*AssetPage.RetentionGridName)

    def GetRetentionGridNotes(self):
        return self.driver.find_element(*AssetPage.RetentionGridNotes)

    def GetRetentionDetailGridRMO(self):
        return self.driver.find_element(*AssetPage.RetentionDetailGridRMO)

    def GetRetentionDetailGridLlimit(self):
        return self.driver.find_element(*AssetPage.RetentionDetailGridLlimit)

    def GetRetentionDetailGridHlimit(self):
        return self.driver.find_element(*AssetPage.RetentionDetailGridHlimit)

    def GetRetentionDetailGridUnit(self):
        return self.driver.find_element(*AssetPage.RetentionDetailGridUnit)

    def GetRetentionDetailGridErr(self):
        return self.driver.find_element(*AssetPage.RetentionDetailGridErr)

    def GetReactorList(self):
        return self.driver.find_element(*AssetPage.ReactorList)

    def GetReactorGridName(self):
        return self.driver.find_element(*AssetPage.ReactorGridName)

    def GetReactorGridInlet(self):
        return self.driver.find_element(*AssetPage.ReactorGridInlet)

    def GetReactorGridOutlet(self):
        return self.driver.find_element(*AssetPage.ReactorGridOutlet)

    def GetReactorGridMaxWrk(self):
        return self.driver.find_element(*AssetPage.ReactorGridMaxWrk)

    def GetReactorGridImplName(self):
        return self.driver.find_element(*AssetPage.ReactorGridImplName)

    def GetReactorGridNotes(self):
        return self.driver.find_element(*AssetPage.ReactorGridNotes)

    def GetReactorinletGridName(self):
        return self.driver.find_element(*AssetPage.ReactorinletGridName)

    def GetReactorinletGridLlimit(self):
        return self.driver.find_element(*AssetPage.ReactorinletGridLlimit)

    def GetReactorinletGridHlimit(self):
        return self.driver.find_element(*AssetPage.ReactorinletGridHlimit)

    def GetReactorinletGridUnit(self):
        return self.driver.find_element(*AssetPage.ReactorinletGridUnit)

    def GetReactorinletGridErr(self):
        return self.driver.find_element(*AssetPage.ReactorinletGridErr)

    def GetReactorOutletGridtab(self):
        return self.driver.find_element(*AssetPage.ReactorOutletGridtab)

    def GetReactorinletGridtab(self):
        return self.driver.find_element(*AssetPage.ReactorinletGridtab)

    def GetReactoroutletGridName(self):
        return self.driver.find_element(*AssetPage.ReactoroutletGridName)

    def GetReactoroutletGridLlimit(self):
        return self.driver.find_element(*AssetPage.ReactoroutletGridLlimit)

    def GetReactoroutletGridHlimit(self):
        return self.driver.find_element(*AssetPage.ReactoroutletGridHlimit)

    def GetReactoroutletGridUnit(self):
        return self.driver.find_element(*AssetPage.ReactoroutletGridUnit)

    def GetReactoroutletGridErr(self):
        return self.driver.find_element(*AssetPage.ReactoroutletGridErr)

    def GetCellDetailGridMNMtab(self):
        return self.driver.find_element(*AssetPage.CellDetailGridMNMtab)

    def GetCellDetailGridPMtab(self):
        return self.driver.find_element(*AssetPage.CellDetailGridPMtab)

    def GetCellDetailGridMNMName(self):
        return self.driver.find_element(*AssetPage.CellDetailGridMNMName)

    def GetCellDetailGridMNMNotes(self):
        return self.driver.find_element(*AssetPage.CellDetailGridMNMNotes)

    def GetCellDetailGridPMName(self):
        return self.driver.find_element(*AssetPage.CellDetailGridPMName)

    def GetCellDetailGridPMGlyco(self):
        return self.driver.find_element(*AssetPage.CellDetailGridPMGlyco)

    def GetCellDetailGridPMCV(self):
        return self.driver.find_element(*AssetPage.CellDetailGridPMCV)

    def GetCellDetailGridPMNotes(self):
        return self.driver.find_element(*AssetPage.CellDetailGridPMNotes)
