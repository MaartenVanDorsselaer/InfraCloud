aclNum = int(input("What is the IPv4 ACL number? "))
if aclNum >= 1 and aclNum <= 99:
    print("This is a stadard acl.")
elif aclNum >= 100 and aclNum <= 199:
    print("This is an extended acl.")
else:
    print("This is not a standard or extended IPv4 acl.")