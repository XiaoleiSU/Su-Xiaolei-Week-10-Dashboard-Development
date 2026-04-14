import random


def process(prompt: str, temperature: float) -> str:
    normalized_prompt = prompt.lower()

    response_groups = {
        "greeting": [
            "Hello! It is great to hear from you.",
            "Hi there! How can I support you today?",
            "Hey! I am ready to help with your request.",
        ],
        "help": [
            "I can help you with general questions, planning, and simple ideas.",
            "Sure, I can assist with guidance, explanations, and task suggestions.",
            "Of course. Tell me what you need help with, and I will do my best.",
        ],
        "weather": [
            "I cannot check live weather, but it may be a good idea to look at a local forecast.",
            "I do not have real-time weather data, but you can check a weather app for the latest update.",
            "For accurate weather information, please use a live forecast service in your area.",
        ],
        "default": [
            "I understand your message. Could you share a bit more detail?",
            "Thanks for your prompt. Please give me more context so I can respond better.",
            "I received your request. A little more information would help me answer clearly.",
        ],
    }

    if any(keyword in normalized_prompt for keyword in ["hello", "hi", "hey", "greetings"]):
        responses = response_groups["greeting"]
    elif any(keyword in normalized_prompt for keyword in ["help", "assist", "support"]):
        responses = response_groups["help"]
    elif any(keyword in normalized_prompt for keyword in ["weather", "rain", "sunny", "forecast"]):
        responses = response_groups["weather"]
    else:
        responses = response_groups["default"]

    if temperature <= 0.3:
        selected_response = responses[0]
    else:
        selected_response = random.choice(responses)

    return selected_response
