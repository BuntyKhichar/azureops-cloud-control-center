
param location string = 'centralindia'
param vnetName string = 'vnet-azureops-lab'
param vnetAddressPrefix string = '10.10.0.0/16'

param subnetOnePrefix string = '10.10.1.0/24'
param subnetTwoPrefix string = '10.10.2.0/24'

resource vnet 'Microsoft.Network/virtualNetworks@2024-05-01' = {
  name: vnetName
  location: location
  properties: {
    addressSpace: {
      addressPrefixes: [
        vnetAddressPrefix
      ]
    }
    subnets: [
      {
        name: 'snet-app'
        properties: {
          addressPrefix: subnetOnePrefix
        }
      }
      {
        name: 'snet-management'
        properties: {
          addressPrefix: subnetTwoPrefix
        }
      }
    ]
  }
}

output virtualNetworkName string = vnet.name
output virtualNetworkAddressSpace string = vnet.properties.addressSpace.addressPrefixes[0]
output subnetNames array = [
  'snet-app'
  'snet-management'
]
