import requests
import json
import time
import copy
import requests
import random
import copy


class Models:
    def __init__(self):
        pass

    def getModels(self):
        response = requests.get(
            url="https://openrouter.ai/api/v1/models"
        )
        return response.json()
    
    def getFreeModels(self):
        response = self.getModels()
        free_models = []
        for model in response['data']:
            prices = copy.copy(model['pricing'])
            for x in prices:
                prices[x] = float(prices[x])
            if sum(prices.values()) == 0:
                free_models.append(model)
        return free_models
    
    def getRandomModel(self):
        response = self.getModels()
        response = list(response['data'])
        return response[random.randint(0, len(response) - 1)]
    
    def getRandomModelID(self):
        response = self.getModels()
        response = list(response['data'])
        return response[random.randint(0, len(response) - 1)]['id']

    def getRandomFreeModel(self):
        response = self.getFreeModels()
        return response[random.randint(0, len(response) - 1)]
    
    def getRandomFreeModelID(self):
        response = self.getFreeModels()
        return response[random.randint(0, len(response) - 1)]['id']

# TODO: This is just for testing purposes. Remove this when done testing.
if __name__ == "__main__":
    models = Models()
    
    print(models.getRandomModelID())

class llmCaller:

    def __init__(self, api_key: str):
        self.api_key = api_key

    def getResponse(self, 
                    prompt: str, 
                    model: str = "openai/gpt-3.5-turbo",
                    temperature: float = 1.0,
                    top_p: float = 1.0,
                    top_k: int = 0,
                    frequency_penalty: float = 0.0,
                    presence_penalty: float = 0.0,
                    repetition_penalty: float = 1.0,
                    min_p: float = 0.0,
                    top_a: float = 0.0,
                    seed: int = None,
                    max_tokens: int = None):
        
        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {self.api_key}",
                # "HTTP-Referer": f"{YOUR_SITE_URL}", # Optional, for including your app on openrouter.ai rankings.
                # "X-Title": f"{YOUR_APP_NAME}", # Optional. Shows in rankings on openrouter.ai.
            },
            data=json.dumps({
                "model": model,
                "messages": [
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                "temperature": temperature,
                "top_p": top_p,
                "top_k": top_k,
                "frequency_penalty": frequency_penalty,
                "presence_penalty": presence_penalty,
                "repetition_penalty": repetition_penalty,
                "min_p": min_p,
                "top_a": top_a,
                "seed": seed,
                "max_tokens": max_tokens
            })
        )

        id = response.json()['id']

        # TODO: Currently we are just hoping the stats are avaliable in 1 second. We should wait until they are avaliable.
        time.sleep(1)
        stats = requests.request("GET", f"https://openrouter.ai/api/v1/generation?id={id}", headers={
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
            })

        #combine into one json
        response = response.json()
        response['stats'] = stats.json()

        return response