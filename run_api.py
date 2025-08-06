#!/usr/bin/env python3
"""
Script to run the User Management API server
"""

import uvicorn
from my_app.api import app

if __name__ == "__main__":
    print("Starting User Management API...")
    print("API will be available at: http://localhost:8000")
    print("Interactive API docs at: http://localhost:8000/docs")
    print("OpenAPI schema at: http://localhost:8000/openapi.json")
    print("\nPress Ctrl+C to stop the server")
    
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        reload=True,  # Auto-reload on code changes
        log_level="info"
    )