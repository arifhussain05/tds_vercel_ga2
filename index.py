from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app, resources = {r"/*": {"origins": "*"}})

student_marks = [{"name":"O1SIGy","marks":42},{"name":"kT","marks":35},{"name":"HARna14","marks":6},{"name":"s2LodD","marks":4},{"name":"ekKkJys1K","marks":84},{"name":"2q","marks":56},{"name":"5","marks":4},{"name":"MX","marks":40},{"name":"R","marks":93},{"name":"jQL8WK7ir","marks":56},{"name":"HJCOifV81","marks":99},{"name":"Z3ioBM","marks":81},{"name":"Y69FAy5VY","marks":31},{"name":"CV6atTyB","marks":49},{"name":"j9yxFeCKU","marks":84},{"name":"eQGg","marks":27},{"name":"kF2U","marks":11},{"name":"KiZAHQE2N","marks":7},{"name":"3q","marks":59},{"name":"77LVkKcO9","marks":50},{"name":"0bbkj","marks":64},{"name":"FUi6OXn","marks":96},{"name":"KeT","marks":32},{"name":"tXlbn1vk","marks":73},{"name":"jrlI","marks":13},{"name":"erk","marks":5},{"name":"1sno","marks":94},{"name":"5Fe","marks":13},{"name":"th5TSFfqT","marks":97},{"name":"t4kEIJW","marks":84},{"name":"RY9gEFW","marks":89},{"name":"Z","marks":15},{"name":"6PW","marks":89},{"name":"pnz8u","marks":74},{"name":"LmJ","marks":75},{"name":"5aEdOcMe","marks":57},{"name":"lqhcIRBv","marks":34},{"name":"ccF6UD","marks":16},{"name":"R6MLE","marks":46},{"name":"seO3pg8","marks":45},{"name":"uA8D","marks":67},{"name":"l9nQd2R","marks":5},{"name":"uRJ","marks":62},{"name":"KbsYoXF","marks":95},{"name":"nMRl","marks":43},{"name":"cn0T","marks":91},{"name":"u8pEadkd","marks":63},{"name":"19K","marks":49},{"name":"zUashM9TWO","marks":75},{"name":"4J7Fg","marks":20},{"name":"pH6F2JH","marks":66},{"name":"LMMEoS","marks":32},{"name":"2jeDg","marks":80},{"name":"3Yu4mDWl","marks":18},{"name":"FgNOBOamb","marks":36},{"name":"m6UlSVJfdu","marks":53},{"name":"PR7KNf7f9u","marks":33},{"name":"VjrjUORos","marks":79},{"name":"6jO00","marks":1},{"name":"F2EiSd","marks":12},{"name":"MWH4tXVW","marks":31},{"name":"C4Q3Zm9h","marks":62},{"name":"jIaO","marks":98},{"name":"psp8","marks":40},{"name":"YO8St","marks":94},{"name":"Cj9ccq","marks":67},{"name":"qahi","marks":91},{"name":"veKCguXpe","marks":19},{"name":"x4kQiHf0C","marks":10},{"name":"yjgENMyPds","marks":5},{"name":"fhC9","marks":62},{"name":"a56","marks":36},{"name":"4g6j2U","marks":58},{"name":"n7cp","marks":66},{"name":"qNkRUXrx8","marks":12},{"name":"HSz","marks":48},{"name":"0oFBFD","marks":49},{"name":"6JKHNgS","marks":92},{"name":"TrjtzKs5","marks":54},{"name":"3YHMjzB1t5","marks":65},{"name":"T7M","marks":79},{"name":"c","marks":58},{"name":"ITswGXShR","marks":50},{"name":"N","marks":23},{"name":"W2E7kOVOV","marks":10},{"name":"BU7B","marks":48},{"name":"rwucmPrX","marks":44},{"name":"vBPly7S","marks":33},{"name":"uYC","marks":62},{"name":"333NPCgO","marks":87},{"name":"VPzO8N4gdA","marks":57},{"name":"XA","marks":24},{"name":"2SQ6z8","marks":37},{"name":"u7yAFwo","marks":38},{"name":"RnSK1CMc","marks":22},{"name":"ui0uG0","marks":88},{"name":"ZKXU79KEho","marks":72},{"name":"6SERsT0KQ","marks":31},{"name":"RoUPGU","marks":4},{"name":"kwToSAJ","marks":12}]
#student_marks = json.loads(student_marks)
#student_marks = json.dumps(student_marks)

@app.route('/api', methods=['GET'])

def get_marks():
    names = request.args.getlist('name')
    marks = [next((student['marks'] for student in student_marks if student['name'] == name.replace('"','')), None) for name in names]
    return jsonify({'marks':marks})
    
if __name__ == '__main__':
    app.run(debug=True)