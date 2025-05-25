"""
CPU Information Tool

This module provides a tool for gathering CPU information.
"""

import time
from typing import Any, Dict

import psutil

def get_cpu_info() -> Dict[str, Any]:
    """
    Gather CPU information including usage, frequency, and core count.

    Returns:
        Dict[str, Any]: A dictionary containing CPU information.
    """
    try:
        # Get CPU information

        cpu_info = {
            "physical_cores": psutil.cpu_count(logical=False),
            "logical_cores": psutil.cpu_count(logical=True),
            "cpu_usage_per_core": [
                f"Core {i}: {percentage:.2f}%"
                for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1))
            ],
            "any_cpu_usage": f"{psutil.cpu_percent(interval=1):.2f}%"
        }

        # Calculate some stats for the result summary

        avg_usage = float(cpu_info["any_cpu_usage"].strip('%'))
        high_usage = avg_usage > 80

        # Format for the ADK tool return structure

        return {
            "result": cpu_info,
            "stats": {
                "physical_cores": cpu_info["physical_cores"],
                "logical_cores": cpu_info["logical_cores"],
                "avg_usage_percentrage": avg_usage,
                "high_usage_alert": high_usage,
            },
            "additional_info": {
                "data_fomat": "dictionary",
                "collection_timestamp": time.time(),
                "perfomamce_concerns": (
                    "High CPU usage detected" if high_usage else "No performance concerns"
                ),
            }
        }
    except Exception as e:
        return {
            "result": {"error": f"Failed to gather CPU information: {str(e)}"},
            "stats": {"success": False},
            "additional_info": {"error_type": str(type(e).__name__)},
        }