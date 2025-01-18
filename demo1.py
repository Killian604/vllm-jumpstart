"""

"""
import vllm_util
vllm_host, vllm_port = 'localhost', 8000  # Put your own info here
vllm_host, vllm_port = '10.0.0.73', 8000  # Put your own info here

model = vllm_util.get_models(vllm_host, vllm_port)[0]  # Fetch first model arbitrarily
api_uri = vllm_util.create_vllm_chat_uri(vllm_host, vllm_port)
print(f'{model=}')
print(f'{api_uri=}')

sample_chat = [
    {'role': 'system', 'content': 'You are a helpful AI assistant.'},
    {'role': 'assistant', 'content': 'How can I help you today?'},
    {'role': 'user', 'content': 'Tell me about the various biomes present on Earth.'}
]

content, role = vllm_util.generate_response(sample_chat, model, api_uri, max_tokens=1_000)

print(f'{role}:\n{content}')
