guest_list = ['Peter', 'James', 'Joseph', 'Henry']
print(f"I hearby invite you {guest_list[0]} to my dinner")
print(f"I hearby invite you {guest_list[1]} to my dinner")
print(f"I hearby invite you {guest_list[2]} to my dinner")
print(f"I hearby invite you {guest_list[3]} to my dinner")

print((f"{guest_list[0]} could not make it"))

guest_list[0] = 'Hillary'
print(guest_list)

print(f"I hearby invite you {guest_list[0]} to my dinner")
print(f"I hearby invite you {guest_list[1]} to my dinner")
print(f"I hearby invite you {guest_list[2]} to my dinner")
print(f"I hearby invite you {guest_list[3]} to my dinner")

guest_list.insert(0, 'Charlie')
guest_list.insert(4, 'Obama')
guest_list.append('Fernendes')
print(guest_list)
