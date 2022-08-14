import pickle

def ranker(text, sentence_lim):
    with open('model_pickle.pkl', 'rb') as f:
        nlp = pickle.load(f)
    
    sent_lim = int(sentence_lim)

    doc = nlp(text)
    half = ""

    for x in doc._.textrank.summary(limit_sentences=sent_lim):
        half += str(x) + " "

    second = ""
    result = ""

    l1 = half.split()

    for x in l1:
        second += x + " "
        if x[-1] == "." and x[-2] == x[-2].lower():
            result += second
            second = ""

    context = {
        'result': result,
        'sentence_limit': sent_lim
    }

    return context

