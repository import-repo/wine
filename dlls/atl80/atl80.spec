10 stdcall AtlAdvise(ptr ptr ptr ptr) atl100.AtlAdvise
11 stdcall AtlUnadvise(ptr ptr long) atl100.AtlUnadvise
12 stdcall AtlFreeMarshalStream(ptr) atl100.AtlFreeMarshalStream
13 stdcall AtlMarshalPtrInProc(ptr ptr ptr) atl100.AtlMarshalPtrInProc
14 stdcall AtlUnmarshalPtr(ptr ptr ptr) atl100.AtlUnmarshalPtr
15 stdcall AtlModuleGetClassObject(ptr ptr ptr ptr) atl.AtlModuleGetClassObject
16 stdcall AtlModuleInit(ptr long long) atl.AtlModuleInit
17 stdcall AtlModuleRegisterClassObjects(ptr long long) atl.AtlModuleRegisterClassObjects
18 stdcall AtlModuleRegisterServer(ptr long ptr) atl.AtlModuleRegisterServer
19 stdcall AtlModuleRegisterTypeLib(ptr wstr) atl.AtlModuleRegisterTypeLib
20 stdcall AtlModuleRevokeClassObjects(ptr) atl.AtlModuleRevokeClassObjects
21 stdcall AtlModuleTerm(ptr) atl.AtlModuleTerm
22 stdcall AtlModuleUnregisterServer(ptr ptr) atl.AtlModuleUnregisterServer
23 stdcall AtlModuleUpdateRegistryFromResourceD(ptr wstr long ptr ptr) atl.AtlModuleUpdateRegistryFromResourceD
24 stub AtlWaitWithMessageLoop
25 stub AtlSetErrorInfo
26 stdcall AtlCreateTargetDC(long ptr) atl100.AtlCreateTargetDC
27 stdcall AtlHiMetricToPixel(ptr ptr) atl100.AtlHiMetricToPixel
28 stdcall AtlPixelToHiMetric(ptr ptr) atl100.AtlPixelToHiMetric
29 stub AtlDevModeW2A
30 stdcall AtlComPtrAssign(ptr ptr) atl100.AtlComPtrAssign
31 stdcall AtlComQIPtrAssign(ptr ptr ptr) atl100.AtlComQIPtrAssign
32 stdcall AtlInternalQueryInterface(ptr ptr ptr ptr) atl100.AtlInternalQueryInterface
34 stdcall AtlGetVersion(ptr)
35 stub AtlAxDialogBoxW
36 stub AtlAxDialogBoxA
37 stdcall AtlAxCreateDialogW(long wstr long ptr long) atl100.AtlAxCreateDialogW
38 stdcall AtlAxCreateDialogA(long str long ptr long) atl100.AtlAxCreateDialogA
39 stdcall AtlAxCreateControl(ptr ptr ptr ptr) atl100.AtlAxCreateControl
40 stdcall AtlAxCreateControlEx(ptr ptr ptr ptr ptr ptr ptr) atl100.AtlAxCreateControlEx
41 stdcall AtlAxAttachControl(ptr ptr ptr) atl100.AtlAxAttachControl
42 stdcall AtlAxWinInit() atl100.AtlAxWinInit
43 stdcall AtlModuleAddCreateWndData(ptr ptr ptr) atl.AtlModuleAddCreateWndData # don't forward to atl100.dll
44 stdcall AtlModuleExtractCreateWndData(ptr) atl.AtlModuleExtractCreateWndData # don't forward to atl100.dll
45 stdcall AtlModuleRegisterWndClassInfoW(ptr ptr ptr) atl.AtlModuleRegisterWndClassInfoW # don't forward to atl100.dll
46 stdcall AtlModuleRegisterWndClassInfoA(ptr ptr ptr) atl.AtlModuleRegisterWndClassInfoA # don't forward to atl100.dll
47 stdcall AtlAxGetControl(long ptr) atl100.AtlAxGetControl
48 stdcall AtlAxGetHost(long ptr) atl100.AtlAxGetHost
49 stub AtlRegisterClassCategoriesHelper
50 stdcall AtlIPersistStreamInit_Load(ptr ptr ptr ptr) atl100.AtlIPersistStreamInit_Load
51 stdcall AtlIPersistStreamInit_Save(ptr long ptr ptr ptr) atl100.AtlIPersistStreamInit_Save
52 stub AtlIPersistPropertyBag_Load
53 stub AtlIPersistPropertyBag_Save
54 stub AtlGetObjectSourceInterface
55 stub AtlModuleUnRegisterTypeLib
56 stdcall AtlModuleLoadTypeLib(ptr wstr ptr ptr) atl.AtlModuleLoadTypeLib
57 stdcall AtlModuleUnregisterServerEx(ptr long ptr) atl.AtlModuleUnregisterServerEx
58 stdcall AtlModuleAddTermFunc(ptr ptr long) atl100.AtlModuleAddTermFunc
59 stub AtlAxCreateControlLic
60 stub AtlAxCreateControlLicEx
61 stdcall AtlCreateRegistrar(ptr) atl100.AtlCreateRegistrar
62 stub AltWinModuleRegisterClassExW
63 stub AltWinModuleRegisterClassExA
64 stdcall AltCallTermFunc(ptr) atl100.AltCallTermFunc
65 stub AltWinModuleInit
66 stub AltWinModuleTerm
