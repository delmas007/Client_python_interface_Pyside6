import zeep

wsdl_url = "http://localhost:8084/Cmu?wsdl"

client = zeep.Client(wsdl=wsdl_url)