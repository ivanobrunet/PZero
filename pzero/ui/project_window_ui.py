# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'project_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ProjectWindow(object):
    def setupUi(self, ProjectWindow):
        ProjectWindow.setObjectName("ProjectWindow")
        ProjectWindow.resize(1418, 800)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ProjectWindow.sizePolicy().hasHeightForWidth())
        ProjectWindow.setSizePolicy(sizePolicy)
        ProjectWindow.setMinimumSize(QtCore.QSize(300, 100))
        ProjectWindow.setStyleSheet("")
        ProjectWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.centralwidget = QtWidgets.QWidget(ProjectWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(1280, 470))
        self.centralwidget.setBaseSize(QtCore.QSize(1280, 470))
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(4, 4, 4, 4)
        self.horizontalLayout.setSpacing(8)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabCentral = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.tabCentral.sizePolicy().hasHeightForWidth())
        self.tabCentral.setSizePolicy(sizePolicy)
        self.tabCentral.setMinimumSize(QtCore.QSize(1272, 462))
        self.tabCentral.setBaseSize(QtCore.QSize(1272, 462))
        self.tabCentral.setObjectName("tabCentral")
        self.tabGeology = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.tabGeology.sizePolicy().hasHeightForWidth())
        self.tabGeology.setSizePolicy(sizePolicy)
        self.tabGeology.setMinimumSize(QtCore.QSize(1266, 430))
        self.tabGeology.setBaseSize(QtCore.QSize(1266, 430))
        self.tabGeology.setObjectName("tabGeology")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tabGeology)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.GeologyTableView = QtWidgets.QTableView(self.tabGeology)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.GeologyTableView.sizePolicy().hasHeightForWidth())
        self.GeologyTableView.setSizePolicy(sizePolicy)
        self.GeologyTableView.setMinimumSize(QtCore.QSize(0, 0))
        self.GeologyTableView.setBaseSize(QtCore.QSize(0, 0))
        self.GeologyTableView.setSortingEnabled(True)
        self.GeologyTableView.setObjectName("GeologyTableView")
        self.verticalLayout_4.addWidget(self.GeologyTableView)
        self.tabCentral.addTab(self.tabGeology, "")
        self.tabXSections = QtWidgets.QWidget()
        self.tabXSections.setObjectName("tabXSections")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tabXSections)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.XSectionsTableView = QtWidgets.QTableView(self.tabXSections)
        self.XSectionsTableView.setSortingEnabled(True)
        self.XSectionsTableView.setObjectName("XSectionsTableView")
        self.verticalLayout_6.addWidget(self.XSectionsTableView)
        self.tabCentral.addTab(self.tabXSections, "")
        self.tabBoundaries = QtWidgets.QWidget()
        self.tabBoundaries.setObjectName("tabBoundaries")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tabBoundaries)
        self.verticalLayout.setObjectName("verticalLayout")
        self.BoundariesTableView = QtWidgets.QTableView(self.tabBoundaries)
        self.BoundariesTableView.setSortingEnabled(True)
        self.BoundariesTableView.setObjectName("BoundariesTableView")
        self.verticalLayout.addWidget(self.BoundariesTableView)
        self.tabCentral.addTab(self.tabBoundaries, "")
        self.tabMeshes3D = QtWidgets.QWidget()
        self.tabMeshes3D.setObjectName("tabMeshes3D")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.tabMeshes3D)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.Meshes3DTableView = QtWidgets.QTableView(self.tabMeshes3D)
        self.Meshes3DTableView.setSortingEnabled(True)
        self.Meshes3DTableView.setObjectName("Meshes3DTableView")
        self.verticalLayout_7.addWidget(self.Meshes3DTableView)
        self.tabCentral.addTab(self.tabMeshes3D, "")
        self.tabDOMs = QtWidgets.QWidget()
        self.tabDOMs.setObjectName("tabDOMs")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.tabDOMs)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.DOMsTableView = QtWidgets.QTableView(self.tabDOMs)
        self.DOMsTableView.setSortingEnabled(True)
        self.DOMsTableView.setObjectName("DOMsTableView")
        self.verticalLayout_8.addWidget(self.DOMsTableView)
        self.tabCentral.addTab(self.tabDOMs, "")
        self.tabImages = QtWidgets.QWidget()
        self.tabImages.setObjectName("tabImages")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.tabImages)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.ImagesTableView = QtWidgets.QTableView(self.tabImages)
        self.ImagesTableView.setSortingEnabled(True)
        self.ImagesTableView.setObjectName("ImagesTableView")
        self.verticalLayout_9.addWidget(self.ImagesTableView)
        self.tabCentral.addTab(self.tabImages, "")
        self.tabWells = QtWidgets.QWidget()
        self.tabWells.setObjectName("tabWells")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.tabWells)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.WellsTableView = QtWidgets.QTableView(self.tabWells)
        self.WellsTableView.setObjectName("WellsTableView")
        self.verticalLayout_10.addWidget(self.WellsTableView)
        self.tabCentral.addTab(self.tabWells, "")
        self.tabFluids = QtWidgets.QWidget()
        self.tabFluids.setEnabled(True)
        self.tabFluids.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.tabFluids.setObjectName("tabFluids")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.tabFluids)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.FluidsTableView = QtWidgets.QTableView(self.tabFluids)
        self.FluidsTableView.setObjectName("FluidsTableView")
        self.verticalLayout_21.addWidget(self.FluidsTableView)
        self.tabCentral.addTab(self.tabFluids, "")
        self.tabBackgrounds = QtWidgets.QWidget()
        self.tabBackgrounds.setObjectName("tabBackgrounds")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.tabBackgrounds)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.BackgroundsTableView = QtWidgets.QTableView(self.tabBackgrounds)
        self.BackgroundsTableView.setObjectName("BackgroundsTableView")
        self.verticalLayout_11.addWidget(self.BackgroundsTableView)
        self.tabCentral.addTab(self.tabBackgrounds, "")
        self.tabLegend = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.tabLegend.sizePolicy().hasHeightForWidth())
        self.tabLegend.setSizePolicy(sizePolicy)
        self.tabLegend.setMinimumSize(QtCore.QSize(1266, 430))
        self.tabLegend.setBaseSize(QtCore.QSize(1266, 430))
        self.tabLegend.setObjectName("tabLegend")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tabLegend)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.LegendTreeWidget = QtWidgets.QTreeWidget(self.tabLegend)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LegendTreeWidget.sizePolicy().hasHeightForWidth())
        self.LegendTreeWidget.setSizePolicy(sizePolicy)
        self.LegendTreeWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.LegendTreeWidget.setBaseSize(QtCore.QSize(0, 0))
        self.LegendTreeWidget.setObjectName("LegendTreeWidget")
        self.LegendTreeWidget.headerItem().setText(0, "1")
        self.verticalLayout_3.addWidget(self.LegendTreeWidget)
        self.tabCentral.addTab(self.tabLegend, "")
        self.tabProperties = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabProperties.sizePolicy().hasHeightForWidth())
        self.tabProperties.setSizePolicy(sizePolicy)
        self.tabProperties.setMinimumSize(QtCore.QSize(1266, 430))
        self.tabProperties.setBaseSize(QtCore.QSize(1266, 430))
        self.tabProperties.setToolTipDuration(-3)
        self.tabProperties.setObjectName("tabProperties")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tabProperties)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.PropertiesTableWidget = QtWidgets.QTableWidget(self.tabProperties)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PropertiesTableWidget.sizePolicy().hasHeightForWidth())
        self.PropertiesTableWidget.setSizePolicy(sizePolicy)
        self.PropertiesTableWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.PropertiesTableWidget.setBaseSize(QtCore.QSize(0, 0))
        self.PropertiesTableWidget.setObjectName("PropertiesTableWidget")
        self.PropertiesTableWidget.setColumnCount(0)
        self.PropertiesTableWidget.setRowCount(0)
        self.verticalLayout_2.addWidget(self.PropertiesTableWidget)
        self.tabCentral.addTab(self.tabProperties, "")
        self.tabTerminal = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.tabTerminal.sizePolicy().hasHeightForWidth())
        self.tabTerminal.setSizePolicy(sizePolicy)
        self.tabTerminal.setMinimumSize(QtCore.QSize(1266, 430))
        self.tabTerminal.setBaseSize(QtCore.QSize(1266, 430))
        self.tabTerminal.setObjectName("tabTerminal")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tabTerminal)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.TextTerminal = QtWidgets.QPlainTextEdit(self.tabTerminal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TextTerminal.sizePolicy().hasHeightForWidth())
        self.TextTerminal.setSizePolicy(sizePolicy)
        self.TextTerminal.setMinimumSize(QtCore.QSize(0, 0))
        self.TextTerminal.setBaseSize(QtCore.QSize(0, 0))
        self.TextTerminal.setReadOnly(True)
        self.TextTerminal.setObjectName("TextTerminal")
        self.verticalLayout_5.addWidget(self.TextTerminal)
        self.tabCentral.addTab(self.tabTerminal, "")
        self.horizontalLayout.addWidget(self.tabCentral)
        ProjectWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ProjectWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1418, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menubar.sizePolicy().hasHeightForWidth())
        self.menubar.setSizePolicy(sizePolicy)
        self.menubar.setMinimumSize(QtCore.QSize(1280, 30))
        self.menubar.setMaximumSize(QtCore.QSize(16777215, 30))
        self.menubar.setBaseSize(QtCore.QSize(1280, 18))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.menubar.setFont(font)
        self.menubar.setAutoFillBackground(False)
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setTearOffEnabled(True)
        self.menuFile.setObjectName("menuFile")
        self.menuWindow = QtWidgets.QMenu(self.menubar)
        self.menuWindow.setTearOffEnabled(True)
        self.menuWindow.setObjectName("menuWindow")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setTearOffEnabled(True)
        self.menuHelp.setObjectName("menuHelp")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setTearOffEnabled(True)
        self.menuEdit.setObjectName("menuEdit")
        self.menuInterpolation_tools = QtWidgets.QMenu(self.menubar)
        self.menuInterpolation_tools.setTearOffEnabled(True)
        self.menuInterpolation_tools.setObjectName("menuInterpolation_tools")
        ProjectWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ProjectWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statusbar.sizePolicy().hasHeightForWidth())
        self.statusbar.setSizePolicy(sizePolicy)
        self.statusbar.setObjectName("statusbar")
        ProjectWindow.setStatusBar(self.statusbar)
        self.actionProjectNew = QtWidgets.QAction(ProjectWindow)
        self.actionProjectNew.setObjectName("actionProjectNew")
        self.actionProjectOpen = QtWidgets.QAction(ProjectWindow)
        self.actionProjectOpen.setObjectName("actionProjectOpen")
        self.actionProjectSave = QtWidgets.QAction(ProjectWindow)
        self.actionProjectSave.setObjectName("actionProjectSave")
        self.actionImportGocad = QtWidgets.QAction(ProjectWindow)
        self.actionImportGocad.setObjectName("actionImportGocad")
        self.actionExportCAD = QtWidgets.QAction(ProjectWindow)
        self.actionExportCAD.setObjectName("actionExportCAD")
        self.actionQuit = QtWidgets.QAction(ProjectWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionView3D = QtWidgets.QAction(ProjectWindow)
        self.actionView3D.setObjectName("actionView3D")
        self.actionViewPlaneXsection = QtWidgets.QAction(ProjectWindow)
        self.actionViewPlaneXsection.setObjectName("actionViewPlaneXsection")
        self.actionViewMap = QtWidgets.QAction(ProjectWindow)
        self.actionViewMap.setObjectName("actionViewMap")
        self.actionViewXYPlot = QtWidgets.QAction(ProjectWindow)
        self.actionViewXYPlot.setObjectName("actionViewXYPlot")
        self.actionAbout = QtWidgets.QAction(ProjectWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionHelp = QtWidgets.QAction(ProjectWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionViewWellLog = QtWidgets.QAction(ProjectWindow)
        self.actionViewWellLog.setObjectName("actionViewWellLog")
        self.actionViewStereoplot = QtWidgets.QAction(ProjectWindow)
        self.actionViewStereoplot.setObjectName("actionViewStereoplot")
        self.actionViewHistogram = QtWidgets.QAction(ProjectWindow)
        self.actionViewHistogram.setObjectName("actionViewHistogram")
        self.actionImportPyvista = QtWidgets.QAction(ProjectWindow)
        self.actionImportPyvista.setObjectName("actionImportPyvista")
        self.actionImportVedo = QtWidgets.QAction(ProjectWindow)
        self.actionImportVedo.setObjectName("actionImportVedo")
        self.actionImportDEM = QtWidgets.QAction(ProjectWindow)
        self.actionImportDEM.setObjectName("actionImportDEM")
        self.actionImportOrthoImage = QtWidgets.QAction(ProjectWindow)
        self.actionImportOrthoImage.setObjectName("actionImportOrthoImage")
        self.actionEditEntityRemove = QtWidgets.QAction(ProjectWindow)
        self.actionEditEntityRemove.setObjectName("actionEditEntityRemove")
        self.actionEditTextureAdd = QtWidgets.QAction(ProjectWindow)
        self.actionEditTextureAdd.setObjectName("actionEditTextureAdd")
        self.actionEditTextureRemove = QtWidgets.QAction(ProjectWindow)
        self.actionEditTextureRemove.setObjectName("actionEditTextureRemove")
        self.actionEditEntityClone = QtWidgets.QAction(ProjectWindow)
        self.actionEditEntityClone.setObjectName("actionEditEntityClone")
        self.actionImportGocadXsection = QtWidgets.QAction(ProjectWindow)
        self.actionImportGocadXsection.setObjectName("actionImportGocadXsection")
        self.actionDelaunay2DInterpolation = QtWidgets.QAction(ProjectWindow)
        self.actionDelaunay2DInterpolation.setCheckable(False)
        self.actionDelaunay2DInterpolation.setObjectName("actionDelaunay2DInterpolation")
        self.actionMergeEntities = QtWidgets.QAction(ProjectWindow)
        self.actionMergeEntities.setObjectName("actionMergeEntities")
        self.actionPoissonInterpolation = QtWidgets.QAction(ProjectWindow)
        self.actionPoissonInterpolation.setObjectName("actionPoissonInterpolation")
        self.actionSurfaceSmoothing = QtWidgets.QAction(ProjectWindow)
        self.actionSurfaceSmoothing.setObjectName("actionSurfaceSmoothing")
        self.actionExtrusion = QtWidgets.QAction(ProjectWindow)
        self.actionExtrusion.setObjectName("actionExtrusion")
        self.actionDecimationPro = QtWidgets.QAction(ProjectWindow)
        self.actionDecimationPro.setObjectName("actionDecimationPro")
        self.actionSubdivisionResampling = QtWidgets.QAction(ProjectWindow)
        self.actionSubdivisionResampling.setObjectName("actionSubdivisionResampling")
        self.actionDecimationQuadric = QtWidgets.QAction(ProjectWindow)
        self.actionDecimationQuadric.setObjectName("actionDecimationQuadric")
        self.actionIntersectionXSection = QtWidgets.QAction(ProjectWindow)
        self.actionIntersectionXSection.setObjectName("actionIntersectionXSection")
        self.actionProject2DEM = QtWidgets.QAction(ProjectWindow)
        self.actionProject2DEM.setObjectName("actionProject2DEM")
        self.actionLoopStructuralImplicitModelling = QtWidgets.QAction(ProjectWindow)
        self.actionLoopStructuralImplicitModelling.setObjectName("actionLoopStructuralImplicitModelling")
        self.actionImportSEGY = QtWidgets.QAction(ProjectWindow)
        self.actionImportSEGY.setObjectName("actionImportSEGY")
        self.actionCalculateNormal = QtWidgets.QAction(ProjectWindow)
        self.actionCalculateNormal.setObjectName("actionCalculateNormal")
        self.actionCalculateLineation = QtWidgets.QAction(ProjectWindow)
        self.actionCalculateLineation.setObjectName("actionCalculateLineation")
        self.actionAddProperty = QtWidgets.QAction(ProjectWindow)
        self.actionAddProperty.setObjectName("actionAddProperty")
        self.actionRemoveProperty = QtWidgets.QAction(ProjectWindow)
        self.actionRemoveProperty.setObjectName("actionRemoveProperty")
        self.actionProject2XSection = QtWidgets.QAction(ProjectWindow)
        self.actionProject2XSection.setObjectName("actionProject2XSection")
        self.actionImportSHP = QtWidgets.QAction(ProjectWindow)
        self.actionImportSHP.setObjectName("actionImportSHP")
        self.actionImportGocadBoundary = QtWidgets.QAction(ProjectWindow)
        self.actionImportGocadBoundary.setObjectName("actionImportGocadBoundary")
        self.actionImportXsectionImage = QtWidgets.QAction(ProjectWindow)
        self.actionImportXsectionImage.setObjectName("actionImportXsectionImage")
        self.actionConnectedParts = QtWidgets.QAction(ProjectWindow)
        self.actionConnectedParts.setObjectName("actionConnectedParts")
        self.actionSplitMultipart = QtWidgets.QAction(ProjectWindow)
        self.actionSplitMultipart.setObjectName("actionSplitMultipart")
        self.actionImportPC = QtWidgets.QAction(ProjectWindow)
        self.actionImportPC.setObjectName("actionImportPC")
        self.actionImportWellData = QtWidgets.QAction(ProjectWindow)
        self.actionImportWellData.setObjectName("actionImportWellData")
        self.actionExportVTK = QtWidgets.QAction(ProjectWindow)
        self.actionExportVTK.setObjectName("actionExportVTK")
        self.actionSplitSurf = QtWidgets.QAction(ProjectWindow)
        self.actionSplitSurf.setObjectName("actionSplitSurf")
        self.actionRetopologize = QtWidgets.QAction(ProjectWindow)
        self.actionRetopologize.setObjectName("actionRetopologize")
        self.actionBuildOctree = QtWidgets.QAction(ProjectWindow)
        self.actionBuildOctree.setObjectName("actionBuildOctree")
        self.actionDecimatePointCloud = QtWidgets.QAction(ProjectWindow)
        self.actionDecimatePointCloud.setObjectName("actionDecimatePointCloud")
        self.actionExportCSV = QtWidgets.QAction(ProjectWindow)
        self.actionExportCSV.setObjectName("actionExportCSV")
        self.menuFile.addAction(self.actionProjectNew)
        self.menuFile.addAction(self.actionProjectOpen)
        self.menuFile.addAction(self.actionProjectSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionImportGocad)
        self.menuFile.addAction(self.actionImportGocadXsection)
        self.menuFile.addAction(self.actionImportGocadBoundary)
        self.menuFile.addAction(self.actionImportPC)
        self.menuFile.addAction(self.actionImportPyvista)
        self.menuFile.addAction(self.actionImportVedo)
        self.menuFile.addAction(self.actionImportSHP)
        self.menuFile.addAction(self.actionImportDEM)
        self.menuFile.addAction(self.actionImportOrthoImage)
        self.menuFile.addAction(self.actionImportXsectionImage)
        self.menuFile.addAction(self.actionImportWellData)
        self.menuFile.addAction(self.actionImportSEGY)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExportCAD)
        self.menuFile.addAction(self.actionExportVTK)
        self.menuFile.addAction(self.actionExportCSV)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuWindow.addAction(self.actionView3D)
        self.menuWindow.addAction(self.actionViewMap)
        self.menuWindow.addAction(self.actionViewPlaneXsection)
        self.menuWindow.addAction(self.actionViewWellLog)
        self.menuWindow.addSeparator()
        self.menuWindow.addAction(self.actionViewXYPlot)
        self.menuWindow.addAction(self.actionViewHistogram)
        self.menuWindow.addAction(self.actionViewStereoplot)
        self.menuWindow.addSeparator()
        self.menuHelp.addAction(self.actionHelp)
        self.menuHelp.addAction(self.actionAbout)
        self.menuEdit.addAction(self.actionEditEntityClone)
        self.menuEdit.addAction(self.actionEditEntityRemove)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionConnectedParts)
        self.menuEdit.addAction(self.actionMergeEntities)
        self.menuEdit.addAction(self.actionSplitMultipart)
        self.menuEdit.addAction(self.actionDecimatePointCloud)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionEditTextureAdd)
        self.menuEdit.addAction(self.actionEditTextureRemove)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionAddProperty)
        self.menuEdit.addAction(self.actionRemoveProperty)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionCalculateNormal)
        self.menuEdit.addAction(self.actionCalculateLineation)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionBuildOctree)
        self.menuInterpolation_tools.addAction(self.actionDelaunay2DInterpolation)
        self.menuInterpolation_tools.addAction(self.actionPoissonInterpolation)
        self.menuInterpolation_tools.addAction(self.actionLoopStructuralImplicitModelling)
        self.menuInterpolation_tools.addSeparator()
        self.menuInterpolation_tools.addAction(self.actionSurfaceSmoothing)
        self.menuInterpolation_tools.addAction(self.actionSubdivisionResampling)
        self.menuInterpolation_tools.addAction(self.actionDecimationPro)
        self.menuInterpolation_tools.addAction(self.actionDecimationQuadric)
        self.menuInterpolation_tools.addAction(self.actionRetopologize)
        self.menuInterpolation_tools.addSeparator()
        self.menuInterpolation_tools.addAction(self.actionExtrusion)
        self.menuInterpolation_tools.addAction(self.actionIntersectionXSection)
        self.menuInterpolation_tools.addAction(self.actionProject2XSection)
        self.menuInterpolation_tools.addAction(self.actionProject2DEM)
        self.menuInterpolation_tools.addAction(self.actionSplitSurf)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuInterpolation_tools.menuAction())
        self.menubar.addAction(self.menuWindow.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(ProjectWindow)
        self.tabCentral.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(ProjectWindow)

    def retranslateUi(self, ProjectWindow):
        _translate = QtCore.QCoreApplication.translate
        ProjectWindow.setWindowTitle(_translate("ProjectWindow", "PZero"))
        self.tabGeology.setToolTip(_translate("ProjectWindow", "Entities"))
        self.tabGeology.setAccessibleName(_translate("ProjectWindow", "Entities"))
        self.GeologyTableView.setToolTip(_translate("ProjectWindow", "Entities"))
        self.GeologyTableView.setAccessibleName(_translate("ProjectWindow", "Entities"))
        self.tabCentral.setTabText(self.tabCentral.indexOf(self.tabGeology), _translate("ProjectWindow", "Geology"))
        self.tabCentral.setTabToolTip(self.tabCentral.indexOf(self.tabGeology), _translate("ProjectWindow", "Geology"))
        self.tabCentral.setTabText(self.tabCentral.indexOf(self.tabXSections), _translate("ProjectWindow", "X Sections"))
        self.tabCentral.setTabToolTip(self.tabCentral.indexOf(self.tabXSections), _translate("ProjectWindow", "X Sections"))
        self.tabCentral.setTabText(self.tabCentral.indexOf(self.tabBoundaries), _translate("ProjectWindow", "Boundaries"))
        self.tabCentral.setTabText(self.tabCentral.indexOf(self.tabMeshes3D), _translate("ProjectWindow", "3D Meshes and Grids"))
        self.tabCentral.setTabToolTip(self.tabCentral.indexOf(self.tabMeshes3D), _translate("ProjectWindow", "3D Meshes and Grids"))
        self.tabCentral.setTabText(self.tabCentral.indexOf(self.tabDOMs), _translate("ProjectWindow", "DEMs and DOMs"))
        self.tabCentral.setTabToolTip(self.tabCentral.indexOf(self.tabDOMs), _translate("ProjectWindow", "DEMs and DOMs"))
        self.tabCentral.setTabText(self.tabCentral.indexOf(self.tabImages), _translate("ProjectWindow", "Images"))
        self.tabCentral.setTabToolTip(self.tabCentral.indexOf(self.tabImages), _translate("ProjectWindow", "Images"))
        self.tabCentral.setTabText(self.tabCentral.indexOf(self.tabWells), _translate("ProjectWindow", "Wells"))
        self.tabCentral.setTabText(self.tabCentral.indexOf(self.tabFluids), _translate("ProjectWindow", "Fluid contacts"))
        self.tabCentral.setTabText(self.tabCentral.indexOf(self.tabBackgrounds), _translate("ProjectWindow", "Background data"))
        self.tabLegend.setToolTip(_translate("ProjectWindow", "Legend"))
        self.tabLegend.setAccessibleName(_translate("ProjectWindow", "Legend"))
        self.LegendTreeWidget.setToolTip(_translate("ProjectWindow", "Legend"))
        self.LegendTreeWidget.setAccessibleName(_translate("ProjectWindow", "Legend"))
        self.tabCentral.setTabText(self.tabCentral.indexOf(self.tabLegend), _translate("ProjectWindow", "Legend"))
        self.tabProperties.setToolTip(_translate("ProjectWindow", "Properties"))
        self.tabProperties.setAccessibleName(_translate("ProjectWindow", "Properties"))
        self.PropertiesTableWidget.setToolTip(_translate("ProjectWindow", "Properties"))
        self.PropertiesTableWidget.setAccessibleName(_translate("ProjectWindow", "Properties"))
        self.tabCentral.setTabText(self.tabCentral.indexOf(self.tabProperties), _translate("ProjectWindow", "Properties"))
        self.tabTerminal.setToolTip(_translate("ProjectWindow", "Terminal"))
        self.tabTerminal.setAccessibleName(_translate("ProjectWindow", "Terminal"))
        self.TextTerminal.setToolTip(_translate("ProjectWindow", "Terminal"))
        self.TextTerminal.setAccessibleName(_translate("ProjectWindow", "Terminal"))
        self.tabCentral.setTabText(self.tabCentral.indexOf(self.tabTerminal), _translate("ProjectWindow", "Terminal"))
        self.tabCentral.setTabToolTip(self.tabCentral.indexOf(self.tabTerminal), _translate("ProjectWindow", "Terminal"))
        self.menuFile.setTitle(_translate("ProjectWindow", "File"))
        self.menuWindow.setTitle(_translate("ProjectWindow", "Window"))
        self.menuHelp.setTitle(_translate("ProjectWindow", "Help"))
        self.menuEdit.setTitle(_translate("ProjectWindow", "Edit"))
        self.menuInterpolation_tools.setTitle(_translate("ProjectWindow", "Interpolation"))
        self.actionProjectNew.setText(_translate("ProjectWindow", "New Project"))
        self.actionProjectOpen.setText(_translate("ProjectWindow", "Open Project"))
        self.actionProjectSave.setText(_translate("ProjectWindow", "Save Project"))
        self.actionImportGocad.setText(_translate("ProjectWindow", "Import Gocad"))
        self.actionImportGocad.setToolTip(_translate("ProjectWindow", "Import Gocad"))
        self.actionExportCAD.setText(_translate("ProjectWindow", "Export CAD"))
        self.actionQuit.setText(_translate("ProjectWindow", "Quit"))
        self.actionView3D.setText(_translate("ProjectWindow", "3D View"))
        self.actionViewPlaneXsection.setText(_translate("ProjectWindow", "Plane X Section View"))
        self.actionViewMap.setText(_translate("ProjectWindow", "Map View"))
        self.actionViewXYPlot.setText(_translate("ProjectWindow", "XY Plot View"))
        self.actionAbout.setText(_translate("ProjectWindow", "About"))
        self.actionHelp.setText(_translate("ProjectWindow", "Help"))
        self.actionViewWellLog.setText(_translate("ProjectWindow", "Well Log View"))
        self.actionViewStereoplot.setText(_translate("ProjectWindow", "Stereoplot View"))
        self.actionViewHistogram.setText(_translate("ProjectWindow", "Histogram View"))
        self.actionImportPyvista.setText(_translate("ProjectWindow", "Import PyVista"))
        self.actionImportVedo.setText(_translate("ProjectWindow", "Import Vedo"))
        self.actionImportDEM.setText(_translate("ProjectWindow", "Import DEM"))
        self.actionImportOrthoImage.setText(_translate("ProjectWindow", "Import OrthoImage"))
        self.actionEditEntityRemove.setText(_translate("ProjectWindow", "Remove Entity"))
        self.actionEditTextureAdd.setText(_translate("ProjectWindow", "Add Texture"))
        self.actionEditTextureRemove.setText(_translate("ProjectWindow", "Remove Texture"))
        self.actionEditEntityClone.setText(_translate("ProjectWindow", "Clone Entity"))
        self.actionImportGocadXsection.setText(_translate("ProjectWindow", "Import Gocad Xsection"))
        self.actionDelaunay2DInterpolation.setText(_translate("ProjectWindow", "Delaunay 2D"))
        self.actionMergeEntities.setText(_translate("ProjectWindow", "Merge Entities"))
        self.actionPoissonInterpolation.setText(_translate("ProjectWindow", "Poisson"))
        self.actionSurfaceSmoothing.setText(_translate("ProjectWindow", "Surface Smoothing"))
        self.actionExtrusion.setText(_translate("ProjectWindow", "Extrusion"))
        self.actionDecimationPro.setText(_translate("ProjectWindow", "Decimation Pro"))
        self.actionDecimationPro.setToolTip(_translate("ProjectWindow", "DecimationPro"))
        self.actionSubdivisionResampling.setText(_translate("ProjectWindow", "Subdivision Resampling"))
        self.actionDecimationQuadric.setText(_translate("ProjectWindow", "Decimation Quadric"))
        self.actionDecimationQuadric.setToolTip(_translate("ProjectWindow", "DecimationQuadric"))
        self.actionIntersectionXSection.setText(_translate("ProjectWindow", "XSection Intersection"))
        self.actionProject2DEM.setText(_translate("ProjectWindow", "Project to DEM"))
        self.actionLoopStructuralImplicitModelling.setText(_translate("ProjectWindow", "LoopStructural Implicit Modelling"))
        self.actionImportSEGY.setText(_translate("ProjectWindow", "Import SEGY"))
        self.actionCalculateNormal.setText(_translate("ProjectWindow", "Calculate normal"))
        self.actionCalculateNormal.setToolTip(_translate("ProjectWindow", "Calculate normal unit vector"))
        self.actionCalculateLineation.setText(_translate("ProjectWindow", "Calculate lineation"))
        self.actionCalculateLineation.setToolTip(_translate("ProjectWindow", "Calculate lineation unit vector"))
        self.actionAddProperty.setText(_translate("ProjectWindow", "Add property"))
        self.actionAddProperty.setToolTip(_translate("ProjectWindow", "Add empty property"))
        self.actionRemoveProperty.setText(_translate("ProjectWindow", "Remove property"))
        self.actionProject2XSection.setText(_translate("ProjectWindow", "Project to XSection"))
        self.actionImportSHP.setText(_translate("ProjectWindow", "Import SHP"))
        self.actionImportGocadBoundary.setText(_translate("ProjectWindow", "Import Gocad Boundary"))
        self.actionImportXsectionImage.setText(_translate("ProjectWindow", "Import Xsection Image"))
        self.actionConnectedParts.setText(_translate("ProjectWindow", "Connected Parts"))
        self.actionSplitMultipart.setText(_translate("ProjectWindow", "Split Multi-part"))
        self.actionImportPC.setText(_translate("ProjectWindow", "Import Point Clouds"))
        self.actionImportWellData.setText(_translate("ProjectWindow", "Import well data"))
        self.actionExportVTK.setText(_translate("ProjectWindow", "Export vtk"))
        self.actionSplitSurf.setText(_translate("ProjectWindow", "Split surfaces"))
        self.actionRetopologize.setText(_translate("ProjectWindow", "Retopologize"))
        self.actionBuildOctree.setText(_translate("ProjectWindow", "Build octree"))
        self.actionDecimatePointCloud.setText(_translate("ProjectWindow", "Decimate point cloud"))
        self.actionExportCSV.setText(_translate("ProjectWindow", "Export CSV"))
