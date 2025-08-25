#!/usr/bin/env python3
"""
Textbook reading functionality for the educational bot.
"""

import os
from openai import OpenAI


def query_textbook(question: str) -> dict:
    """
    Query the textbook model with a given question using OpenAI's responses API.
    
    Args:
        question (str): The question to ask the textbook model
        
    Returns:
        dict: The response from OpenAI containing the textbook answer
    """
    client = OpenAI()
    
    response = client.responses.create(
        prompt={
            "id": "pmpt_68abdcf7825481969b25a0b18e78206d072e6c98afd3ce07",
            "version": "3"
        },
        input=question
    )
    
    return response