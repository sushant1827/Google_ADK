from datetime import datetime

def get_current_time() -> dict:
    """
    Get the current date and time in the format YYYY-MM-DD HH:MM:SS.
    """
    print("----- Tool: get_current_time called -----")
    
    # Get the current date and time
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    return {        
        "current_time": current_time,
    }