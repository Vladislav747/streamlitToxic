def is_data_correct(df):
    return {"toxicity", "comment_text"}.issubset(df.columns)

