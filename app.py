from moto import mock_s3
import streamlit as st
import boto3
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def setup_mock_s3():
    s3 = boto3.resource("s3", region_name="us-east-1")
    bucket_name = "mock-learning-paths"
    s3.create_bucket(Bucket=bucket_name)
    data = {
        "resources": [
            {"title": "Introduction to AWS", "tags": "AWS, Cloud Computing, Basics"},
            {"title": "Deep Learning on AWS", "tags": "AWS, Deep Learning, AI"},
            {"title": "NLP with SageMaker", "tags": "AWS, NLP, Machine Learning"},
            {"title": "Serverless with AWS Lambda", "tags": "AWS, Serverless, Lambda"},
        ]
    }
    s3.Bucket(bucket_name).put_object(Key="mock_resources.json", Body=json.dumps(data))
    return bucket_name

def recommend_learning_path(user_input, bucket_name):
    s3 = boto3.client("s3", region_name="us-east-1")
    obj = s3.get_object(Bucket=bucket_name, Key="mock_resources.json")
    data = json.loads(obj['Body'].read().decode('utf-8'))
    
    resources = data["resources"]
    titles = [resource["title"] for resource in resources]
    tags = [resource["tags"] for resource in resources]
    
    corpus = tags + [user_input]
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)
    similarity = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])
    
    scores = similarity.flatten()
    ranked_indices = scores.argsort()[::-1]
    
    recommendations = [titles[i] for i in ranked_indices[:3]]
    return recommendations

st.title("AWS Learning Path Recommender")

user_input = st.text_input("What do you want to learn about AWS?", "I want to learn about AWS and AI")

if st.button("Get Recommendations"):
    with mock_s3():
        bucket_name = setup_mock_s3()
        recommendations = recommend_learning_path(user_input, bucket_name)
    
    st.subheader("Recommended Learning Path:")
    for i, rec in enumerate(recommendations, 1):
        st.write(f"{i}. {rec}")
