from selenium.webdriver.common.by import By
import pytest
class WorkSpacePage:

    def __init__(self, driver):
        self.driver = driver


    UserName = (By.CSS_SELECTOR,"input[id='gigya-loginID-77152811960799260']")
    Login = (By.CSS_SELECTOR,'input[value="SIGN IN"]')
    PassWord = (By.CSS_SELECTOR,"input[id='#gigya-password-116353530441464400']")
    PageTitle = (By.CSS_SELECTOR, 'app-workspace-list h1')
    EnterToken = (By.CSS_SELECTOR,'input[class="gig-tfa-code-textbox"]')
    SubmitBtn = (By.CSS_SELECTOR,"div[class*='gig-tfa-button-submit']")
    GridNameColumn = (By.XPATH,"//app-workspace-shell//div[@class='ag-header-cell-label']//span[contains(text(),'Name')]")
    GridDescColumn = (By.XPATH, "//app-workspace-shell//div[@class='ag-header-cell-label']//span[contains(text(),'Description')]")
    GridCreatedOnColumn = (By.XPATH, "//app-workspace-shell//div[@class='ag-header-cell-label']//span[contains(text(),'Created_on')]")
    GridCreatedByColumn = (By.XPATH, "//app-workspace-shell//div[@class='ag-header-cell-label']//span[contains(text(),'Created_by')]")
    WorkSpaceAddBtn = (By.CSS_SELECTOR,"app-workspace-shell button")
    WSpaceName = (By.CSS_SELECTOR,"app-workspace-create input[id='name']")
    WSpaceDesc = (By.CSS_SELECTOR,"app-workspace-create textarea[formcontrolname='description']")
    WspaceCreateBtn= (By.CSS_SELECTOR,"app-workspace-create button[type='submit']")
    WspaceDetail = (By.CSS_SELECTOR,"app-workspace-detail")
    WorkSpaceUspDt = (By.CSS_SELECTOR,"app-workspace-detail app-workspace-detail-item a[href*='/usp-dt']")
    SideNavWSpace = (By.CSS_SELECTOR,"yib-layout-sidenav a[title='Workspace']")
    WspaceNameFltr = (By.XPATH,"//app-workspace-shell//div[@class='ag-header-cell-label']//span[contains(text(),'Name')]/parent::div/parent::div/span")

    FilterSearBox = (By.CSS_SELECTOR,"input[aria-label='Search filter values']")
    FilterApplyBtn = (By.CSS_SELECTOR,"button[type='submit']")
    SelectWspace = (By.XPATH,"//div[contains(@class,'ag-row-first')]//div[@col-id='workspace_name']/parent::div")
    SideNavUspDt = (By.CSS_SELECTOR,"a[title='USP - Digital Twin']")
    SideNavDi = (By.CSS_SELECTOR, "a[title='Data Integration']")
    SideNavAsset = (By.CSS_SELECTOR, "a[title='Assets']")
    SideNavReports = (By.CSS_SELECTOR,"a[title='Reports']")
    WsLandingUspList = (By.CSS_SELECTOR,"a[class*='landing-page-routerlink'][href*='/usp-dt']")
    WsLandingDIList = (By.CSS_SELECTOR, "a[class*='landing-page-routerlink'][href*='/data-integration']")
    WsLandingAssetList = (By.CSS_SELECTOR, "a[class*='landing-page-routerlink'][href*='/assets']")
    WsLandingReportsList = (By.CSS_SELECTOR, "a[class*='landing-page-routerlink'][href*='/reports']")
    WsLandingProductMolecules = (By.CSS_SELECTOR,"app-assets-assets-list-ws-card a[href*='product-molecules']")
    WsLandingCells = (By.CSS_SELECTOR,"app-assets-assets-list-ws-card a[href*='cells']")
    WsLandingMedium = (By.CSS_SELECTOR, "app-assets-assets-list-ws-card a[href*='medium']")
    WsLandingSpargingGas = (By.CSS_SELECTOR, "app-assets-assets-list-ws-card a[href*='sparging-gases']")
    WsLandingSensors = (By.CSS_SELECTOR, "app-assets-assets-list-ws-card a[href*='sensors']")
    WsLandingControllers = (By.CSS_SELECTOR, "app-assets-assets-list-ws-card a[href*='controllers']")
    WsLandingRentention = (By.CSS_SELECTOR, "app-assets-assets-list-ws-card a[href*='retention-system']")
    WsLandingReactors = (By.CSS_SELECTOR, "app-assets-assets-list-ws-card a[href*='reactors']")





    def getPageTitle(self):
        return self.driver.find_element(*WorkSpacePage.PageTitle)
    def getUserName(self):
        return self.driver.find_element(*WorkSpacePage.UserName)
    def getLogin(self):
        return self.driver.find_element(*WorkSpacePage.Login)
    def getPassWord(self):
        return self.driver.find_element(*WorkSpacePage.PassWord)
    def GetEnterToken(self):
        return self.driver.find_element(*WorkSpacePage.EnterToken)
    def GetSubmitBtn(self):
        return self.driver.find_element(*WorkSpacePage.SubmitBtn)
    def GetGridNameColumn(self):
        return self.driver.find_element(*WorkSpacePage.GridNameColumn)

    def GetGridDescColumn(self):
        return self.driver.find_element(*WorkSpacePage.GridDescColumn)
    def GetGridCreatedOnColumn(self):
        return self.driver.find_element(*WorkSpacePage.GridCreatedOnColumn)

    def GetGridCreatedByColumn(self):
        return self.driver.find_element(*WorkSpacePage.GridCreatedByColumn)

    def GetWorkSpaceAddBtn(self):
        return self.driver.find_element(*WorkSpacePage.WorkSpaceAddBtn)

    def GetWSpaceName(self):
        return self.driver.find_element(*WorkSpacePage.WSpaceName)

    def GetWSpaceDesc(self):
        return self.driver.find_element(*WorkSpacePage.WSpaceDesc)

    def GetWspaceCreateBtn(self):
        return self.driver.find_element(*WorkSpacePage.WspaceCreateBtn)

    def GetWspaceDetail(self):
        return self.driver.find_element(*WorkSpacePage.WspaceDetail)

    def GetWorkSpaceUspDt(self):
        return self.driver.find_element(*WorkSpacePage.WorkSpaceUspDt)
    def GetSideNavWSpace(self):
        return self.driver.find_element(*WorkSpacePage.SideNavWSpace)
    def GetWspaceNameFltr(self):
        return self.driver.find_element(*WorkSpacePage.WspaceNameFltr)
    def GetFilterSearBox(self):
        return self.driver.find_element(*WorkSpacePage.FilterSearBox)
    def GetFilterApplyBtn(self):
        return self.driver.find_element(*WorkSpacePage.FilterApplyBtn)

    def GetSelectWspace(self):
        return self.driver.find_element(*WorkSpacePage.SelectWspace)

    def GetSideNavUspDt(self):
        return self.driver.find_element(*WorkSpacePage.SideNavUspDt)
    def GetSideNavDi(self):
        return self.driver.find_element(*WorkSpacePage.SideNavDi)
    def GetSideNavAsset(self):
        return self.driver.find_element(*WorkSpacePage.SideNavAsset)
    def GetSideNavReports(self):
        return self.driver.find_element(*WorkSpacePage.SideNavReports)
    def GetWsLandingUspList(self):
        return self.driver.find_element(*WorkSpacePage.WsLandingUspList)

    def GetWsLandingDIList(self):
        return self.driver.find_element(*WorkSpacePage.WsLandingDIList)
    def GetWsLandingAssetList(self):
        return self.driver.find_element(*WorkSpacePage.WsLandingAssetList)
    def GetWsLandingReportsList(self):
        return self.driver.find_element(*WorkSpacePage.WsLandingReportsList)
    def WsLandingProductMolecules(self):
        return self.driver.find_element(*WorkSpacePage.WsLandingProductMolecules)