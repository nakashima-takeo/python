
def DisplayMemberCode(industorialCode, branchCode, subbranchCode, memberCode, familyCode):
    print('"' + "{:03d}".format(industorialCode) + "{:03d}".format(branchCode) + "{:03d}".format(
        subbranchCode) + "{:06d}".format(memberCode) + "{:02d}".format(familyCode) + '"')


DisplayMemberCode(60, 0, 0, 2, 1)
