from google import genai

client = genai.Client(api_key = "AIzaSyDNWRFn9t9i7gs9E_coVkPFa4p2hafVx-w")

models = client.models.list()
for m in models:
    print(m)
