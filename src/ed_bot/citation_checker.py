#!/usr/bin/env python3
"""
Citation checking functionality for the educational bot.
"""

import os
from openai import OpenAI


def check_citation(claim: str, passage: str) -> dict:
    """
    Check if a claim is supported by a given passage using OpenAI's responses API.
    
    Args:
        claim (str): The claim to verify
        passage (str): The passage to check against
        
    Returns:
        dict: The response from OpenAI containing the citation verification
    """
    client = OpenAI()
    
    response = client.responses.create(
        prompt={
            "id": "pmpt_68abdb6010fc8197b565fc48ea64abe0053aeee519702ceb",
            "version": "2",
            "variables": {
                "claim": claim,
                "passage": passage
            }
        }
    )
    
    return response