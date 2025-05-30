import pandas as pd

def schedule_classes(df):
    # فرض بر این است که ستون‌های df شامل: درس، استاد، زمان شروع، زمان پایان، کلاس هستند
    df['وضعیت'] = 'برنامه‌ریزی شد'
    return df, []
