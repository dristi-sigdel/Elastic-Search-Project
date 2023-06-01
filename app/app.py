from flask import render_template
from elasticsearch import Elasticsearch
from flask import Flask, request, jsonify

app = Flask(__name__)


es = Elasticsearch('http://localhost:9200')
print(es.ping())


@app.route("/")
def home():
    return render_template('index.html')

@app.route('/search/', methods=['GET', 'POST'])
def elastic_search():
    queries = request.args.get('queries',None)
    query = {
        "multi_match": {
        "query": queries,
        "fields": ["name"]
    }
  }
    
    search_results = es.search(query=query, index="one_piece")
    # print(search_results)

    # print(search_results['hits']['hits'])
   
    return jsonify({"data":search_results['hits']['hits']})

    # return jsonify({"data":search_results['hits']['hits'][0]['_source']})

app.run(debug=True)