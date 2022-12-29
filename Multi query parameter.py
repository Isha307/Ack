from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def search():
    query = request.args.to_dict(flat=False)
    query_params = normalize_query(query)
    print(query_params)
    return f'Searching for: {query_params}'
    #return "Hello world"



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=50100, debug=True)
