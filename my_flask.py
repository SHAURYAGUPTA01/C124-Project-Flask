from flask import Flask,jsonify,request

app = Flask(__name__)

data = [
    {
        'id': 1,
        'name': 'Shaurya',
        'contact': '9876543210', 
        'done': False
    },
    {
        'id': 2,
        'name': 'Sanjay',
        'contact': '1234567890', 
        'done': False
    },
]

@app.route("/addData", methods = ["POST"])

def add_task() :
    
    if not request.json:
        return jsonify({
             "status":"error",
            "message": "no data found"
        },400)
        
    task = {
        "id" : data[-1]['id']+1,
        "name" : request.json["name"],
        "contact" : request.json.get("contact" , ""),
        "done" : False
    }
    
    data.append(task)
    return jsonify({
        "status":"success",
        "message": "task added successfully!"
    })
    
@app.route("/getdata")
def gettask():
    return jsonify({"data":data})

if __name__ == "__main__" :
    app.run(debug = True)