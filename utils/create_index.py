import os

from dotenv import load_dotenv
from llama_index import GPTSimpleVectorIndex, QuestionAnswerPrompt, download_loader, SimpleDirectoryReader


load_dotenv()
openai_api_key = os.environ.get('OPENAI_API_KEY')

SimpleWebPageReader = download_loader("SimpleWebPageReader")



loader = SimpleWebPageReader()
documents = SimpleDirectoryReader('../documents/pdfs').load_data()
index = GPTSimpleVectorIndex(documents, chunk_size_limit=1024)
index.save_to_disk('../indexed_articles/django_custom_user_model.json')

# documents = loader.load_data(urls=['https://e-motionagency.com/en/OurExperiences/'])
# documents = loader.load_data(urls=['https://testdriven.io/blog/django-custom-user-model/'])
# index = GPTSimpleVectorIndex(documents)

# index.save_to_disk('../indexed_articles/django_custom_user_model.json')