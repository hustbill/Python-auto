import xml.dom.minidom

def main():

    # use the parse() function to load and parse xml file
    doc = xml.dom.minidom.parse("test.xml")
    print(doc.nodeName)  # #document
    print(doc.firstChild.tagName)  # Configuration
    child_nodes = doc.firstChild.childNodes

    count = 0
    for index, node in enumerate(child_nodes):
        
        if (node.localName != None):
            count = count + 1
            print(count, node.localName)

if __name__ == "__main__":
    main()

"""
❯ python parse-xml.py

#document
Configuration
1 Alias
2 AcceptRequestsRoutedThroughGateway
3 AllowAddingDataElementToMigrationAPIException
4 AllowIncubationTenantsSync
5 AllowResponseGovernorToLimitDirectoryChangesResponse
6 AllowSiMoveForMultiGeoEnabledService
7 AppLogoBackfillAppLimit
8 AssumeAllRedirectedCallsFromBlackforest
9 AuditTableStorageEndpointSuffixOverride
10 AuthorizeCertByMsitTrustedIssuers
11 AuthorizeCertByTrustedIssuers
12 AzureEntityPropertySizeLimit
13 AzureAccountToDsmsSasTokenPathMapping
14 AzureAccountToDsmsStorageAccountPathMapping
15 AzureEntityPropertySizeLimitPhased
16 AzureStorageTableClientResetIntervalInMinutes
17 AzureStorageTableClientResetIntervalInMinutesPhased
18 BackfillFailoverThreshold
"""