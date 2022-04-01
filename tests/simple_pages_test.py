"""This test the homepage"""

def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'<a class="nav-link" href="/about">About Me</a>' in response.data
    assert b'<a class="nav-link" href="/page1">Git</a>' in response.data
    assert b'<a class="nav-link" href="/page2">Docker</a>' in response.data
    assert b'<a class="nav-link" href="/page3">Python/Flask</a>' in response.data
    assert b'<a class="nav-link" href="/page4">CI/CD</a>' in response.data
    assert b'<a class="nav-link" href="/page5">Article1</a>' in response.data
    assert b'<a class="nav-link" href="/page6">Article2</a>' in response.data
    assert b'<a class="nav-link" href="/page7">Article3</a>' in response.data
    assert b'<a class="nav-link" href="/page8">Article4</a>' in response.data

def test_request_index(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Profile" in response.data

def test_request_about(client):
    """This makes the index page"""
    response = client.get("/about")
    assert response.status_code == 200
    assert b"Projects" in response.data

def test_request_page1(client):
    """This makes the index page"""
    response = client.get("/page1")
    assert response.status_code == 200
    assert b"Branches" in response.data

def test_request_page2(client):
    """This makes the index page"""
    response = client.get("/page2")
    assert response.status_code == 200
    assert b"Container" in response.data

def test_request_page3(client):
    """This makes the index page"""
    response = client.get("/page3")
    assert response.status_code == 200
    assert b"Root File" in response.data

def test_request_page4(client):
    """This makes the index page"""
    response = client.get("/page4")
    assert response.status_code == 200
    assert b"Project Setup" in response.data

def test_request_page5(client):
    """This makes the index page"""
    response = client.get("/page5")
    assert response.status_code == 200
    assert b"Pylint" in response.data

def test_request_page6(client):
    """This makes the index page"""
    response = client.get("/page6")
    assert response.status_code == 200
    assert b"AAA testing" in response.data

def test_request_page7(client):
    """This makes the index page"""
    response = client.get("/page7")
    assert response.status_code == 200
    assert b"OOPs" in response.data

def test_request_page8(client):
    """This makes the index page"""
    response = client.get("/page8")
    assert response.status_code == 200
    assert b"SOLID" in response.data

