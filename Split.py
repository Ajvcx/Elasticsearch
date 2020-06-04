import glob
import re
pattern = re.compile(r'="(.*?)"')
text = ""
result = ""
#wikidate以下のデータを全て参照
wiki_path = glob.glob(".//*/*")
#glob.globで以下のファイルを参照することになる
with open("./.txt","w") as g:
    pass
for wp in wiki_path:
    with open (wp) as f:
        wiki = f.readlines()
        for w in wiki:
            if w == "\n":
                continue
            elif "<doc" in w:
                result = pattern.findall(txt)
                continue
            elif "</doc>" in w:
                #del _id, url, title
                break
                continue
            text += w
            # with open("./献上品.txt","a") as g:
            #     print(w,end=" ",file=g)
        print(result, text)
    break