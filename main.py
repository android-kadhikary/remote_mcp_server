from fastmcp import FastMCP
import os
import sqlite3
import random
import json

# DB_PATH = os.path.join(os.path.dirname(__file__), "expenses.db")
# CATEGORIES_PATH = os.path.join(os.path.dirname(__file__), "categories.json")

mcp = FastMCP("Simple calulator")

@mcp.tool()
def add_2numbers(num1: int, num2:int) -> int:
    '''Add 2 numbers
    Args : 
    num1 : first number
    num2 : second Number 

    Returns : 
    The sun of num1 and num2
    '''
    return (num1+num2)
    
@mcp.tool()
def add_3numbers(num1: int, num2:int, num3:int) -> int:
    '''Add 2 numbers
    Args : 
    num1 : first number
    num2 : second Number 
    num3 : third Number 

    Returns : 
    The sun of num1 and num2 and num3
    '''
    return (num1+ num2 + num3)

@mcp.resource("info://server")
def server_info() -> str:
    # server info
    info = {
        "name" : "simple clac",
        "tools" : ["add 2 numbers", "add 3 numbers"],
        "desc" : "simple clac description",
        "author" : "Karabi"
    }
    return json.dumps(info, indent=2)

if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port = 8000)
# Explicitly set the path to match what the inspector expects
    # mcp.run(transport="http", host="0.0.0.0", port=8000, path="/mcp/sse")