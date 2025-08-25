#!/usr/bin/env python3
"""
Tests for the textbook reader functionality.
"""

import pytest
from unittest.mock import Mock, patch
from src.ed_bot.textbook_reader import query_textbook


class TestTextbookReader:
    """Test cases for textbook reader functionality."""
    
    @patch('src.ed_bot.textbook_reader.OpenAI')
    def test_query_textbook_success(self, mock_openai):
        """Test successful textbook query."""
        mock_client = Mock()
        mock_response = Mock()
        mock_openai.return_value = mock_client
        mock_client.responses.create.return_value = mock_response
        
        question = "What is photosynthesis?"
        
        result = query_textbook(question)
        
        mock_client.responses.create.assert_called_once_with(
            prompt={
                "id": "pmpt_68abdcf7825481969b25a0b18e78206d072e6c98afd3ce07",
                "version": "1",
                "variables": {
                    "question": question
                }
            }
        )
        
        assert result == mock_response
    
    @patch('src.ed_bot.textbook_reader.OpenAI')
    def test_query_textbook_with_empty_question(self, mock_openai):
        """Test textbook query with empty question."""
        mock_client = Mock()
        mock_response = Mock()
        mock_openai.return_value = mock_client
        mock_client.responses.create.return_value = mock_response
        
        result = query_textbook("")
        
        mock_client.responses.create.assert_called_once_with(
            prompt={
                "id": "pmpt_68abdcf7825481969b25a0b18e78206d072e6c98afd3ce07",
                "version": "1",
                "variables": {
                    "question": ""
                }
            }
        )
        
        assert result == mock_response