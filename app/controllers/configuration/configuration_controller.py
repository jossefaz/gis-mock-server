

def get_mock_config():
    return {
    "MapConfig": {
        "target": "map",
        "proj": "EPSG:2039",
        "center": [
            221102,
            631882
        ],
        "zoom": 6
    },
    "Search": {
        "Geocode": {
            "url": "http://127.0.0.1:4000"
        }
    },
    "ContextMenus": {
        "Manti": {
            "url": "http://meitarimds:5002/api/BankPkudot/groupBy?filter={\"AdaptorId\": \"MTCS\", \"category\": \"Tsirkel\"}&MENU_TYPE=BY_LAYERID",
            "path": "Manti",
            "status": 1,
            "configuration": {
                "commandApiAddress": "http://meitarimds:2210/api/commands",
                "mockUpApiAddress": "http://meitarimds:5002/api/MockupData/byName?name="
            }
        },
        "Junctions": {
            "url": "",
            "path": "Junctions",
            "status": 1,
            "configuration": {}
        }
    },
    "SearchConfigs": [
        {
            "name": "חיפוש לדוגמא",
            "type": "OBJ_ARRAY",
            "field": "field1",
            "itemTitlePrefix": "לפני_",
            "itemTitleField": "field3",
            "itemTitlePostfix": "_אחרי",
            "data": [
                {
                    "field1": "שלום כיתה א",
                    "field2": 12,
                    "field3": "ערך 1",
                    "X": 222000,
                    "Y": 630000
                },
                {
                    "field1": "וגם כיתה ב",
                    "field2": 15,
                    "field3": "ערך 2",
                    "X": 222010,
                    "Y": 630050
                },
                {
                    "field1": "ואולי גם ג",
                    "field2": 17,
                    "field3": "ערך 3",
                    "X": 222020,
                    "Y": 630070
                }
            ]
        },
        {
            "name": "חיפוש אחר",
            "type": "OBJ_ARRAY",
            "field": "field1",
            "itemTitlePrefix": "לפני_",
            "itemTitleField": "field3",
            "itemTitlePostfix": "_אחרי",
            "data": [
                {
                    "field1": "מה נשמע בכיתה",
                    "field2": 12,
                    "field3": "ערך 4",
                    "X": 222000,
                    "Y": 630000
                },
                {
                    "field1": "ימי קורונה",
                    "field2": 15,
                    "field3": "ערך 5",
                    "X": 222010,
                    "Y": 630050
                },
                {
                    "field1": "וימי אביב",
                    "field2": 17,
                    "field3": "ערך 6",
                    "X": 222020,
                    "Y": 630070
                }
            ]
        }
    ],
    "layers": [
        {
            "id": 1,
            "name": "dimigcompile",
            "alias": "שכבה לדוגמא",
            "url": "http://localhost:8080/geoserver/Jeru/wms",
            "params": {
                "LAYERS": "Jeru:dimigcompile"
            },
            "serverType": "geoserver",
            "visible": 1,
            "selectable": 1
        }
    ],
    "Widgets": {
        "tools": [
            {
                "Id": 1,
                "ToolName": "BaseMapGallery",
                "ToolTip": "מפות רקע",
                "ToolImage": "basemap.png",
                "ToolIcon": "map-rolled",
                "ToolActionInvoker": "",
                "ToolInvokerType": 0,
                "ToolTypeID": 1,
                "OnCreate": "default",
                "OnDestroy": "default",
                "ToolParams": "",
                "ToolLocation": "",
                "Order": 1,
                "IsAGroup": 0,
                "ToolGroupId": 0,
                "ToolContainer": "TopNav",
                "IsOpen": 0
            },
            {
                "Id": 4,
                "ToolName": "Identify",
                "ToolTip": "בחירת יישות",
                "ToolIcon": "dashed-square-arrow",
                "ToolActionInvoker": "",
                "ToolInvokerType": 0,
                "ToolTypeID": 1,
                "OnCreate": "default",
                "OnDestroy": "default",
                "ToolParams": "",
                "ToolLocation": "",
                "Order": 1,
                "IsAGroup": 0,
                "ToolGroupId": 0,
                "ToolContainer": "TopNav",
                "IsOpen": 0
            },
            {
                "Id": 6,
                "ToolName": "MeasureDistance",
                "ToolTip": "מחשבון מרחקים",
                "ToolIcon": "ruler-l",
                "ToolActionInvoker": "",
                "ToolInvokerType": 0,
                "ToolTypeID": 1,
                "OnCreate": "default",
                "OnDestroy": "default",
                "ToolParams": "",
                "ToolLocation": "",
                "Order": 1,
                "IsAGroup": 0,
                "ToolGroupId": 0,
                "ToolContainer": "TopNav",
                "IsOpen": 0
            },
            {
                "Id": 8,
                "ToolName": "Draw",
                "ToolTip": "צייר",
                "ToolIcon": "artist-palette",
                "ToolActionInvoker": "",
                "ToolInvokerType": 0,
                "ToolTypeID": 1,
                "OnCreate": "default",
                "OnDestroy": "default",
                "ToolParams": "",
                "ToolLocation": "",
                "Order": 1,
                "IsAGroup": 0,
                "ToolGroupId": 0,
                "ToolContainer": "TopNav",
                "IsOpen": 0
            },
            {
                "Id": 9,
                "ToolName": "Legend",
                "ToolTip": "מקרא",
                "ToolImage": "legend.png",
                "ToolIcon": "legend",
                "ToolActionInvoker": "",
                "ToolInvokerType": 0,
                "ToolTypeID": 1,
                "OnCreate": "default",
                "OnDestroy": "default",
                "ToolParams": "",
                "ToolLocation": "",
                "Order": 1,
                "IsAGroup": 0,
                "ToolGroupId": 0,
                "ToolContainer": "TopNav",
                "IsOpen": 0
            },
            {
                "Id": 10,
                "ToolName": "Coordinates",
                "ToolTip": "המרת קורדינטות",
                "ToolIcon": "radar",
                "ToolActionInvoker": "",
                "ToolInvokerType": 0,
                "ToolTypeID": 1,
                "OnCreate": "default",
                "OnDestroy": "default",
                "ToolParams": "",
                "ToolLocation": "",
                "Order": 1,
                "IsAGroup": 0,
                "ToolGroupId": 0,
                "ToolContainer": "TopNav",
                "IsOpen": 0
            },
            {
                "Id": 11,
                "ToolName": "Screenshooter",
                "ToolTip": "תצלום מסך",
                "ToolIcon": "camera",
                "ToolActionInvoker": "",
                "ToolInvokerType": 0,
                "ToolTypeID": 1,
                "OnCreate": "default",
                "OnDestroy": "default",
                "ToolParams": "",
                "ToolLocation": "",
                "Order": 1,
                "IsAGroup": 0,
                "ToolGroupId": 0,
                "ToolContainer": "TopNav",
                "IsOpen": 0
            },
            {
                "Id": 13,
                "ToolName": "TestTableOfFeature",
                "ToolTip": "טבלת נתונים",
                "ToolIcon": "table",
                "ToolActionInvoker": "",
                "ToolInvokerType": 0,
                "ToolTypeID": 1,
                "OnCreate": "default",
                "OnDestroy": "default",
                "ToolParams": "",
                "ToolLocation": "",
                "Order": 1,
                "IsAGroup": 0,
                "ToolGroupId": 0,
                "ToolContainer": "TopNav",
                "IsOpen": 0
            },
            {
                "Id": 13,
                "ToolName": "TestSpatialSelect",
                "ToolTip": "ניתוח מרחבי",
                "ToolIcon": "cube",
                "ToolActionInvoker": "",
                "ToolInvokerType": 0,
                "ToolTypeID": 1,
                "OnCreate": "default",
                "OnDestroy": "default",
                "ToolParams": "",
                "ToolLocation": "",
                "Order": 1,
                "IsAGroup": 0,
                "ToolGroupId": 0,
                "ToolContainer": "TopNav",
                "IsOpen": 0
            }
        ],
        "groups": [
            {
                "Id": 1,
                "GroupContainer": "TopNav",
                "GroupName": "General",
                "GroupImage": "toolsGroup.png",
                "IsOpen": 0
            }
        ]
    },
    "channels": {
        "name": "MTCS.Units PubSub Channel",
        "type": "PubSub",
        "Channel": "MTCS.Units",
        "reduxTarget": "units",
        "reduxFunction": "UPDATE_FEATURE_ATTRIBUTES",
        "idSourceKey": "id",
        "atrributeListKey": "changes",
        "attributeKey": "field-name",
        "attributeValue": "value",
        "description": "change is MTCS.Units attribute(s)"
    },
    "metaDataApi": {
        "url": "https://localhost:5001/MetaData/getMetaData/"
    },
    "mantiLayerUrl": "http://localhost:8080/geoserver/Jeru/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=Jeru%3Amanti_intersections&maxFeatures=500&outputFormat=application%2Fjson",
    "geoserverUrl": "http://localhost:8080/geoserver/Jeru/",
    "authUrl" : "http://localhost:8040/auth/login"
}