

import json

"RowNumber",
"ProtoNumber",
"TubeSerialNumber",
"HVPSNumber",
"Sampler",
"DateStamp",
"AOM1SerialNumber",
"AOM2SerialNumber",
"SamplerBoard",
"ControllerBoard",
"RFBoard",
"ConnectorBoard"
data = []
for i in range (10):

    d =dict(
        id=i,
        protoNumber=f'ProtoNumber_{i}',
        tubeSerialNumber=f'TubeSerialNumber_{i}',
        hvpsNumber=f'HVPSNumber_{i}',
        dateStamp=f'DateStamp_{i}',
        aom1SerialNumber=f'AOM1SerialNumber_{i}',
        aom2SerialNumber=f'AOM2SerialNumber_{i}',
        samplerBoard=f'SamplerBoard_{i}',
        controllerBoard=f'ControllerBoard_{i}',
        rfBoard=f'RFBoard_{i}',
        connectorBoard=f'ConnectorBoard_{i}',
    )
    data.append(d)

with open('sampleProject.json', 'w') as fp:

    json.dump(data, fp, indent=2)