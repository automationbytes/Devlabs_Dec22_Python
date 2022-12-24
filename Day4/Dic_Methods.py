#add
mydic = {
    "fruit" :"Apple",
    "vegetable": "Carrot",
    "language":"python",
    "vegetable":"onion"
}

print(mydic)

mydic["color"] = "blue"
print(mydic)

#update
mydic.update({"color":"red"})
print(mydic)

mydic.update({"sports":"football"})
print(mydic)

#setdefault - if yu hav key it will not update anythg, else if it wll add
mydic.setdefault("color","green")
mydic.setdefault("cartoon","tom_Jerry")
print(mydic)


#rremove
mydic.pop("vegetable")
print(mydic)

#popitem - it wil last value
mydic.popitem()
print(mydic)

#copy
newdict = mydic.copy()
print(newdict)

#clear
newdict.clear()
print(newdict)