from flask import Flask, jsonify
import redis
import os

app = Flask(__name__)

# Configuración de Redis
REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
REDIS_DB = int(os.getenv("REDIS_DB", 0))

db = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB, decode_responses=True)

@app.route('/')
def get_all_keys():
    keys = db.keys("*")
    data = {key: db.get(key) for key in keys}
    return jsonify(data)

@app.route('/set/<key>/<value>', methods=['POST'])
def set_value(key, value):
    db.set(key, value)
    return jsonify({"message": "Value set successfully"}), 201

@app.route('/get/<key>', methods=['GET'])
def get_value(key):
    value = db.get(key)
    if value:
        return jsonify({"key": key, "value": value})
    return jsonify({"message": "Key not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)