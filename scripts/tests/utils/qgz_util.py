import zipfile
import xml.etree.ElementTree as ET

def verify_qgz_file(qgz_file,target_layer):
    # qgz_file = "/home/jyoti.mikkilineni/pi_7/reservoirs/reservoirs.qgz"
    # target_layer = "reference-reservoirs.mbtiles" #nwm_corrected — reservoirs"
    with zipfile.ZipFile(qgz_file, 'r') as z:
        files = z.namelist()
        for f in files:
            print(f)
        qgs_file = [f for f in files if f.endswith(".qgs")][0]
        xml_data = z.read(qgs_file)
        root = ET.fromstring(xml_data)
        layers = root.findall(".//maplayer")
        layer_names = [layer.find("layername").text for layer in layers]
        if target_layer in layer_names:
            print(f"Layer {target_layer} exists")
        else:
            print(f"Doesn't exist")