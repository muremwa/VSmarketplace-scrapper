""""
Get details of an VS or VSCODE extension from marketplace
details are [title, publisher_name, installs, default_image]
All you need is the extension id
"""
from typing import Dict, Any

from .scrap import retrieve_extension_page, m_address, extract_details


def main(extension_id: str) -> Dict[str, Any]:
    """Connect scrap"""
    # retrieve page
    page_text = retrieve_extension_page(
        m_address(extension_id)
    )

    # extract details
    return extract_details(page_text) if page_text else {}
