PMAX_member = ["jakarin akrin","phasit sritonchai","prakrapong pongpang","chayutra chantachote","nattaphong pannengpet",
"nattanon moontip","kitsakron sophawan","sangnapha akrin"]

# ข้อ 1
PMAX_member.pop(2)
save_member = PMAX_member.pop()
PMAX_member.insert(2,save_member)
PMAX_member.insert(0,"anuwat max")
PMAX_member.insert(3,"rattanaporn wan")
PMAX_member.insert(4,"rattanaporn beauty")
PMAX_member.append('phakawat bootnampetch')
PMAX_member.append('chaowarin man')
PMAX_member.append('kunlanat numnim')
PMAX_member.append('chanachai nuay')
print('ข้อ 1 :')
print(PMAX_member)
print()

# ข้อ 2
PMAX_member.sort(reverse=True)
print('ข้อ 2 :')
print(PMAX_member)
print()

# ข้อ 3
print('ข้อ 3 :')
for list_name in PMAX_member:
    name = list_name.split(" ")
    firstname = name[0]
    firstname = firstname[0].upper() + firstname[1:]
    lastname = name[-1]
    lastname = lastname[0].upper()+"."
    print(firstname , lastname)
print()

# ข้อ 4
PMAX_member.append('krit')
PMAX_member.append('tan')
PMAX_member.append('natty')
PMAX_member.sort()
print('ข้อ 4 :')
print(PMAX_member)
