import pickle

import numpy as np
from flask import Flask, request, jsonify


model = pickle.load(open('model.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello word"


@app.route('/predict', methods=['POST'])
def predict():
    Src_bytes=request.form.get('Src_bytes')
    Dst_bytes = request.form.get('Dst_bytes')
    #Hot = request.form.get('Hot')
    #Count = request.form.get('Count')
    srv_count = request.form.get('srv_count')
    diff_srv_rate = request.form.get('diff_srv_rate')
    same_srv_rate = request.form.get('same_srv_rate')
    #dst_host_srv_count = request.form.get('dst_host_srv_count')
    #dst_host_same_srv_rate = request.form.get('dst_host_same_srv_rate')
   # dst_host_diff_srv_rate = request.form.get('dst_host_diff_srv_rate')
    dst_host_diff_srv_rate = request.form.get('dst_host_diff_srv_rate')
    dst_host_srv_diff_host_rate = request.form.get('dst_host_srv_diff_host_rate')
    dst_host_same_src_port_rate = request.form.get('dst_host_same_src_port_rate')
    dst_host_serror_rate = request.form.get('dst_host_serror_rate')
    dst_host_srv_serror_rate = request.form.get('dst_host_srv_serror_rate')
    protocol_type = request.form.get('protocol_type')
    Service = request.form.get('Service')
    Flag = request.form.get('Flag')
    DifficultyLevel = request.form.get('DifficultyLevel')

    input_query = np.array([[Service,Flag,DifficultyLevel,protocol_type,Src_bytes,Dst_bytes,srv_count,diff_srv_rate,same_srv_rate,dst_host_diff_srv_rate
                                ,dst_host_srv_diff_host_rate,dst_host_same_src_port_rate,dst_host_serror_rate,dst_host_srv_serror_rate]])
    result = model.predict(input_query)[0]



    return jsonify({'xAttack':str(result)})

if __name__=='__main__':
    app.run(debug=True)



