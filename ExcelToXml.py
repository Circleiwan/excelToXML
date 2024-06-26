import pandas as pd
import xml.etree.ElementTree as ET

def dataZip(filename):
	dataset = pd.read_excel(filename)
	vinList = list(dataset['vin'])
	iccidList = list(dataset['iccid'])
	combinedVinIccid = list(zip(vinList, iccidList))
	return combinedVinIccid

def generateXML(VSNContent=1234, explainContent, SBM_76Content, PBCContent, CTPContent, BCContent, CMContent, CTContent, CBContent, OVContent, VINContent):
	processVehTerminal = ET.Element('processVehTerminal')
	WSInput = ET.SubElement(processVehTerminal, 'WSInput')
	TraceCode = ET.SubElement(WSInput, 'TraceCode')
	VSN = ET.SubElement(TraceCode, 'VSN')
	Explain = ET.SubElement(TraceCode, 'Explain')
	SBM_76 = ET.SubElement(TraceCode, 'SBM_76')
	PowerBatteryCapacity = ET.SubElement(TraceCode, 'PowerBatteryCapacity')
	CarTypePlatform = ET.SubElement(TraceCode, 'CarTypePlatform')
	BatteryCapacity = ET.SubElement(TraceCode, 'BatteryCapacity')
	CarModel = ET.SubElement(TraceCode, 'CarModel')
	CarType = ET.SubElement(TraceCode, 'CarType')
	CarBrand = ET.SubElement(TraceCode, 'CarBrand')
	OperatingVoltage = ET.SubElement(TraceCode, 'OperatingVoltage')
	VIN = ET.SubElement(TraceCode, 'VIN')
	VSN.text = VSNContent
	Explain.text = explainContent
	SBM_76.text = SBM_76Content
	PowerBatteryCapacity.text = PBCContent
	CarTypePlatform.text = CTPContent
	BatteryCapacity.text = BCContent
	CarModel.text = CMContent
	CarType.text = CTContent
	CarBrand.text = CBContent
	OperatingVoltage.text = OVContent
	VIN.text = VINContent
	tree = ET.ElementTree(processVehTerminal)
	tree.write('person.xml')



filename = "VIN ICCID dataset.xlsx"

combinedVinIccid = dataZip(filename)
print(combinedVinIccid)




