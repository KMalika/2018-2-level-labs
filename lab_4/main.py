import math

import math

undexpected = list("1234567890/?<>,.()-+=&*^:;%$#@!'""")
REFERENCE_TEXTS = []
if __name__ == '__main__':
    texts = ['5_7.txt', '15_2.txt', '10547_3.txt', '12230_7.txt']
    for text in texts:
        with open(text, 'r') as f:
            REFERENCE_TEXTS.append(f.read())


def clean_tokenize_corpus(REFERENCE_TEXTS) -> list:
    corpus = []
    if REFERENCE_TEXTS is None:
        corpus = []
    else:
        REFERENCE_TEXTS = list(filter(lambda x: x is not None and type(x) == str, REFERENCE_TEXTS))
        if REFERENCE_TEXTS == []:
            corpus = []
        else:
            for c in REFERENCE_TEXTS:
                if "\n" in c:
                    f = f.replace("\n", " ")
                if "<ch />" in f:
                    f = f.replace("<ch />", " ")
                while "  " in f:
                    f = f.replace("  ", " ")
                f = list(f)
                f = list(filter(lambda x: x not in unexpected, f))
                for i in range(len(f)):
                    f[i] = f[i].lower()
                f = ''.join(f)
                f = f.split(" ")
                corpus.append(f)
                for i in range(len(corpus)):
                    corpus[i] = list(filter(lambda x: x != '', corpus[i]))
    return corpus


class TfIdfCalculator:
    def __init__(self, corpus):
        self.corpus = corpus
        self.tf_values = []
        self.idf_values = {}
        self.tf_idf_values = []

    def calculate_tf(self):
        if self.corpus is None:
            self.tf_values = []
        else:
            self.corpus = list(filter(lambda x: x is not None and type(x) == list, self.corpus))
            for text in self.corpus:
                text = list(filter(lambda x: type(x) == str, text))
                dic = {}
                for i in range(len(text)):
                    num = 0
                    for f in text:
                        if text[i] == f:
                            num += 1
                    dic[text[i]] = num / len(text)
                self.tf_values.append(dic)
        return self.tf_values

    def calculate_idf(self):
        if self.corpus is None:
            self.tf_values = []
        else:
            all_words = []
            self.corpus = list(filter(lambda x: x is not None and type(x) == list, self.corpus))
            for i in range(len(self.corpus)):
                self.corpus[i] = list(filter(lambda x: type(x) == str, self.corpus[i]))
                for word in self.corpus[i]:
                    if word not in all_words:
                        all_words.append(word)
                for word in all_words:
                    num = 0
                    for i in range(len(self.corpus)):
                        if word in self.corpus[i]:
                            num += 1
                    self.idf_values[word] = math.log(len(self.corpus) / num)
        return self.idf_values

    def calculate(self):
        if self.tf_values == [] or self.idf_values == {} or self.tf_values is None or self.idf_values is None:
            return []
        else:
            for i in range(len(self.tf_values)):
                dic = {}
                for k, v in self.tf_values[i].items():
                    dic[k] = v * self.idf_values[k]
                self.tf_idf_values.append(dic)
        return self.tf_idf_values

    def report_on(self, word, document_index):
        if self.tf_idf_values is None:
            return ()
        elif self.tf_idf_values is []:
            return ()
        elif document_index >= len(self.tf_idf_values):
            return ()
        else:
            val = []
            for v in self.tf_idf_values[document_index].values():
                if v not in val:
                    val.append(v)
            ord_list = []
            while len(val) != 0:
                maxi = max(val)
                ord_list.append(maxi)
                val.remove(maxi)
            return (self.tf_idf_values[document_index][word], ord_list.index(self.tf_idf_values[document_index][word]))


