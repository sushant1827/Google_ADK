from datetime import datetime

import yfinance as yf
from google.adk.agents import Agent


def get_stock_price(ticker: str) -> dict:
    """
    Get the current stock price for a given ticker symbol.
    """
    print(f"----- Tool: get_stock_price called with ticker: {ticker} -----")

    try:
        # Fetch the stock data
        stock_data = yf.Ticker(ticker)
        current_price = stock_data.info.get("currentPrice")

        if current_price is None:
            return {
                "status": "error", 
                "message": f"Could not retrieve price for {ticker}"
                }
        
        # Get the current date and time
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        return {
            "status": "success",
            "ticker": ticker,
            "price": current_price,
            "timestamp": current_time,
        }
    
    except Exception as e:
        return {
            "status": "error",
            "error_message": f"Error fetching stock data: {str(e)}",
        }
    

# Create the stock analyst agent
stock_analyst = Agent(
    name="stock_analyst",
    model="gemini-2.0-flash",
    description="A stock analyst agent that provides stock price information.",
    instruction="""
    You are a stock analyst agent that provides stock price information.
    
    When asked about a specific stock:
    1. Use the get_stock_price tool to fetch the current price of the requested stock
    2. Format the response to include both the price and the date/time of the request
    3. If the stock is not found, inform the user and suggest they check the ticker symbol
    
    Example response format:
    "The current price of <TICKER> is <PRICE> as of <DATE/TIME>"
    
    If the user asks about anything else during the conversation that is not related to stock prices,
    please inform them that you are a stock analyst agent and cannot assist with that. Instead, 
    suggest they ask about stock prices or market trends.
    """,
    tools=[get_stock_price],
)
