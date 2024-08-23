from flask import Flask, request, jsonify
from langchain_community.llms import Ollama
from langchain_community.embeddings import OllamaEmbeddings
from transformers import BertTokenizer, BertModel
import torch

app = Flask(__name__)

cached_model = Ollama(model="llama3")


# end point for generating text using ollama
@app.route("/query_model", methods=["POST"])
def generate_text():
    print("POST method invoked")
    json_content = request.json
    user_query = json_content.get("query")
    print(f"query: {user_query}")

    response = cached_model.invoke(user_query)
    print(response)

    response_answer = {"answer": response}
    return response_answer


# end point for generating embedding using ollama or ollama available embedding models
@app.route("/ollama_embedding", methods=["POST"])
def generate_ollama_embedding():
    print("POST method invoked")
    json_content = request.json
    user_query = json_content.get("query")
    print(f"query: {user_query}")

    embed = OllamaEmbeddings(model="llama3")
    embedding = embed.embed_query(user_query)
    response_answer = {"answer": embedding}
    return response_answer


# end point for generating embedding using general embedding models using transformer for torch
@app.route("/general_embedding", methods=["POST"])
def general_embedding():
    # Load pre-trained model and tokenizer
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    model = BertModel.from_pretrained('bert-base-uncased')

    print("POST method invoked")
    json_content = request.json
    user_query = json_content.get("query")
    print(f"query: {user_query}")

    inputs = tokenizer(user_query, return_tensors='pt', truncation=True, padding=True)
    # Generate embeddings
    with torch.no_grad():
        outputs = model(**inputs)
        embeddings = outputs.last_hidden_state.mean(dim=1).squeeze().tolist()
        response_answer = {"answer": embeddings}
        return response_answer


# general error message
@app.errorhandler(500)
def handle_500(error):
    return jsonify({'error': 'Internal server error'}), 500


# start the app
def start_the_app():
    app.run(port=5000, debug=True)


if __name__ == "__main__":
    start_the_app()
