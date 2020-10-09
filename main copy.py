import zeep
from zeep.transports import Transport
from requests import Session, Request
from codetiming import Timer

with Timer(name="context manager"):
    session = Session()
    session.verify = False
    transport = Transport(session=session)

    wsdl = 'https://rdws.rd.go.th/serviceRD3/vatserviceRD3.asmx?wsdl'
    client = zeep.Client(wsdl=wsdl, transport=transport)

    # result = client.service.Service('anonymous', 'anonymous', '', "โฟลว์แอคเคาท์", 0,0,0)
    result = client.service.Service('anonymous', 'anonymous', '0105558096348', "", 0,0,0)
    print(result)