import httpx


def test_analyze_smoke():
  resp = httpx.post('http://127.0.0.1:8000/analyze', json={'text': 'Hello world'})
  assert resp.status_code == 200
  data = resp.json()
  assert 'text' in data
