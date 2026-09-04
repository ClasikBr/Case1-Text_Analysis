import hashlib
import json
from typing import Optional

try:
  import redis
except Exception:
  redis = None

_CACHE_STORE: dict = {}


def _key_for(text: str) -> str:
  return hashlib.sha256(text.encode("utf-8")).hexdigest()


def get_cached(redis_client, text: str) -> Optional[dict]:
  key = _key_for(text)
  if redis and redis_client:
    try:
      val = redis_client.get(key)
      if val:
        return json.loads(val)
    except Exception:
      return None
  return _CACHE_STORE.get(key)


def set_cached(redis_client, text: str, result: dict, ttl: int = 3600) -> None:
  key = _key_for(text)
  if redis and redis_client:
    try:
      redis_client.setex(key, ttl, json.dumps(result))
      return
    except Exception:
      pass
  _CACHE_STORE[key] = result
