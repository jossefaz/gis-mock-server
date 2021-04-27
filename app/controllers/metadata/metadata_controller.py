


def layerListRelations() :
    return [{"subjectid": 1, "semanticid": 10}, {"subjectid": 2, "semanticid": 10}, {"subjectid": 3, "semanticid": 10}, {"subjectid": 3, "semanticid": 0}, {"subjectid": 1, "semanticid": 1}, {"subjectid": 1, "semanticid": 2}, {"subjectid": 2, "semanticid": 2}]

def subjects():
    return [{"subjectid": 1, "description": "תחבורה", "subjectorder": 10}, {"subjectid": 2, "description": "מבנים ואוכלוסיה", "subjectorder": 20}, {"subjectid": 3, "description": "תבע וייעודי קרקע", "subjectorder": 30}, {"subjectid": 5, "description": "מנת\"י", "subjectorder": 40}]

def layers():
    return [
{
"title": "צמתים",
"restid": "manti_intersections",
"groupid": None,
"layerid": 1,
"storeid": None,
"viewcode": "\\N",
"layertype": "OL_ImageLayer",
"workspace": "Jeru",
"orderlayer": None,
"selectable": None,
"semanticid": 2,
"sourcename": "manti_intersections",
"updatecode": "\\N",
"restaddress": "http://localhost:8080/geoserver/Jeru/wms?&LAYERS=Jeru%3Amanti_intersections",
"downloadcode": "\\N",
"hookedevents": "\\N",
"symbologyurl": None,
"symbologyname": None,
"symbologyfield": None,
"geojoinfieldname": None,
"displayexpression": "taba",
"updateattributecode": "\\N",
"symbologycalculation": None,
"channelregistrationname": None
},
{
"title": "יעודי קרקע",
"restid": "dimigcompile",
"groupid": None,
"layerid": 10,
"storeid": None,
"viewcode": "\\N",
"layertype": "OL_ImageLayer",
"workspace": "Jeru",
"orderlayer": None,
"selectable": True,
"semanticid": 1,
"sourcename": "\\N",
"updatecode": "\\N",
"restaddress": "http://localhost:8080/geoserver/Jeru/wms?&LAYERS=Jeru%3Adimigcompile",
"downloadcode": "\\N",
"hookedevents": "\\N",
"symbologyurl": None,
"symbologyname": None,
"symbologyfield": None,
"geojoinfieldname": None,
"displayexpression": "mispartzomet",
"updateattributecode": "\\N",
"symbologycalculation": None,
"channelregistrationname": None
},
{
"title": "לינקים MATIS",
"restid": "matisLinks",
"groupid": None,
"layerid": 12,
"storeid": None,
"viewcode": None,
"layertype": "OL_StreamingLayer",
"workspace": "Jeru",
"orderlayer": None,
"selectable": True,
"semanticid": 4,
"sourcename": "matis_links",
"updatecode": None,
"restaddress": "http://localhost:8080/geoserver/Jeru/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=Jeru%3Amatis_links&maxFeatures=50000&outputFormat=application%2Fjson",
"downloadcode": None,
"hookedevents": None,
"symbologyurl": "http://localhost:8080/geoserver/rest/styles/matisLinks.sld",
"symbologyname": "matis_links",
"symbologyfield": "symbol_calculation_result",
"geojoinfieldname": "meitarimId",
"displayexpression": None,
"updateattributecode": None,
"symbologycalculation": "(f['length_m']/1000)/(sourceItem['AVG_TRAV']/3600)",
"channelregistrationname": "MATIS.BTLinks"
},
{
"title": "יחידות MATIS",
"restid": "matisUnits",
"groupid": None,
"layerid": 11,
"storeid": None,
"viewcode": None,
"layertype": "OL_StreamingLayer",
"workspace": "Jeru",
"orderlayer": None,
"selectable": True,
"semanticid": 3,
"sourcename": "matis_units",
"updatecode": None,
"restaddress": "http://localhost:8080/geoserver/Jeru/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=Jeru%3Amatis_units&maxFeatures=50000&outputFormat=application%2Fjson",
"downloadcode": None,
"hookedevents": None,
"symbologyurl": "http://localhost:8080/geoserver/rest/styles/matis_units.sld",
"symbologyname": "matis_units",
"symbologyfield": "symbol_calculation_result",
"geojoinfieldname": "meitarimId",
"displayexpression": None,
"updateattributecode": None,
"symbologycalculation": "sourceItem['cs_state']",
"channelregistrationname": "MATIS.BTUnits"
}
]

registry = {
    "layerListRelations" : layerListRelations,
    "subjects" : subjects,
    "layers" : layers
}