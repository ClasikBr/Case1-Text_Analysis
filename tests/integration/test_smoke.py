import httpx


def test_analyze_smoke():
  resp = httpx.post('http://localhost:8000/analyze', json={'text': 'Hello world'})
  assert resp.status_code == 200
  data = resp.json()
  assert 'language' in data
  assert 'polarity' in data
