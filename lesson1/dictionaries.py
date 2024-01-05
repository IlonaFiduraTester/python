band = {
    "vocal": "Plant",
    "guitar": "Page"
}

band2 = dict(vocals="Plant", guitar="Page")

print(band)
print(band2)
print(type(band))
print(len(band))
print(band["vocal"])
print(band.get("guitar"))

print(band.keys())

print("guitar" in band)
print("sax" in band)

band["vocal"] = "Coverdale"
print(band["vocal"])
print(band)
print(band2)
if "vocal" in band:
    print("correct")

if 'vocal'not in band2:
    print("incorrect")

band2["guitar"] = "Slash"
print(band2)

band.update({"bass":"JPJ"})
print(band)
print(band.keys()) 
print(band.values())
band2['drums'] = 'Chad Smith'
print(band2)
keys_list = list(band.keys())
print(keys_list)
del band["guitar"]
print(band)



