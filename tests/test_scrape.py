from scrape import Grabber
import pytest

def test_grabber_smoke_test():
    grab = Grabber()
    assert grab is not None

# def test_grabber_fetch_page_returns_string():
#     grab = Grabber()
#     assert

def test_url_exists():
    grab = Grabber()
    assert grab.base_url is not None