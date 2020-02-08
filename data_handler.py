import data_ext
import json
res=[]

def view_all():
    print(data_ext.view())

def search(key):
    global res
    res=data_ext.search_db(key)
    return res
    if not res:
        return None


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
    res2=data_ext.mssg()
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

def Fetch_phone():
    res2=data_ext.fetch_phone()
    print(res2)
    with open("phone.json","w")as json_file:
        json.dump(res2,json_file)

def Add_user(f_name,l_name,age,sex,phone,att,carb,pro,vit,fat):
    data_ext.add_user(data_ext.last_id()[0][0]+1,f_name,l_name,age,sex,phone,att,carb,pro,vit,fat)
