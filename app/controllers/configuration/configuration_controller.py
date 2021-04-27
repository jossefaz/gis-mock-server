

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
            "url" :  "http://meitarimds:5002/api/BankPkudot/groupBy?",
            "path" : "Manti",
            "status" : 1,
            "configuration" : {
                "commandApiAddress": "http://meitarimds:2210/api/commands",
                "mockUpApiAddress": "http://meitarimds:5002/api/MockupData/byName?name=",
                "pkudatItemByIdAddress": "http://meitarimds:5002/api/BankPkudot/pkudaById?id="
            }
        },
        "Junctions": {
            "url": "",
            "path": "Junctions",
            "status": 1,
            "configuration": {}
        }
    },
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
                "Id": 14,
                "ToolName": "Geofiles",
                "ToolTip": "GEOFILES",
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
   "channels": [{
    "name": "MTCS.Units PubSub Channel",
    "type": "PubSub",
    "Channel": "MTCS.Units",
    "reduxTarget": "units",
    "reduxFunction": "UPDATE_FEATURE_ATTRIBUTES",
    "description": "change is MTCS.Units attribute(s)"
  },
  {
    "name": "MATIS.BTLinks PubSub Channel",
    "type": "PubSub",
    "Channel": "MATIS.BTLinks",
    "reduxTarget": "matisLinks",
    "reduxFunction": "UPDATE_FEATURE_ATTRIBUTES",    
    "messageItemIdFieldName" : "id",  
    "description": "change is MATIS.BTLinks attribute(s)"
  },
  {
    "name": "MATIS.BTUnits PubSub Channel",
    "type": "PubSub",
    "Channel": "MATIS.BTUnits",
    "reduxTarget": "matisUnits",
    "reduxFunction": "UPDATE_FEATURE_ATTRIBUTES",  
    "messageItemIdFieldName" : "id",        
    "description": "change is MATIS.BTUnits attribute(s)"
  }],
    "API" : {
        "geoserver": "http://meitarimdb:8080/geoserver/",
        "auth" : "http://meitarimdb:8040/auth/login",
        "geofiles" : "http://meitarimdb:8050/files",
        "users-layers" : "http://meitarimdb:8060/layers",
        "metaData" : "http://meitarimdb:5001/MetaData/getMetaData/"
    },
    "Auth": {
        "headerName": "token",
        "headerType": "bearer",
        "headerRequestId" : "x-Request-id"
    },
    "mantiLayerUrl": "http://meitarimdb:8080/geoserver/Jeru/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=Jeru%3Amanti_intersections&maxFeatures=500&outputFormat=application%2Fjson",
}