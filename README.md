# **README File for Embedding endpoints**

## **Introduction**
Embedding points is a project that provides a simple endpoints for 

1. Chatting with ollama model
2. Embedding with ollama embedding model
3. Embedding with embedding models from torch transformer 

This code was tested in Windows 10



## **Installation**

To install Embedding endpoints, follow these steps:

1. Clone the repository 
2. Install dependencies: **pip install -r requirements.txt**
3. Install Ollama from here **https://ollama.com/download**
4. Install Postman from here **https://www.postman.com/downloads/**

## **Before executing the code**

1. After the installation of Ollama, start the ollama by executing **ollama serve** in the command prompt
2. Check if ollama is running in your browser by visiting **http://localhost:11434**
3. From the command prompt, pull the ollama model for text generation and embedding with **ollama pull your_modelname**

## **Testing the text generation end point**
To run/test the code, follow these steps:

1. In Postman,  select POST method and type **http://localhost:5000/query_model**
2. Next, select Body and select JSON type as the input for the endpoint and provide the following json 

```
{
    "query": "Tell me a joke"
}
```

## **Testing the text embedding end point**
To run/test the code, follow these steps:

1. In Postman,  select POST method and type **http://localhost:5000/ollama_embedding**
2. Next, select Body and select JSON type as the input for the endpoint and provide the following json 

```
{
    "query": "embedd this text"
}
```

## **Testing the text embedding end point with hugging face transformer**
To run/test the code, follow these steps:

1. In Postman,  select POST method and type **http://localhost:5000/general_embedding**
2. Next, select Body and select JSON type as the input for the endpoint and provide the following json 

```
{
    "query": "embedd this text"
}
```



## **Changelog**

- **1.0.0:** Initial release"# endpoints_openml" 
