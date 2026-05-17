def gen_reaction(args, resource, depletable=0):
    task = resource.lower()
    if task[:3] == "res":
        task = task[3:]
    while task[-1].isdigit():
        task = task[:-1]
    name = resource[3:]
    return "".join(["REACTION ", name, " ", task, " process:resource=",
                    resource, ":value=", str(args.taskValDict[task]), ":type=",
                    args.rxnType, ":frac=", str(args.frac), ":max=",
                    str(args.resMax), ":depletable=", str(int(depletable)),
                    " requisite:max_count=", str(args.maxCount), "\n"])