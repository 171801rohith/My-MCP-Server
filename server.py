from mcp.server.fastmcp import FastMCP
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware import Middleware


from Tools.notesTool import get_my_notes, add_note


mcp = FastMCP("My-MCP-Server")

mcp.add_tool(fn=get_my_notes, name="get_notes", description="Get all notes for a User.")
mcp.add_tool(fn=add_note, name="add_note", description="Add a note for a User.")


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
