def key_func(n): #keyfunc
    return n[0]

def RGBtoHSV(rgb): #RGBからHSV(HSB)に変換する関数->引数はrgb[r,g,b]の配列
    R = rgb[0]
    G = rgb[1]
    B = rgb[2]
    RGBlavel = [(R,'R'),(G, 'G'),(B, 'B')]
    #print(RGBlavel)
    MAX = max(RGBlavel, key=key_func)
    #print(MAX)
    MIN = min(RGBlavel, key=key_func)
    #print(MIN)
    if (R == G) & (G == B):
        H = 0
    elif (MAX[1] == 'R'):
        H = 60 * ((G - B) / (MAX[0] - MIN[0]))
    elif (MAX[1] == 'G'):
        H = 60 * ((B - R) / (MAX[0] - MIN[0])) + 120
    elif (MAX[1] == 'B'):
        H = 60 * ((R - G) / (MAX[0] - MIN[0])) + 240
    if H < 0:
        H += 360
    #print(H)
    S = 100 * (MAX[0] - MIN[0]) / MAX[0]
    #print(S)
    V = 100 * MAX[0] / 255
    #print(V)
    hsv = [H,S,V]
    return hsv

def Searchrecomend(list, items, id, nowseason): #listからidの服に対するおすすめの服を選ぶ関数->引数はHSVLISTのようなdictionaly, 全ての服の数, 服のlist内のid
    target = list[id]
    targethsv = target['hsv']
    hues = [] #色相
    saturations = [] #彩度
    Values = [] #明度
    for num in range(items):
        if num != id:
            if list[num]['season'] == nowseason: #季節判定
                if target['pos'] != list[num]['pos']: #場所判定
                    itemhsv = list[num]['hsv']
                    #色相を比べる
                    Hdistance = (abs(targethsv[0] - itemhsv[0]), num)
                    hues.append(Hdistance)
                    #彩度を比べる
                    Sdistance = (abs(targethsv[1] - itemhsv[1]), num)
                    saturations.append(Sdistance)
                    #明度を比べる
                    Vdistance = (abs(targethsv[2] - itemhsv[2]), num)
                    Values.append(Vdistance)
    #色相が近い方を選択
    print(hues)
    print(min(hues, key=key_func))
    #彩度が近い方を選択
    print(saturations)
    print(min(saturations, key=key_func))
    #明度が近いほうを選択
    print(Values)
    print(min(Values, key=key_func))


RGB1 = [170,221,221]
RGB2 = [0,153,68]
RGB3 = [0,84,153]
RGB4 = [204,204,204]

HSV = RGBtoHSV(RGB1)
print(HSV)

SEASON = "spring"
ID = 1
ITEM = 4
HSVLIST = {
    0: {
        'type' : 'top', #服のtype
        'pos' : 'tops(innner)', #服のpos...同じ位置の服を選ばない
        'hsv' : RGBtoHSV(RGB1), #服のhsv...色の情報
        'season' : 'spring', #服の季節...おすすめ時に選択
    },
    1: {
        'type' : 'top',
        'pos' : 'tops(innner)',
        'hsv' : RGBtoHSV(RGB2),
        'season' : 'spring',
    },
    2: {
        'type' : 'pants',
        'pos' : 'bottoms',
        'hsv' : RGBtoHSV(RGB3),
        'season' : 'spring',
    },
    3: {
        'type' : 'pants',
        'pos' : 'bottoms',
        'hsv' : RGBtoHSV(RGB4),
        'season' : 'spring',
    },
}

Searchrecomend(HSVLIST, ITEM, ID, SEASON)