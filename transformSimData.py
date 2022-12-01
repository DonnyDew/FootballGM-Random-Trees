import pandas as pd

def cleanData(sim):
    df = pd.read_csv(f"Sim {sim}.csv")
    #Remove uneccessary columns
    df.drop(df.iloc[:, 10:105], inplace=True, axis=1)
    df.drop(df.iloc[:, 16:], inplace=True, axis=1)
    df.drop(df.columns[[3]],axis=1,inplace=True)
    #Remove unwanted rows
    df = df[df.Season > 2023]
    df = df[df.G > 5]
    df = df[df.GS > 5]
    return df

df1 = cleanData(1)
df2 = cleanData(2)
df3 = cleanData(3)
df4 = cleanData(4)
df5 = cleanData(5)

winnersXLSX = pd.read_excel("SB Winners.xlsx")
winners = []
for i in winnersXLSX:
    for e in range(0,4):
        if winnersXLSX[i][e][0] != "S":
            winners.append(winnersXLSX[i][e])
def transformData(df,sim):
    teamDic = {}
    for row in df.iterrows():
        if row[1]["Team"] not in teamDic.keys():
            teamDic[str(sim)+row[1]["Team"]+str(row[1]["Season"])[2:]] = []

    for row in df.iterrows():
        teamDic[str(sim) + row[1]["Team"]+str(row[1]["Season"])[2:]].append(row[1])

    teamDic2 = {}
    offense = ["QB","RB","WR","OL","TE"]
    defense = ["DL","LB","S","CB"]
    for i in teamDic:
        teamDic2[i] = {"Ovr":"","Speed":"","Off Rating":"","Def Rating":"","QB Rating":"",
                                                        "Salary":"","Potential":"","Height":"","Strength":"","Endurance":"",
                                                        "RB/WR Rating":"","SB Win":""}
        speed = 0
        ovr = 0
        Oovr = 0
        Dovr = 0
        Ocount = 0
        Dcount = 0
        QBCount = 0
        QBovr = 0
        salary = 0
        pot = 0
        hgt = 0
        Str = 0
        end = 0
        RBWR = 0
        RBWRCount = 0
        SBWin = "N"
        if i in winners:
            SBWin = "Y"
        for e in range(0,len(teamDic[i])):
            speed += teamDic[i][e]["Spd"]
            ovr += teamDic[i][e]["Ovr"]
            salary += teamDic[i][e]["Salary"]
            pot += teamDic[i][e]["Pot"]
            hgt += teamDic[i][e]["Hgt"]
            Str += teamDic[i][e]["Str"]
            end += teamDic[i][e]["End"]
            if teamDic[i][e]["Pos"] in offense:
                Oovr += teamDic[i][e]["Ovr"]
                Ocount += 1
            elif teamDic[i][e]["Pos"] in defense:
                Dovr += teamDic[i][e]["Ovr"]
                Dcount += 1
            if teamDic[i][e]["Pos"] == "QB":
                QBovr += teamDic[i][e]["Ovr"]
                QBCount += 1
            if teamDic[i][e]["Pos"] == "RB" or teamDic[i][e]["Pos"] == "WR":
                RBWR += teamDic[i][e]["Ovr"]
                RBWRCount += 1
        teamDic2[i]["Speed"] = round(speed/len(teamDic[i]),2)
        teamDic2[i]["Ovr"] = round(ovr/len(teamDic[i]),2)
        teamDic2[i]["Off Rating"] = round(Oovr/Ocount,2)
        teamDic2[i]["Def Rating"] = round(Dovr/Dcount,2)
        teamDic2[i]["QB Rating"] = round(QBovr/QBCount,2)
        teamDic2[i]["Salary"] = round(salary,2)
        teamDic2[i]["Potential"] = round(pot/len(teamDic[i]),2)
        teamDic2[i]["Height"] = round(hgt/len(teamDic[i]),2)
        teamDic2[i]["Strength"] = round(Str/len(teamDic[i]),2)
        teamDic2[i]["Endurance"] = round(end/len(teamDic[i]),2)
        teamDic2[i]["RB/WR Rating"] = round(RBWR/RBWRCount,2)
        teamDic2[i]["SB Win"] = SBWin 
    newDf = pd.DataFrame.from_dict(teamDic2).transpose()
    return newDf

DF1 = transformData(df1,1)
DF2 = transformData(df2,2)
DF3 = transformData(df3,3)
DF4 = transformData(df4,4)
DF5 = transformData(df5,5)
DF = pd.concat([DF1,DF2,DF3,DF4,DF5])




DF.to_csv("transformeddata.csv")
    
    




