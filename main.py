import zeep
from zeep.transports import Transport
from requests import Session, Request
from codetiming import Timer

with Timer(name="context manager"):
    session = Session()
    session.verify = False
    transport = Transport(session=session)

    wsdl = 'https://rdws.rd.go.th/serviceRD3/checktinpinservice.asmx?wsdl'
    client = zeep.Client(wsdl=wsdl, transport=transport)

    result = client.service.ServiceTIN('anonymous', 'anonymous', '1419900489238')
    print(result)