# VoiceCloning

## Original Repository
This project is based on [Coqui-AI TTS](https://github.com/idiap/coqui-ai-TTS)

## Local Setup
1. Create a Python virtual environment:
```bash
uv venv --python 3.9.1
```

2. Install requirements:
```bash
uv pip install -r requirements.txt
```

3. After installation, you can use the TTS commands as described in the original repository.

## Data Preparation
Use `process_dataset.py` for preparing your data. The script expects a `videos` folder with the following structure:
```
videos/
    01.mp4
    01.srt
    02.mp4
    02.srt
    ...etc
```

## Training
Follow the training process as demonstrated in [this tutorial video](https://www.youtube.com/watch?v=8ACPGw-Z_U8)

## Inference
After training, you can use your model through the `inference.py` script.

---

<div dir="rtl">

# استنساخ الصوت

## المستودع الأصلي
هذا المشروع مبني على [Coqui-AI TTS](https://github.com/idiap/coqui-ai-TTS)

## الإعداد المحلي
1. إنشاء بيئة Python افتراضية:
```bash
uv venv --python 3.9.1
```

2. تثبيت المتطلبات:
```bash
uv pip install -r requirements.txt
```

3. بعد التثبيت، يمكنك استخدام أوامر TTS كما هو موضح في المستودع الأصلي.

## تحضير البيانات
استخدم `process_dataset.py` لتحضير البيانات. يتوقع السكريبت مجلد `videos` بالهيكل التالي:
```
videos/
    01.mp4
    01.srt
    02.mp4
    02.srt
    ...إلخ
```

## التدريب
اتبع عملية التدريب كما هو موضح في [فيديو الشرح هذا](https://www.youtube.com/watch?v=8ACPGw-Z_U8)

## الاستنتاج
بعد التدريب، يمكنك استخدام النموذج الخاص بك من خلال سكريبت `inference.py`.

</div>