#!/usr/bin/env python3
"""
Tests for the citation checking functionality.
"""

import pytest
from unittest.mock import Mock, patch
from src.ed_bot.citation_checker import check_citation


class TestCitationChecker:
    """Test cases for citation checking functionality."""
    
    @patch('src.ed_bot.citation_checker.OpenAI')
    def test_check_citation_success(self, mock_openai):
        """Test successful citation checking."""
        mock_client = Mock()
        mock_response = Mock()
        mock_openai.return_value = mock_client
        mock_client.responses.create.return_value = mock_response
        
        claim = "The earth is round"
        passage = "Scientific observations confirm that the earth has a spherical shape"
        
        result = check_citation(claim, passage)
        
        mock_client.responses.create.assert_called_once_with(
            prompt={
                "id": "pmpt_68abd887d87481959c71b8ea26fb6cc608c1dd109b0c3f97",
                "version": "1",
                "variables": {
                    "claim": claim,
                    "passage": passage
                }
            }
        )
        
        assert result == mock_response
    
    @patch('src.ed_bot.citation_checker.OpenAI')
    def test_check_citation_with_empty_strings(self, mock_openai):
        """Test citation checking with empty strings."""
        mock_client = Mock()
        mock_response = Mock()
        mock_openai.return_value = mock_client
        mock_client.responses.create.return_value = mock_response
        
        result = check_citation("", "")
        
        mock_client.responses.create.assert_called_once_with(
            prompt={
                "id": "pmpt_68abd887d87481959c71b8ea26fb6cc608c1dd109b0c3f97",
                "version": "1",
                "variables": {
                    "claim": "",
                    "passage": ""
                }
            }
        )
        
        assert result == mock_response