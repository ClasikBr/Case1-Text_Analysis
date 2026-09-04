from domain.interfaces import Language_Detector, Sentiment_Analyzer, Syllable_Counter
from domain.types import Language


def getSyllableCounter(lang: Language) -> Syllable_Counter:
  # Возвращает заглушку для подсчёта слогов.
  def _stub(word: str) -> int:
    return max(1, len(word) // 3)

  return _stub


def getSentimentAnalyzer() -> Sentiment_Analyzer:
  # Возвращает заглушку для анализа тональности.
  def _analyze(text: str):
    from domain.types import Polarity
    return Polarity.NEUTRAL, 0.0

  return _analyze


def getLanguageDetector() -> Language_Detector:
  # Возвращает заглушку для детектора языка.
  def _detect(text: str):
    return Language.EN

  return _detect
