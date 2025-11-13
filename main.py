from fastapi import FastAPI

app=FastAPI()

@app.get("/test")
def msg():
    return {"msg": "hi from test"}



@app.get("/test/{name}")
def save_user(name:str):
    with open("names.txt","a")as f:
        f.write(f"{name} \n")


@app.post("/caeser")
def code_ceasar(item:dict):
    new_word=""
    if item["mode"] == "encrypt":
    
        list_words=["a","b","c","d","e","f","g","h",
            "i","g","k","l","m","n","o","p","q",
            "r","s","t","u","v","w","x","y","z"]
        
        for ch in item["text"]:
            new_ch=list_words.index(ch)
            new_word +=list_words[(new_ch+item["offset"])% 26]
        return new_word
    if item["mode"] == "encrypt":
       


@app.get("/caeser")
def code_ceasar_split(item:str):
    list_words=["a","b","c","d","e","f","g","h",
        "i","g","k","l","m","n","o","p","q",
        "r","s","t","u","v","w","x","y","z"]

    double=""
    odd_number=""
    for ch in range(len(item)):
        
        if ch % 2 ==0:
            double+= item[ch]
        if ch % 2 != 0:
            odd_number+=item[ch]
    new_word=double+odd_number
    return {"encrypted_text": new_word}


