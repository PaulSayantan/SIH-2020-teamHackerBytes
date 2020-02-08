import data_ext
import json
res=[]

def view_all():
    print(data_ext.view())

def search(key):
    global res
    res=data_ext.search_db(key)
    print(res)
    if not res:
        return("No Data Found")


def get_UID():
    return(res[0][0])
def get_Fname():
    return(res[0][1])
def get_Lname():
    return(res[0][2])
def get_Age():
    return(res[0][3])
def get_Sex():
    return(res[0][4])
def get_Phone():
    return(res[0][5])
def get_attend():
    return(res[0][6])

def get_att():
    res2=data_ext.mssg(3)
    with open("att.json","w")as json_file:
        json.dump(res2,json_file)


def Att_update():
    data_ext.att_update(100)

def get_cal_check():
    res2=data_ext.carb_check(200)
    with open("carb.json","w")as json_file:
        json.dump(res2,json_file)

def get_vit_check():
    res2=data_ext.carb_check(200)
    with open("vit.json","w")as json_file:
        json.dump(res2,json_file)

def get_fat_check():
    res2=data_ext.carb_check(200)
    with open("fat.json","w")as json_file:
        json.dump(res2,json_file)

def get_prot_check():
    res2=data_ext.carb_check(200)
    with open("prot.json","w")as json_file:
        json.dump(res2,json_file)



get_fat_check()
