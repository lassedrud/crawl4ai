from .web_crawler import WebCrawler
from .async_webcrawler import AsyncWebCrawler
from .models import CrawlResult

__version__ = "0.2.77"

__all__ = [
    "WebCrawler",
    "AsyncWebCrawler",
    "CrawlResult",
]
