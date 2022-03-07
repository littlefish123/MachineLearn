import spacy
from spacy import displacy
from pathlib import Path
from pandas import DataFrame


def displayResult(doc):
    keyword = ['DATE', 'STOCKCODE', 'PRICE', 'NAME', 'ACCNUM']
    keywordDict = {"text":[], "label":[]}
    df = DataFrame(keywordDict)
    for ent in doc.ents:
        if ent.label_ in keyword:
            print(ent.text, ent.label_)
            df.loc[len(df.index)] = [ent.label_, ent.text]

    print(df)


def displayHTML(result, fileName):
    htm = displacy.render(result, style="ent", page=True)
    output_path = Path(fileName)
    output_path.open("w", encoding="utf-8").write(htm)


def parseStatement(fileName):
    with open(fileName, 'r') as file:
        data = file.read()
        parseline1 = nlp1(data)
        parseline2 = nlp2(data)
        displayResult(parseline1)
        displayResult(parseline2)
        file.close()

    return parseline1, parseline2


if __name__ == "__main__":
    print('Best Model')
    print('===============')
    nlp1 = spacy.load(R"training/model-best") #load the best model
    # doc1 = nlp1("Who is Vijay??") # input sample tex
    # displayResult(doc1)
    # doc2 = nlp1("I like CA") # input sample tex
    # displayResult(doc2)
    # doc3 = nlp1("i like 00700 22APR2022") # input sample tex
    # displayResult(doc3)
    # doc4 = nlp1("account number 773-183280-123")
    # displayResult(doc4)
    # doc5 = nlp1("100,9000")
    # displayResult(doc5)
    # doc6 = nlp1("HKD 500.344")
    # displayResult(doc6)
    # doc7 = nlp1("0857 PetroChina")
    # displayResult(doc7)


    print('Last Model')
    print('===============')
    nlp2 = spacy.load(R"training/model-last") #load the best model
    # doc1 = nlp2("Who is Vijay??") # input sample tex
    # displayResult(doc1)
    # doc2 = nlp2("I like CA") # input sample tex
    # displayResult(doc2)
    # doc3 = nlp2("i like 00700 22APR2022") # input sample tex
    # displayResult(doc3)
    # doc4 = nlp2("account number 773-183280-123")
    # displayResult(doc4)
    # doc5 = nlp2("100,9000")
    # displayResult(doc5)
    # doc6 = nlp2("HKD 333.000344")
    # displayResult(doc6)
    # doc7 = nlp2("0857 PetroChina")
    # displayResult(doc7)

    # displayHTML([doc1, doc2, doc3, doc4,doc5, doc6, doc7])

    nlp1 = spacy.load(R"training/model-best")
    nlp2 = spacy.load(R"training/model-last")
    result1, result2 = parseStatement('d://spacy//testcode//hangseng.txt')
    displayHTML(result1, "images/result1.htm")
    displayHTML(result2, "images/result2.htm")
    displayResult(result1)
