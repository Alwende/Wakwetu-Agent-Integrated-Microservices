from flask import Flask, jsonify
import os

app = Flask(__name__)

# Root Route - Friendly response for manual testing
@app.route('/', methods=['GET'])
def index():
    return jsonify({
        "service": "Wakwetu Banking API",
        "status": "Online",
        "version": "1.0.0"
    })

# Health Check - The "Heartbeat" for the Load Balancer and Bedrock
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({
        "status": "healthy",
        "cluster": "Wakwetu-AIME-Cluster",
        "node_type": "Fargate/AutoMode"
    })

# Business Logic - What the Agent actually queries
@app.route('/balance', methods=['GET'])
def get_balance():
    return jsonify({
        "account_id": "WAK-789", 
        "balance": 5250.75, 
        "currency": "USD",
        "status": "Live from EKS"
    })

if __name__ == '__main__':
    # Running on 0.0.0.0 to accept traffic from the VPC
    app.run(host='0.0.0.0', port=5000)