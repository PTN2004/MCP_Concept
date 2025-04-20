import requests
import os
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

# ===== Cấu hình môi trường =====#
load_dotenv()

#===== Khởi tạo MCP Server =====#
mcp_server = FastMCP("TinHocVietNam") # Khởi tạo MCP Server với tên "TinHocVietNam"

#===== Cấu hình GitHub =====#
GITHUB_TOKEN = os.getenv("GITHUB_TOKENS")
GITHUB_API_URL = "https://api.github.com"

print(GITHUB_TOKEN)

headers = {
    "Accept": "application/vnd.github.v3+json",
    "Authorization" : f"token {GITHUB_TOKEN}"
}

#===== Định nghĩa các tool =====#
@mcp_server.tool()
def get_list_repo():
    """List user Repositories"""
    respone = requests.get(f"{GITHUB_API_URL}/user/repos", headers=headers)
    
    return respone.json()

@mcp_server.tool()
def create_repo(repo_name: str, des: str, private: bool):
    """Create a new repository """
    data = {
        'name': repo_name,
        'description': des,
        'private': private
    }    

    respone = requests.post(f"{GITHUB_API_URL}/user/repos", headers=headers, json=data)
    return respone.json()

if __name__ == "__main__":
    mcp_server.run(transport='sse')