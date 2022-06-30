from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/findCustomer/<string:nome>/<string:cpf>/<string:cartao>", methods=['GET'])
def findCustomer(nome, cpf, cartao):
    nomeCompleto = "Cristiano Hoshikawa";
    plano = "Plano Super";
    return jsonify({'nomeCompleto': nomeCompleto, 'plano': plano});

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
