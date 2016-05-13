from flask import Flask, render_template, request, jsonify
app = Flask(__name__)


@app.route('/info.json')
def info():
    # retrieve parameters and get their data from the /info.json endpoint
    lat = request.args.get('lat')
    lng = request.args.get('lng')
    constructed_json = {'lat': lat, 'lng': lng}
    print "This is request.args", request.args
    print "This is constructed_json", constructed_json
    return jsonify(constructed_json)


@app.route('/')
def index():
    """ runs app name mainspace """
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
