# 🦙 Local Llama Demo

Інтерактивне демо для використання локальної LLM моделі через Ollama.

## Структура

```
local-llama-demo/
├── index.html         # Веб-інтерфейс
├── app.py             # Flask сервер (проксі для Ollama)
├── requirements.txt   # Залежності
├── PERFORMANCE.md     # Звіт продуктивності
└── README.md          # Документація
```

## Підготовка

### 1. Встановити Ollama

Завантажити з https://ollama.com/ та встановити для вашої OS.

### 2. Завантажити модель

```bash
ollama pull llama3
```

### 3. Переконатись що Ollama запущена

```bash
ollama serve
# Сервер буде на localhost:11434
```

## Запуск

```bash
pip install -r requirements.txt
python app.py
```

Відкрити браузер: http://localhost:8000

## Як це працює

```
Браузер → Flask (localhost:8000) → Ollama (localhost:11434)
```

Flask перехоплює запити з браузера і перенаправляє їх до Ollama, обходячи CORS обмеження.

## API Endpoints

| Метод | Endpoint | Опис |
|-------|----------|------|
| GET | `/` | Веб-інтерфейс |
| GET | `/api/tags` | Список доступних моделей |
| POST | `/api/generate` | Генерація відповіді |

### Приклади

```bash
# Список моделей
curl http://localhost:8000/api/tags

# Генерація
curl -X POST http://localhost:8000/api/generate \
  -H "Content-Type: application/json" \
  -d '{"model": "llama3", "prompt": "Hello", "stream": false}'
```

## Вимоги

- Python 3.10+
- Ollama встановлена та запущена
- Мінімум 8 GB RAM для 7B моделей
