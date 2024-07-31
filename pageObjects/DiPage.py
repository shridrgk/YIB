from selenium.webdriver.common.by import By
import pytest
class DiPage:

    def __init__(self, driver):
        self.driver = driver


    DiLandingPageTitle = (By.CSS_SELECTOR,"app-di-data-integration-list h1")
    AddDiBtn = (By.CSS_SELECTOR,"app-di-data-integration-list p-button[ptooltip='Add Data Integration'] button")
    CreateDiTtitle = (By.CSS_SELECTOR,"app-data-integration-create h3")
    CreateDiName=(By.CSS_SELECTOR,"app-data-integration-create input[id='name']")
    CreateDiDesc=(By.CSS_SELECTOR,"app-data-integration-create textarea[formcontrolname='description']")
    CreateDiBtn=(By.CSS_SELECTOR,"app-data-integration-create button[type='submit']")
    DiGridName = (By.XPATH,"//app-di-data-integration-list//div[@class='ag-header-cell-label']//span[contains(text(),'Name')]")
    DiGridDescription = (By.XPATH,"//app-di-data-integration-list//div[@class='ag-header-cell-label']//span[contains(text(),'Description')]")
    DiGridCreated_on = (By.XPATH,"//app-di-data-integration-list//div[@class='ag-header-cell-label']//span[contains(text(),'Created_on')]")
    DiGridCreated_by = (By.XPATH,"//app-di-data-integration-list//div[@class='ag-header-cell-label']//span[contains(text(),'Created_by')]")
    DiGridStatus = (By.XPATH,"//app-di-data-integration-list//div[@class='ag-header-cell-label']//span[contains(text(),'Status')]")
    DiGridNameFilter = (By.XPATH,"//app-di-data-integration-list//div[@class='ag-header-cell-label']//span[contains(text(),'Name')]/parent::div/parent::div/span")
    FilterSearBox = (By.CSS_SELECTOR, "input[aria-label='Search filter values']")
    FilterApplyBtn = (By.CSS_SELECTOR, "button[type='submit']")
    SelectDI=(By.XPATH,"//div[contains(@class,'ag-row-first')]//div[@col-id='data_integration_name']/parent::div")

    DiStageTitle=(By.CSS_SELECTOR,"app-di-data-stage h1")
    DiStageUploadFileBtn = (By.CSS_SELECTOR,"app-di-data-stage p-button[ptooltip='Upload Files'] button")
    DiStageUploaderTitle=(By.CSS_SELECTOR,"app-di-data-stage-uploader h3")
    DiStageUploaderFile=(By.CSS_SELECTOR,"app-di-data-stage-uploader input[type='file']")
    DiStageUploaderBtn=(By.XPATH,"//app-di-data-stage-uploader//uploadicon/parent::button")
    DistageuploadToast = (By.CSS_SELECTOR,"p-toastitem div[class*='p-toast-message']")
    DiStageRefreshBtn = (By.CSS_SELECTOR,"app-di-data-stage p-button[ptooltip='Refresh'] button")
    DiStageUploadCloseBtn = (By.CSS_SELECTOR,"button[class*='p-dialog-header-close']")
    DiStageNextBtn = (By.CSS_SELECTOR,"app-di-data-stage p-button[label='Next']")

    DiMatchingTempTitle = (By.CSS_SELECTOR,"app-di-matching-templates h1")
    DiMatchingTempName=(By.XPATH,"//app-di-matching-templates//div[@class='ag-header-cell-label']//span[contains(text(),'Name')]")
    DiMatchingTempAuthor=(By.XPATH,"//app-di-matching-templates//div[@class='ag-header-cell-label']//span[contains(text(),'Author')]")
    DiMatchingPublish_on=(By.XPATH,"//app-di-matching-templates//div[@class='ag-header-cell-label']//span[contains(text(),'Published On')]")
    DiMatchingVersion=(By.XPATH,"//app-di-matching-templates//div[@class='ag-header-cell-label']//span[contains(text(),'Version')]")
    DiMatchingTempNameFilter = (By.XPATH,"//app-di-matching-templates//div[@class='ag-header-cell-label']//span[contains(text(),'Name')]/parent::div/parent::div/span")
    SelectTemplate = (By.CSS_SELECTOR, "app-di-matching-templates div[class='ag-selection-checkbox'] div")
    DiMatchingCodeSpaceBtn= (By.CSS_SELECTOR,"app-di-code-files-cell-renderer button")
    DiMatchingApplyBtn= (By.CSS_SELECTOR,"p-button[label='Apply'] button")
    DiCodeSpaceTitle = (By.CSS_SELECTOR,"span[class*='p-dialog-title']")
    DiCodeSpaceFileCultivation = (By.CSS_SELECTOR,"app-di-code-space li[aria-label='cultivation.py']")
    DiCodeSpaceFilediConfig = (By.CSS_SELECTOR, "app-di-code-space li[aria-label='di_config.py']")
    DiCodeSpaceFilediInflux = (By.CSS_SELECTOR, "app-di-code-space li[aria-label='influx.py']")
    DiCodeSpaceFilediMain = (By.CSS_SELECTOR, "app-di-code-space li[aria-label='main.py']")
    DiCodeSpaceFilediMappings = (By.CSS_SELECTOR, "app-di-code-space li[aria-label='mappings.py']")
    DiCodeSpaceFilediOutflux = (By.CSS_SELECTOR, "app-di-code-space li[aria-label='outflux.py']")
    DiCodeSpaceFilediRelation = (By.CSS_SELECTOR, "app-di-code-space li[aria-label='relation_mapping.py']")
    DiCodeSpaceFilediSesnor = (By.CSS_SELECTOR, "app-di-code-space li[aria-label='sensor_measurements.py']")
    DiCodeSpaceFilediTransform = (By.CSS_SELECTOR, "app-di-code-space li[aria-label='transformed_files.py']")
    DiCodeSpaceFilediValidation = (By.CSS_SELECTOR, "app-di-code-space li[aria-label='validations.py']")
    DiCodeSpaceCloseBtn = (By.CSS_SELECTOR,"div[class*='codespace-dialog'] button")

    DiTemplateDetailTitle = (By.CSS_SELECTOR,"app-di-etl-template-detail h1")
    DiTemplateDetailChangeTempBtn = (By.CSS_SELECTOR,"app-di-etl-template-detail p-button[ptooltip='Change Template']")
    DiTemplateDetailRefreshBtn = (By.CSS_SELECTOR, "app-di-etl-template-detail p-button[ptooltip='Refresh']")
    DiTemplateDetailExecuteBtn = (By.CSS_SELECTOR, "app-di-etl-template-detail p-button[ptooltip='Execute']")
    DiTemplateDetailConfig = (By.CSS_SELECTOR,"a[id='configuuration']")
    DiTemplateDetailCodeSpace = (By.CSS_SELECTOR,"a[id='code_space']")
    DiTemplateDetailAltVarCheckBox = (By.XPATH,"//app-di-etl-configurations//p-radiobutton//input[@id='alternative_names']/parent::div/parent::div")
    DiTemplateDetailTempVarCheckBox = (By.XPATH,"//app-di-etl-configurations//p-radiobutton//input[@id='template_variables']/parent::div/parent::div")
    DiTemplateDetailAltVarGridName = (By.XPATH,"//app-di-etl-configurations//div[@class='ag-header-cell-label']//span[contains(text(),'Name')]")
    DiTemplateDetailAltVarGridAlias = (By.XPATH,"//app-di-etl-configurations//div[@class='ag-header-cell-label']//span[contains(text(),'Alias')]")
    DiTemplateDetailTempVarName = (By.XPATH, "//app-di-etl-configurations//div[@class='ag-header-cell-label']//span[contains(text(),'Name')]")
    DiTemplateDetailTempVarDesc = (By.XPATH, "//app-di-etl-configurations//div[@class='ag-header-cell-label']//span[contains(text(),'Description')]")
    DiTemplateDetailTempVarValue = (By.XPATH, "//app-di-etl-configurations//div[@class='ag-header-cell-label']//span[contains(text(),'Value')]")


    DiTemplateDetailPrevBtn = (By.XPATH,"//span[contains(text(),'Previous')]")
    DiTempateDetailNextBtn = (By.XPATH,"//span[contains(text(),'Next')]")

    DiTempDetailCodeSpaceFileCultivation = (By.CSS_SELECTOR,"app-di-etl-template-detail app-di-code-space app-di-code-file-list  li[aria-label='cultivation.py']")
    DiTempDetailCodeSpaceFilediConfig = (By.CSS_SELECTOR,"app-di-etl-template-detail app-di-code-space app-di-code-file-list  li[aria-label='di_config.py']")
    DiTempDetailCodeSpaceFilediInflux = (By.CSS_SELECTOR, "app-di-etl-template-detail app-di-code-space app-di-code-file-list  li[aria-label='influx.py']")
    DiTempDetailCodeSpaceFilediMain = (By.CSS_SELECTOR, "app-di-etl-template-detail app-di-code-space app-di-code-file-list  li[aria-label='main.py']")
    DiTempDetailCodeSpaceFilediMappings = (By.CSS_SELECTOR, "app-di-etl-template-detail app-di-code-space app-di-code-file-list  li[aria-label='mappings.py']")
    DiTempDetailCodeSpaceFilediOutflux = (By.CSS_SELECTOR, "app-di-etl-template-detail app-di-code-space app-di-code-file-list  li[aria-label='outflux.py']")
    DiTempDetailCodeSpaceFilediRelation = (By.CSS_SELECTOR, "app-di-etl-template-detail app-di-code-space app-di-code-file-list  li[aria-label='relation_mapping.py']")
    DiTempDetailCodeSpaceFilediSesnor = (By.CSS_SELECTOR, "app-di-etl-template-detail app-di-code-space app-di-code-file-list  li[aria-label='sensor_measurements.py']")
    DiTempDetailCodeSpaceFilediTransform = (By.CSS_SELECTOR, "app-di-etl-template-detail app-di-code-space app-di-code-file-list  li[aria-label='transformed_files.py']")
    DiTempDetailCodeSpaceFilediValidation = (By.CSS_SELECTOR, "app-di-etl-template-detail app-di-code-space app-di-code-file-list  li[aria-label='validations.py']")
    DiTempolateExecuteBtn=(By.CSS_SELECTOR,"p-button[ptooltip='Execute'] button")
    DiTemplateExecuteFDialog = (By.CSS_SELECTOR,"div[role='alertdialog'] span[class*='p-confirm-dialog-message']")
    DiTemplateDialogAcpt=(By.CSS_SELECTOR,"button[class*='p-confirm-dialog-accept']")
    DiTemplateExecuteRefreshBtn=(By.CSS_SELECTOR,"p-button[ptooltip='Refresh']")




    def GetDiLandingPageTitle(self):
        return self.driver.find_element(*DiPage.DiLandingPageTitle)

    def GetAddDiBtn(self):
        return self.driver.find_element(*DiPage.AddDiBtn)

    def GetCreateDiTtitle(self):
        return self.driver.find_element(*DiPage.CreateDiTtitle)

    def GetCreateDiName(self):
        return self.driver.find_element(*DiPage.CreateDiName)

    def GetCreateDiDesc(self):
        return self.driver.find_element(*DiPage.CreateDiDesc)


    def GetCreateDiBtn(self):
        return self.driver.find_element(*DiPage.CreateDiBtn)

    def GetDiGridName(self):
        return self.driver.find_element(*DiPage.DiGridName)

    def GetDiGridDescription(self):
        return self.driver.find_element(*DiPage.DiGridDescription)

    def GetDiGridCreated_on(self):
        return self.driver.find_element(*DiPage.DiGridCreated_on)

    def GetDiGridCreated_by(self):
        return self.driver.find_element(*DiPage.DiGridCreated_by)

    def GetDiGridStatus(self):
        return self.driver.find_element(*DiPage.DiGridStatus)

    def GetDiGridNameFilter(self):
        return self.driver.find_element(*DiPage.DiGridNameFilter)

    def GetFilterSearBox(self):
        return self.driver.find_element(*DiPage.FilterSearBox)

    def GetFilterApplyBtn(self):
        return self.driver.find_element(*DiPage.FilterApplyBtn)

    def GetSelectDI(self):
        return self.driver.find_element(*DiPage.SelectDI)


    def GetDiStageTitle(self):
        return self.driver.find_element(*DiPage.DiStageTitle)

    def GetDiStageUploadFileBtn(self):
        return self.driver.find_element(*DiPage.DiStageUploadFileBtn)

    def GetDiStageUploaderTitle(self):
        return self.driver.find_element(*DiPage.DiStageUploaderTitle)
    def GetDiStageUploaderFile(self):
        return self.driver.find_element(*DiPage.DiStageUploaderFile)

    def GetDiStageUploaderBtn(self):
        return self.driver.find_element(*DiPage.DiStageUploaderBtn)

    def GetDistageuploadToast(self):
        return self.driver.find_element(*DiPage.DistageuploadToast)

    def GetDiStageRefreshBtn(self):
        return self.driver.find_element(*DiPage.DiStageRefreshBtn)


    def GetDiStageNextBtn(self):
        return self.driver.find_element(*DiPage.DiStageNextBtn)

    def GetDiMatchingTempTitle(self):
        return self.driver.find_element(*DiPage.DiMatchingTempTitle)

    def GetDiMatchingTempName(self):
        return self.driver.find_element(*DiPage.DiMatchingTempName)

    def GetDiMatchingTempAuthor(self):
        return self.driver.find_element(*DiPage.DiMatchingTempAuthor)

    def GetDiMatchingPublish_on(self):
        return self.driver.find_element(*DiPage.DiMatchingPublish_on)

    def GetDiMatchingVersion(self):
        return self.driver.find_element(*DiPage.DiMatchingVersion)

    def GetDiMatchingTempNameFilter(self):
        return self.driver.find_element(*DiPage.DiMatchingTempNameFilter)

    def GetSelectTemplate(self):
        return self.driver.find_element(*DiPage.SelectTemplate)

    def GetDiMatchingCodeSpaceBtn(self):
        return self.driver.find_element(*DiPage.DiMatchingCodeSpaceBtn)



    def GetDiMatchingApplyBtn(self):
        return self.driver.find_element(*DiPage.DiMatchingApplyBtn)
    def GetDiCodeSpaceTitle(self):
        return self.driver.find_element(*DiPage.DiCodeSpaceTitle)
    def GetDiCodeSpaceFileCultivation(self):
        return self.driver.find_element(*DiPage.DiCodeSpaceFileCultivation)

    def GetDiCodeSpaceFilediConfig(self):
        return self.driver.find_element(*DiPage.DiCodeSpaceFilediConfig)

    def GetDiCodeSpaceFilediInflux(self):
        return self.driver.find_element(*DiPage.DiCodeSpaceFilediInflux)

    def GetDiCodeSpaceFilediMain(self):
        return self.driver.find_element(*DiPage.DiCodeSpaceFilediMain)

    def GetDiCodeSpaceFilediMappings(self):
        return self.driver.find_element(*DiPage.DiCodeSpaceFilediMappings)

    def GetDiCodeSpaceFilediOutflux(self):
        return self.driver.find_element(*DiPage.DiCodeSpaceFilediOutflux)

    def GetDiCodeSpaceFilediRelation(self):
        return self.driver.find_element(*DiPage.DiCodeSpaceFilediRelation)

    def GetDiCodeSpaceFilediSesnor(self):
        return self.driver.find_element(*DiPage.DiCodeSpaceFilediSesnor)

    def GetDiCodeSpaceFilediTransform(self):
        return self.driver.find_element(*DiPage.DiCodeSpaceFilediTransform)

    def GetDiCodeSpaceFilediValidation(self):
        return self.driver.find_element(*DiPage.DiCodeSpaceFilediValidation)

    def GetDiCodeSpaceCloseBtn(self):
        return self.driver.find_element(*DiPage.DiCodeSpaceCloseBtn)

    def GetDiTemplateDetailTitle(self):
        return self.driver.find_element(*DiPage.DiTemplateDetailTitle)

    def GetDiTemplateDetailChangeTempBtn(self):
        return self.driver.find_element(*DiPage.DiTemplateDetailChangeTempBtn)

    def GetDiTemplateDetailRefreshBtn(self):
        return self.driver.find_element(*DiPage.DiTemplateDetailRefreshBtn)

    def GetDiTemplateDetailExecuteBtn(self):
        return self.driver.find_element(*DiPage.DiTemplateDetailExecuteBtn)

    def GetDiTemplateDetailConfig(self):
        return self.driver.find_element(*DiPage.DiTemplateDetailConfig)

    def GetDiTemplateDetailCodeSpace(self):
        return self.driver.find_element(*DiPage.DiTemplateDetailCodeSpace)

    def GetDiTemplateDetailAltVarCheckBox(self):
        return self.driver.find_element(*DiPage.DiTemplateDetailAltVarCheckBox)

    def GetDiTemplateDetailTempVarCheckBox(self):
        return self.driver.find_element(*DiPage.DiTemplateDetailTempVarCheckBox)

    def GetDiTemplateDetailTempVarGridName(self):
        return self.driver.find_element(*DiPage.DiTemplateDetailTempVarName)

    def GetDiTemplateDetailTempVarGridDesc(self):
        return self.driver.find_element(*DiPage.DiTemplateDetailTempVarDesc)

    def GetDiTemplateDetailTempVarValue(self):
        return self.driver.find_element(*DiPage.DiTemplateDetailTempVarValue)


    def GetDiTemplateDetailAltVarGridName(self):
        return self.driver.find_element(*DiPage.DiTemplateDetailAltVarGridName)

    def GetDiTemplateDetailAltVarGridAlias(self):
        return self.driver.find_element(*DiPage.DiTemplateDetailAltVarGridAlias)

    def GetDiTemplateDetailPrevBtn(self):
        return self.driver.find_element(*DiPage.DiTemplateDetailPrevBtn)

    def GetDiTempateDetailNextBtn(self):
        return self.driver.find_element(*DiPage.DiTempateDetailNextBtn)

    def GetDiTempDetailCodeSpaceFileCultivation(self):
        return self.driver.find_element(*DiPage.DiTempDetailCodeSpaceFileCultivation)

    def GetDiTempDetailCodeSpaceFilediConfig(self):
        return self.driver.find_element(*DiPage.DiTempDetailCodeSpaceFilediConfig)

    def GetDiTempDetailCodeSpaceFilediInflux(self):
        return self.driver.find_element(*DiPage.DiTempDetailCodeSpaceFilediInflux)

    def GetDiTempDetailCodeSpaceFilediMain(self):
        return self.driver.find_element(*DiPage.DiTempDetailCodeSpaceFilediMain)

    def GetDiTempDetailCodeSpaceFilediMappings(self):
        return self.driver.find_element(*DiPage.DiTempDetailCodeSpaceFilediMappings)

    def GetDiTempDetailCodeSpaceFilediOutflux(self):
        return self.driver.find_element(*DiPage.DiTempDetailCodeSpaceFilediOutflux)

    def GetDiTempDetailCodeSpaceFilediRelation(self):
        return self.driver.find_element(*DiPage.DiTempDetailCodeSpaceFilediRelation)

    def GetDiTempDetailCodeSpaceFilediSesnor(self):
        return self.driver.find_element(*DiPage.DiTempDetailCodeSpaceFilediSesnor)

    def GetDiTempDetailCodeSpaceFilediTransform(self):
        return self.driver.find_element(*DiPage.DiTempDetailCodeSpaceFilediTransform)

    def GetDiTempDetailCodeSpaceFilediValidation(self):
        return self.driver.find_element(*DiPage.DiTempDetailCodeSpaceFilediValidation)

    def GetDiTempolateExecuteBtn(self):
        return self.driver.find_element(*DiPage.DiTempolateExecuteBtn)

    def GetDiTemplateExecuteFDialog(self):
        return self.driver.find_element(*DiPage.DiTemplateExecuteFDialog)

    def GetDiTemplateDialogAcpt(self):
        return self.driver.find_element(*DiPage.DiTemplateDialogAcpt)

    def GetDiTemplateExecuteRefreshBtn(self):
        return self.driver.find_element(*DiPage.DiTemplateExecuteRefreshBtn)

    def GetDiStageUploadCloseBtn(self):
        return self.driver.find_element(*DiPage.DiStageUploadCloseBtn)