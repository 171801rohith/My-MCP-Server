from mcp.server.fastmcp import FastMCP
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware import Middleware


from Tools.notesTool import get_my_notes, add_note
from Tools.filesModification import (
    rename_to_episodes,
    delete_folder,
    move_folder_trash,
    open_app,
    close_app,
)

mcp = FastMCP("My-MCP-Server")

mcp.add_tool(
    fn=get_my_notes, name="get_notes", description="""Get all notes for a User."""
)
mcp.add_tool(fn=add_note, name="add_note", description="""Add a note for a User.""")
mcp.add_tool(
    fn=rename_to_episodes,
    name="rename_file_to_episodes",
    description="""
                    Opens a directory in the system's file explorer using the provided full path.
                    And renames the files (episodes) to certain format.
                    Args:
                    - full_path (str): The absolute path to the directory (e.g., 'C:\\Users\\Rohit\\Documents').
                    Returns:
                    - str: Success or error message based on the outcome.
                """,
)
mcp.add_tool(
    fn=delete_folder,
    name="delete_folder",
    description="""
                    Deletes the folder of specified path.
                    Args:
                    - path (str): The absolute path to the directory (e.g., 'C:\\Users\\Rohit\\Documents').
                    Returns:
                    - str: Success or error message based on the outcome.
                """,
)
mcp.add_tool(
    fn=move_folder_trash,
    name="move_folder_trash",
    description="""
                    Moves the folder of specified path to trash (Recycle Bin).
                    Args:
                    - path (str): The absolute path to the directory (e.g., 'C:\\Users\\Rohit\\Documents').
                    Returns:
                    - str: Success or error message based on the outcome.
                """,
)
mcp.add_tool(
    fn=open_app,
    name="app_opener",
    description="""Opens any app in system. Args: app_name""",
)
mcp.add_tool(
    fn=close_app,
    name="app_closer",
    description="""Closes any app in system that is open. Args: app_name""",
)


if __name__ == "__main__":
    mcp.run(
        transport="http",
        host="127.0.0.1",
        port=8000,
        middleware=[
            Middleware(
                CORSMiddleware,
                allow_origins=["*"],
                allow_credentials=True,
                allow_methods=["*"],
                allow_headers=["*"],
            )
        ],
    )
