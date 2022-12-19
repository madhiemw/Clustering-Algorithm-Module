    #case folding process

    df['text'] = df['text'].astype(str).str.lower()
    df['text'] = df['text'].str.replace('\d+', '')
    
    #proses tokenizing
    regexp = RegexpTokenizer('\w+')
    df['text_token']=df['text'].apply(regexp.tokenize)
    #filtering dan #ostopwords
    list_stopwords = stopwords.words('indonesian')
    list_stopwords.extend(["yg", "dg", "rt", "dgn", "ny", "d", 'klo', 
                       'kalo', 'amp', 'biar', 'bikin', 'bilang', 
                       'gak', 'ga', 'krn', 'nya', 'nih', 'sih', 
                       'si', 'tau', 'tdk', 'tuh', 'utk', 'ya', 
                       'jd', 'jgn', 'sdh', 'aja', 'n', 't', 
                       'nyg', 'hehe', 'pen', 'u', 'nan', 'loh', 'rt',
                       '&amp', 'yah', 'cing','tuh','wkwkwkw',])
    txt_stopword = pd.read_csv("stopwords.txt", names= ["stopwords"], header = None)
    list_stopwords.extend(txt_stopword["stopwords"][0].split(' '))
    list_stopwords = set(list_stopwords)
    
    def stopwords_removal(words):
        return [word for word in words if word not in list_stopwords]

    df['token steaming'] = df['text_token'].apply(stopwords_removal) 
    print(df.head(3))

    i=0
    final_string_tokens = []
    for text in df['token steaming'].values:
        EachReviewText = ""
        EachReviewText = ' '.join(text)
        final_string_tokens.append(EachReviewText)
    df["final_result"] = final_string_tokens

    # create stemmer
    factory = StemmerFactory()
    stemmer = factory.create_stemmer()

    # apply stemmed term to dataframe
    final_string = []
    s = ""
    for sentence in df["final_result"].values:
        filteredSentence = []
        EachReviewText = ""
        s = (stemmer.stem(sentence))
        filteredSentence.append(s)
        EachReviewText = ' '.join(filteredSentence)
        final_string.append(EachReviewText)

   # df["final_result"] = final_string
   # df.head(5)
