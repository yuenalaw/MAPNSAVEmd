"""
Register KivyMD widgets to use without import
"""

from kivy.factory import Factory

r = Factory.register
r("MDCarousel", module="kivymd.uix.carousel")
r("MDFloatLayout", module="kivymd.uix.floatlayout")
r("MDScreen", module="kivymd.uix.screen")
r("MDBoxLayout", module="kivymd.uix.boxlayout")
r("MDRelativeLayout", module="kivymd.uix.relativelayout")
r("MDGridLayout", module="kivymd.uix.gridlayout")
r("MDStackLayout", module="kivymd.uix.stacklayout")
r("MDExpansionPanel", module="kivymd.uix.expansionpanel")
r("MDExpansionPanelOneLine", module="kivymd.uix.expansionpanel")
r("MDExpansionPanelTwoLine", module="kivymd.uix.expansionpanel")
r("MDExpansionPanelThreeLine", module="kivymd.uix.expansionpanel")
r("FitImage", module="kivymd.utils.fitimage")
r("MDBackdrop", module="kivymd.uix.backdrop")
r("MDBanner", module="kivymd.uix.banner")
r("MDTooltip", module="kivymd.uix.tooltip")
r("MDBottomNavigation", module="kivymd.uix.bottomnavigation")
r("MDBottomNavigationItem", module="kivymd.uix.bottomnavigation")
r("MDBottomNavigationHeader", module="kivymd.uix.bottomnavigation")
r("MDBottomNavigationBar", module="kivymd.uix.bottomnavigation")
r("MDTab", module="kivymd.uix.bottomnavigation")
r("MDBottomSheet", module="kivymd.uix.bottomsheet")
r("MDListBottomSheet", module="kivymd.uix.bottomsheet")
r("MDGridBottomSheet", module="kivymd.uix.bottomsheet")
r("MDFloatingActionButtonSpeedDial", module="kivymd.uix.button")
r("MDIconButton", module="kivymd.uix.button")
r("MDRoundImageButton", module="kivymd.uix.button")
r("MDFlatButton", module="kivymd.uix.button")
r("MDRaisedButton", module="kivymd.uix.button")
r("MDFloatingActionButton", module="kivymd.uix.button")
r("MDRectangleFlatButton", module="kivymd.uix.button")
r("MDTextButton", module="kivymd.uix.button")
r("MDCustomRoundIconButton", module="kivymd.uix.button")
r("MDRoundFlatButton", module="kivymd.uix.button")
r("MDFillRoundFlatButton", module="kivymd.uix.button")
r("MDRectangleFlatIconButton", module="kivymd.uix.button")
r("MDRoundFlatIconButton", module="kivymd.uix.button")
r("MDFillRoundFlatIconButton", module="kivymd.uix.button")
r("MDCard", module="kivymd.uix.card")
r("MDSeparator", module="kivymd.uix.card")
r("MDChip", module="kivymd.uix.chip")
r("MDChooseChip", module="kivymd.uix.chip")
r("MDDialog", module="kivymd.uix.dialog")
r("MDInputDialog", module="kivymd.uix.dialog")
r("MDFileManager", module="kivymd.uix.filemanager")
r("Tile", module="kivymd.uix.imagelist")
r("SmartTile", module="kivymd.uix.imagelist")
r("SmartTileWithLabel", module="kivymd.uix.imagelist")
r("SmartTileWithStar", module="kivymd.uix.imagelist")
r("MDLabel", module="kivymd.uix.label")
r("MDIcon", module="kivymd.uix.label")
r("MDList", module="kivymd.uix.list")
r("ILeftBody", module="kivymd.uix.list")
r("ILeftBodyTouch", module="kivymd.uix.list")
r("IRightBody", module="kivymd.uix.list")
r("IRightBodyTouch", module="kivymd.uix.list")
r("ContainerSupport", module="kivymd.uix.list")
r("OneLineListItem", module="kivymd.uix.list")
r("TwoLineListItem", module="kivymd.uix.list")
r("ThreeLineListItem", module="kivymd.uix.list")
r("OneLineAvatarListItem", module="kivymd.uix.list")
r("TwoLineAvatarListItem", module="kivymd.uix.list")
r("ThreeLineAvatarListItem", module="kivymd.uix.list")
r("OneLineIconListItem", module="kivymd.uix.list")
r("TwoLineIconListItem", module="kivymd.uix.list")
r("ThreeLineIconListItem", module="kivymd.uix.list")
r("OneLineRightIconListItem", module="kivymd.uix.list")
r("TwoLineRightIconListItem", module="kivymd.uix.list")
r("ThreeLineRightIconListItem", module="kivymd.uix.list")
r("OneLineAvatarIconListItem", module="kivymd.uix.list")
r("TwoLineAvatarIconListItem", module="kivymd.uix.list")
r("ThreeLineAvatarIconListItem", module="kivymd.uix.list")
r("MDMenu", module="kivymd.uix.menu")
r("MDDropdownMenu", module="kivymd.uix.menu")
r("MDContextMenu", module="kivymd.uix.context_menu")
r("MDMenuItem", module="kivymd.uix.menu")
r("HoverBehavior", module="kivymd.uix.behaviors.hover_behavior")
r("FocusBehavior", module="kivymd.uix.behaviors.hover_behavior")
r("MDNavigationDrawer", module="kivymd.uix.navigationdrawer")
r("NavigationLayout", module="kivymd.uix.navigationdrawer")
r("MDDatePicker", module="kivymd.uix.picker")
r("MDTimePicker", module="kivymd.uix.picker")
r("MDThemePicker", module="kivymd.uix.picker")
r("MDProgressBar", module="kivymd.uix.progressbar")
r("MDProgressLoader", module="kivymd.uix.progressloader")
r("MDScrollViewRefreshLayout", module="kivymd.uix.refreshlayout")
r("MDCheckbox", module="kivymd.uix.selectioncontrol")
r("Thumb", module="kivymd.uix.selectioncontrol")
r("MDSwitch", module="kivymd.uix.selectioncontrol")
r("MDSlider", module="kivymd.uix.slider")
r("Snackbar", module="kivymd.uix.snackbar")
r("MDSpinner", module="kivymd.uix.spinner")
r("MDFloatingLabel", module="kivymd.uix.tab")
r("MDTabsLabel", module="kivymd.uix.tab")
r("MDTabsBase", module="kivymd.uix.tab")
r("MDTabsMain", module="kivymd.uix.tab")
r("MDTabsCarousel", module="kivymd.uix.tab")
r("MDTabsScrollView", module="kivymd.uix.tab")
r("MDTabsBar", module="kivymd.uix.tab")
r("MDTabs", module="kivymd.uix.tab")
r("MDTextField", module="kivymd.uix.textfield")
r("MDTextField", module="kivymd.uix.textfield")
r("MDTextFieldRound", module="kivymd.uix.textfield")
r("MDTextFieldRect", module="kivymd.uix.textfield")
r("MDToolbar", module="kivymd.uix.toolbar")
r("MDBottomAppBar", module="kivymd.uix.toolbar")
r("MDDropDownItem", module="kivymd.uix.dropdownitem")
