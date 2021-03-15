


def layerListRelations() :
    return [{"subjectid": 1, "semanticid": 10}, {"subjectid": 2, "semanticid": 10}, {"subjectid": 3, "semanticid": 10}, {"subjectid": 3, "semanticid": 0}, {"subjectid": 1, "semanticid": 1}, {"subjectid": 1, "semanticid": 2}, {"subjectid": 2, "semanticid": 2}]

def subjects():
    return [{"subjectid": 1, "description": "תחבורה", "subjectorder": 10}, {"subjectid": 2, "description": "מבנים ואוכלוסיה", "subjectorder": 20}, {"subjectid": 3, "description": "תבע וייעודי קרקע", "subjectorder": 30}, {"subjectid": 5, "description": "מנת\"י", "subjectorder": 40}]

def layers():
    return [{"title": "צמתים", "restid": "manti_intersections", "groupid": None, "layerid": 0, "storeid": None, "viewcode": "\\N", "workspace": "Jeru", "orderlayer": None, "selectable": True, "semanticid": 2, "sourcename": "\\N", "updatecode": "\\N", "restaddress": "http://localhost:8080/geoserver/Jeru/wms?&LAYERS=Jeru%3Amanti_intersections", "downloadcode": "\\N", "hookedevents": "\\N", "displayexpression": "taba", "updateattributecode": "\\N"}, {"title": "יעודי קרקע", "restid": "dimigcompile", "groupid": None, "layerid": 10, "storeid": None, "viewcode": "\\N", "workspace": "Jeru", "orderlayer": None, "selectable": True, "semanticid": 1, "sourcename": "\\N", "updatecode": "\\N", "restaddress": "http://localhost:8080/geoserver/Jeru/wms?&LAYERS=Jeru%3Adimigcompile", "downloadcode": "\\N", "hookedevents": "\\N", "displayexpression": "mispartzomet", "updateattributecode": "\\N"}]

registry = {
    "layerListRelations" : layerListRelations,
    "subjects" : subjects,
    "layers" : layers
}